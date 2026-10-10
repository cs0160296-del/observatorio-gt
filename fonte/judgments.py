# -*- coding: utf-8 -*-
"""Researched judgment layer, keyed by the creating act's number.

area       - policy area
name_en    - short English handle for the group
mission_en - 1-2 sentence plain-English summary
dl         - deadlines: (label, kind, value, original Portuguese wording)
             kinds: wd=working days from publication, cd=calendar days from publication,
             cds=calendar days from signature, months, date=ISO, q=(year,quarter),
             month_end=(year,month)
primary    - index into dl used for the status/delay calculation (default: last)
status     - exactly one of the seven allowed values
ev         - evidence for the status, with links
delivered  - ISO date used to measure lateness (policy act or report), if known
notes      - caveats; report/policy distinction
"""

NOEV = ("Sem evidência pública de entrega. Pesquisado: (1) Diário da República — "
        "todos os atos publicados entre 2024-04-02 e 2026-10-10 que citam este despacho "
        "(varrimento automático, sem resultados relevantes); (2) sumários do DR na área "
        "temática; (3) pesquisa web (gov.pt, Lusa/Público/Expresso/Observador/ECO).")

J = {}

# ----------------------------------------------------------------- 2024
J["6475/2024"] = dict(
    area="Fundos europeus / Economia", name_en="STEP implementation interministerial group",
    mission_en="Coordinates Portugal's implementation of the EU STEP regulation, mapping funding "
               "instruments and advising on reprogramming RRF and cohesion funds.",
    dl=[("Indicação de representantes — prazo administrativo interno, não é prazo de entrega", "cd", 10,
         "As entidades referidas no n.º 3 devem indicar à Agência, I. P., até 10 dias após a publicação do presente despacho, o respetivo representante")],
    no_primary=True,
    status="Sem informação pública",
    ev="O despacho não fixa prazo de entrega nem data de extinção; não há relatório público. " + NOEV,
    notes="Grupo de coordenação permanente, sem produto datado. Não é possível aferir atraso.")

J["6563/2024"] = dict(
    area="Saúde", name_en="Health access / Emergency Health Plan group",
    mission_en="Drafted the guidelines to improve timely access to health care — the group that "
               "produced the Government's Emergency and Transformation Plan for Health (PETS).",
    dl=[("Relatório final", "cd", 30,
         "O grupo de trabalho deverá apresentar um relatório final que cumpra os objetivos mencionados no n.º 1, no prazo de 30 dias após a entrada em vigor do presente despacho")],
    status="Concluído no prazo", delivered="2024-05-28",
    ev="O PETS, com 54 medidas, foi apresentado pelo Governo a 28/05/2024 "
       "(https://observador.pt/2024/05/28/plano-de-emergencia-para-a-saude-com-incentivos-para-medicos-de-familia-obstetras-e-pediatras-e-foco-na-recuperacao-de-cirurgias/). "
       "O Despacho n.º 10208-A/2024 criou depois um GT para acompanhar a execução do PETS "
       "(https://diariodarepublica.pt/dr/detalhe/despacho/10208-a-2024-886333775).",
    notes="O despacho produz efeitos a 05/04/2024 (retroativo) e só foi publicado a 12/06/2024, "
          "depois de o plano já ter sido apresentado. O relatório do GT não foi publicado; a "
          "entrega é confirmada pela apresentação do PETS. O plano foi entregue; a sua execução "
          "é objeto de crítica pública e de um GT de acompanhamento separado.")

J["6564/2024"] = dict(
    area="Saúde", name_en="SNS 24 obstetrics algorithms group",
    mission_en="Reviews and clinically validates the pregnancy-problem triage algorithms used by "
               "the SNS 24 contact centre.",
    dl=[], status="Sem informação pública",
    ev="O despacho não fixa qualquer prazo. " + NOEV,
    notes="Substituído na prática pelo Despacho n.º 8252/2024 (24/07/2024), que recria o grupo com "
          "cinco membros em vez de três.")

J["6757-A/2024"] = dict(
    area="Energia / Ambiente", name_en="GT-RED III (renewables directive transposition)",
    mission_en="Prepares the transposition of EU Directive 2023/2413 (RED III) on renewable energy "
               "into Portuguese law, in two phases.",
    dl=[("Fase 1 — conclusão", "date", "2024-07-01",
         "A Fase 1 [...] a ser concluída até 1 de julho de 2024"),
        ("Fase 2 — conclusão", "date", "2025-05-21",
         "A Fase 2 [...] a ser concluída até 21 de maio de 2025")],
    status="Concluído no prazo", delivered="2024-12-03",
    ev="Decreto-Lei n.º 99/2024, de 3 de dezembro, altera o quadro regulatório aplicável às "
       "energias renováveis (https://diariodarepublica.pt/dr/detalhe/decreto-lei/99-2024-898705893) "
       "— ato legislativo que concretiza o output do GT, publicado antes do prazo da Fase 2.",
    notes="O relatório do GT não é público; a entrega é inferida do diploma legislativo. A "
          "transposição integral da RED III pode não estar esgotada por este diploma.")

J["7321/2024"] = dict(
    area="Segurança social / Ação social", name_en="Social-response funding formula group",
    mission_en="Defines a funding formula for each social response (creche, lar, etc.) setting how "
               "the State's annual transfers are calculated.",
    dl=[("Apresentação da fórmula", "month_end", (2024, 7),
         "O grupo de trabalho deve apresentar o previsto no número anterior até ao final do mês de julho de 2024")],
    status="Em atraso", ev=NOEV,
    notes="Prazo extremamente curto: o despacho foi publicado a 05/07/2024 e dava até 31/07/2024.")

J["7613/2024"] = dict(
    area="Transportes / Regiões autónomas", name_en="Mobility subsidy review group",
    mission_en="Studies and revises the model of the social mobility subsidy for residents of the "
               "Azores and Madeira travelling to the mainland.",
    dl=[("Relatório final", "date", "2024-09-15",
         "O grupo de trabalho deve concluir os seus trabalhos até 15 de setembro de 2024 com a entrega ao Governo de um relatório final")],
    status="Concluído com atraso", delivered="2025-03-24",
    ev="Decreto-Lei n.º 37-A/2025, de 24 de março, define um novo modelo para a atribuição do "
       "subsídio social de mobilidade (https://diariodarepublica.pt/dr/detalhe/decreto-lei/37-a-2025-912256331) "
       "— exatamente o objeto do GT.",
    notes="O relatório não é público; o atraso é medido até à publicação do novo modelo legal. "
          "O modelo continua contestado: Lei n.º 23/2026 alterou-o por apreciação parlamentar e os "
          "Açores pediram a declaração de inconstitucionalidade (Resolução ALRAA 6/2026/A).")

J["7821/2024"] = dict(
    area="Ambiente / Água", name_en='"Água que Une" water strategy group',
    mission_en="Drafts a new national water-management strategy, framing the National Water Plan "
               "(PNA 2035) and a new irrigation plan (Plano REGA).",
    dl=[("Duração / relatório final", "cds", 180,
         'O Grupo de Trabalho "Água que Une" tem natureza temporária, com a duração de 180 dias, a contar da data da assinatura do presente despacho')],
    status="Concluído com atraso", delivered="2026-06-24",
    ev="Resolução do Conselho de Ministros n.º 133/2026, de 24 de junho, aprova a Estratégia "
       "«Água Que Une» (https://diariodarepublica.pt/dr/detalhe/resolucao-conselho-ministros/133-2026-1138160260).",
    notes="O relatório do GT não foi publicado. O atraso é medido até à aprovação da estratégia em "
          "Conselho de Ministros, 18 meses depois do fim do mandato de 180 dias.")

J["8023/2024"] = dict(
    area="Energia / Habitação", name_en="GT-EPBD (buildings energy performance directive)",
    mission_en="Prepares the transposition of EU Directive 2024/1275 on the energy performance of "
               "buildings, including amendments to Decreto-Lei n.º 101-D/2020.",
    dl=[("Relatório e suporte à consulta pública", "date", "2025-11-30",
         "Relatório e documentação de suporte à consulta pública [...] até 30 de novembro de 2025"),
        ("Relatório final e propostas atualizadas", "date", "2026-01-31",
         "Relatório relativo ao disposto na alínea e) e propostas atualizadas [...] até 31 de janeiro de 2026")],
    status="Em atraso", ev=NOEV,
    notes="O prazo de transposição da Diretiva (UE) 2024/1275 para os Estados-Membros é 29/05/2026; "
          "não há diploma de transposição publicado no DR até 10/10/2026.")

J["8151/2024"] = dict(
    area="Cultura", name_en="Carlos Paredes centenary group",
    mission_en="Prepares the official programme for the centenary of the birth of guitarist "
               "Carlos Paredes.",
    dl=[("Proposta de programa oficial", "month_end", (2024, 9),
         "o Grupo de Trabalho apresenta, até ao final de setembro de 2024, uma proposta de programa oficial das comemorações")],
    status="Em atraso", ev=NOEV,
    notes="O mandato cessa com a apresentação da proposta (n.º 7). Não há despacho de aprovação do "
          "programa oficial publicado no DR.")

J["8251/2024"] = dict(
    area="Educação / Ação social", name_en="Early-childhood education access group",
    mission_en="Diagnoses the creche and pre-school network and proposes a plan to make pre-school "
               "education free and ensure continuity from creche to pre-school.",
    dl=[("Diagnóstico e plano de gratuitidade", "date", "2024-06-28",
         "o grupo de trabalho deve apresentar o previsto nas alíneas a) e b) [...] até 28 de junho de 2024"),
        ("Estratégia de continuidade 0-6 anos", "month_end", (2024, 11),
         "e o previsto na alínea c) do número anterior até ao final do mês de novembro de 2024")],
    status="Em atraso", ev=NOEV,
    notes="O primeiro prazo (28/06/2024) é anterior à própria publicação do despacho (24/07/2024) — "
          "era inexequível à data da publicação.")

J["8252/2024"] = dict(
    area="Saúde", name_en="SNS 24 obstetrics algorithms group (recreated)",
    mission_en="Reviews and clinically validates the SNS 24 obstetrics triage algorithms; replaces "
               "the three-member group created in June 2024 with a five-member one.",
    dl=[], status="Sem informação pública",
    ev="O despacho não fixa qualquer prazo. " + NOEV,
    notes="Recria o grupo do Despacho n.º 6564/2024 com cinco profissionais.")

J["8277/2024"] = dict(
    area="Cultura", name_en="Venice Architecture Biennale 2025 selection group",
    mission_en="Selects Portugal's official representation at the 2025 Venice Architecture Biennale.",
    dl=[("Prazo de candidaturas (prazo para terceiros, não para o GT)", "cd", 30,
         "As candidaturas devem ser enviadas até 30 dias corridos a contar da data de publicação do presente despacho")],
    no_primary=True,
    status="Concluído no prazo", delivered="2024-12-06",
    ev='O GT selecionou 3 de 31 candidaturas; o projeto "Paraíso, Hoje." foi escolhido em dezembro '
       "de 2024 (https://rr.pt/noticia/pais/2024/12/06/paraiso-hoje-representa-portugal-na-bienal-de-veneza-de-arquitetura-em-2025/404844/) "
       "e o pavilhão foi inaugurado a 08/05/2025 "
       "(https://observador.pt/2025/05/08/pavilhao-de-portugal-e-inaugurado-esta-quinta-feira-na-bienal-de-veneza-de-arquitetura/).",
    notes="O despacho não fixa prazo ao GT, apenas às candidaturas. Objetivo cumprido: representação "
          "selecionada e pavilhão realizado.")

J["8335/2024"] = dict(
    area="Economia / Energia", name_en="GT REMPC (critical raw materials regulation)",
    mission_en="Maps the legal changes Portugal needs to comply with EU Regulation 2024/1252 on "
               "critical raw materials.",
    dl=[("Primeiro relatório e plano de ação", "months", 3,
         "O Grupo de Trabalho deverá apresentar o primeiro relatório no prazo de três meses após a entrada em vigor do presente despacho")],
    status="Em atraso", ev=NOEV, notes="Nenhum relatório público; nenhum diploma de conformação publicado.")

J["8344/2024"] = dict(
    area="Desporto", name_en="EPAS ministerial conference organising group",
    mission_en="Organises the 18th Council of Europe EPAS Conference of Sports Ministers held in "
               "Portugal in 2024.",
    dl=[("Fim do funcionamento do GT", "date", "2024-12-31",
         "O funcionamento do Grupo de Trabalho entre 22 de fevereiro de 2024 e 31 de dezembro de 2024")],
    status="Concluído no prazo", delivered="2024-12-31",
    ev="Grupo com mandato até 31/12/2024 destinado a organizar um evento datado (a 18.ª Conferência "
       "EPAS realizou-se em Portugal em 2024). Ato emitido pelo IPDJ, I. P.",
    notes="Ato do IPDJ, I. P. (organismo), não de um gabinete governamental — incluído por criar "
          "formalmente um grupo de trabalho da administração do Estado.")

J["8591/2024"] = dict(
    area="Justiça / Administração interna", name_en='"72 hours" domestic violence group',
    mission_en="Improves what GNR, PSP and PJ do in the 72 hours after a domestic-violence report, "
               "including revising the victim risk-assessment instrument and piloting urgent-response networks.",
    dl=[("Designação de representantes — prazo administrativo interno, não é prazo de entrega", "cd", 10,
         "Os representantes referidos no número anterior são designados no prazo de 10 dias, a contar da data da publicação do presente despacho")],
    no_primary=True,
    status="Sem informação pública",
    ev="Entrega parcial documentada: Portaria n.º 228/2025/1, de 21 de maio, aprova o Instrumento de "
       "Avaliação de Risco em Violência Doméstica revisto (RVD-R) "
       "(https://diariodarepublica.pt/dr/detalhe/portaria/228-2025-918823456), que corresponde a um dos "
       "objetivos do GT. Não há evidência de relatório final nem de extinção. " + NOEV,
    notes="O despacho não fixa prazo final nem data de cessação, pelo que não é possível apurar atraso. "
          "Criado duas semanas depois de o Primeiro-Ministro anunciar o grupo no Parlamento.")

J["8914-A/2024"] = dict(
    area="Cibersegurança / Presidência", name_en="NIS2 cybersecurity transposition group",
    mission_en="Drafts the legislation transposing the EU NIS2 Directive and implementing the "
               "Cybersecurity Act, including ICT cybersecurity certification.",
    dl=[("Projeto legislativo", "date", "2024-09-30",
         "O grupo de trabalho deve apresentar o projeto legislativo referido no n.º 1 até dia 30 de setembro de 2024")],
    status="Concluído com atraso", delivered="2025-12-04",
    ev="Lei n.º 59/2025, de 22 de outubro, concede a autorização legislativa "
       "(https://diariodarepublica.pt/dr/detalhe/lei/59-2025-941547424) e o Decreto-Lei n.º 125/2025, de 4 de "
       "dezembro, que transpõe a Diretiva (UE) 2022/2555 "
       "(https://diariodarepublica.pt/dr/detalhe/decreto-lei/125-2025-962603401).",
    notes="Único GT do universo com senhas de presença expressas: 150 € por reunião. O prazo de "
          "transposição da NIS2 para os Estados-Membros era 17/10/2024; Portugal legislou em dezembro de 2025.")

J["8972/2024"] = dict(
    area="Infância / Ação social", name_en="Children's rights single strategy group",
    mission_en="Evaluates three overlapping national strategies on children's rights, child poverty "
               "and the Child Guarantee, and proposes a single national strategy.",
    dl=[("Avaliação e conclusões", "date", "2024-11-30",
         "o grupo de trabalho apresenta [...] a avaliação e respetivas conclusões [...] até 30 de novembro de 2024"),
        ("Proposta de Estratégia Nacional única", "date", "2024-11-30",
         "apresenta [...] uma proposta de Estratégia Nacional única [...] até 30 de novembro de 2024")],
    status="Concluído com atraso", delivered="2025-02-28",
    ev="Resolução do Conselho de Ministros n.º 34/2025, de 28 de fevereiro, aprova a Estratégia Única "
       "dos Direitos das Crianças e Jovens 2025-2035 "
       "(https://diariodarepublica.pt/dr/detalhe/resolucao-conselho-ministros/34-2025-909307237); o "
       "respetivo Plano de Ação foi aprovado pela RCM n.º 158/2025, de 13 de outubro.",
    notes="Atraso medido até à aprovação da estratégia em Conselho de Ministros; a data de entrega do "
          "relatório do GT não é pública.")

J["9075-A/2024"] = dict(
    area="Administração Pública / Reforma do Estado", name_en="Public Administration reform group",
    mission_en="Prepares and executes the organic and functional reform of the Portuguese public "
               "administration, including concentrating services and government offices in a single site.",
    dl=[("Fim do mandato", "date", "2026-12-31",
         "o mandato do grupo de trabalho termina a 31 de dezembro de 2026"),
        ("Relatório final (mandato + 6 meses)", "date", "2027-06-30",
         "sendo concedido um período adicional de seis meses para a apresentação de relatório sobre os trabalhos desenvolvidos")],
    status="Em curso – dentro do prazo",
    ev="Alterado três vezes (Despacho n.º 3407/2025, Despacho n.º 8479/2025, Despacho n.º 9712-A/2025) e "
       "com nomeações sucessivas de consultores até 2026. Output intermédio: Resolução do Conselho de "
       "Ministros n.º 121/2025, de 12 de agosto, aprova as linhas orientadoras da Reforma dos Ministérios "
       "(https://diariodarepublica.pt/dr/detalhe/resolucao-conselho-ministros/121-2025-928506359).",
    notes="É o GT com maior aparato institucional do período: passou a poder recrutar até 15 "
          "trabalhadores e tem consultores nomeados em comissão de serviço (pagos). Em 2025 passou a ser "
          "tratado nos atos como «Grupo de Trabalho para a Reforma do Estado».")

J["9123/2024"] = dict(
    area="Justiça / Propriedade industrial", name_en="Industrial Property Code revision group",
    mission_en="Analyses the draft amendments to the Industrial Property Code with industry and "
               "professional associations.",
    dl=[("Conclusões", "date", "2024-12-01",
         "O presente Grupo de Trabalho deverá apresentar, até 1 de dezembro de 2024, as conclusões relativas ao projeto de alterações do CPI")],
    status="Em atraso", ev=NOEV, notes="Nenhuma alteração ao Código da Propriedade Industrial publicada no DR no período.")

J["9477/2024"] = dict(
    area="Fronteiras / Administração interna", name_en="EES/ETIAS border systems group",
    mission_en="Monitors the rollout of the EU Entry/Exit System and ETIAS at Portuguese airports and "
               "manages peak-season border control.",
    dl=[("Conclusão dos trabalhos e relatório final", "date", "2025-04-30",
         "O grupo de trabalho deve concluir os trabalhos até 30 de abril de 2025, com possibilidade de prorrogação em caso de decisão europeia de adiamento")],
    status="Em atraso", ev=NOEV,
    notes="O despacho admitia prorrogação se a UE adiasse o EES — o que sucedeu (arranque progressivo do "
          "EES a partir de 12/10/2025) — mas não foi publicada qualquer prorrogação no DR.")

J["9589/2024"] = dict(
    area="Ambiente / Qualidade do ar", name_en="NO2 air-quality group",
    mission_en="Drives air-quality plans in zones exceeding nitrogen-dioxide health-protection limits "
               "(Porto, Matosinhos, Braga, Lisboa).",
    dl=[("Duração inicial", "months", 18,
         "O GT tem natureza temporária, com a duração de 18 meses, prorrogável"),
        ("Prorrogação (18 meses a contar de 13/04/2026)", "date", "2027-10-13",
         "Prorrogar o mandato do grupo de trabalho [...] por um período de 18 meses")],
    status="Prorrogado",
    ev="Despacho n.º 4750/2026, de 13 de abril, prorroga o mandato por 18 meses "
       "(https://diariodarepublica.pt/dr/detalhe/despacho/4750-2026-1084035716).",
    notes="O GT extingue-se apenas quando se verificar o cumprimento consistente dos objetivos de "
          "qualidade do ar para o NO2 — critério material, não temporal.")

J["9648/2024"] = dict(
    area="Habitação / Sem-abrigo", name_en="Homelessness strategy evaluation group",
    mission_en="Evaluates the 2017-2023 national homelessness strategy and proposes the 2025-2030 one.",
    dl=[("Ponto de situação e conclusões", "date", "2024-10-15",
         "O grupo de trabalho extingue-se com a apresentação do ponto de situação [...] no dia 15 de outubro de 2024")],
    status="Concluído com atraso", delivered="2024-12-30",
    ev="Resolução do Conselho de Ministros n.º 208/2024, de 30 de dezembro, aprova a Nova Estratégia "
       "Nacional para a Integração das Pessoas em Situação de Sem-Abrigo 2025-2030 e o respetivo plano "
       "(https://diariodarepublica.pt/dr/detalhe/resolucao-conselho-ministros/208-2024-901536082).",
    notes="Atraso medido até à aprovação da estratégia; a data da entrega do ponto de situação não é pública.")

J["9649/2024"] = dict(
    area="Acessibilidade / Inclusão", name_en="Accessibility rules (DL 163/2006) revision group",
    mission_en="Proposes the revision of Decreto-Lei n.º 163/2006 and its technical accessibility "
               "standards for people with disabilities.",
    dl=[("Prazo inicial (6 meses)", "months", 6,
         "o prazo para a conclusão dos objetivos do grupo de trabalho é de seis meses, prorrogável por três meses"),
        ("Prorrogação", "date", "2025-12-31",
         "É prorrogado até 31 de dezembro de 2025 o mandato do grupo de trabalho constituído pelo Despacho n.º 9649/2024")],
    status="Em atraso",
    ev="Prorrogado até 31/12/2025 pelo Despacho n.º 9463/2025, de 8 de agosto "
       "(https://diariodarepublica.pt/dr/detalhe/despacho/9463-2025-928296838). O prazo prorrogado "
       "expirou sem relatório público nem alteração do Decreto-Lei n.º 163/2006. " + NOEV,
    notes="Este despacho revogou e substituiu um GT anterior (Despacho n.º 10752-A/2023) com o mesmo "
          "objeto — o tema arrasta-se desde 2023.")

J["10208-A/2024"] = dict(
    area="Saúde", name_en="PETS implementation monitoring group",
    mission_en="Monitors implementation of the measures in the Emergency and Transformation Plan for Health.",
    dl=[("Vigência (1 ano a contar de 01/06/2024)", "date", "2025-06-01",
         "O presente despacho produz efeitos a 1 de junho de 2024 e vigorará pelo prazo de um ano, sem prejuízo da possibilidade de prorrogação dos seus efeitos")],
    status="Em atraso", ev=NOEV,
    notes="O coordenador, Carlos Robalo Cordeiro, substituiu Eurico Castro Alves, que saiu em dezembro "
          "de 2024 na sequência de denúncias de conflito de interesses "
          "(https://www.publico.pt/2024/12/12/sociedade/noticia/eurico-castro-alves-pede-sair-comissao-avalia-plano-emergencia-saude-2115461). "
          "Nenhuma prorrogação publicada; nenhum relatório de acompanhamento público.")

J["10559/2024"] = dict(
    area="Energia / Transportes", name_en="GT AFIR (alternative fuels infrastructure)",
    mission_en="Maps the legal changes needed under EU Regulation 2023/1804 and prepares Portugal's "
               "National Policy Framework for alternative-fuels infrastructure.",
    dl=[("Indicação de representantes — prazo administrativo interno, não é prazo de entrega", "cd", 10,
         "As entidades referidas no n.º 3 indicam os representantes ao coordenador, no prazo de 10 dias após a entrada em vigor")],
    no_primary=True,
    status="Sem informação pública",
    ev="O despacho não fixa prazo para o Quadro de Ação Nacional nem data de extinção. " + NOEV,
    notes="O Regulamento AFIR exigia o Quadro de Ação Nacional até 31/12/2025; não há ato publicado no DR.")

J["10989/2024"] = dict(
    area="Justiça / Penal", name_en="Asset-recovery legislation group",
    mission_en="Drafts a bill revising criminal and procedural law on confiscation of the proceeds of "
               "crime, transposing EU Directive 2024/1260.",
    dl=[("Anteprojeto à Ministra da Justiça", "month_end", (2025, 1),
         "O grupo de trabalho deve apresentar o anteprojeto à Ministra da Justiça até ao final do mês de janeiro de 2025")],
    status="Em atraso", ev=NOEV,
    notes="Participação parcialmente remunerada: contrapartida financeira para membros não magistrados "
          "e externos ao Ministério da Justiça. O prazo de transposição da Diretiva (UE) 2024/1260 é "
          "23/11/2026; não há diploma publicado.")

J["11152/2024"] = dict(
    area="Educação", name_en="School bullying group",
    mission_en="Prepares a national anti-bullying campaign, a diagnostic instrument, guides for staff "
               "and pupils, and a reporting channel.",
    dl=[("Cessação do mandato", "date", "2024-12-31",
         "O Grupo de Trabalho cessa o seu mandato no final do ano de 2024")],
    status="Em atraso", ev=NOEV,
    notes="Os objetivos incluíam recomendações a implementar no ano letivo de 2025/2026; não há relatório público.")

J["11271/2024"] = dict(
    area="Administração interna / Formação policial", name_en="Police training pedagogical strategy group",
    mission_en="Prepares a pedagogical strategy for the training schools of the security forces "
               "(GNR, PSP, ISCPSI, Academia Militar).",
    dl=[("Conclusão dos trabalhos", "date", "2024-12-16",
         "O grupo de trabalho deve concluir os trabalhos até 16 de dezembro de 2024"),
        ("Prorrogação", "date", "2025-06-30",
         "A prorrogação, até 30 de junho de 2025, do mandato do grupo de trabalho")],
    status="Em atraso",
    ev="Prorrogado até 30/06/2025 pelo Despacho n.º 2701/2025, de 27 de fevereiro "
       "(https://diariodarepublica.pt/dr/detalhe/despacho/2701-2025-909150575). O prazo prorrogado "
       "expirou sem relatório público. " + NOEV,
    notes="O despacho obriga à entrega de um relatório final na data de cessação (n.º 12); não foi publicado.")

J["11856-A/2024"] = dict(
    area="Migrações / Asilo", name_en="EU Migration and Asylum Pact implementation group",
    mission_en="Prepares, coordinates and executes Portugal's National Implementation Plan for the EU "
               "Pact on Migration and Asylum, including the legislative acts and service reorganisation it requires.",
    dl=[("Fim do mandato", "date", "2026-12-31",
         "Sem prejuízo do cumprimento das metas associadas à execução da reforma, o mandato do grupo de trabalho termina a 31 de dezembro de 2026")],
    status="Em curso – dentro do prazo",
    ev="Coordenado por Manuel Jarmela Palos, ex-diretor do SEF "
       "(https://observador.pt/2024/10/08/nomeado-ex-diretor-do-sef-para-coordenar-grupo-que-vai-gerir-pacto-de-migracao/). "
       "Uma primeira versão do Plano foi entregue em dezembro de 2024 para cumprir prazos da UE e debatida "
       "no Parlamento em janeiro de 2025 "
       "(https://observador.pt/2025/01/16/primeira-versao-do-plano-portugues-do-pacto-europeu-de-migracoes-e-asilo-vai-ser-debatida-esta-quinta-feira/).",
    notes="Tem comissão executiva com trabalhadores em funções públicas a tempo inteiro. A versão final "
          "do Plano não consta do DR.")

J["12071/2024"] = dict(
    area="Saúde", name_en="Medical device reprocessing group",
    mission_en="Evaluates how single-use and reusable surgical medical devices are reprocessed across NHS units.",
    dl=[("Relatório final", "cd", 60,
         "No prazo máximo de 60 dias após a entrada em vigor do presente despacho, o grupo de trabalho remete ao meu Gabinete um relatório final")],
    status="Em atraso", ev=NOEV, notes="")

J["12072/2024"] = dict(
    area="Saúde / Urgências", name_en="Emergency services network reform group",
    mission_en="Evaluates how emergency departments work and the rules for accessing them, proposing a "
               "global reform of the NHS emergency network.",
    dl=[("Relatório final", "cd", 90,
         "No prazo máximo de 90 dias após a entrada em vigor do presente despacho, o grupo de trabalho remete ao meu Gabinete, um relatório final")],
    status="Concluído com atraso", delivered="2026-01-14",
    ev="Decreto-Lei n.º 2/2026, de 14 de janeiro, estabelece um modelo organizativo que prevê o "
       "funcionamento centralizado dos serviços de urgência externa do SNS "
       "(https://diariodarepublica.pt/dr/detalhe/decreto-lei/2-2026-1006464116).",
    notes="O relatório do GT não é público; o atraso é medido até ao diploma que concretiza a reforma. "
          "Em 2026 foram criados novos GTs para as redes de referenciação e para a Rede Nacional de "
          "Urgência e Emergência (Despachos n.os 5900/2026, 7541/2026, 7542/2026, 7543/2026).")

J["12293/2024"] = dict(
    area="Educação", name_en="Teacher professionalisation plan group",
    mission_en="Designs a flexible route for teachers without professional qualification to obtain it "
               "through master's programmes.",
    dl=[("Apresentação do plano", "date", "2025-01-08",
         "O grupo de trabalho apresenta o plano a que se refere o n.º 1 até ao dia 8 de janeiro de 2025")],
    status="Em atraso", ev=NOEV,
    notes="Em setembro de 2025 foi criado um novo GT sobre matéria próxima (habilitação própria para a "
          "docência, Despacho n.º 11297/2025), sem que o plano de 2024 tenha sido tornado público.")

J["12645/2024"] = dict(
    area="Ação social / Educação especial", name_en="Special-education allowance revision group",
    mission_en="Reviews Decreto Regulamentar n.º 3/2016 governing the special-education allowance.",
    dl=[("Conclusões e recomendações", "date", "2025-01-31",
         "É criado um grupo de trabalho com o objetivo de, até 31 de janeiro de 2025, apresentar conclusões e recomendações de alteração ao Decreto Regulamentar n.º 3/2016")],
    status="Em atraso", ev=NOEV, notes="O Decreto Regulamentar n.º 3/2016 não foi alterado no período.")

J["12964/2024"] = dict(
    area="Saúde", name_en="SoHO regulation legal review group",
    mission_en="Reviews Portuguese law on blood, tissues and cells against EU Regulation 2024/1938 and "
               "identifies the competent SoHO authorities.",
    dl=[("Documento de análise e propostas", "cd", 180,
         "no prazo de 180 dias após a entrada em vigor do presente despacho, produzir documento(s) que reflita(m) a análise desenvolvida e as conclusões alcançadas")],
    status="Em atraso", ev=NOEV,
    notes="O Regulamento (UE) 2024/1938 é aplicável a partir de agosto de 2027; a designação das "
          "autoridades competentes não foi publicada.")

J["13345/2024"] = dict(
    area="Saúde / Justiça", name_en="Health in prisons group",
    mission_en="Coordinates health promotion and access to care for people deprived of liberty, and "
               "prepares the transfer of prison health management to the Ministry of Health.",
    dl=[("1.º relatório intercalar semestral", "cd", 182,
         "O grupo de trabalho deve apresentar relatórios intercalares, em cada semestre, aos membros do Governo"),
        ("Vigência — sem data fixa", "none", None,
         "O grupo de trabalho mantém-se em funções durante o mandato do XXIV Governo Constitucional, salvo se vier a ser extinto por despacho")],
    no_primary=True, open_ended=True,
    status="Em curso – dentro do prazo",
    ev="Mandato renovado pelo Despacho n.º 12550/2025, de 27 de outubro "
       "(https://diariodarepublica.pt/dr/detalhe/despacho/12550-2025-942405334), já sob o XXV Governo.",
    notes="Sem data-limite fixa: a vigência estava ligada ao mandato do XXIV Governo e foi expressamente "
          "renovada. Os relatórios semestrais não são públicos.")

J["13355/2024"] = dict(
    area="Saúde / Cuidados primários", name_en="Primary care performance indicators group",
    mission_en="Reviews the performance indices and indicators of primary health care units, including "
               "the USF team performance index (IDE).",
    dl=[("Relatório", "cd", 60,
         "O grupo de trabalho deve apresentar um relatório no prazo de 60 dias contados a partir da data da publicação do presente despacho")],
    status="Em atraso",
    ev="Composição alterada pelo Despacho n.º 14236/2024, de 2 de dezembro "
       "(https://diariodarepublica.pt/dr/detalhe/despacho/14236-2024-898377838), sem alteração de prazo. " + NOEV,
    notes="")

J["13583/2024"] = dict(
    area="Administração Pública", name_en="Public Administration reform change-management group",
    mission_en="Designs and runs the change-management and communication strand of the public "
               "administration reform.",
    dl=[("Duração ligada à Reforma AP (data herdada do GT principal, Despacho n.º 9075-A/2024)", "date", "2026-12-31",
         "O grupo de trabalho tem a duração prevista para a duração do processo de implementação da Reforma AP, extinguindo-se quando a Reforma AP for considerada finalizada")],
    status="Em curso – dentro do prazo",
    ev="Grupo satélite do GT da Reforma da Administração Pública (Despacho n.º 9075-A/2024), cujo mandato "
       "termina a 31/12/2026. Reúne semanalmente nos termos do n.º 5.",
    notes="Sem prazo próprio: extingue-se quando a Reforma AP for dada por concluída. A data usada para o "
          "cálculo é a do mandato do GT principal.")

J["13786/2024"] = dict(
    area="Justiça / Infraestruturas", name_en="Lisbon Justice Campus strategic plan group",
    mission_en="Draws up the national strategic plan for the Lisbon Justice Campus.",
    dl=[("Plano Estratégico (prazo original)", "date", "2025-01-31",
         "Que o presente Grupo de Trabalho deverá apresentar, até ao dia 31 de janeiro de 2025, o referido Plano Estratégico"),
        ("Plano Estratégico (alterado)", "date", "2025-03-31",
         "Que o presente Grupo de Trabalho deverá apresentar, até ao dia 31 de março de 2025, o referido Plano Estratégico")],
    status="Em atraso",
    ev="Prazo alterado para 31/03/2025 pelo Despacho n.º 35/2025, de 2 de janeiro "
       "(https://diariodarepublica.pt/dr/detalhe/despacho/35-2025-901693477). Nenhum plano publicado. " + NOEV,
    notes="Em dezembro de 2025 foi criado um GT equivalente para o Campus da Justiça do Porto "
          "(Despacho n.º 15275/2025), sem que o de Lisboa tenha produzido plano público.")

J["13890/2024"] = dict(
    area="Justiça / Trabalho", name_en="Prisoner labour legal regime group",
    mission_en="Drafts the law governing the special employment relationship of prisoners working in "
               "prison production units (art. 43.º of the Prison Code).",
    dl=[("Anteprojeto e relatório", "months", 12,
         "O grupo de trabalho tem a duração de 12 meses, devendo, no termo desse prazo, apresentar aos membros do Governo o anteprojeto de diploma e um relatório dos trabalhos")],
    status="Em atraso", ev=NOEV, notes="")

J["13946/2024"] = dict(
    area="Justiça", name_en="Alternative dispute resolution (RAL) group",
    mission_en="Relaunches the debate on alternative dispute resolution, mapping obstacles and proposing "
               "measures, with civil-society thematic groups.",
    dl=[("Relatório final", "months", 4,
         "submeter à Secretária de Estado, no prazo de 4 meses a contar da data do presente despacho, um relatório final")],
    status="Em atraso", ev=NOEV, notes="")

J["14013-A/2024"] = dict(
    area="Ambiente / Resíduos", name_en="Waste and landfill emergency group",
    mission_en="Develops the Landfill Emergency Plan and the medium-term strategy for urban and "
               "non-urban waste management.",
    dl=[("Relatório de conclusões e propostas", "date", "2025-01-31",
         "O Grupo de Trabalho apresenta as suas conclusões e propostas ao membro do Governo responsável pela área do ambiente, sob a forma de um relatório organizado por assuntos, até 31 de janeiro de 2025")],
    status="Concluído com atraso", delivered="2026-09-17",
    ev="Resolução do Conselho de Ministros n.º 181/2026, de 17 de setembro, aprova a Estratégia TERRA+ "
       "para 2026-2030 (https://diariodarepublica.pt/dr/detalhe/resolucao-conselho-ministros/181-2026-1171535220).",
    notes="O relatório do GT não é público; o atraso é medido até à aprovação da estratégia, 594 dias "
          "depois do prazo.")

J["14284/2024"] = dict(
    area="Justiça / Documentos de identificação", name_en="New Portuguese passport group",
    mission_en="Designs, builds and rolls out the new Portuguese passport model, including extending "
               "validity from 5 to 10 years and reusing citizen-card biometrics.",
    dl=[("Planeamento das atividades", "wd", 30,
         "O Grupo de Trabalho deve apresentar o planeamento das atividades no prazo máxima de 30 dias úteis após a publicação do presente despacho"),
        ("Relatórios trimestrais", "cd", 90,
         "O Grupo de Trabalho deve apresentar, trimestralmente, um relatório sobre o estado de execução das atividades"),
        ("Novo passaporte disponível", "q", (2026, 2),
         "O Grupo de Trabalho deve orientar as suas atividades de modo a ser possível disponibilizar o novo modelo de passaporte a partir do segundo trimestre de 2026")],
    status="Em atraso",
    ev="O novo passaporte não está disponível a 10/10/2026. Não existe no DR, entre 2024-04-02 e "
       "2026-10-10, qualquer diploma que altere o prazo de validade do passaporte: a única alteração ao "
       "Decreto-Lei n.º 83/2000 no período é a Lei n.º 52/2025, de 7 de abril, sobre passaportes especiais "
       "para funcionários consulares (https://diariodarepublica.pt/dr/detalhe/lei/52-2025-913947254) — "
       "matéria distinta. O alargamento de 5 para 10 anos exige alteração legislativa que não foi publicada. "
       "Nenhum despacho de prorrogação, alteração ou extinção cita o Despacho n.º 14284/2024. " + NOEV,
    notes="CASO-TESTE. Os três prazos do despacho: plano de atividades devido a 16/01/2025 (não público), "
          "relatórios trimestrais (nenhum público), disponibilização do novo passaporte devida até "
          "30/06/2026. A validade de 10 anos NÃO está em vigor. Distinção relatório/política: não há "
          "evidência nem da entrega do GT nem da concretização da política.")

J["14622/2024"] = dict(
    area="Finanças / Setor empresarial do Estado", name_en="Strategic state-owned enterprises group",
    mission_en="Identifies which state-owned enterprises should be classified as strategic.",
    dl=[("Entrega do relatório", "date", "2025-03-31",
         "O relatório a elaborar, de acordo com o n.º 2 do presente despacho, deve ser entregue até ao dia 31 de março de 2025")],
    status="Em atraso", ev=NOEV, notes="")

J["14758/2024"] = dict(
    area="Proteção civil / Bombeiros", name_en="Firefighters' career and benefits group",
    mission_en="Proposes a career framework for professional firefighters in humanitarian associations, "
               "benefits for volunteers, and a training model.",
    dl=[("Relatório final", "cd", 60,
         "Que o grupo de trabalho apresenta ao Secretário de Estado da Proteção Civil um relatório final, com as conclusões do seu trabalho e a formulação de propostas, no prazo de 60 dias após a sua constituição")],
    status="Em atraso", ev=NOEV,
    notes="Prazo contado da constituição do GT (não publicada); calculado a partir da publicação, o que "
          "subestima ligeiramente o atraso.")

J["14926/2024"] = dict(
    area="Infância / Justiça", name_en="CPCJ and adoption regimes group",
    mission_en="Evaluates the child-protection commissions (CPCJ) and the legal regimes for adoption, "
               "civil sponsorship and foster care, and proposes legislative changes.",
    dl=[("Avaliação e propostas (prazo original)", "date", "2025-03-01",
         "O grupo de trabalho apresenta [...] a avaliação e respetivas conclusões, bem como as propostas de alteração legislativa [...] até 1 de março de 2025"),
        ("Prorrogação", "date", "2025-06-01",
         "O grupo de trabalho constituído pelo Despacho n.º 14926/2024 [...] mantém-se em funções até 1 de junho de 2025")],
    status="Em atraso",
    ev="Prorrogado até 01/06/2025 pelo Despacho n.º 3182/2025, de 12 de março "
       "(https://diariodarepublica.pt/dr/detalhe/despacho/3182-2025-910469452). O prazo prorrogado "
       "expirou sem conclusões públicas nem alterações legislativas. " + NOEV,
    notes="")

J["15073/2024"] = dict(
    area="Juventude", name_en="National Youth Agenda group",
    mission_en="Drafts the National Youth Agenda, including its structure, targets, monitoring metrics "
               "and implementation mechanisms.",
    dl=[("Entrega da proposta", "date", "2025-06-30",
         "A proposta da Agenda Nacional da Juventude é entregue durante o primeiro semestre de 2025 ao membro do Governo que tutela a área da juventude")],
    status="Em atraso", ev=NOEV, notes="")

# ----------------------------------------------------------------- 2025
J["382/2025"] = dict(
    area="Energia", name_en="GT-EED (energy efficiency directive)",
    mission_en="Prepares the transposition of EU Directive 2023/1791 on energy efficiency.",
    dl=[("Cronograma dos trabalhos", "cd", 30,
         "Cronograma dos trabalhos de transposição, até 30 dias após a data de publicação do presente despacho"),
        ("Propostas legislativas e regulamentares", "date", "2025-07-31",
         "Apresentar as propostas legislativas e regulamentares, tendo por base as propostas referidas na alínea anterior, até ao dia 31 de julho de 2025")],
    status="Em atraso", ev=NOEV,
    notes="O prazo de transposição da Diretiva (UE) 2023/1791 era 11/10/2025; não há diploma de "
          "transposição publicado no DR até 10/10/2026.")

J["507/2025"] = dict(
    area="Finanças / Fiscalidade", name_en="IMI land cost method group (dams and power plants)",
    mission_en="Defines how the 'added land cost' valuation method in the municipal property tax code "
               "applies, notably to dams and power-generation facilities.",
    dl=[("Recomendações ao Governo", "months", 4,
         "As recomendações referidas no n.º 4 são apresentadas ao Governo no prazo de quatro meses contados desde a publicação deste despacho")],
    status="Em atraso", ev=NOEV, notes="Presidido por uma juíza conselheira; membros renunciaram a remuneração.")

J["986/2025"] = dict(
    area="Saúde", name_en="NHS waste reduction group (GTRD-SNS)",
    mission_en="Diagnoses inefficient use of NHS resources (hospital pharmacy, non-urgent patient "
               "transport, prescribing) and prioritises measures to cut waste.",
    dl=[("Relatório do diagnóstico (45 dias de mandato)", "cd", 46,
         "Até ao final dos primeiros 45 dias de mandato, um relatório a que corresponda o resultado do objetivo referido na alínea a) do n.º 2"),
        ("Mandato (180 dias)", "cd", 181,
         "O mandato do GTRD-SNS tem a duração de 180 dias, a contar da entrada em vigor do presente despacho, sem prejuízo da possibilidade da sua prorrogação")],
    status="Em atraso", ev=NOEV,
    notes="O n.º 12 obriga expressamente a tornar público o relatório final no sítio do SNS — não foi "
          "localizado. É um dos poucos GTs com obrigação legal de publicação do relatório.")

J["1116/2025"] = dict(
    area="Economia / Portos", name_en="Lisbon and Setúbal ports logistics group",
    mission_en="Proposes improvements to customs clearance, direct discharge and logistics operations "
               "at the ports of Lisbon and Setúbal.",
    dl=[("Relatório", "wd", 60,
         "No prazo máximo de 60 dias úteis, o grupo de trabalho apresenta [...] um relatório com os resultados do trabalho realizado e com propostas de melhoria")],
    status="Em atraso", ev=NOEV, notes="O mandato cessa com a apresentação do relatório (n.º 10).")

J["1391/2025"] = dict(
    area="Trabalho / Formação profissional", name_en="Vocational training reform group",
    mission_en="Diagnoses the vocational training system and drafts a proposal for its reform, "
               "including a new legal regime and a common glossary.",
    dl=[("Proposta de Reforma", "date", "2025-09-30",
         "a apresentar ao membro do Governo responsável pela área do trabalho, solidariedade e segurança social, até 30 de setembro de 2025, sem prejuízo de eventual prorrogação"),
        ("Vigência do GT", "date", "2025-10-31",
         "O grupo de trabalho tem natureza temporária e vigora até 31 de outubro de 2025")],
    primary=0,
    status="Em atraso", ev=NOEV,
    notes="Política parcialmente avançada por outra via: Decreto-Lei n.º 42/2026, de 16 de fevereiro "
          "(https://diariodarepublica.pt/dr/detalhe/decreto-lei/42-2026-1051282280), reestrutura o IEFP, I. P., e a Portaria n.º 230/2026/1 aprova os novos estatutos — mas não "
          "há evidência de que resultem do relatório deste GT, que não é público.")

J["1452/2025"] = dict(
    area="Segurança social", name_en="Social Security reform group",
    mission_en="Proposes measures to reform the Portuguese social security system, including an "
               "actuarial review of the contribution rate and a long-term sustainability analysis.",
    dl=[("Relatório de progresso (6 meses)", "date", "2025-07-30",
         "Decorridos 6 meses a contar da data de início de funções, deverá o grupo de trabalho apresentar um relatório de progresso"),
        ("Relatório final (12 meses)", "date", "2026-01-30",
         "O grupo de trabalho inicia funções a 30 de janeiro de 2025, devendo apresentar no prazo de 12 meses um relatório final"),
        ("Relatório final (prorrogado)", "date", "2026-06-30",
         "O relatório final deverá ser apresentado até ao dia 30 de junho de 2026")],
    status="Concluído com atraso", delivered="2026-07-13",
    ev="Prazo prorrogado para 30/06/2026 pelo Despacho n.º 5409/2026, de 24 de abril "
       "(https://diariodarepublica.pt/dr/detalhe/despacho/5409-2026-1090795689). O Governo recebeu o "
       "relatório final em 13/07/2026 "
       "(https://eco.sapo.pt/2026/07/13/governo-ja-recebeu-relatorio-final-sobre-sustentabilidade-da-seguranca-social/) "
       "e o relatório foi apresentado publicamente a 18/08/2026 "
       "(https://eco.sapo.pt/2026/08/18/apresentado-novo-relatorio-sobre-seguranca-social-ultimo-defendia-travao-as-reformas-antecipadas/). "
       "Relatório integral: https://www.dgcp.mtsss.gov.pt/documents/10182/331337/Relatorio_Final_GT_Reforma_Seg_Social_Jun_2026.pdf",
    notes="Coordenado por Jorge Bravo (Nova IMS). Composição alterada pelo Despacho n.º 3519/2025. "
          "Relatório PÚBLICO — um dos poucos casos. A política ainda não aconteceu: o relatório esteve em "
          "consulta até 18/09/2026 e não há legislação de reforma publicada.")

J["1498/2025"] = dict(
    area="Mar / Ambiente", name_en="Ocean acidification action plan group (PACAO)",
    mission_en="Drafts the National Action Plan to Combat Ocean Acidification.",
    dl=[("Proposta de PACAO e suporte à consulta pública", "date", "2025-05-30",
         "O Grupo de Trabalho apresenta a proposta do Plano de Ação para Combate à Acidificação do Oceano e documentação de suporte à consulta pública [...] até ao dia 30 de maio de 2025")],
    status="Em atraso", ev=NOEV, notes="Seis áreas governativas envolvidas; coordenação da DGRM.")

J["2367/2025"] = dict(
    area="Saúde / Cuidados continuados", name_en="RNCCI funding model group",
    mission_en="Proposes changes to how the National Network of Integrated Continuing Care operates "
               "and is financed, including a complexity-adjusted per-diem model.",
    dl=[("Conclusões", "date", "2025-04-30",
         "O grupo de trabalho apresenta as conclusões aos membros do Governo responsáveis pelas áreas da saúde e trabalho, solidariedade e segurança social, até 30 de abril de 2025")],
    status="Em atraso",
    ev="Possível output parcial: Portaria n.º 229/2025/1, de 22 de maio, procede à atualização "
       "extraordinária dos valores por utente/dia da RNCCI "
       "(https://diariodarepublica.pt/dr/detalhe/portaria/229-2025-918999082) — mas é uma atualização de "
       "preços, não a revisão do modelo de funcionamento e financiamento pedida ao GT. " + NOEV,
    notes="O mandato cessa com a apresentação das conclusões (n.º 9), que não são públicas.")

J["2820/2025"] = dict(
    area="Presidência / Setor fundacional", name_en="Foundations legal framework group",
    mission_en="Reviews the legal and regulatory framework for foundations, aiming at simplification "
               "and reduced red tape.",
    dl=[("Relatório final (prazo original)", "date", "2025-12-31",
         "O grupo de trabalho apresenta ao Secretário de Estado da Presidência do Conselho de Ministros um relatório final, com a formulação de propostas legislativas e regulamentares concretas, até ao final do ano de 2025"),
        ("Anteprojeto (mandato renovado)", "date", "2026-12-31",
         "O grupo de trabalho tem por missão elaborar e apresentar [...] até 31 de dezembro de 2026, um anteprojeto de diploma legislativo que concretize a reforma do setor fundacional")],
    status="Prorrogado",
    ev="Mandato renovado e composição revista pelo Despacho n.º 7603/2026, de 18 de junho "
       "(https://diariodarepublica.pt/dr/detalhe/despacho/7603-2026-1133518850), com novo prazo a 31/12/2026.",
    notes="O prazo original (final de 2025) foi ultrapassado sem relatório público; a renovação só ocorreu "
          "em junho de 2026, quase seis meses depois.")

J["2919/2025"] = dict(
    area="Cultura", name_en="Venice Art Biennale 2026 pre-selection group",
    mission_en="Defines and runs the pre-selection stage for Portugal's official representation at the "
               "61st Venice Art Biennale.",
    dl=[], status="Sem informação pública",
    ev="Alterado pelo Despacho n.º 8816/2025, de 29 de julho "
       "(https://diariodarepublica.pt/dr/detalhe/despacho/8816-2025-926748682). A fase de candidaturas foi "
       "aberta pelo Aviso n.º 18915/2025/2, de 29 de julho. Não há ato público que confirme a conclusão "
       "dos trabalhos do GT. " + NOEV,
    notes="O despacho não fixa prazo ao GT — apenas encadeia a seleção a um despacho posterior da Ministra "
          "da Cultura. Não é possível apurar atraso.")

J["2961/2025"] = dict(
    area="Trabalho", name_en="Labour law reform group (Trabalho XXI)",
    mission_en="Advises the Government on reviewing labour legislation and drafting amendments — the "
               "group behind the 'Trabalho XXI' reform.",
    dl=[], status="Concluído no prazo", delivered="2025-07-24",
    ev="O anteprojeto «Trabalho XXI — Flexibilizar para valorizar e crescer» foi aprovado em Conselho de "
       "Ministros a 24/07/2025 "
       "(https://portugal.gov.pt/gc25/comunicacao/documentos/trabalho-xxi-flexibilizar-para-valorizar-e-crescer-anteprojeto-de-reforma-da-legislacao-laboral); "
       "o coordenador do GT foi Pedro Madeira Brito. A proposta de lei foi entregue no Parlamento em maio "
       "de 2026 (https://eco.sapo.pt/2026/05/19/governo-ja-entregou-no-parlamento-proposta-para-rever-lei-laboral-veja-aqui/).",
    notes="O despacho não fixa prazo, pelo que a entrega não pode ser tardia. Distinção relatório/política: "
          "o GT entregou; a reforma legislativa ainda não está aprovada — seguiu para o Parlamento em "
          "maio de 2026 com 50 alterações face ao anteprojeto.")

J["3143/2025"] = dict(
    area="Saúde / Medicamento", name_en="Innovative medicines funding group (1st)",
    mission_en="Evaluates how access to innovative medicines is financed and monitored, and proposes "
               "solutions for equity and financial sustainability.",
    dl=[("Relatório preliminar", "date", "2025-06-16",
         "produzir um relatório preliminar, a apresentar até 16 de junho de 2025"),
        ("Relatório final", "date", "2025-07-15",
         "e um relatório final, a apresentar até 15 de julho de 2025")],
    status="Em atraso",
    ev="Nenhum relatório público. A 05/09/2025 foi criado um novo GT com missão praticamente idêntica "
       "(Despacho n.º 10519/2025, https://diariodarepublica.pt/dr/detalhe/despacho/10519-2025-934179787), "
       "o que sugere que este não concluiu — mas o despacho novo não o revoga expressamente. " + NOEV,
    notes="Sinal de recomeço: dois GTs sucessivos com a mesma missão em seis meses.")

J["3402/2025"] = dict(
    area="Cultura / Património", name_en="Cultural heritage risk governance group",
    mission_en="Strengthens risk governance for cultural heritage, defining strategies to reduce risks "
               "from climate change and natural disasters.",
    dl=[("Relatório", "cd", 365,
         "O Grupo de Trabalho deve apresentar um relatório à Ministra da Cultura [...] no prazo de um ano a contar da data da publicação do presente despacho")],
    status="Em atraso", ev=NOEV, notes="Mandato de um ano, expirado em março de 2026.")

J["3406-A/2025"] = dict(
    area="Ambiente / Litoral", name_en="Barrier islands group (Ria Formosa)",
    mission_en="Reflects on how to implement and schedule measures safeguarding the barrier islands, "
               "with the Algarve regional authorities.",
    dl=[("Relatório detalhado", "date", "2025-12-31",
         "O GT deve apresentar, até ao final do ano, um relatório detalhado e fundamentado sobre as questões referidas no n.º 2 e eventuais propostas")],
    status="Em atraso",
    ev="Retificado pela Declaração de Retificação n.º 368/2025/2, de 10 de abril. " + NOEV, notes="")

J["3518/2025"] = dict(
    area="Saúde / Dados", name_en="European Health Data Space governance group",
    mission_en="Proposes the governance model for implementing the EU European Health Data Space Regulation.",
    dl=[("Primeiro relatório (6 meses)", "cd", 183,
         "No prazo máximo de 6 meses a contar da entrada em vigor do presente despacho, um relatório"),
        ("Relatório final (12 meses)", "cd", 366,
         "No prazo máximo de 12 meses, um relatório final")],
    status="Em atraso", ev=NOEV, notes="Inclui representantes dos Governos Regionais dos Açores e da Madeira.")

J["3675/2025"] = dict(
    area="Ciência / Energia", name_en="Iberian energy storage research centre group",
    mission_en="Coordinates with Spanish scientific partners to create the Iberian Centre for Research "
               "in Energy Storage (CIIAE).",
    dl=[("Relatório", "date", "2025-04-30",
         "O grupo de trabalho deverá apresentar, até ao dia 30 de abril de 2025, um relatório com os contributos e as recomendações adequados ao desenvolvimento das atividades")],
    status="Em atraso", ev=NOEV, notes="Prazo de pouco mais de um mês a contar da publicação.")

J["3918/2025"] = dict(
    area="Saúde", name_en="SIGIC to SINACC transition group",
    mission_en="Prepares the shutdown of the old waiting-list platforms and the move to the new National "
               "Access to Consultation and Surgery System (SINACC).",
    dl=[("Relatório intercalar", "cd", 60,
         "devendo, no prazo de 60 dias, apresentar um relatório intercalar com um diagnóstico sobre os desafios e requisitos para a transição do SIGIC para o SINACC"),
        ("Relatório final / duração", "cd", 180,
         "O grupo de trabalho terá a duração de seis meses [...] e um relatório final, no prazo máximo de 180 dias, com as recomendações e plano de implementação")],
    status="Em atraso",
    ev="Retificado pela Declaração de Retificação n.º 377/2025/2. A 27/11/2025 foi criado um GT sucessor "
       "para apoiar a implementação faseada do SINACC (Despacho n.º 14188/2025), o que sugere continuidade "
       "dos trabalhos, mas não há relatório público. " + NOEV,
    notes="Antecedente: louvor coletivo ao grupo de trabalho para a extinção do SIGIC e criação do SINACC "
          "(Louvor n.º 130/2025, DE-SNS, 06/02/2025).")

J["5725/2025"] = dict(
    area="Cultura / Defesa", name_en="Underwater cultural heritage group (GT-PCS)",
    mission_en="Identifies, studies, protects and monitors underwater cultural heritage in waters under "
               "Portuguese sovereignty and jurisdiction.",
    dl=[("Relatório anual", "cd", 365,
         "apresenta ao Ministério da Defesa Nacional e ao Ministério da Cultura, a partir de 2025, um relatório anual"),
        ("Relatório final de missão", "date", "2029-12-31",
         "e submete o relatório final de missão com o trabalho produzido até 31 de dezembro de 2029")],
    status="Em curso – dentro do prazo",
    ev="Mandato de cinco anos a contar da entrada em vigor; prazo final em 31/12/2029, ainda não decorrido.",
    notes="Os relatórios anuais devidos desde 2025 não são públicos. Co-coordenação entre o Museu de "
          "Marinha e o Centro Nacional de Arqueologia Náutica e Subaquática.")

J["9698/2025"] = dict(
    area="Saúde", name_en='"Ponto Parceiro" regime evaluation group',
    mission_en="Evaluates the impact of the 'Ponto Parceiro' regime in the NHS, weighing its benefits "
               "and financial sustainability.",
    dl=[("Relatório (30 dias após constituição)", "cd", 45,
         "o grupo de trabalho deverá, no prazo de 30 dias após a sua constituição, apresentar um relatório que responda às tarefas elencadas no n.º 1")],
    status="Em atraso", ev=NOEV,
    notes="Prazo contado da constituição; o cálculo soma os 15 dias de designação de representantes aos "
          "30 dias de relatório, a partir da publicação.")

J["10519/2025"] = dict(
    area="Saúde / Medicamento", name_en="Innovative medicines funding group (2nd)",
    mission_en="Evaluates and proposes a funding and monitoring model for access to innovative medicines "
               "— recreates the mandate of the March 2025 group.",
    dl=[("Relatório preliminar", "date", "2025-11-26",
         "produzir um relatório preliminar, a apresentar até 26 de novembro de 2025"),
        ("Relatório final", "date", "2026-01-14",
         "e um relatório final, a apresentar até 14 de janeiro de 2026")],
    status="Em atraso", ev=NOEV,
    notes="Segunda tentativa: repete a missão do Despacho n.º 3143/2025, agora com membros nomeados "
          "individualmente.")

J["10547/2025"] = dict(
    area="Espaço / Negócios estrangeiros", name_en="Interministerial space group (1st)",
    mission_en="Defines Portugal's national positions at the European Space Agency Council and in EU "
               "space programmes.",
    dl=[("Duração", "date", "2028-12-31", "O grupo de trabalho tem duração até 31 de dezembro de 2028")],
    status="Extinto / substituído",
    ev="Revogado pelo Despacho n.º 4643/2026, de 9 de abril, que reconstitui o Grupo de Trabalho "
       "Interministerial para o Espaço com nova composição "
       "(https://diariodarepublica.pt/dr/detalhe/despacho/4643-2026-1082906758).",
    notes="Vigorou sete meses. O grupo sucessor mantém o mesmo prazo final (31/12/2028) e acrescenta os "
          "Governos Regionais dos Açores e da Madeira.")

J["10662/2025"] = dict(
    area="Ensino superior", name_en="Higher education degrees legal regime group",
    mission_en="Revises the legal regime for higher-education degrees and diplomas, in particular the "
               "requirements institutions must meet to award them.",
    dl=[("Relatório final", "date", "2025-10-31",
         "O grupo de trabalho deve apresentar um relatório final, contendo as suas conclusões e propostas, até ao dia 31 de outubro de 2025")],
    status="Em atraso",
    ev="Retificado pela Declaração de Retificação n.º 869/2025/2, de 22 de setembro. " + NOEV,
    notes="Coordenado pela própria Secretária de Estado do Ensino Superior; integra CRUP, CCISP, APESP, "
          "CNE, A3ES e DGES.")

J["10903/2025"] = dict(
    area="Saúde / Defesa", name_en="National strategic reserve (RescEU) group",
    mission_en="Proposes the governance model for the national strategic reserve following the rollout "
               "of the European RescEU reserve in Portugal.",
    dl=[("Relatório final", "cd", 90,
         "O Grupo de Trabalho deverá apresentar um relatório final com as suas propostas no prazo máximo de 90 dias a contar da data da publicação do presente despacho")],
    status="Em atraso", ev=NOEV, notes="")

J["10918/2025"] = dict(
    area="Saúde / Dados", name_en="Health data retention periods group",
    mission_en="Defines how long health data must be kept in the information systems used in primary "
               "and hospital care.",
    dl=[("Relatório intercalar (6 meses)", "cd", 183,
         "No prazo máximo de 6 meses a contar da entrada em vigor do presente despacho, um relatório, com proposta de resposta às alíneas a) a c)"),
        ("Relatório final (12 meses)", "cd", 366,
         "No prazo máximo de 12 meses, o relatório final referido na alínea d) do n.º 4")],
    status="Em atraso", ev=NOEV,
    notes="O mandato admite prorrogação até mais 6 meses, não publicada. Integra representantes de todas "
          "as ULS e dos IPO.")

J["10945/2025"] = dict(
    area="Educação / Digital", name_en='"Digital and AI in Education" group',
    mission_en="Diagnoses digital transition in Portuguese education and sets strategic objectives, "
               "targets and a governance and funding model for digital and AI in education to 2030.",
    dl=[("Diagnóstico", "month_end", (2025, 11),
         "O Grupo de Trabalho deve apresentar o previsto na alínea a) do número anterior até ao final do mês de novembro de 2025"),
        ("Objetivos estratégicos e metas", "month_end", (2026, 3),
         "o previsto na alínea b) até ao final do mês de março de 2026"),
        ("Modelo de governança e plano de implementação", "month_end", (2026, 5),
         "e o previsto na alínea c) até ao final do mês de maio de 2026")],
    status="Em atraso", ev=NOEV,
    notes="O GT tem duração até 31/12/2026, mas os três marcos intercalares já venceram sem entregas "
          "públicas. O atraso é medido ao último marco vencido (31/05/2026).")

J["11297/2025"] = dict(
    area="Educação", name_en="Teaching qualification requirements group",
    mission_en="Defines the requirements and procedures for holders of pre- and post-Bologna degrees to "
               "obtain their own teaching qualification for basic and secondary education.",
    dl=[("Relatório preliminar", "date", "2025-10-06",
         "O grupo de trabalho deve apresentar um Relatório Preliminar, contendo as suas conclusões e propostas, até ao dia 6 de outubro de 2025")],
    status="Em atraso", ev=NOEV,
    notes="Prazo de 11 dias a contar da publicação (25/09/2025). Nenhum relatório público.")

J["11412-A/2025"] = dict(
    area="Ciência e inovação", name_en="R&I institutions legal regime group",
    mission_en="Revises the legal regime, recognition, evaluation and funding of research and innovation "
               "institutions in the national science and technology system.",
    dl=[("Relatório final", "date", "2026-02-28",
         "O grupo de trabalho deve apresentar um relatório final até ao dia 28 de fevereiro de 2026")],
    status="Em atraso", ev=NOEV,
    notes="Coordenado por dois Secretários de Estado. Em fevereiro de 2026 foi criado outro GT sobre o "
          "ecossistema de I&I (Despacho n.º 1994/2026), sem relatório público deste.")

J["11649/2025"] = dict(
    area="Saúde", name_en="Chronic disease prevention group",
    mission_en="Analyses NHS strategies for preventing and managing chronic disease and proposes an "
               "implementation plan.",
    dl=[("Relatório final", "cd", 120,
         "no prazo de 120 dias a contar da data de entrada em vigor do presente despacho, remeter ao meu Gabinete o relatório previsto na alínea d) do n.º 1")],
    status="Em atraso", ev=NOEV, notes="")

J["11843/2025"] = dict(
    area="Energia", name_en="Gas and hydrogen markets directive group",
    mission_en="Prepares the transposition of EU Directive 2024/1788 on common rules for the internal "
               "markets in renewable gas, natural gas and hydrogen.",
    dl=[("Identificação de diplomas a emitir/alterar", "date", "2025-11-30",
         "Até 30 de novembro de 2025: Identificação dos diplomas legais e regulamentares a emitir e a alterar")],
    status="Em atraso", ev=NOEV,
    notes="O prazo de transposição da Diretiva (UE) 2024/1788 é 05/08/2026; não há diploma publicado no DR.")

J["14188/2025"] = dict(
    area="Saúde", name_en="SINACC implementation support group",
    mission_en="Supports the phased rollout of the National Access to Consultation and Surgery System "
               "(SINACC), harmonising indicators with the Transparency Portal.",
    dl=[("Cessação do mandato — evento, sem data", "none", None,
         "O mandato do grupo de trabalho cessa com a publicação do decreto-lei que procede à criação do SINACC, bem como da regulamentação complementar nele prevista")],
    no_primary=True, open_ended=True,
    status="Em curso – dentro do prazo",
    ev="Louvor n.º 317/2026, de 3 de junho, concede louvor a Cláudia Belo Ferreira pelo trabalho "
       "desempenhado neste GT (https://diariodarepublica.pt/dr/detalhe/louvor/317-2026-1129395626) — "
       "evidência de atividade. O decreto-lei do SINACC não foi publicado até 10/10/2026.",
    notes="O mandato está ligado a um evento (publicação do DL do SINACC), não a uma data: não é possível "
          "apurar atraso formal. A data usada no cálculo é convencional e não corresponde a um prazo do ato.")

J["14492/2025"] = dict(
    area="Economia / Energia", name_en="Fluid transport legislation group (GT-ANLTF)",
    mission_en="Identifies substances whose pipeline transport is not properly regulated and the "
               "regulatory gaps, with a view to a legislative proposal.",
    dl=[("Relatório final (4 meses após início)", "cd", 130,
         "As entidades que integram o GT apresentam o relatório final no prazo de 4 meses após o início dos trabalhos")],
    status="Em atraso", ev=NOEV,
    notes="O início dos trabalhos não é público; o cálculo soma os 10 dias de designação de "
          "representantes aos 4 meses, a contar da publicação.")

J["14507/2025"] = dict(
    area="Agricultura / Ambiente", name_en="Pesticides action plan revision group (PANUSPF)",
    mission_en="Revises the National Action Plan for the Sustainable Use of Plant Protection Products.",
    dl=[("Projeto a consulta pública", "date", "2025-12-31",
         "Preparar e submeter a consulta pública até 31 de dezembro de 2025 um projeto de PANUSPF revisto"),
        ("Entrega da versão final (1 mês após a consulta)", "date", "2026-01-31",
         "Proceder, no prazo de um mês após o termo do prazo da consulta pública do projeto do PANUSPF revisto, à entrega da versão final")],
    status="Concluído com atraso", delivered="2026-03-19",
    ev="Portaria n.º 119/2026/1, de 19 de março, aprova o Plano de Ação Nacional para o Uso Sustentável "
       "dos Produtos Fitofarmacêuticos — 2.ª Revisão, declarando expressamente que foi «elaborado pelo "
       "grupo de trabalho designado através do Despacho n.º 14507/2025» "
       "(https://diariodarepublica.pt/dr/detalhe/portaria/119-2026-1074104065).",
    notes="Um dos raros casos em que o ato de aprovação identifica o GT autor. A data de entrega do GT não "
          "é pública: o atraso é medido até à publicação da portaria, pelo que é um limite superior.")

J["15275/2025"] = dict(
    area="Justiça / Infraestruturas", name_en="Porto Justice Campus strategic plan group",
    mission_en="Draws up the national strategic plan for the Porto Justice Campus.",
    dl=[("Plano Estratégico (relatório)", "date", "2026-05-31",
         "O referido Plano Estratégico deve ser apresentado pelo presente Grupo de Trabalho, sob a forma de relatório, até ao dia 31 de maio de 2026")],
    status="Em atraso", ev=NOEV,
    notes="Replica a estrutura do GT do Campus da Justiça de Lisboa (Despacho n.º 13786/2024), que também "
          "não entregou publicamente.")

J["15438/2025"] = dict(
    area="Saúde", name_en="Haematopoietic stem cell transplant network group",
    mission_en="Designs the national network and integrated system for haematopoietic progenitor cell "
               "transplantation, including a Portuguese registry (RPTPH).",
    dl=[("Relatório final", "cd", 120,
         "elaborar, no prazo de 120 dias contados da data da sua entrada em vigor, um relatório final que contenha a análise desenvolvida, as conclusões alcançadas e as propostas concretas")],
    status="Em atraso", ev=NOEV, notes="")

# ----------------------------------------------------------------- 2026
J["661/2026"] = dict(
    area="Defesa / Cooperação", name_en="Cape Verde EPF assistance measure group",
    mission_en="Implements the European Peace Facility assistance measure for Cape Verde, overseeing "
               "procurement and project execution.",
    dl=[("Comunicação de representantes — prazo administrativo interno, não é prazo de entrega", "wd", 5,
         "Determinar que as entidades referidas no número anterior comunicam à DGAPDN os seus representantes no GT-MEAP/CV, no prazo de 5 dias úteis após assinatura do presente despacho")],
    no_primary=True,
    status="Sem informação pública",
    ev="O despacho não fixa prazo de entrega nem data de extinção. " + NOEV,
    notes="Grupo de execução de um projeto financiado pela UE, sem produto datado.")

J["831/2026"] = dict(
    area="Trabalho / Cultura", name_en="Calceteiros and Portuguese pavement group",
    mission_en="Proposes measures to safeguard and upgrade the calceteiro trade and Portuguese pavement, "
               "including training and working conditions.",
    dl=[("Relatório final (6 meses)", "cd", 182,
         "O Grupo de Trabalho apresenta um relatório final com propostas e recomendações de intervenção legislativa ou outras, no prazo de deis [seis] meses a contar da data de entrada em vigor do presente despacho"),
        ("Prorrogação (6 meses a contar de 04/08/2026)", "date", "2027-02-04",
         "prorroga-se o prazo de vigência do Grupo de Trabalho que apresenta relatório final [...] no prazo de seis meses a contar da data de entrada em vigor do presente despacho")],
    status="Prorrogado",
    ev="Despacho n.º 9701/2026, de 3 de agosto, designa os representantes e prorroga o prazo de vigência "
       "(https://diariodarepublica.pt/dr/detalhe/despacho/9701-2026-1153917423).",
    notes="Os representantes só foram designados mais de seis meses depois da criação do grupo, no mesmo "
          "ato que prorrogou o prazo — ou seja, o GT esteve praticamente todo o primeiro mandato por "
          "constituir. O despacho original contém a gralha «deis meses».")

J["1994/2026"] = dict(
    area="Ciência e inovação", name_en="R&I ecosystem analysis group",
    mission_en="Analyses Portugal's research and innovation ecosystem — scientific capacity, technology "
               "transfer, results and international positioning.",
    dl=[("Relatório final técnico", "date", "2026-02-24",
         "o grupo de trabalho, até ao dia 24 de fevereiro, produz e apresenta [...] um relatório final técnico")],
    status="Em atraso", ev=NOEV,
    notes="Prazo de sete dias a contar da publicação (17/02/2026) — um dos mais curtos do universo.")

J["3089/2026"] = dict(
    area="Habitação / Fundos europeus", name_en="Affordable housing Portugal 2030 group",
    mission_en="Defines guidelines for Portugal 2030 investment in affordable housing and monitors the "
               "related calls for applications.",
    dl=[("Indicação de representantes — prazo administrativo interno, não é prazo de entrega", "cd", 5,
         "As entidades referidas no n.º 4 devem indicar à Agência, I. P., até 5 dias após a publicação do presente despacho, o respetivo representante")],
    no_primary=True,
    status="Sem informação pública",
    ev="O despacho não fixa prazo de entrega nem data de extinção. " + NOEV,
    notes="Grupo de acompanhamento de fundos, sem produto datado.")

J["3317/2026"] = dict(
    area="Educação", name_en="Prohibited school activities guidelines group",
    mission_en="Produces guidance for school heads on barring activities by outside entities or "
               "individuals deemed contrary to the purposes and democratic values of education.",
    dl=[("Relatório final / cessação", "date", "2026-03-31",
         "O Grupo de Trabalho cessa o seu mandato no dia 31 de março, com a apresentação de um relatório final dos trabalhos")],
    status="Em atraso", ev=NOEV,
    notes="Prazo de 18 dias a contar da publicação (13/03/2026); representantes a designar em dois dias.")

J["3808/2026"] = dict(
    area="Ação social", name_en="Family creche and childminders group",
    mission_en="Studies the redefinition of the family creche social response and simplification of "
               "access to the childminder (ama) profession.",
    dl=[], status="Sem informação pública",
    ev="O n.º 7 obriga à apresentação de um relatório final mas não fixa data; o mandato cessa com a "
       "entrega. " + NOEV,
    notes="Sem prazo no ato: não é possível apurar atraso.")

J["3965/2026"] = dict(
    area="Defesa / Fundos europeus", name_en="Defence sector Portugal 2030 group",
    mission_en="Defines guidelines for Portugal 2030 support to the defence sector and monitors the "
               "related calls.",
    dl=[], status="Sem informação pública",
    ev="O despacho não fixa prazo de entrega nem data de extinção. " + NOEV,
    notes="Gémeo do GT da habitação acessível (Despacho n.º 3089/2026), com a mesma arquitetura.")

J["4319/2026"] = dict(
    area="Economia / Relações bilaterais", name_en="Portugal-Spain Strategic Forum support group",
    mission_en="Provides technical support to the Portugal-Spain Strategic Forum for Greater "
               "Competitiveness, tracking commitments on grid interconnections, e-invoicing and "
               "cross-border procurement.",
    dl=[("Relatório — 30 dias antes de cada reunião ministerial (data não fixada no ato)", "none", None,
         "O relatório referido no número anterior deve ser apresentado [...] com, pelo menos, 30 dias de antecedência relativamente às reuniões ministeriais do Fórum Estratégico Luso-Espanhol para uma Maior Competitividade")],
    no_primary=True, open_ended=True,
    status="Em curso – dentro do prazo",
    ev="Prazo associado a eventos (reuniões ministeriais do Fórum), sem data fixa no ato.",
    notes="Não é possível apurar atraso: o prazo depende do calendário das cimeiras. A data usada no "
          "cálculo é convencional.")

J["4643/2026"] = dict(
    area="Espaço / Negócios estrangeiros", name_en="Interministerial space group (2nd)",
    mission_en="Defines Portugal's positions at the ESA Council and in EU space programmes; replaces the "
               "September 2025 group and adds the Azores and Madeira regional governments.",
    dl=[("Relatório anual", "cd", 365,
         "O Grupo de Trabalho apresenta ao Conselho de Ministros um relatório anual com a descrição dos trabalhos desenvolvidos"),
        ("Duração", "date", "2028-12-31", "O Grupo de Trabalho tem duração até 31 de dezembro de 2028")],
    status="Em curso – dentro do prazo",
    ev="Revoga e substitui o Despacho n.º 10547/2025. Prazo final em 31/12/2028, ainda não decorrido.",
    notes="Composto por membros do Governo (nível ministerial), não por representantes técnicos.")

J["4749/2026"] = dict(
    area="Finanças locais", name_en="Local Finance Law revision group",
    mission_en="Revises the Local and Intermunicipal Finance Regime (Lei n.º 73/2013), including "
               "borrowing limits, shared services between municipalities and transparency.",
    dl=[("Projeto de alterações legislativas e relatório", "date", "2026-12-31",
         "O Grupo de Trabalho apresenta ao Governo um projeto de alterações legislativas, acompanhado de um relatório justificativo das alterações propostas, até ao final de 2026")],
    status="Em curso – dentro do prazo", ev="Prazo em 31/12/2026, ainda não decorrido.",
    notes="Coordenado pelo Secretário de Estado da Administração Local e Ordenamento do Território.")

J["5900/2026"] = dict(
    area="Saúde", name_en="Cardiology referral networks group",
    mission_en="Drafts the hospital referral networks for cardiology, cardiac surgery and thoracic "
               "surgery, including an emergency services network.",
    dl=[("Propostas de redes", "cd", 90,
         "O grupo de trabalho deverá apresentar, no prazo de 90 dias, propostas de redes de referenciação hospitalar de cardiologia, de cirurgia cardíaca e de cirurgia torácica")],
    status="Em atraso", ev=NOEV, notes="")

J["6859/2026"] = dict(
    area="Justiça / Penal", name_en="Criminal procedure reform group",
    mission_en="Drafts a bill reforming criminal procedure — appeals, the instruction phase, and the "
               "speed and effectiveness of criminal proceedings.",
    dl=[("Anteprojeto à Ministra da Justiça", "date", "2026-07-31",
         "O grupo de trabalho deve apresentar o anteprojeto à Ministra da Justiça até dia 31 de julho de 2026")],
    status="Em atraso", ev=NOEV,
    notes="Participação remunerada por ajudas de custo; para membros sem vínculo público aplica-se o "
          "montante fixado para a remuneração. Ligado à Agenda Anticorrupção.")

J["6941/2026"] = dict(
    area="Energia", name_en="Electricity grid access reform group (GT-Acesso-RESP)",
    mission_en="Prepares the reform of the model for accessing the public electricity grid for "
               "generation, storage and consumption projects.",
    dl=[("Constituição do GT pela DGEG", "cd", 20,
         "No prazo de 20 dias a contar da entrada em vigor do presente despacho, a DGEG deverá assegurar a constituição do GT-Acesso-RESP"),
        ("Vigência (1 ano)", "cd", 366,
         "O GT-Acesso-RESP mantém-se em atividade pelo prazo de um ano a contar da data de entrada em vigor do presente despacho, até à publicação no Diário da República das propostas de alterações legislativas")],
    status="Em curso – dentro do prazo", ev="Prazo de um ano, a terminar em junho de 2027.", notes="")

J["7229/2026"] = dict(
    area="Trabalho / Segurança e saúde", name_en="General Occupational Safety and Health Act group",
    mission_en="Drafts a proposal for a General Act on Occupational Safety and Health, consolidating "
               "the scattered legislation.",
    dl=[("Calendário — conclusão no 3.º trimestre de 2026", "q", (2026, 3),
         "O calendário do desenvolvimento dos trabalhos é o seguinte: [...] Atividade 2.º Q 3.º Q [...]")],
    status="Em atraso", ev=NOEV,
    notes="O prazo resulta de uma tabela de calendário por trimestres no n.º 5 do despacho, não de uma "
          "data expressa; o último trimestre previsto (3.º de 2026) terminou a 30/09/2026. "
          "Interpretação do analista — ver nota metodológica.")

J["7381/2026"] = dict(
    area="Justiça / Família", name_en="Hague Conventions implementation group",
    mission_en="Drafts legislation ensuring application of the 1980 and 1996 Hague Conventions and the "
               "Brussels II ter Regulation on child abduction and parental responsibility.",
    dl=[("Apresentação das propostas", "date", "2026-12-31",
         "As propostas do Grupo de Trabalho devem ser apresentadas até ao final do ano de 2026")],
    status="Em curso – dentro do prazo", ev="Prazo em 31/12/2026, ainda não decorrido.", notes="")

J["7541/2026"] = dict(
    area="Saúde", name_en="Orthopaedics referral network group",
    mission_en="Drafts the hospital referral network for orthopaedics, including an emergency services network.",
    dl=[("Proposta de rede", "cd", 90,
         "Deve proceder-se à elaboração de proposta da Rede de Referenciação Hospitalar de Ortopedia, incluindo uma rede de serviços de urgência [...] no prazo de 90 dias")],
    status="Em atraso", ev=NOEV, notes="")

J["7542/2026"] = dict(
    area="Saúde / Urgências", name_en="National Urgency and Emergency Network group",
    mission_en="Drafts the update of the National Urgency and Emergency Network, including centralised "
               "emergency departments.",
    dl=[("Proposta sobre Urgências Centralizadas", "date", "2026-11-27",
         "ressalvando o respeitante às Urgências Centralizadas, que deve ser objeto de proposta até 27 de novembro de 2026"),
        ("Mandato (1 ano)", "cd", 366,
         "É definido o mandato de um ano contado a partir da data de produção de efeitos do presente despacho")],
    primary=0,
    status="Em curso – dentro do prazo", ev="Primeiro marco em 27/11/2026, ainda não decorrido.",
    notes="Sucede, em parte, ao GT de reforma das urgências de 2024 (Despacho n.º 12072/2024).")

J["7543/2026"] = dict(
    area="Saúde", name_en="Immunoallergology referral network group",
    mission_en="Drafts the hospital referral network for immunoallergology.",
    dl=[("Proposta de rede", "cd", 90,
         "Deve proceder-se à elaboração de proposta da Rede de Referenciação Hospitalar de Imunoalergologia [...] no prazo de 90 dias")],
    status="Em atraso", ev=NOEV, notes="")

J["7971/2026"] = dict(
    area="Finanças", name_en="Treasury Cash Offices reorganisation group",
    mission_en="Analyses and reorganises the Treasury Cash Offices within public financial "
               "administration and the State's collection network.",
    dl=[("Primeiro relatório (6 meses)", "cd", 183,
         "No prazo de 6 meses a contar da data de entrada em vigor [...] apresentar ao Ministro de Estado e das Finanças"),
        ("Funcionamento (12 meses)", "cd", 366,
         "O Grupo de Trabalho funcionará pelo período de 12 meses a contar da data da entrada em vigor do presente despacho")],
    primary=0,
    status="Em curso – dentro do prazo", ev="Primeiro relatório devido em dezembro de 2026.", notes="")

J["144/2026"] = dict(
    area="Finanças regionais", name_en="Regional Finance Law revision group",
    mission_en="Reviews the Regional Finance Law governing the financing of the Azores and Madeira.",
    dl=[("Relatório final", "date", "2027-12-31",
         "Estabelecer que, até 31 de dezembro de 2027, o grupo de trabalho apresenta ao Governo um relatório final")],
    status="Em curso – dentro do prazo", ev="Prazo em 31/12/2027, ainda não decorrido.",
    notes="Único GT do período criado por Resolução do Conselho de Ministros (1.ª série) e não por despacho.")

J["8971/2026"] = dict(
    area="Justiça / Tráfico de seres humanos", name_en="Trafficking victims legal regime group",
    mission_en="Drafts the legal regime for the protection and assistance of victims of human trafficking.",
    dl=[("Proposta de regime jurídico", "cd", 150,
         "O Grupo de Trabalho apresenta à tutela coordenadora uma proposta de regime jurídico [...] no prazo de 150 dias, sem prejuízo de eventual prorrogação")],
    status="Em curso – dentro do prazo", ev="Prazo a terminar em dezembro de 2026.", notes="")

J["9999/2026"] = dict(
    area="Violência doméstica", name_en="Domestic violence shelter responses group",
    mission_en="Evaluates, plans, finances and monitors shelter and autonomy responses for victims of "
               "domestic violence.",
    dl=[("Relatório final", "cd", 90,
         "O grupo de trabalho apresenta, no prazo de 90 dias, um relatório final contendo o diagnóstico efetuado e a formulação de recomendações")],
    status="Em curso – dentro do prazo", ev="Prazo a terminar em novembro de 2026.", notes="")

J["10174/2026"] = dict(
    area="Coesão territorial", name_en="Low-density territories criteria group",
    mission_en="Reappraises the criteria defining low-density territories and proposes regional "
               "development policies.",
    dl=[("Relatório final", "cd", 183,
         "O Grupo de Trabalho tem natureza temporária e deve apresentar o seu relatório final no prazo de seis meses a contar da data da publicação do presente despacho")],
    status="Em curso – dentro do prazo", ev="Prazo a terminar em fevereiro de 2027.", notes="")

J["11130/2026"] = dict(
    area="Igualdade / Cidadania", name_en="Harmful practices prevention group",
    mission_en="Prevents and combats harmful practices — early and forced child marriage, female genital "
               "mutilation and honour crimes.",
    dl=[("Duração (182 dias)", "cd", 182,
         "O Grupo de Trabalho tem natureza temporária, com duração de 182 dias a contar da data de publicação do presente despacho")],
    status="Em curso – dentro do prazo", ev="Prazo a terminar em março de 2027.", notes="")

J["11488/2026"] = dict(
    area="Transportes / Ferrovia", name_en="Rail punctuality group",
    mission_en="Diagnoses the causes of rail delays and proposes improvements, with an action plan.",
    dl=[("Relatório com diagnóstico e propostas", "cd", 122,
         "O Grupo de Trabalho entrega, no prazo de quatro meses após a publicação do presente despacho, um relatório contendo o diagnóstico da pontualidade ferroviária e as respetivas propostas de melhoria")],
    status="Em curso – dentro do prazo", ev="Prazo a terminar em janeiro de 2027.", notes="")

J["11672/2026"] = dict(
    area="Administração interna / Segurança privada", name_en="Private security regime revision group",
    mission_en="Revises the legal regime for private security activity (Lei n.º 34/2013) and related "
               "regulation.",
    dl=[("Proposta de alteração legislativa (6 meses após início)", "cd", 193,
         "O grupo de trabalho dispõe de um prazo de seis meses, contado da data referida no número anterior, para apresentar ao Secretário de Estado da Administração Interna uma proposta de alteração legislativa")],
    status="Em curso – dentro do prazo",
    ev="O GT inicia funções 10 dias após a publicação; prazo a terminar em abril de 2027.", notes="")
