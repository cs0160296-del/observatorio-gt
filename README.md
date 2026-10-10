# Observatório dos Grupos de Trabalho

Rastreador de **todos os grupos de trabalho criados por despacho do Governo português**
desde que o XXIV Governo Constitucional tomou posse, a 2 de abril de 2024, incluindo o
XXV Governo (desde junho de 2025).

Para cada grupo: quando foi criado, o que lhe foi pedido, quem o integra, que prazos lhe
foram fixados e o que se sabe publicamente sobre o que entregou — sempre com ligação ao
ato original no Diário da República.

**Dados até 10 de outubro de 2026. 106 grupos de trabalho.**

| | |
|---|---|
| Grupos criados | **106** (64 no XXIV Governo, 42 no XXV) |
| Em atraso | **58** (54,7 %) |
| Concluídos | 14 (5 no prazo, 9 com atraso) |
| Em curso, dentro do prazo | 20 |
| Prorrogados | 3 |
| Extintos / substituídos | 1 |
| Sem informação pública | 10 |
| Atraso mediano | **376 dias** (nos 67 grupos com atraso apurável) |
| Atraso máximo | 801 dias |

---

## Ficheiros

| Ficheiro | Conteúdo |
|---|---|
| `index.html` + `data.js` | O site. Estático, sem dependências de servidor. |
| `grupos_de_trabalho.xlsx` | Tabela principal: 106 linhas × 31 colunas, com filtros. |
| `grupos_de_trabalho.csv` | O mesmo em CSV (UTF-8 com BOM, abre direito no Excel). |
| `orgaos_relacionados.csv` | Lista separada: 32 comissões, estruturas de missão e *task forces*. |
| `METODOLOGIA.md` | Como os dados foram recolhidos, verificados e classificados. |
| `fonte/` | O pipeline que gera tudo (ver abaixo). |

---

## Pôr o site no ar (GitHub Pages)

O site é um ficheiro HTML e um ficheiro de dados — não precisa de build nem de servidor.

```bash
cd observatorio-gt
git init -b main
git add .
git commit -m "Observatório dos Grupos de Trabalho — dados até 2026-10-10"
```

Criar o repositório no GitHub e enviar:

```bash
gh repo create observatorio-gt --public --source=. --push
```

(ou, sem o `gh`: criar o repositório vazio em github.com e depois
`git remote add origin https://github.com/UTILIZADOR/observatorio-gt.git && git push -u origin main`)

Ativar o Pages: **Settings → Pages → Source: Deploy from a branch → Branch: `main` / `/ (root)` → Save.**
Ao fim de um minuto o site fica em `https://UTILIZADOR.github.io/observatorio-gt/`.

Por fim, corrigir o URL nas etiquetas de partilha, para o cartão de pré-visualização
ficar certo no Reddit, no X e no WhatsApp:

```bash
python3 fonte/standalone.py index.html https://UTILIZADOR.github.io/observatorio-gt/
git commit -am "URL canónico" && git push
```

### Alternativas

- **Netlify / Cloudflare Pages** — arrastar a pasta para a área de *deploy*; dá HTTPS e
  domínio próprio de graça, e aceita ficheiros maiores que o Pages.
- **Domínio próprio** (ex.: `grupos-de-trabalho.pt`) — funciona em qualquer das três:
  apontar o DNS e, no GitHub, escrever o domínio em Settings → Pages → Custom domain.

---

## Atualizar os dados

O pipeline está em `fonte/` e separa o que é **facto** do que é **análise**:

| Ficheiro | Papel |
|---|---|
| `data/acts.json` | Texto integral estruturado dos 106 atos + citações posteriores no DR. Recolhido do Diário da República. |
| `judgments.py` | A camada de análise: prazos, estado, evidência, notas — uma entrada por ato. É aqui que se altera um estado. |
| `pt.py` | Designação curta e resumo da missão de cada grupo. |
| `dates.py` | Aritmética de prazos: dias úteis, feriados nacionais, trimestres. |
| `engine.py` | Extração automática de coordenador, composição e remuneração a partir do texto do ato. |
| `build.py` | Gera o XLSX, o CSV e as estatísticas; valida a coerência de cada linha. |
| `mkdata.py` | Gera o `data.js` que o site carrega. |
| `pagina.html` | O corpo da página (sem `<head>`). É aqui que se mexe no site. |
| `standalone.py` | Embrulha `pagina.html` num documento completo, com as etiquetas de partilha. |

```bash
python3 -m pip install openpyxl
cd fonte
python3 build.py        # -> ../grupos_de_trabalho.{xlsx,csv} + verificação de coerência
python3 mkdata.py       # -> ../data.js
python3 standalone.py   # -> ../index.html
```

O `build.py` verifica, em cada linha, que o estado não contradiz as datas (nenhum
«Em atraso» com prazo por vencer, nenhum «Em curso» com prazo vencido, etc.) e recusa-se
a passar em silêncio: imprime as inconsistências que encontrar.

Para mudar a data de referência — e portanto todos os dias de atraso — basta editar
`TODAY` em `dates.py` e voltar a correr os três comandos.

---

## O que este rastreador não faz

Está tudo em `METODOLOGIA.md`, mas o essencial:

- **«Em atraso» não significa que o grupo não entregou.** Significa que o prazo do
  próprio despacho passou e que o Estado não tornou público nada que demonstre a
  entrega. A ausência de evidência não é evidência de ausência.
- **Relatório entregue ≠ política concretizada.** São colunas diferentes. Em 9 dos 14
  grupos concluídos, a única prova pública é o diploma posterior, não o relatório — por
  isso esses atrasos são um **limite superior**.
- **Grupos criados no articulado sem menção no sumário não são apanhados.** A pesquisa
  por texto integral do Diário da República é demasiado difusa para fechar essa lacuna.
- Só **um** relatório final está publicamente disponível na íntegra, em 106 grupos.

Correções são bem-vindas: abrir um *issue* com o número do despacho e a fonte.

---

## Fonte e reutilização

Fonte primária: [Diário da República Eletrónico](https://diariodarepublica.pt), 1.ª e
2.ª séries, de 2 de abril de 2024 a 10 de outubro de 2026. As 133 ligações ao DR usadas
na tabela e na coluna de evidência foram carregadas e confirmadas uma a uma.

- **Dados** (`*.csv`, `*.xlsx`, `fonte/data/acts.json`): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt) — usar livremente, citando a fonte.
- **Código** (`fonte/*.py`, `index.html`): MIT.

Os sumários, títulos dos atos e objetivos são transcrições do Diário da República e
estão no domínio público.
