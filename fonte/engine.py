"""Auto-derivation of structured fields from the raw despacho text."""
import json, re, unicodedata
from datetime import date
from dates import add_working_days, add_calendar_days, quarter_end, TODAY

# XXV Governo Constitucional took office on 5 June 2025.
XXV_START = date(2025, 6, 5)


def nd(s):
    return unicodedata.normalize("NFD", s or "").encode("ascii", "ignore").decode().lower()


def iso(s):
    y, m, d = (int(x) for x in s.split("-"))
    return date(y, m, d)


# ---------------------------------------------------------------- deadlines
def resolve(kind, value, pub, sig=None):
    """Return (due_date, human-readable calculation)."""
    if kind == "none":
        return None, "o ato não fixa data (prazo ligado a um evento, ou inexistente)"
    if kind == "wd":
        due = add_working_days(pub, value)
        return due, (f"{value} dias úteis a contar do dia seguinte à publicação "
                     f"({pub.isoformat()}), excluindo sábados, domingos e feriados nacionais "
                     f"→ {due.isoformat()}")
    if kind == "cd":
        due = add_calendar_days(pub, value)
        return due, (f"{value} dias seguidos a contar da publicação ({pub.isoformat()}) "
                     f"→ {due.isoformat()}"
                     + ("" if due == pub.fromordinal(pub.toordinal() + value)
                        else " (transitado para o dia útil seguinte)"))
    if kind == "cds":
        base = sig or pub
        due = add_calendar_days(base, value)
        return due, f"{value} dias seguidos a contar da assinatura ({base.isoformat()}) → {due.isoformat()}"
    if kind == "months":
        n, base = value, (sig or pub)
        y, m = base.year, base.month + n
        y += (m - 1) // 12
        m = (m - 1) % 12 + 1
        d = min(base.day, [31, 29 if y % 4 == 0 and (y % 100 or y % 400 == 0) else 28,
                           31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1])
        due = date(y, m, d)
        return due, f"{n} meses a contar de {base.isoformat()} → {due.isoformat()}"
    if kind == "date":
        due = iso(value)
        return due, f"data fixada expressamente no ato → {due.isoformat()}"
    if kind == "q":
        y, q = value
        due = quarter_end(y, q)
        return due, f"fim do {q}.º trimestre de {y} → {due.isoformat()}"
    if kind == "month_end":
        y, m = value
        last = [31, 29 if y % 4 == 0 and (y % 100 or y % 400 == 0) else 28,
                31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1]
        due = date(y, m, last)
        return due, f"fim do mês indicado no ato → {due.isoformat()}"
    raise ValueError(kind)


# ------------------------------------------------------------ text mining
# Verb forms that actually assign coordination OF THE GROUP. Deliberately strict:
# the loose word "coordenacao" also appears inside group *names* ("GT para a
# coordenacao do processo...") and in references to other plans, which produced
# false positives.
COORD_RE = re.compile(
    r"(que coordenam?\b|que o coordena|que a coordena|que preside[mn]?\b|que presida"
    r"|coordenad[oa] pel|coordenad[oa] por|e coordenado|e coordenada"
    r"|sendo um nomeado coordenador|nomeado coordenador"
    r"|exerce a funcao de entidade coordenadora|enquanto entidade coordenadora"
    r"|a quem compete a coordenacao|que assegura a coordenacao"
    r"|a coordenacao do grupo de trabalho compete|que coordena em articulacao"
    r"|^um coordenador|^o coordenador-geral|^o coordenador,|coordenador-geral, que"
    r"|^um representante .{0,80}, que coordena|a coordenacao do grupo de trabalho e)")

COMP_RE = re.compile(r"(e constituido por|e composto por|tem a seguinte composicao|"
                     r"e constituida por|integra ainda|e composta por|tem a seguinte constituicao|"
                     r"integram o|e constituido pelos seguintes|e composto pelos seguintes|"
                     r"apresenta a seguinte constituicao|integra um representante|"
                     r"e constituido pelas seguintes|sera composto por|tem a seguinte estrutura|"
                     r"sera constituido p|constituido pelos seguintes elementos|"
                     r"composto pelos seguintes|designo os seguintes|integrado pelos seguintes|"
                     r"e constituido pelas seguintes entidades|tem a seguinte composicao:)")


MARKER = re.compile(r"^(?:\d{1,2}\s*\|\s*|[a-z]\)\s*|[ivxIVX]+\)\s*)+")


def _frags(p):
    p = MARKER.sub("", p.strip())          # drop the leading "3| " paragraph number
    parts = [f.strip() for f in re.split(r"\s*\|\s*", p) if f.strip()]
    if len(parts) <= 1:
        # some acts list members inline, separated by semicolons
        body = re.split(r":\s*", p, maxsplit=1)
        body = body[1] if len(body) > 1 else p
        parts = [f.strip() for f in re.split(r";\s*", body) if len(f.strip()) > 3]
    return parts


def find_members(paras):
    best = ""
    for p in paras:
        if COMP_RE.search(nd(p)) and len(p) > len(best):
            best = p
    return best[:2500]


def find_coordinator(paras):
    """Who coordinates the group. Looks first inside the composition clause,
    because that is where the coordination marker normally sits on an alinea."""
    comp = find_members(paras)
    for source in ([comp] if comp else []) + [p for p in paras if p != comp]:
        if not source:
            continue
        for frag in _frags(source):
            clean = MARKER.sub("", frag).strip()
            if COORD_RE.search(nd(clean)):
                return clean[:300]
    return ""


def member_list(paras):
    """Readable list of member entities/people, one per alinea."""
    comp = find_members(paras)
    if not comp:
        return ""
    frags = _frags(comp)
    # drop the stem ("O grupo de trabalho e constituido por:") when present
    if frags and (frags[0].rstrip().endswith(":") or COMP_RE.search(nd(frags[0]))):
        frags = frags[1:] or frags
    out = []
    for f in frags:
        f = MARKER.sub("", f).strip(" ;.")
        f = re.sub(r"\s+", " ", f)
        if len(f) < 3:
            continue
        # drop long biographies: keep the part before the first comma-bio marker
        f = re.split(r",\s*(licenciad|doutorad|mestre em|professor|assistente graduad|médic)", f)[0]
        out.append(f[:110])
    seen, uniq = set(), []
    for o in out:
        k = nd(o)
        if k not in seen:
            seen.add(k)
            uniq.append(o)
    return "; ".join(uniq[:25])


PAID_RE = re.compile(r"(senhas? de presenca|contrapartida financeira|e devida uma remuneracao|"
                     r"tem direito ao pagamento de ajudas de custo|auferem)")
UNPAID_RE = re.compile(r"(nao (e )?(devido|devida|confere|auferem|recebem)|"
                       r"nao conferem|renunciam a qualquer|sem direito a|"
                       r"nao auferem|nao e devido o pagamento|nao recebem qualquer|"
                       r"nao e devida qualquer|realiza-se sem que daí decorra)")


def find_pay(paras):
    hits = [p for p in paras if re.search(r"remunerac|abono|senha|ajudas de custo|contrapartida|encargo",
                                          nd(p))]
    if not hits:
        return "Sem menção no ato", ""
    blob = " ".join(hits)
    n = nd(blob)
    if re.search(r"senhas de presenca, por cada reuniao|e devida uma contrapartida financeira"
                 r"|tem direito ao pagamento de ajudas de custo", n):
        return "Remunerado (parcialmente)", blob[:400]
    if UNPAID_RE.search(n):
        extra = " (ressalvadas ajudas de custo)" if "ajudas de custo" in n else ""
        return "Não remunerado" + extra, blob[:400]
    return "Sem menção clara", blob[:400]


def ministries(emit):
    return (emit or "").split(" - ")[0].strip()


def government(pub):
    return "XXV" if pub >= XXV_START else "XXIV"


def sig_date(sig, pub):
    MES = dict(janeiro=1, fevereiro=2, marco=3, abril=4, maio=5, junho=6, julho=7,
               agosto=8, setembro=9, outubro=10, novembro=11, dezembro=12)
    m = re.match(r"(\d{1,2}) de ([a-zç]+) de (20\d\d)", nd(sig or ""))
    if not m:
        return None
    try:
        return date(int(m.group(3)), MES[m.group(2)], int(m.group(1)))
    except Exception:
        return None


def load_acts(path="data/acts.json"):
    return json.load(open(path))
