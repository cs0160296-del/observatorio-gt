# -*- coding: utf-8 -*-
"""Gera data.js — o payload que o painel carrega."""
import json, re
from collections import Counter

rows = json.load(open("data/rows.json"))
stats = json.load(open("data/stats.json"))

ABREV = [
    ("Presidência do Conselho de Ministros", "PCM"),
    ("Trabalho, Solidariedade e Segurança Social", "Trabalho/Seg. Social"),
    ("Educação, Ciência e Inovação", "Educação/Ciência"),
    ("Infraestruturas e Habitação", "Infraestruturas/Habitação"),
    ("Economia e Coesão Territorial", "Economia/Coesão"),
    ("Cultura, Juventude e Desporto", "Cultura/Juventude"),
    ("Negócios Estrangeiros", "Negócios Estrang."),
    ("Administração Interna", "Adm. Interna"),
]


def curto(m):
    for a, b in ABREV:
        m = m.replace(a, b)
    return m


def principal(m):
    """Área governativa que encabeça o despacho."""
    return re.split(r"\s+e\s+|,\s*", curto(m))[0].strip()


CAMPOS = [
    ("id", "ID"), ("ato", "Ato criador"), ("url", "Link DR"),
    ("dp", "Data de publicação (DR)"), ("ds", "Data de assinatura"),
    ("nome", "Nome do grupo (sumário do DR)"), ("nc", "Designação curta"),
    ("gov", "Governo"), ("area", "Área de política"), ("coord", "Coordenador"),
    ("mem", "Membros (entidades)"), ("comp", "Composição (texto do ato)"),
    ("mRes", "Missão (resumo)"), ("mPT", "Missão (texto do ato)"),
    ("obj", "Objetivos específicos (do ato)"), ("prazos", "Prazos — todos"),
    ("pl", "Prazo principal"), ("pd", "Data-limite principal"),
    ("calc", "Como foi calculada"), ("pago", "Participação remunerada"),
    ("est", "Estado"), ("ent", "Data de entrega / diploma"),
    ("ev", "Evidência"), ("xref", "Atos posteriores que citam este (DR)"),
    ("not", "Notas"), ("vig", "Entrada em vigor / produção de efeitos"),
]

out = []
for r in rows:
    o = {k: r[c] for k, c in CAMPOS}
    o["min"] = curto(r["Ministérios / Secretarias de Estado"])
    o["lead"] = principal(r["Ministérios / Secretarias de Estado"])
    o["atr"] = r["Dias de atraso"] if isinstance(r["Dias de atraso"], int) else None
    out.append(o)

stats["by_lead"] = dict(Counter(o["lead"] for o in out))

with open("../data.js", "w", encoding="utf-8") as f:
    f.write("window.GT=" + json.dumps({"rows": out, "stats": stats},
                                      ensure_ascii=False, separators=(",", ":")) + ";")

import os
print("data.js", round(os.path.getsize("../data.js") / 1024, 1), "KB |", len(out), "linhas")
assert all(o["nc"] and o["mRes"] for o in out), "faltam designações/resumos"
print("designação curta e resumo presentes em todas as linhas")
