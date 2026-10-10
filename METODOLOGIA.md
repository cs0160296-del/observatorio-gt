# Nota metodológica

**Observatório dos Grupos de Trabalho — XXIV e XXV Governos Constitucionais**
Período coberto: 2 de abril de 2024 a 10 de outubro de 2026 (31 meses).
Dados extraídos a 10 de outubro de 2026. Fonte primária: Diário da República Eletrónico.

---

## 1. Como os grupos foram encontrados

### O problema da pesquisa no DR

O motor de pesquisa do `diariodarepublica.pt` **não faz correspondência exata de
expressões**: procurar `"grupo de trabalho"` em texto integral devolve 22 232 atos no
período, a maioria dos quais contém apenas uma das palavras. A pesquisa por texto
integral é, por isso, inutilizável para este efeito — testei-a e descartei-a
(ver §5, «o que não funcionou»).

O canal fiável é o **sumário oficial**: um resumo normalizado que a INCM redige para
cada ato publicado. Um despacho que cria um grupo de trabalho di-lo quase sempre no
sumário («Cria o Grupo de Trabalho para…», «Constitui um grupo de trabalho com vista
a…»).

### Procedimento

1. **Recolha.** Para cada um dos 31 meses do período, e separadamente para a 1.ª e a
   2.ª séries, recolhi todos os atos cujo sumário corresponde a «grupo de trabalho».
   A fatiagem mensal foi necessária porque a paginação profunda sobre resultados
   ordenados por relevância é instável (devolve duplicados); com janelas mensais a
   paginação é rasa e determinística.
   **Resultado: 2 695 atos da 2.ª série + 31 da 1.ª série = 2 726 atos.**

2. **Filtragem exata.** Dos 2 726, filtrei localmente os que contêm de facto a
   expressão «grupo(s) de trabalho» no sumário (normalização Unicode, sem
   acentuação, minúsculas). **Resultado: 153 atos.**

3. **Classificação.** Classifiquei os 153 atos, com revisão manual de cada um:

   | Categoria | N.º | Tratamento |
   |---|---|---|
   | **Atos de criação de GT do Governo** | **106** | tabela principal |
   | Alterações, prorrogações, renovações, revogações | 18 | usados como evidência |
   | Nomeações, designações, louvores | 17 | usados como evidência |
   | Entidades não governamentais (tribunais, universidades, assembleias legislativas regionais, CCDR) | 12 | excluídos |

   Dois atos foram reclassificados manualmente para «criação» porque o sumário
   começa por outro verbo mas o articulado cria um grupo: o Despacho n.º 9649/2024
   («Revoga… e determina a criação…») e o Despacho n.º 4643/2026 («Altera a
   composição… e revoga…», mas no n.º 1 lê-se «É constituído um Grupo de Trabalho»).
   Quatro despachos da Saúde de 2026 («Define o grupo de trabalho que irá proceder
   a…») foram igualmente tratados como atos de criação.

4. **Extração.** Obtive o texto integral dos 106 atos de criação e dos 18 atos de
   alteração directamente das páginas do DR, e extraí de forma estruturada: emitente,
   data de assinatura, produção de efeitos, número de parágrafos operativos,
   coordenação, composição, objetivos, cláusulas de prazo e cláusula de remuneração.

---

## 2. Como os estados foram apurados

### Varrimento de citações (a base da evidência)

Para cada um dos 106 despachos de criação, pesquisei no DR **todos os atos publicados
entre 2024-04-02 e 2026-10-10 que citam o despacho pelo número**. Ao contrário da
pesquisa por expressões, a pesquisa por número de ato é precisa: o controlo com o
Despacho n.º 11271/2024 devolveu exatamente dois resultados — o próprio ato e a sua
prorrogação.

Filtrei depois o ruído de coincidência numérica (um «Aviso n.º 7321/2024/2» não é uma
citação do «Despacho n.º 7321/2024») exigindo que o ato citante (i) seja posterior à
criação e (ii) não partilhe o mesmo número de ordem.

**Resultado: 101 citações relevantes, distribuídas por 45 dos 106 grupos.** É esta a
base factual das prorrogações, substituições, extinções e, em vários casos, da própria
entrega.

### Confirmação de entrega

Onde o varrimento não bastou, procurei o **produto** do grupo: decreto-lei, lei,
resolução do Conselho de Ministros ou portaria que concretize o que foi pedido ao
grupo, mais fontes jornalísticas de referência (Lusa, Público, Expresso, Observador,
ECO) e comunicação do Governo em gov.pt.

### A regra que não foi quebrada

**Nenhum estado foi presumido.** Quando o prazo passou e não existe evidência pública,
o estado é «Em atraso» e a coluna *Evidência* declara exatamente o que foi pesquisado.
Quando o ato não fixa prazo algum, o estado é «Sem informação pública» e **não é
imputado qualquer atraso**.

### Convenções de estado

| Situação | Estado atribuído |
|---|---|
| Entrega comprovada dentro do prazo | Concluído no prazo |
| Entrega comprovada depois do prazo | Concluído com atraso |
| Prazo por vencer | Em curso – dentro do prazo |
| Prazo vencido, sem evidência de entrega | Em atraso |
| Prazo formalmente prorrogado e **novo prazo ainda não vencido** | Prorrogado |
| Prazo formalmente prorrogado mas **novo prazo também já vencido**, sem entrega | **Em atraso** (a prorrogação consta da evidência) |
| Revogado ou substituído por outro ato | Extinto / substituído |
| Sem prazo no ato e sem evidência de conclusão | Sem informação pública |

A penúltima linha é uma opção deliberada: classificar como «Prorrogado» um grupo cujo
prazo alargado também já expirou esconderia o atraso atrás da prorrogação. Três grupos
estão em «Prorrogado» (prazo novo ainda a correr); quatro foram prorrogados e **ainda
assim** contam como «Em atraso».

---

## 3. Prazos: como foram convertidos em datas

Todos os prazos relativos foram convertidos em datas de calendário, e cada linha da
folha de cálculo mostra o cálculo na coluna *Como foi calculada*.

- **«N dias úteis»** — conta-se a partir do dia seguinte à publicação, excluindo
  sábados, domingos e os feriados nacionais obrigatórios (art. 87.º do CPA). O
  Carnaval não é feriado obrigatório e não foi excluído.
  *Exemplo (caso-teste):* Despacho n.º 14284/2024, publicado a 2024-12-03, «30 dias
  úteis» → **2025-01-16**.
- **«N dias»** — dias seguidos; se o termo cair em dia não útil, transita para o dia
  útil seguinte.
- **«N meses»** — mesmo dia do mês de destino, a contar da assinatura quando o ato o
  diz, caso contrário da publicação.
- **«segundo trimestre de 2026»** → **2026-06-30** (último dia do trimestre).
  *Exemplo (caso-teste):* a disponibilização do novo passaporte era devida até
  2026-06-30; a 2026-10-10 vão **102 dias** de atraso.
- **«até ao final do mês de X»** → último dia desse mês.

### Prazo principal

Cada grupo tem um *prazo principal* — o da entrega final — usado para o estado e para
o cálculo do atraso. Todos os restantes prazos do ato ficam registados na coluna
*Prazos — todos*, com o texto original em português.

**Prazos administrativos não geram atraso.** Cinco despachos fixam apenas um prazo
interno para as entidades designarem representantes (5 a 10 dias) e nenhum prazo de
entrega. Medir «atraso» contra esse relógio produziria números enganadores (até 841
dias), pelo que esses grupos ficam sem atraso imputado e com estado «Sem informação
pública».

---

## 4. Relatório entregue ≠ política concretizada

As duas coisas estão separadas e assinaladas.

Em **9 dos 14 grupos dados como concluídos**, a única evidência pública de entrega é o
*diploma posterior* que concretiza o trabalho — não o relatório do grupo. Nesses casos:

- o atraso é medido **até à publicação desse diploma**, pelo que é um **limite
  superior**: o grupo pode ter entregado bastante antes;
- a coluna *Notas* assinala-o explicitamente.

Apenas **um** relatório final está publicamente disponível na íntegra: o do grupo de
trabalho para a reforma da Segurança Social (Despacho n.º 1452/2025). Note-se que o
Despacho n.º 986/2025 (desperdício no SNS) **obriga por lei** à publicação do relatório
final no sítio do SNS — e esse relatório não foi localizado.

Casos em que o grupo entregou mas a política ainda não aconteceu estão assinalados nas
notas — por exemplo o Trabalho XXI (anteprojeto aprovado em julho de 2025, proposta de
lei no Parlamento desde maio de 2026, ainda sem aprovação) e a reforma da Segurança
Social (relatório público em agosto de 2026, sem legislação).

---

## 5. Lacunas e limitações

**O que esta lista pode não apanhar**

1. **Grupos criados no articulado sem menção no sumário.** Se um despacho ou RCM cria
   um grupo de trabalho como disposição acessória e o sumário não o refere, o método
   não o apanha. Testei o canal alternativo — pesquisa por texto integral de
   «é criado um grupo de trabalho» — e sondei os 489 resultados mais relevantes:
   415 não tinham a expressão no sumário e **nenhum** era um ato de criação de grupo
   de trabalho (eram códigos de conduta, nomeações, alterações de ciclos de estudos —
   ruído do motor difuso). A pesquisa por texto integral do DR não tem precisão
   suficiente para fechar esta lacuna de forma sistemática.

2. **Relatórios entregues mas não publicados.** São invisíveis para qualquer método
   documental. A ausência de evidência **não é** evidência de não-entrega, e os 58
   grupos «Em atraso» devem ser lidos nesse sentido: *o prazo passou e o Estado não
   tornou público nada que demonstre a entrega*.

3. **Datas de constituição efetiva.** Não são publicadas. Em 4 atos o prazo conta-se
   «a partir da constituição do grupo»; calculei a partir da publicação, o que
   **subestima** ligeiramente o atraso.

4. **Interpretação de um prazo.** O Despacho n.º 7229/2026 (Lei Geral da Segurança e
   Saúde no Trabalho) fixa o prazo através de uma tabela de calendário por trimestres,
   não de uma data. Li o último trimestre previsto (3.º de 2026) como 2026-09-30. É
   uma interpretação, assinalada nas notas.

**Fora de âmbito, por opção**

Comissões, comissões técnicas, estruturas de missão e *task forces* **não** entram na
tabela principal, conforme pedido. Estão numa lista separada — `orgaos_relacionados.csv`,
**32 órgãos**: 30 comissões, 1 estrutura de missão (bolsa de peritos da EMER 2030) e 1
*task force* (instalações das forças de segurança, Despacho n.º 3183/2025).

O universo bruto foi de 6 292 atos com «comissão» no sumário, 321 com «estrutura de
missão» e 20 com «task force». A redução para 32 resulta de excluir, além dos verbos
que não criam nada: comissões de serviço (nomeações), comissões de negociação de
contratos, comissões de cogestão de áreas protegidas, comissões consultivas de planos
diretores municipais, CPCJ locais, comissões parlamentares de inquérito e órgãos de
entidades não governamentais. Essas exclusões são assumidas: são atos administrativos
de rotina, não órgãos de política criados *ad hoc* — que é o objeto deste trabalho.

Nota: há um padrão visível nesta lista — sete comissões idênticas criadas em janeiro de
2025 para transferir áreas portuárias para sete municípios, e três mais em 2026, uma
das quais revoga e substitui a de 2025 (Lagoa). E o Despacho n.º 4846/2026 recria uma
comissão de acompanhamento da AI² com a mesma redação do Despacho n.º 2534/2026, de
dois meses antes.

**Atribuição de governo**

XXIV até 2025-06-04, XXV a partir de 2025-06-05 (tomada de posse), por data de
publicação. Alguns despachos publicados em abril-junho de 2024 foram assinados por
membros do XXIII Governo cessante; nenhum deles é um ato de criação na tabela — o
primeiro GT criado no período é de 11 de junho de 2024.

---

## 6. Verificação

- **Ligações.** Todas as 106 linhas têm ligação ao ato original no DR. Todas as
  ligações da tabela e da coluna *Evidência* (133 no total) foram carregadas e
  confirmadas uma a uma.
- **Coerência.** Uma verificação automática confirma, para cada linha, que o estado
  é compatível com as datas: nenhum «Em atraso» com prazo por vencer, nenhum
  «Em curso» com prazo vencido, nenhum «Concluído no prazo» com entrega posterior ao
  prazo. Zero inconsistências.
- **Caso-teste.** O Despacho n.º 14284/2024 (passaporte) foi usado como controlo: 12
  entidades membros extraídas automaticamente, coincidentes com a composição do ato;
  três prazos convertidos; estado «Em atraso» com 102 dias, sustentado pela ausência,
  no DR, de qualquer diploma que altere o prazo de validade do passaporte.

---

## 7. Ficheiros

| Ficheiro | Conteúdo |
|---|---|
| `grupos_de_trabalho.xlsx` | Tabela principal, 106 linhas × 31 colunas, com filtros e painéis fixos |
| `grupos_de_trabalho.csv` | O mesmo em CSV (UTF-8 com BOM) |
| `orgaos_relacionados.csv` | Lista separada: 32 comissões, estruturas de missão e task forces |
| `index.html` + `data.js` | Painel interativo |
| `data/acts.json` | Texto integral estruturado dos 106 atos + citações posteriores |
| `judgments.py` | Camada de análise: área, missão, prazos, estado, evidência, notas |
| `dates.py`, `engine.py`, `build.py` | Cálculo de datas, extração e construção |
