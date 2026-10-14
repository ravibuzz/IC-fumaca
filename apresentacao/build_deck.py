"""Gera a apresentação do VIII SEMICA sobre o modelo oficial.

Uso:  python3 build_deck.py  [saida.pptx]
"""
from __future__ import annotations

import sys
from pathlib import Path

from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

from deck_lib import (ASSETS, AMBER, BOT, BOT_T, GOLD, GOLD_TINT, GRAY, GREEN, GREEN_TINT, INK, L, LIGHT, NAVY,
                      NAVY_DARK, NAVY_TINT, R, RED, RED_TINT, TEAL, TEAL_TINT, TOP, WHITE, Deck, bar_chart, card,
                      circle, fill_text, icon, icon_badge, line, pic, rect, rgb, stat, table, tb)

FIG = ASSETS / "figuras"
IMG = ASSETS / "imagens"
TEMPLATE = ASSETS / "modelo" / "modelo_oficial_semica.pptx"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent / "SEMICA_Fumaca_Cirurgica_Baccaro.pptx"

TITULO = ("Sintomas, desfechos objetivos e biomarcadores em profissionais de centro cirúrgico "
          "ocupacionalmente expostos à fumaça cirúrgica: revisão sistemática e metanálise de prevalência")

deck = Deck(TEMPLATE)
prs = deck.prs

# =====================================================================
# SLIDE 1 — CAPA (edita o slide do modelo)
# =====================================================================
capa = prs.slides[0]
shapes = {s.name: s for s in capa.shapes}
tit = shapes["CaixaDeTexto 5"]          # "TÍTULO: ..."
aut = shapes["CaixaDeTexto 4"]          # "Autor(a): / Orientador(a):"
tit.left, tit.top, tit.width, tit.height = Inches(2.6), Inches(5.35), Inches(14.8), Inches(1.75)
tf = tit.text_frame
tf.clear()
tf.word_wrap = True
fill_text(tf, [{"runs": [(TITULO, {})], "align": PP_ALIGN.CENTER}], size=32, color=NAVY, bold=True,
          space_after=0, line_spacing=1.0, font="Calibri")
aut.left, aut.top, aut.width, aut.height = Inches(4.0), Inches(7.25), Inches(12.0), Inches(1.7)
tf = aut.text_frame
tf.clear()
tf.word_wrap = True
fill_text(tf, [
    {"runs": [("Autor: ", {"bold": True}), ("Theo Augusto Lopes de Moraes Báccaro", {})], "align": PP_ALIGN.CENTER},
    {"runs": [("Orientadora: ", {"bold": True}), ("Profa. Lisie Tocci Justo", {})], "align": PP_ALIGN.CENTER},
    {"runs": [("Coautores: Luiz Henrique Ledesma Pereira; Mariana Matera Veras (LIM05, HC-FMUSP)",
               {"size": 18, "color": GRAY})], "align": PP_ALIGN.CENTER, "space_before": 6},
], size=24, color=INK, space_after=4, font="Tahoma")
deck.notes(capa, """[0:00–0:15] CAPA
Bom dia a todos. Meu nome é Theo Báccaro, sou aluno de Medicina da São Leopoldo Mandic de Araras. Vou apresentar a Iniciação Científica que desenvolvi ao longo de um ano, sob orientação da Profa. Lisie Tocci Justo, com a colaboração do Luiz Henrique Ledesma Pereira e da Dra. Mariana Matera Veras, do LIM05 da USP.
O trabalho é uma revisão sistemática com metanálise de prevalência sobre os efeitos à saúde da exposição ocupacional à fumaça cirúrgica na equipe de centro cirúrgico.

DICA: fale o título de forma natural, sem ler palavra por palavra. Respire e vá para o próximo slide.""")

# remove os slides-modelo 2..10 (índices 1..9); o slide 11 (encerramento) é preservado
deck.remove_slides(range(1, 10))

# =====================================================================
# SLIDE 2 — INTRODUÇÃO
# =====================================================================
s = deck.content_slide("INTRODUÇÃO", "Fumaça cirúrgica: o que é e por que importa")
pic(s, IMG / "centro_cirurgico_fumaca.png", L, 1.9, w=8.3, name="Foto centro cirúrgico")
tb(s, L, 6.6, 8.3, 0.35, ["Imagem ilustrativa (gerada por IA): pluma de fumaça do eletrocautério no campo cirúrgico."],
   size=13, color=GRAY, space_after=0)
# sintomas agudos
rect(s, L, 7.05, 8.3, 2.45, fill=NAVY_TINT)
tb(s, L + 0.3, 7.2, 7.7, 0.45, ["Sintomas agudos relatados pela equipe exposta"], size=19, color=NAVY, bold=True,
   space_after=0)
for i, (ic, txt) in enumerate([("eye", "Irritação ocular e lacrimejamento"),
                               ("lungs", "Tosse e irritação das vias aéreas e mucosas"),
                               ("exclaim", "Cefaleia e náusea")]):
    yy = 7.75 + i * 0.55
    icon(s, ic, L + 0.35, yy + 0.02, 0.4, color="navy")
    tb(s, L + 0.95, yy, 7.0, 0.5, [txt], size=18, color=INK, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
# coluna direita: 4 linhas com ícone
rows = [
    ("smoke", "O que é", "Subproduto da destruição térmica dos tecidos por dispositivos de energia: eletrocautério "
                         "(bisturi elétrico), laser e bisturi ultrassônico (Benaim; Jaspers, 2024)."),
    ("flask", "O que contém", "Hidrocarbonetos aromáticos policíclicos, compostos orgânicos voláteis (benzeno, tolueno, "
                              "xileno), material particulado ultrafino (PM2,5) e material genético viral, como o HPV."),
    ("warning", "O que se sabe (e o que não se sabe)", "Sintomas agudos são frequentes. Efeitos crônicos (neoplasias, doença "
                                                      "respiratória) são plausíveis, mas sem relação causal estabelecida; o tema "
                                                      "é controverso (Hurst; Stewart, 2024)."),
    ("shield", "Por que importa", "Exaustão de fumaça e máscaras de alta filtração ainda são pouco adotadas e não há "
                                  "diretrizes harmonizadas. As revisões anteriores eram descritivas, sem síntese quantitativa."),
]
x0, y0 = 10.0, 1.9
for i, (ic, t, body) in enumerate(rows):
    yy = y0 + i * 1.92
    icon_badge(s, ic, x0 + 0.45, yy + 0.45, d=0.9, fill=NAVY)
    tb(s, x0 + 1.2, yy - 0.02, 8.25, 0.45, [t], size=20, color=NAVY, bold=True, space_after=0)
    tb(s, x0 + 1.2, yy + 0.45, 8.25, 1.4, [body], size=17, color=INK, space_after=0, line_spacing=1.05)
# lacuna
rect(s, 10.0, 9.6, 9.45, 1.1, fill=GOLD_TINT)
tb(s, 10.25, 9.68, 9.0, 0.95, [[("Lacuna → ", {"bold": True, "color": RED}),
                                ("síntese em camadas: ", {"bold": True}),
                                ("metanálise da prevalência de sintomas + síntese narrativa, com GRADE, dos desfechos "
                                 "objetivos e biomarcadores.", {})]], size=16, color=INK, space_after=0,
   anchor=MSO_ANCHOR.MIDDLE)
deck.notes(s, """[0:15–1:05] INTRODUÇÃO (~50 s)
Fumaça cirúrgica é o subproduto da destruição térmica dos tecidos pelo eletrocautério, pelo laser e pelo bisturi ultrassônico. Ela não é só "fumaça": contém hidrocarbonetos aromáticos policíclicos, compostos orgânicos voláteis como benzeno, tolueno e xileno, partículas ultrafinas que chegam às vias aéreas inferiores e até material genético viral, como o HPV.
Quem trabalha no centro cirúrgico relata com frequência irritação ocular, tosse, irritação de mucosas, cefaleia e náusea. O que não sabemos é o efeito de longo prazo: há plausibilidade biológica para câncer e doença respiratória, mas a relação causal nunca foi estabelecida, e revisões recentes chegam a dizer que o risco pode estar superestimado.
Enquanto isso, exaustão de fumaça e máscaras de alta filtração ainda são pouco adotadas. E a literatura prévia era descritiva, sem metanálise. Por isso desenhamos uma síntese em camadas: metanálise de prevalência dos sintomas e síntese narrativa, com GRADE, dos desfechos objetivos.

PONTO-CHAVE: a palavra "controvérsia" justifica a revisão. Se a banca perguntar "por que mais uma revisão?", a resposta é: nenhuma anterior quantificou a prevalência com intervalo de predição e GRADE.""")

# =====================================================================
# SLIDE 3 — OBJETIVOS
# =====================================================================
s = deck.content_slide("OBJETIVOS", "Pergunta estruturada: PECO para os desfechos comparativos e CoCoPop para a prevalência")
rect(s, L, 1.95, 18.2, 1.35, fill=NAVY)
tb(s, L + 0.3, 2.0, 17.6, 1.25, [[("Objetivo geral: ", {"bold": True, "color": GOLD}),
                                  ("avaliar os desfechos de saúde associados à exposição ocupacional à fumaça cirúrgica na "
                                   "equipe de centro cirúrgico, com ênfase na prevalência de sintomas, nos desfechos objetivos "
                                   "e nos biomarcadores de exposição ou de possível efeito.", {})]],
   size=21, color=WHITE, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
peco = [
    ("P", "População", "Equipe de centro cirúrgico: cirurgiões, residentes, enfermagem perioperatória, instrumentadores e "
                       "profissionais de anestesia."),
    ("E", "Exposição", "Exposição ocupacional à fumaça gerada por dispositivos de energia (eletrocautério, laser, bisturi "
                       "ultrassônico)."),
    ("C", "Comparador", "Não expostos, minimamente expostos ou com medidas de proteção."),
    ("O", "Outcome (desfecho)", "Efeitos à saúde: sintomas, função pulmonar, biomarcadores urinários, mucosa nasal, "
                                "HPV-DNA nas vias aéreas."),
]
cw, gap = 4.31, 0.33
for i, (letter, name, body) in enumerate(peco):
    x = L + i * (cw + gap)
    rect(s, x, 3.6, cw, 2.75, fill=LIGHT)
    circle(s, x + 0.65, 4.05, 0.75, fill=NAVY, text=letter, size=26)
    tb(s, x + 1.2, 3.78, cw - 1.4, 0.55, [name], size=20, color=NAVY, bold=True, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
    tb(s, x + 0.3, 4.6, cw - 0.6, 1.7, [body], size=16, color=INK, space_after=0, line_spacing=1.05)
tb(s, L, 6.6, 18.2, 0.4, [[("Para a prevalência (metanálise de proporções): ", {"bold": True, "color": NAVY}),
                           ("esquema CoCoPop (Munn et al., 2015)", {"color": GRAY})]], size=18, space_after=0)
coco = [("Condição", "Sintomas oculares e respiratórios autorrelatados, relacionados à exposição"),
        ("Contexto", "Centro cirúrgico com uso de dispositivos de energia"),
        ("População", "Equipe de centro cirúrgico")]
cw2 = 5.87
for i, (name, body) in enumerate(coco):
    x = L + i * (cw2 + 0.3)
    rect(s, x, 7.05, cw2, 1.3, fill=TEAL_TINT)
    tb(s, x + 0.3, 7.12, cw2 - 0.6, 0.4, [name], size=18, color=TEAL, bold=True, space_after=0)
    tb(s, x + 0.3, 7.5, cw2 - 0.6, 0.8, [body], size=16, color=INK, space_after=0)
# objetivos específicos + alerta
rect(s, L, 8.65, 10.6, 2.0, fill=GOLD_TINT)
tb(s, L + 0.3, 8.72, 10.0, 1.9, [
    {"runs": [("Objetivos específicos", {"bold": True, "color": NAVY})], "space_after": 3},
    {"runs": [("Estimar por metanálise a prevalência de sintoma ocular (principal) e respiratório (exploratório);", {})], "bullet": "1."},
    {"runs": [("Sintetizar narrativamente os desfechos objetivos e biomarcadores;", {})], "bullet": "2."},
    {"runs": [("Graduar a certeza da evidência por desfecho (GRADE).", {})], "bullet": "3."},
], size=16, color=INK, space_after=2)
rect(s, 12.15, 8.65, 7.3, 2.0, fill=RED_TINT)
icon(s, "warning", 12.45, 8.9, 0.55, color="red")
tb(s, 13.15, 8.75, 6.15, 1.8, [[("Atenção: ", {"bold": True, "color": RED}),
                                ("a metanálise de proporções estima a ", {}),
                                ("frequência", {"bold": True}),
                                (" de sintomas em populações expostas, não o efeito causal atribuível à fumaça. A inferência "
                                 "causal depende dos estudos comparativos e dos desfechos objetivos.", {})]],
   size=16, color=INK, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
deck.notes(s, """[1:05–1:35] OBJETIVOS (~30 s)
O objetivo foi avaliar os desfechos de saúde associados à exposição ocupacional à fumaça cirúrgica na equipe de centro cirúrgico, com ênfase em três coisas: prevalência de sintomas, desfechos objetivos e biomarcadores.
A pergunta foi estruturada em PECO: população é a equipe de centro cirúrgico; exposição é a fumaça dos dispositivos de energia; comparador são os não expostos ou protegidos; desfecho são os efeitos à saúde. Para a parte de prevalência usamos o esquema CoCoPop, condição, contexto e população, que é o recomendado pelo JBI para metanálises de proporção.
Um ponto que gosto de deixar claro desde o início: metanálise de proporção estima frequência, não efeito causal. Isso vai ser importante na hora de interpretar.

SE PERGUNTAREM "por que PECO e não PICO?": porque é exposição, não intervenção; não houve alocação de intervenção.""")

# =====================================================================
# SLIDE 4 — METODOLOGIA: MAPA DOS 7 PASSOS
# =====================================================================
s = deck.content_slide("METODOLOGIA", "Mapa da revisão: 7 passos, do protocolo à certeza da evidência (PRISMA 2020)")
steps = [
    ("Pergunta e protocolo", "PECO e CoCoPop\nPRISMA 2020 e Diretrizes do MS\nRegistro PROSPERO CRD420251238727 antes da extração\nDispensa do CEP (prot. 2025/0743)"),
    ("Busca", "7 bases eletrônicas + literatura cinzenta + busca por citação\nSem filtro de idioma ou data\nÚltima busca: 09/07/2026"),
    ("Seleção", "Zotero → Rayyan\nDeduplicação automática\nTriagem de título/resumo e leitura na íntegra\nControle de sobreposição amostral"),
    ("Extração", "Planilha padronizada\nEventos e denominadores por desfecho\nDefinição operacional e taxa de resposta"),
    ("Risco de viés", "Ferramentas JBI: prevalência (9 itens), transversal analítico (8) e coorte (11)\nJulgamento por domínios críticos"),
    ("Síntese", "Metanálise de proporções: logito, efeitos aleatórios, Hartung-Knapp\nIntervalo de predição e sensibilidade\nNarrativa para desfechos objetivos"),
    ("Certeza (GRADE)", "5 domínios, adaptados à prevalência\nPonto de partida: certeza baixa\nJustificativa por domínio (Anexo F)"),
]
n = len(steps)
seg = 18.2 / n
cy = 2.5
line(s, L + seg / 2, cy, R - seg / 2, cy, color=rgb("C9CFDA"), width=4)
for i, (t, body) in enumerate(steps, start=1):
    cx = L + seg * (i - 0.5)
    circle(s, cx, cy, 0.95, fill=NAVY if i != 6 else RED, text=str(i), size=28)
    tb(s, cx - seg / 2 + 0.05, 3.15, seg - 0.1, 0.8, [t], size=19, color=NAVY, bold=True, align=PP_ALIGN.CENTER,
       space_after=0, anchor=MSO_ANCHOR.TOP)
    rect(s, cx - seg / 2 + 0.08, 3.95, seg - 0.16, 3.15, fill=LIGHT)
    tb(s, cx - seg / 2 + 0.22, 4.05, seg - 0.44, 3.0, body.split("\n"), size=16, color=INK, space_after=5,
       line_spacing=1.02)
# ferramentas
rect(s, L, 7.4, 18.2, 1.65, fill=NAVY_TINT)
tb(s, L + 0.3, 7.5, 2.9, 1.45, [[("Ferramentas", {"bold": True, "color": NAVY, "size": 19})], "(função operacional)"],
   size=14, color=GRAY, space_after=2, anchor=MSO_ANCHOR.MIDDLE)
tools = [("database", "Zotero 6", "gestão de referências"), ("filter", "Rayyan", "deduplicação e triagem"),
         ("link", "OpenAlex", "metadados e busca por citação"), ("code", "Python 3.13", "NumPy, SciPy, statsmodels"),
         ("robot", "Assistente de IA", "só priorizou a ordem de leitura; decisões 100% humanas")]
tx = L + 3.2
tw = (18.2 - 3.2) / len(tools)
for i, (ic, name, desc) in enumerate(tools):
    x = tx + i * tw
    icon(s, ic, x, 7.85, 0.55, color="navy")
    tb(s, x + 0.7, 7.62, tw - 0.8, 0.45, [name], size=16, color=NAVY, bold=True, space_after=0)
    tb(s, x + 0.7, 8.05, tw - 0.8, 0.95, [desc], size=14, color=INK, space_after=0)
tb(s, L, 9.3, 18.2, 1.2, [
    [("Transparência e reprodutibilidade: ", {"bold": True, "color": NAVY}),
     ("checklist PRISMA 2020 com 27 itens preenchido; estratégias completas por base (Anexo A); extração, risco de viés e "
      "perfil GRADE em anexos; códigos de análise, figuras e planilhas abertos no OSF (osf.io/jktmn). ", {}),
     ("Uso de IA declarado conforme a Portaria CNPq nº 2.664/2026.", {"color": GRAY})]],
   size=15, color=INK, space_after=0)
deck.notes(s, """[1:35–2:05] METODOLOGIA – MAPA (~30 s)
A parte que mais me orgulho é o método, então vou apresentá-lo como um passo a passo, do jeito que o PRISMA 2020 recomenda. São sete passos.
Um: a pergunta e o protocolo, registrado no PROSPERO antes da extração de dados, e a dispensa do Comitê de Ética, por ser revisão de literatura. Dois: a busca em sete bases, mais literatura cinzenta e busca por citação. Três: a seleção, com deduplicação, triagem e leitura na íntegra. Quatro: a extração padronizada. Cinco: o risco de viés com as ferramentas do JBI. Seis: a síntese, que é a metanálise de proporções. Sete: a certeza da evidência pelo GRADE.
Tudo foi feito com ferramentas abertas: Zotero, Rayyan, OpenAlex e análise em Python. Um assistente de IA foi usado apenas para priorizar a ordem de leitura; nenhuma decisão de elegibilidade ou extração foi delegada. O código e as planilhas estão públicos no OSF.

DICA: não detalhe nada aqui; é só o mapa. Os próximos cinco slides percorrem os passos.""")

# =====================================================================
# SLIDE 5 — PASSOS 1 e 2: ELEGIBILIDADE E BUSCA
# =====================================================================
s = deck.content_slide("METODOLOGIA", "Passos 1 e 2 · Critérios de elegibilidade e busca de alta sensibilidade", track={1, 2})
rect(s, L, 1.95, 8.4, 7.9, fill=LIGHT)
tb(s, L + 0.3, 2.05, 7.8, 0.45, ["Critérios de elegibilidade (definidos no protocolo)"], size=19, color=NAVY, bold=True,
   space_after=0)
icon(s, "check", L + 0.3, 2.62, 0.4, color="teal")
tb(s, L + 0.85, 2.57, 7.3, 0.45, ["Incluímos"], size=18, color=TEAL, bold=True, space_after=0)
tb(s, L + 0.3, 3.05, 7.8, 3.1, [
    "Estudos observacionais primários: transversais, caso-controle e coorte;",
    "Profissionais de centro cirúrgico expostos à fumaça cirúrgica;",
    "Efeitos à saúde ou marcadores de exposição como desfecho;",
    "Português, inglês ou espanhol; sem restrição de data;",
    "Resumos de congresso só com população, cenário, definição do desfecho, eventos e denominador "
    "(classificados como preocupação alta e testados em análise de sensibilidade).",
], size=17, color=INK, bullet=True, bullet_color=TEAL, space_after=6)
icon(s, "xmark", L + 0.3, 6.3, 0.4, color="red")
tb(s, L + 0.85, 6.25, 7.3, 0.45, ["Excluímos"], size=18, color=RED, bold=True, space_after=0)
tb(s, L + 0.3, 6.73, 7.8, 3.1, [
    "Estudos in vitro ou em animais;",
    "População fora do centro cirúrgico (ex.: ambulatórios de dermatologia ou ginecologia);",
    "Desfecho apenas no paciente;",
    "Caracterização físico-química do ar sem desfecho humano;",
    "Revisões, editoriais, cartas e comentários;",
    "Exposição não atribuível à fumaça (ex.: só gases anestésicos ou radiação).",
], size=17, color=INK, bullet=True, bullet_color=RED, space_after=6)
# gráfico de fontes
rect(s, 9.95, 1.95, 9.5, 4.9, fill=WHITE, line=rgb("C9CFDA"))
tb(s, 10.2, 2.02, 9.0, 0.4, ["Registros recuperados por fonte (busca em 09/07/2026)"], size=18, color=NAVY, bold=True,
   space_after=0)
bar_chart(s, 10.0, 2.45, 6.7, 4.35,
          ["PubMed/MEDLINE", "Embase", "Web of Science", "Scopus", "BVS (LILACS/IBECS)", "Google Scholar", "SciELO",
           "Cochrane CENTRAL", "Catálogo CAPES"],
          [4522, 4660, 3629, 2639, 1229, 50, 28, 0, 0], color=NAVY, font_size=13)
stat(s, 16.85, 2.6, 2.5, "16.757", "registros identificados", h=1.6, num_size=40, lab_size=15, num_color=RED)
stat(s, 16.85, 4.35, 2.5, "+ 443", "referências avaliadas na busca por citação (OpenAlex)", h=1.6, num_size=32,
     lab_size=14, num_color=NAVY)
tb(s, 16.85, 5.95, 2.5, 0.8, ["Cinzenta: 4 estratégias no Google Scholar (50 primeiros resultados cada) e Catálogo CAPES"],
   size=12, color=GRAY, space_after=0)
# estratégia
rect(s, 9.95, 7.05, 9.5, 2.8, fill=GOLD_TINT)
tb(s, 10.2, 7.12, 9.0, 0.4, ["Como a estratégia foi construída"], size=18, color=NAVY, bold=True, space_after=0)
tb(s, 10.2, 7.55, 9.0, 2.3, [
    [("Dois blocos: ", {"bold": True}), ("(equipe cirúrgica) AND (fumaça OU dispositivos de energia), com termos MeSH/Emtree e "
                                        "texto livre; sem bloco de desfecho, para não perder estudos.", {})],
    [("Sem filtro de idioma ou data na busca ", {"bold": True}), ("→ alta sensibilidade (estratégias completas no Anexo A).", {})],
    [("Busca por citação (snowballing) automatizada no OpenAlex: ", {"bold": True}),
     ("referências dos incluídos (reversa) e artigos que os citam (direta).", {})],
], size=15, color=INK, bullet=True, bullet_color=GOLD, space_after=4)
deck.notes(s, """[2:05–2:40] PASSOS 1 E 2 (~35 s)
Os critérios de elegibilidade foram fixados no protocolo. Incluímos estudos observacionais primários com profissionais de centro cirúrgico expostos, com qualquer efeito à saúde ou marcador de exposição como desfecho, em português, inglês ou espanhol, sem restrição de data. Excluímos estudos em animais, populações fora do centro cirúrgico, desfechos só no paciente, medições de ar sem desfecho humano e exposições não atribuíveis à fumaça.
A busca foi desenhada para sensibilidade máxima: dois blocos, população e exposição, sem bloco de desfecho, sem filtro de idioma nem de data. Rodamos em sete bases, mais literatura cinzenta e busca por citação automatizada no OpenAlex. Resultado: 16.757 registros, mais 443 referências rastreadas por citação. PubMed e Embase trouxeram quase metade.

SE PERGUNTAREM por que a Cochrane CENTRAL deu zero: ela indexa ensaios clínicos e a revisão só incluiu observacionais; era esperado.
SE PERGUNTAREM por que sem bloco de desfecho: porque os desfechos eram heterogêneos (sintomas, espirometria, HPV...) e um bloco de desfecho reduziria a sensibilidade.""")

# =====================================================================
# SLIDE 6 — PASSO 3: SELEÇÃO
# =====================================================================
s = deck.content_slide("METODOLOGIA", "Passo 3 · Seleção dos estudos: do registro bruto ao relatório incluído", track=3)
flow = [("16.757", "registros identificados\n(bases + literatura cinzenta)", NAVY),
        ("10.910", "registros únicos\n(5.839 duplicatas; 8 não exportados)", NAVY),
        ("32", "relatórios buscados na íntegra\n(28 da triagem + 4 por citação)", NAVY),
        ("26", "avaliados para elegibilidade\n(6 não recuperados)", NAVY),
        ("22", "relatórios incluídos\n(4 excluídos na íntegra)", RED)]
between = ["", "10.882 excluídos\nna triagem", "6 não\nrecuperados", "4 excluídos\nna íntegra"]
bw, bg = 3.0, 0.8
for i, (num, lab, col) in enumerate(flow):
    x = L + i * (bw + bg)
    rect(s, x, 2.0, bw, 2.15, fill=RED_TINT if col == RED else LIGHT)
    tb(s, x + 0.2, 2.08, bw - 0.4, 0.8, [num], size=40, color=col, bold=True, align=PP_ALIGN.CENTER, space_after=0)
    tb(s, x + 0.2, 2.9, bw - 0.4, 1.2, lab.split("\n"), size=14, color=INK, align=PP_ALIGN.CENTER, space_after=0)
    if i < len(flow) - 1:
        line(s, x + bw + 0.08, 3.05, x + bw + bg - 0.08, 3.05, color=NAVY, width=2.5, arrow=True)
        if between[i]:
            tb(s, x + bw - 0.2, 3.35, bg + 0.4, 0.8, between[i].split("\n"), size=12, color=GRAY,
               align=PP_ALIGN.CENTER, space_after=0)
cards = [
    ("filter", "Deduplicação e triagem", [
        "Zotero → Rayyan; duplicatas por DOI, PMID e similaridade de título.",
        "Triagem de título e resumo de todos os 10.910 registros por um único revisor (o primeiro autor).",
        "Script em Python (regras por palavras-chave) e IA só priorizaram a ordem de leitura; nunca decidiram elegibilidade.",
    ]),
    ("book", "Leitura na íntegra", [
        "Critérios definitivos aplicados; motivo de exclusão registrado para cada relatório (Anexo C).",
        "Excluídos: 1 resumo de congresso sem dados extraíveis e 3 por população ou contexto inelegível.",
        "Regra do sintoma-índice: se >1 sintoma elegível por via, adotou-se o mais específico (lacrimejamento ou irritação ocular; tosse ou irritação de vias aéreas).",
    ]),
    ("people", "Sobreposição amostral", [
        "7 publicações do mesmo grupo brasileiro (Paraná) vêm de coortes com sobreposição parcial.",
        "Regra (definida antes da síntese): 1 representante por desfecho combinado, com numerador e denominador: Bieniek et al., 2022.",
        "Resultado: nenhum participante contado duas vezes em qualquer agrupamento.",
    ]),
]
cw3 = 5.87
for i, (ic, t, body) in enumerate(cards):
    x = L + i * (cw3 + 0.3)
    card(s, x, 4.45, cw3, 4.1, title=t, body=body, icon_name=ic, body_size=15, bullet=True, fill=LIGHT,
         body_space_after=5)
rect(s, L, 8.75, 18.2, 1.1, fill=GOLD_TINT)
icon(s, "exclaim", L + 0.25, 9.03, 0.55, color="navy")
tb(s, L + 1.0, 8.82, 17.1, 1.0, [
    [("Relatórios não recuperados (n = 6): ", {"bold": True, "color": NAVY}),
     ("tentativas por acesso institucional, repositórios e preprints, páginas dos autores, comutação bibliográfica e "
      "contato com autores correspondentes. Entre eles, dois inquéritos de sintomas (Navarro-Meza 2013; Gjini 2025) e um "
      "estudo de olho seco → possível impacto na prevalência, registrado como limitação (Anexo C).", {})]],
   size=14, color=INK, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
deck.notes(s, """[2:40–3:15] PASSO 3 – SELEÇÃO (~35 s)
Da esquerda para a direita: 16.757 registros entraram no Zotero e foram importados no Rayyan, que removeu 5.839 duplicatas por DOI, PMID e similaridade de título. Sobraram 10.910 registros únicos, e eu li o título e o resumo de todos eles. Um script em Python e um assistente de IA só reordenaram a fila de leitura; quem decidia era eu, com os critérios.
Vinte e oito foram para texto completo, mais quatro vindos da busca por citação, total de 32; seis não foram recuperados apesar de tentativas por acesso institucional e contato com autores; 26 foram avaliados na íntegra e 22 incluídos.
Um cuidado importante: sete publicações vêm do mesmo grupo brasileiro, com amostras sobrepostas. Para não contar ninguém duas vezes, cada agrupamento recebeu só um representante desse cluster, o Bieniek 2022, que era o relato mais completo.

HONESTIDADE METODOLÓGICA: a triagem foi feita por um único revisor. Isso está declarado como limitação; o PRISMA pede dupla revisão independente. Se perguntarem, diga que a decisão foi registrada com justificativa e que a replicação em duplicata está nas perspectivas.""")

# =====================================================================
# SLIDE 7 — PASSOS 4 e 5: EXTRAÇÃO E RISCO DE VIÉS
# =====================================================================
s = deck.content_slide("METODOLOGIA", "Passos 4 e 5 · Extração padronizada e avaliação do risco de viés (JBI)", track={4, 5})
card(s, L, 1.95, 7.3, 8.0, title="Extração dos dados", icon_name="table", fill=LIGHT, body_size=16, bullet=True, body=[
    [("Planilha padronizada: ", {"bold": True}), ("autor, ano, país; desenho; população; dispositivo gerador; comparador; "
                                                 "instrumento e definição operacional do desfecho; taxa de resposta; medidas de "
                                                 "resultado.", {})],
    [("Para a metanálise: ", {"bold": True}), ("número de eventos e denominador de cada grupo (Anexo D). Ex.: İlçe 2017, "
                                              "lacrimejamento: 33/81 = 40,7%.", {})],
    [("Período de recordatório e validação do instrumento ", {"bold": True}), ("raramente informados → registrados como "
                                                                              "“não relatado”.", {})],
    [("Taxa de resposta ", {"bold": True}), ("extraída quando disponível; quase nunca relatada (limitação dos inquéritos).", {})],
    [("Sem contato com autores ", {"bold": True}), ("para dados adicionais; planilha completa pública no OSF.", {})],
])
tb(s, L + 0.3, 6.95, 6.7, 0.4, ["Exemplo de linhas extraídas (Anexo D, sintoma ocular)"], size=14, color=NAVY, bold=True,
   space_after=0)
table(s, L + 0.3, 7.35, 6.7, [
    ["Estudo", "Eventos", "n", "Prev.", "Definição"],
    ["İlçe et al., 2017", "33", "81", "40,7%", "lacrimejamento"],
    ["Usta et al., 2019", "57", "105", "54,3%", "lacrimejamento"],
    ["Mohd Fikri Rosely; Titi R., 2019", "28", "137", "20,4%", "irritação ocular"],
    ["Bieniek et al., 2022", "67", "155", "43,2%", "escala (sistema ocular)"],
], col_widths=[2.55, 0.8, 0.6, 0.8, 1.95], size=12, row_h=0.4,
      align_cols={1: PP_ALIGN.CENTER, 2: PP_ALIGN.CENTER, 3: PP_ALIGN.CENTER})
# JBI
tb(s, 8.85, 1.95, 10.6, 0.45, ["Risco de viés: ferramenta JBI escolhida pela função de cada estudo na síntese"], size=18,
   color=NAVY, bold=True, space_after=0)
jbi = [("Prevalência", "9 itens", "estudos das metanálises (k = 7)", NAVY),
       ("Transversal analítico", "8 itens", "comparativos e desfechos objetivos", TEAL),
       ("Coorte", "11 itens", "3 coortes prospectivas", GOLD)]
jw = 3.4
for i, (t, items, who, col) in enumerate(jbi):
    x = 8.85 + i * (jw + 0.2)
    rect(s, x, 2.5, jw, 1.45, fill=LIGHT)
    tb(s, x + 0.2, 2.56, jw - 0.4, 0.4, [t], size=16, color=col if col != GOLD else rgb("8A6D1F"), bold=True, space_after=0)
    tb(s, x + 0.2, 2.95, jw - 0.4, 0.4, [items], size=22, color=INK, bold=True, space_after=0)
    tb(s, x + 0.2, 3.4, jw - 0.4, 0.5, [who], size=13, color=GRAY, space_after=0)
tb(s, 8.85, 4.1, 10.6, 1.0, [
    [("Regra do julgamento global: ", {"bold": True, "color": NAVY}),
     ("qualitativo, orientado pelos domínios críticos (amostragem, tamanho amostral, validade da mensuração e taxa de "
      "resposta), não por corte percentual. “Não” pesou mais do que “incerto”. Nenhuma pontuação foi combinada entre "
      "instrumentos. Todos os estudos foram mantidos; a classificação alimentou o GRADE.", {})]], size=14, color=INK,
   space_after=0)
pic(s, FIG / "figE1_jbi_prev.png", 8.85, 5.2, w=8.6, h=3.95, name="Figura E1 JBI")
tb(s, 17.6, 5.3, 1.9, 3.8, [
    {"runs": [("Itens JBI (prevalência)", {"bold": True, "color": NAVY})], "space_after": 4},
    "1 marco amostral", "2 amostragem", "3 tamanho amostral", "4 sujeitos e cenário", "5 cobertura", "6 validade do desfecho",
    "7 padronização", "8 análise", "9 taxa de resposta",
], size=11, color=INK, space_after=1)
tb(s, 8.85, 9.2, 8.6, 0.7, [[("Figura E1. ", {"bold": True}), ("Sete estudos das metanálises. ", {}),
                            ("+ sim  ", {"color": GREEN, "bold": True}), ("? incerto  ", {"color": AMBER, "bold": True}),
                            ("− não.  ", {"color": RED, "bold": True}),
                            ("Preocupação global: moderada ou alta em todos; nenhum com preocupação baixa.", {})]],
   size=13, color=INK, space_after=0)
deck.notes(s, """[3:15–3:45] PASSOS 4 E 5 (~30 s)
A extração foi feita em planilha padronizada: identificação, desenho, população, dispositivo gerador, comparador, instrumento e definição do desfecho, taxa de resposta e, para a metanálise, o número de eventos e o denominador de cada estudo. Por exemplo, no İlçe 2017, 33 de 81 profissionais relataram lacrimejamento.
O risco de viés foi avaliado com as ferramentas do Joanna Briggs Institute, escolhidas pela função de cada estudo: a lista de prevalência, com nove itens, para os sete estudos das metanálises; a de transversal analítico para os comparativos; e a de coorte para os três longitudinais. O julgamento global foi qualitativo, guiado pelos domínios críticos: amostragem, tamanho amostral, validade da mensuração e taxa de resposta.
O semáforo resume: a preocupação foi moderada ou alta em todos, principalmente por amostragem não probabilística, taxa de resposta não relatada e desfecho autorrelatado. Nenhum estudo teve preocupação baixa, e isso vai pesar no GRADE.

SE PERGUNTAREM por que JBI e não Newcastle-Ottawa ou ROBINS-E: o JBI tem lista específica para estudos de prevalência, alinhada ao CoCoPop; NOS não cobre prevalência e ROBINS-E é para exposição comparativa.""")

# =====================================================================
# SLIDE 8 — PASSO 6: METANÁLISE DE PREVALÊNCIA
# =====================================================================
s = deck.content_slide("METODOLOGIA", "Passo 6 · Metanálise de prevalência explicada: de 7 proporções a uma estimativa combinada",
                       track=6)
pipe = [
    ("Proporção de cada estudo", "p = eventos ÷ n", [
        "Ex.: 33/81 = 40,7%.",
        "IC95% individual pelo método de Wilson (melhor que o normal para proporções).",
    ]),
    ("Transformação logito", "ln[ p ÷ (1 − p) ]", [
        "Leva a proporção (0 a 1) para a escala de −∞ a +∞.",
        "Aproxima a distribuição da normal e garante que a estimativa e os IC fiquem entre 0 e 100%.",
        "Sem 0% ou 100% → sem correção de continuidade.",
    ]),
    ("Modelo de efeitos aleatórios", "τ² por Paule-Mandel", [
        "Assume que a prevalência verdadeira varia entre estudos.",
        "τ² = variância entre estudos; peso de cada estudo = 1 ÷ (variância interna + τ²).",
        "Paule-Mandel é mais estável que DerSimonian-Laird com poucos estudos.",
    ]),
    ("Ajuste de Hartung-Knapp", "IC com distribuição t (k − 1 gl)", [
        "Corrige o IC da estimativa combinada quando há poucos estudos e heterogeneidade alta.",
        "Produz intervalos mais honestos (geralmente mais largos) do que o método clássico (IntHout et al., 2014).",
    ]),
    ("Voltar para % e interpretar", "I² e intervalo de predição", [
        "Retrotransformação do logito para porcentagem.",
        "I² = % da variação total devida à heterogeneidade.",
        "Intervalo de predição = faixa esperada para um novo estudo (Riley et al., 2011); instável com k < 10.",
    ]),
]
pw = 3.4
for i, (t, formula, body) in enumerate(pipe, start=1):
    x = L + (i - 1) * (pw + 0.3)
    rect(s, x, 1.95, pw, 4.75, fill=LIGHT)
    circle(s, x + 0.5, 2.35, 0.6, fill=RED, text=str(i), size=20)
    tb(s, x + 0.95, 2.05, pw - 1.1, 0.65, [t], size=16, color=NAVY, bold=True, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
    rect(s, x + 0.2, 2.85, pw - 0.4, 0.6, fill=WHITE, line=rgb("C9CFDA"))
    tb(s, x + 0.25, 2.85, pw - 0.5, 0.6, [formula], size=17, color=RED, bold=True, align=PP_ALIGN.CENTER, space_after=0,
       anchor=MSO_ANCHOR.MIDDLE)
    tb(s, x + 0.2, 3.6, pw - 0.4, 3.05, body, size=15, color=INK, bullet=True, bullet_color=NAVY, space_after=5)
    if i < len(pipe):
        line(s, x + pw + 0.02, 4.3, x + pw + 0.28, 4.3, color=NAVY, width=2.5, arrow=True)
# robustez
tb(s, L, 6.9, 18.2, 0.4, [[("Verificando a robustez ", {"bold": True, "color": NAVY}),
                           ("(análises de sensibilidade, influência e subgrupo)", {"color": GRAY})]], size=18, space_after=0)
chips = [("Freeman-Tukey", "duplo-arcoseno, DerSimonian-Laird"), ("GLMM logístico", "intercepto aleatório por estudo"),
         ("Leave-one-out", "retira 1 estudo por vez"), ("Gráfico de Baujat", "quem puxa a heterogeneidade"),
         ("Subgrupo por país", "exploratório; teste Q"), ("Sensibilidade extra", "sem resumo de congresso; definições específicas")]
chw = 2.9
for i, (t, d) in enumerate(chips):
    x = L + i * (chw + 0.16)
    rect(s, x, 7.35, chw, 1.1, fill=TEAL_TINT)
    tb(s, x + 0.15, 7.4, chw - 0.3, 0.4, [t], size=15, color=TEAL, bold=True, space_after=0)
    tb(s, x + 0.15, 7.78, chw - 0.3, 0.65, [d], size=13, color=INK, space_after=0)
rect(s, L, 8.65, 18.2, 1.2, fill=GOLD_TINT)
icon(s, "question", L + 0.25, 8.95, 0.6, color="navy")
tb(s, L + 1.05, 8.72, 17.1, 1.1, [
    [("Por que não fizemos gráfico de funil nem teste de Egger? ", {"bold": True, "color": NAVY}),
     ("Em metanálise de proporção o erro-padrão depende da própria proporção, o que gera assimetria espúria, e os testes "
      "exigem ≥ 10 estudos. O viés de relato foi apreciado qualitativamente. ", {}),
     ("Sem metarregressão ", {"bold": True}), ("(poucos estudos por covariável). ", {}),
     ("Riscos relativos ", {"bold": True}), ("dos desfechos objetivos: escala log, método de Wald.", {})]],
   size=14, color=INK, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
deck.notes(s, """[3:45–4:35] PASSO 6 – METANÁLISE (~50 s)  ← o coração da apresentação
Vou explicar a metanálise em cinco passos. Primeiro, cada estudo vira uma proporção: eventos dividido pelo n. Segundo, aplicamos a transformação logito, o logaritmo da chance: isso tira a proporção da escala de zero a um, aproxima da distribuição normal e garante que a estimativa combinada e os intervalos fiquem entre 0 e 100%. Terceiro, usamos modelo de efeitos aleatórios, porque não faz sentido supor uma única prevalência verdadeira em hospitais da Turquia, da Malásia e do Brasil; a variância entre estudos, o tau-quadrado, foi estimada por Paule-Mandel. Quarto, o intervalo de confiança da estimativa combinada recebeu o ajuste de Hartung-Knapp, que usa a distribuição t e é mais honesto quando há poucos estudos e muita heterogeneidade. Quinto, voltamos para porcentagem e reportamos o I² e o intervalo de predição, que diz onde cairia a prevalência de um novo estudo.
Para testar a robustez, repetimos tudo com a transformação de Freeman-Tukey e com um modelo logístico misto, fizemos leave-one-out, gráfico de Baujat e subgrupo por país.
Não fizemos gráfico de funil nem Egger, porque em proporções o erro-padrão depende da própria proporção, o que cria assimetria falsa, e seriam necessários dez estudos.

ANALOGIA se precisar: efeitos fixos = "todos os estudos medem a mesma coisa com ruído"; efeitos aleatórios = "cada estudo mede a sua prevalência, e queremos a média dessas prevalências e a dispersão delas".""")

# =====================================================================
# SLIDE 9 — PASSO 7: GRADE
# =====================================================================
s = deck.content_slide("METODOLOGIA", "Passo 7 · Certeza da evidência: GRADE adaptado a desfechos de prevalência", track=7)
dom = [
    ("balance", "Risco de viés", "Do JBI: amostragem não probabilística, tamanho amostral não justificado, taxa de resposta "
                                 "não relatada, desfecho autorrelatado; nos objetivos, ausência de ajuste para confundidores."),
    ("spiral", "Inconsistência", "I² acima de 90%, prevalências individuais de 19% a 56% e intervalo de predição amplo "
                                 "→ muito grave nos desfechos de prevalência."),
    ("compass", "Evidência indireta", "Não rebaixada na prevalência: o sintoma autorrelatado É o desfecho da pergunta. "
                                      "Rebaixada nos biomarcadores: coexposições e desfechos substitutos."),
    ("target", "Imprecisão", "Amplitude do IC95% (ex.: 21,9–56,5) ou ausência de IC no estudo original; poucos eventos "
                             "nos desfechos objetivos."),
    ("search", "Viés de publicação", "Apreciação qualitativa: busca ampla, mas poucos estudos, amostras pequenas e 6 "
                                     "relatórios não recuperados → não excluível, sem base formal para rebaixar."),
]
dw = 3.4
for i, (ic, t, body) in enumerate(dom):
    x = L + i * (dw + 0.3)
    card(s, x, 1.95, dw, 3.45, title=t, body=[body], icon_name=ic, fill=LIGHT, body_size=15, title_size=17, pad=0.25)
rect(s, L, 5.65, 10.6, 4.2, fill=NAVY_TINT)
tb(s, L + 0.3, 5.75, 10.0, 4.0, [
    {"runs": [("Como a certeza foi graduada", {"bold": True, "color": NAVY, "size": 18})], "space_after": 6, "bullet": False},
    [("Ponto de partida: certeza BAIXA ", {"bold": True}), ("para evidência observacional (decisão metodológica dos autores; parte "
                                                            "da literatura sugere iniciar em alta para prevalência, Murad et al., 2017).", {})],
    [("Regra: ", {"bold": True}), ("um domínio grave já leva a MUITO BAIXA; a certeza final não muda com o ponto de partida "
                                  "alternativo.", {})],
    [("Sem dupla contagem: ", {"bold": True}), ("o intervalo de predição entrou em inconsistência; a amplitude do IC95%, em "
                                               "imprecisão.", {})],
    [("Desfechos com um único estudo: ", {"bold": True}), ("inconsistência não aplicável; viés de publicação não avaliável.", {})],
    {"runs": [("●●●● alta   ●●●○ moderada   ●●○○ baixa   ●○○○ muito baixa", {"color": NAVY, "bold": True})],
     "space_before": 6, "bullet": False},
], size=15, color=INK, bullet=True, bullet_color=NAVY, space_after=5)
rect(s, 12.15, 5.65, 7.3, 4.2, fill=GOLD_TINT)
icon(s, "clipboard", 12.4, 5.8, 0.5, color="navy")
tb(s, 13.05, 5.75, 6.3, 0.5, ["Decisões posteriores ao registro (transparência)"], size=17, color=NAVY, bold=True,
   space_after=0, anchor=MSO_ANCHOR.MIDDLE)
tb(s, 12.4, 6.4, 6.85, 3.4, [
    "Ocular como desfecho principal; respiratório exploratório (maior variação na definição);",
    "Modelo principal: logito com efeitos aleatórios e Hartung-Knapp;",
    "1 publicação por desfecho no cluster com sobreposição; análises por país e de influência exploratórias;",
    "Resumos de congresso com dados suficientes admitidos (preocupação alta);",
    "Durante a análise: regra do sintoma-índice e sensibilidade por definição específica, independentes dos resultados.",
], size=14, color=INK, bullet=True, bullet_color=GOLD, space_after=4)
deck.notes(s, """[4:35–5:05] PASSO 7 – GRADE (~30 s)
O último passo foi graduar a certeza da evidência pelo GRADE, nos cinco domínios: risco de viés, inconsistência, evidência indireta, imprecisão e viés de publicação. Como não existe adaptação universal do GRADE para prevalência, explicitamos os critérios em cada domínio.
Partimos de certeza baixa, por ser evidência observacional, e qualquer domínio grave leva a muito baixa. Um detalhe que mostra cuidado: a evidência indireta não foi rebaixada nos sintomas, porque o sintoma autorrelatado é exatamente o desfecho da pergunta de frequência; já nos biomarcadores foi rebaixada, por coexposição e desfecho substituto. E evitamos dupla contagem: o intervalo de predição entrou em inconsistência, e a largura do IC em imprecisão.
À direita estão as decisões tomadas depois do registro no PROSPERO, todas declaradas no manuscrito.

SE PERGUNTAREM "se começasse em alta, mudaria?": não. Com inconsistência muito grave, risco de viés grave e imprecisão grave, a certeza cairia três níveis e chegaria igualmente a muito baixa.""")

# =====================================================================
# SLIDE 10 — RESULTADOS: SELEÇÃO E CARACTERÍSTICAS
# =====================================================================
s = deck.content_slide("RESULTADOS", "Seleção (PRISMA 2020) e características dos 22 relatórios incluídos")
pic(s, FIG / "fig1_prisma.png", L, 1.9, w=9.3, h=8.75, name="Figura 1 PRISMA")
sx, sy, sw, sh = 10.85, 1.95, 4.15, 1.75
stat(s, sx, sy, sw, "22", "relatórios de estudos observacionais incluídos", h=sh, fill=LIGHT, num_size=44, lab_size=14)
stat(s, sx + sw + 0.3, sy, sw, "9", "países: Turquia, Malásia, Brasil, Paquistão, China, México, EUA, Sudão e Tailândia",
     h=sh, fill=LIGHT, num_size=44, lab_size=13)
stat(s, sx, sy + sh + 0.3, sw, "19 + 3", "transversais + coortes prospectivas (Navarro 2016; Stanganelli 2019; Stanganelli Caus 2025)",
     h=sh, fill=LIGHT, num_size=36, lab_size=13)
stat(s, sx + sw + 0.3, sy + sh + 0.3, sw, "6 | 7", "amostras independentes na metanálise ocular (n = 756) | respiratória (n = 1.428)",
     h=sh, fill=RED_TINT, num_size=36, lab_size=13, num_color=RED)
card(s, 10.85, 6.05, 8.6, 4.6, title="Risco de viés (JBI): resumo", icon_name="balance", fill=LIGHT, body_size=14,
     bullet=True, body=[
         [("Estimativas de prevalência: ", {"bold": True}), ("preocupação moderada a alta: amostragem não probabilística, tamanho "
                                                            "amostral não justificado, taxa de resposta não informada, sintomas "
                                                            "autorrelatados. Só Mohd Fikri Rosely e Titi Rahmawati (2019) usaram "
                                                            "amostragem aleatória estratificada.", {})],
         [("Resumo de congresso (Mohd Fikri Rosely, 2022): ", {"bold": True}), ("alta preocupação por relato incompleto.", {})],
         [("Comparativos e desfechos objetivos (HPV-DNA, biópsia, biomarcadores, espirometria): ", {"bold": True}),
          ("preocupação moderada: mensuração da exposição por ocupação, sem estimativas ajustadas, controle insuficiente de "
           "confundidores.", {})],
         [("Nenhum estudo alcançou preocupação baixa ", {"bold": True, "color": RED}),
          ("→ análise restrita a baixo risco não foi factível.", {})],
     ])
deck.notes(s, """[5:05–5:30] RESULTADOS – SELEÇÃO E CARACTERÍSTICAS (~25 s)
Este é o fluxograma PRISMA completo, que vocês já viram em números. Ficaram 22 relatórios de estudos observacionais, de nove países, a maioria transversal; três eram coortes prospectivas.
Depois do controle de sobreposição, seis amostras independentes, com 756 profissionais, entraram na metanálise ocular, e sete amostras, com 1.428, na respiratória.
No risco de viés, a preocupação foi moderada a alta nos inquéritos de prevalência, e moderada nos estudos de desfechos objetivos. Nenhum estudo teve preocupação baixa.""")

# =====================================================================
# SLIDE 11 — RESULTADOS: SINTOMA OCULAR
# =====================================================================
s = deck.content_slide("RESULTADOS", "Desfecho principal · Prevalência combinada de sintoma ocular (irritação ou lacrimejamento)")
pic(s, FIG / "fig2_forest_ocular.png", L, 1.95, w=12.3, name="Figura 2 forest plot ocular")
tb(s, L, 8.35, 12.3, 0.5, [[("Figura 2. ", {"bold": True}),
                            ("Modelo logito com Paule-Mandel e ajuste de Hartung-Knapp. Quadrado = prevalência do estudo "
                             "(tamanho ∝ peso); linha preta = IC95% de Wilson; losango = estimativa combinada; linha vermelha = "
                             "intervalo de predição; tracejado = estimativa combinada.", {})]], size=13, color=GRAY, space_after=0)
rect(s, L, 8.95, 12.3, 1.7, fill=NAVY_TINT)
tb(s, L + 0.3, 9.02, 11.7, 1.6, [
    [("Como ler: ", {"bold": True, "color": NAVY}),
     ("cerca de 4 em cada 10 profissionais relataram irritação ou lacrimejamento ocular; mas os estudos variam de 19% "
      "(Malásia) a 56% (Turquia), e um novo estudo poderia encontrar qualquer valor entre 7% e 83%. ", {}),
     ("A estimativa é a proporção que relatou o sintoma segundo a definição de cada estudo, não uma prevalência "
      "temporalmente homogênea.", {"color": GRAY})]], size=15, color=INK, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
rect(s, 13.85, 1.95, 5.6, 4.0, fill=RED_TINT)
stat(s, 14.1, 2.05, 5.1, "37,6%", "prevalência combinada de sintoma ocular", h=2.0, num_size=66, lab_size=16, num_color=RED,
     number_h=1.2)
tb(s, 14.1, 4.0, 5.1, 1.9, [
    [("IC95% ", {"bold": True}), ("21,9 – 56,5", {})],
    [("Intervalo de predição ", {"bold": True}), ("7 – 83%", {})],
    [("I² = 93% · k = 6 · n = 756", {"bold": True})],
], size=17, color=INK, space_after=3)
card(s, 13.85, 6.2, 5.6, 4.45, title="Características do agrupamento", fill=LIGHT, body_size=14, bullet=True, body=[
    "6 inquéritos transversais: Turquia (3), Malásia (2) e Brasil (1).",
    "Preocupação com viés moderada ou alta em todos; nenhum com preocupação baixa.",
    "Definições: lacrimejamento, irritação ocular ou escala de sintomas do sistema ocular.",
    "Maior inquérito elegível (Van Giersbergen 2019, n = 672) não entrou: sem numerador/denominador ocular extraível.",
])
deck.notes(s, """[5:30–6:10] RESULTADO PRINCIPAL – OCULAR (~40 s)
Este é o resultado principal. A prevalência combinada de sintoma ocular, irritação ou lacrimejamento, foi de 37,6%, com intervalo de confiança de 21,9 a 56,5%. São seis amostras independentes, 756 profissionais.
No gráfico de floresta, cada quadrado é a prevalência de um estudo, com o tamanho proporcional ao peso; a linha é o intervalo de confiança; o losango vermelho é a estimativa combinada e a linha vermelha mais longa é o intervalo de predição, de 7 a 83%. Essa linha longa é a mensagem honesta: a heterogeneidade é de 93%, os estudos vão de 19% na Malásia a 56% na Turquia, e um novo estudo poderia cair em quase qualquer valor.
Reforço: isto é a proporção de profissionais que relataram o sintoma, conforme a definição de cada estudo, e não uma prevalência com período de recordatório homogêneo.

SE PERGUNTAREM "I² de 93% não invalida a metanálise?": em prevalência, I² alto é a regra, não a exceção (Barker et al., 2021). Por isso reportamos o intervalo de predição e investigamos as fontes (país, definição), em vez de esconder a heterogeneidade num único número.""")

# =====================================================================
# SLIDE 12 — RESULTADOS: RESPIRATÓRIO + ROBUSTEZ
# =====================================================================
s = deck.content_slide("RESULTADOS", "Desfecho exploratório · Sintoma respiratório ou de vias aéreas, e robustez das estimativas")
pic(s, FIG / "fig3_forest_resp.png", L, 1.95, w=10.2, name="Figura 3 forest plot respiratório")
tb(s, L, 7.9, 10.2, 0.5, [[("Figura 3. ", {"bold": True}),
                           ("Sete amostras independentes (n = 1.428). Definições variam: tosse, ardência de garganta, "
                            "irritação de vias aéreas superiores, escala por sistema.", {})]], size=13, color=GRAY, space_after=0)
rect(s, L, 8.5, 10.2, 2.15, fill=NAVY_TINT)
tb(s, L + 0.3, 8.57, 9.6, 2.0, [
    {"runs": [("Subgrupo por país (sintoma ocular; exploratório)", {"bold": True, "color": NAVY})], "space_after": 4},
    [("Turquia 50,5% ", {"bold": True, "color": RED}), ("(k = 3; n = 268; I² = 57%)   ", {}),
     ("Malásia 19,8% ", {"bold": True, "color": RED}), ("(k = 2; n = 333; I² = 0%)   ", {}),
     ("Brasil 43,2% ", {"bold": True}), ("(k = 1, descritivo)", {})],
    [("Teste entre subgrupos p < 0,001, mas: ", {"bold": True}), ("poucos estudos por país e um resumo de congresso no estrato da "
                                                                   "Malásia → gera hipótese (contexto, exaustão, EPI, forma de "
                                                                   "aferir), não prova moderação causal.", {})],
], size=14, color=INK, space_after=3)
rect(s, 11.85, 1.95, 7.6, 1.75, fill=RED_TINT)
tb(s, 12.1, 2.0, 2.9, 1.1, ["41,7%"], size=50, color=RED, bold=True, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
tb(s, 15.0, 2.05, 4.3, 1.6, [
    [("prevalência combinada de sintoma respiratório", {"bold": True})],
    "IC95% 30,4 – 53,9 · IP 15 – 74%",
    "I² = 91% · k = 7 · n = 1.428",
], size=14, color=INK, space_after=2, anchor=MSO_ANCHOR.MIDDLE)
tb(s, 11.85, 3.9, 7.6, 0.4, ["Robustez: estável entre modelos e estudos"], size=16, color=NAVY,
   bold=True, space_after=0)
table(s, 11.85, 4.35, 7.6, [
    ["Análise", "Ocular", "Respiratório"],
    ["Logito + Hartung-Knapp (principal)", "37,6%", "41,7%"],
    ["Freeman-Tukey (DerSimonian-Laird)", "38,1%", "41,7%"],
    ["GLMM logístico (intercepto aleatório)", "37,5%", "42,0%"],
    ["Leave-one-out (faixa)", "34,3–42,1%", "38,9–45,5%"],
    ["Sem o resumo de congresso", "42,1%", "42,4%"],
    ["Só definições específicas", "36,5% (I² 94%)", "35,8% (I² 61%)"],
], col_widths=[4.3, 1.55, 1.75], size=13, row_h=0.42, align_cols={1: PP_ALIGN.CENTER, 2: PP_ALIGN.CENTER}, bold_rows=(1,))
tb(s, 11.85, 7.4, 7.6, 0.5, [[("Sem o estudo de definição mais divergente (Van Giersbergen 2019): ", {"bold": True}),
                              ("38,9%, sem mudar a conclusão.", {})]], size=13, color=INK, space_after=0)
card(s, 11.85, 8.0, 7.6, 2.65, title="O que a sensibilidade ensina", icon_name="lightbulb", fill=GOLD_TINT, body_size=14,
     bullet=True, pad=0.25, body=[
         "Restringir a definições específicas reduziu o I² respiratório de 91% para 61%: a definição do desfecho explica "
         "parte relevante da heterogeneidade.",
         "No ocular, a heterogeneidade não depende de um único estudo (Baujat: Mohd Fikri Rosely 2022 é o mais influente).",
     ])
deck.notes(s, """[6:10–6:40] RESPIRATÓRIO E ROBUSTEZ (~30 s)
O desfecho respiratório, tratado como exploratório porque as definições variam muito, deu 41,7%, com intervalo de predição de 15 a 74%, em sete amostras e 1.428 profissionais.
A tabela mostra por que confio nas estimativas: os três modelos, logito com Hartung-Knapp, Freeman-Tukey e o modelo logístico misto, deram praticamente o mesmo número; retirar um estudo por vez movimenta a estimativa ocular só entre 34 e 42%; e excluir o resumo de congresso não muda a leitura.
Um achado interessante: quando restringimos a definições específicas de sintoma respiratório, o I² caiu de 91 para 61%. Ou seja, boa parte da heterogeneidade vem de como cada estudo definiu o sintoma.
Na análise por país, a Turquia ficou em 50% e a Malásia em 20%, com diferença significativa, mas com dois ou três estudos por país isso é hipótese, não conclusão.""")

# =====================================================================
# SLIDE 13 — RESULTADOS: DESFECHOS OBJETIVOS E GRADE
# =====================================================================
s = deck.content_slide("RESULTADOS", "Desfechos objetivos e biomarcadores: sinais além do incômodo agudo (1 estudo por desfecho)")
obj = [
    ("lungs", "Função pulmonar (espirometria)", "Ibrahim et al., 2025 · Sudão · 92 expostos vs 92 não expostos pareados", [
        [("VEF1 2,78 vs 3,14 L · CVF 3,02 vs 3,45 L · PFE 327,5 vs 483,5 L/min ", {"bold": True}), ("(p = 0,001, Mann-Whitney)", {})],
        "Mais tempo em centro cirúrgico → menores valores (ajuste por idade e IMC).",
        [("Cautela: ", {"bold": True, "color": RED}), ("VEF1/CVF ≈ 91% nos dois grupos (não obstrutivo); PFE depende do esforço; "
                                                      "manobras de qualidade B/C em 44 de 184.", {})],
    ]),
    ("vial", "Biomarcadores urinários", "Canicoba, 2025 · Brasil · 52 expostos vs 49 controles", [
        [("Ác. trans,trans-mucônico 202,9 vs 46,1 µg/L ", {"bold": True}), ("(metabólito do benzeno)", {})],
        [("Ác. metil-hipúrico 468,2 vs 184,4 µg/L ", {"bold": True}), ("(xileno) · ", {}),
         ("malondialdeído 9,33 vs 3,22 nmol/mg ", {"bold": True}), ("(estresse oxidativo); todos p < 0,001", {})],
        [("Cautela: ", {"bold": True, "color": RED}), ("sem IC95%; t,t-mucônico não é específico (ácido sórbico, tabagismo).", {})],
    ]),
    ("biotech", "Mucosa nasal (biópsia)", "Navarro et al., 2016 · México · coorte de 4 anos · 23 vs 20 residentes", [
        [("Metaplasia ou hiperplasia: 70% (16/23) vs 5% (1/20)", {"bold": True})],
        [("RR 13,9 (IC95% 2,0 – 95,8)", {"bold": True, "color": RED}), (" · IC amplo: 1 evento no grupo não exposto", {})],
        [("Cautela: ", {"bold": True, "color": RED}), ("resposta inespecífica da mucosa a irritantes inalados; exposição por proxy.", {})],
    ]),
    ("virus", "HPV-DNA na mucosa nasal", "Hu et al., 2021 · China · 700 ginecologistas", [
        [("8,96% (42/469) com eletrocirurgia vs 1,73% (4/231) sem", {"bold": True})],
        [("RR 5,2 (IC95% 1,9 – 14,2)", {"bold": True, "color": RED}), (" · maior com mais tempo de eletrocirurgia", {})],
        [("Cautela: ", {"bold": True, "color": RED}), ("detecção de DNA ≠ infecção ou doença; 0/196 com N95 vs 13,98% com máscara "
                                                      "comum é comparação de subgrupo sem ajuste.", {})],
    ]),
]
ow, oh = 8.95, 2.95
for i, (ic, t, src, body) in enumerate(obj):
    x = L + (i % 2) * (ow + 0.3)
    y = 1.95 + (i // 2) * (oh + 0.25)
    rect(s, x, y, ow, oh, fill=LIGHT)
    icon_badge(s, ic, x + 0.65, y + 0.6, d=0.8, fill=NAVY)
    tb(s, x + 1.25, y + 0.15, ow - 1.45, 0.45, [t], size=18, color=NAVY, bold=True, space_after=0)
    tb(s, x + 1.25, y + 0.58, ow - 1.45, 0.4, [src], size=13, color=GRAY, space_after=0)
    tb(s, x + 0.3, y + 1.08, ow - 0.6, oh - 1.2, body, size=15, color=INK, bullet=True, bullet_color=NAVY, space_after=5)
# faixa GRADE
rect(s, L, 8.4, 18.2, 1.8, fill=NAVY)
tb(s, L + 0.3, 8.45, 5.6, 1.7, [[("●○○○  Certeza MUITO BAIXA", {"bold": True, "color": GOLD, "size": 20})],
                                [("em todos os desfechos (GRADE); medidas comparativas não combinadas (desenhos e desfechos "
                                  "heterogêneos).", {"size": 14})]], size=14, color=WHITE, space_after=2,
   anchor=MSO_ANCHOR.MIDDLE)
tb(s, 7.2, 8.45, 5.6, 1.7, [[("0 estudos sobre câncer ou DPOC", {"bold": True, "color": GOLD, "size": 20})],
                            [("vazio de evidência: ausência de estudos ≠ ausência de risco.", {"size": 14})]],
   size=14, color=WHITE, space_after=2, anchor=MSO_ANCHOR.MIDDLE)
tb(s, 13.1, 8.45, 6.2, 1.7, [[("Direção consistente, mas…", {"bold": True, "color": GOLD, "size": 20})],
                             [("coexposições (gases anestésicos, radiação), 1 estudo por desfecho e IC amplos: marcadores de "
                               "exposição/efeito, não doença crônica atribuível.", {"size": 14})]],
   size=14, color=WHITE, space_after=2, anchor=MSO_ANCHOR.MIDDLE)
deck.notes(s, """[6:40–7:20] DESFECHOS OBJETIVOS E GRADE (~40 s)
Além dos sintomas, quatro estudos, um por desfecho, trouxeram medidas objetivas, e todos apontam na mesma direção, desfavorável aos expostos.
Espirometria no Sudão: VEF1, CVF e pico de fluxo menores nos expostos, com gradiente pelo tempo de atuação; mas a relação VEF1/CVF foi normal e o pico de fluxo depende de esforço, então lemos com cautela. Biomarcadores urinários no Brasil: metabólitos de benzeno e xileno e malondialdeído muito mais altos nos expostos. Biópsia nasal numa coorte mexicana de quatro anos: metaplasia em 70% dos expostos contra 5%, risco relativo de 13,9, com intervalo muito amplo. E DNA de HPV na mucosa nasal de ginecologistas chineses: 9% contra 1,7%, risco relativo de 5,2.
Pelo GRADE, a certeza foi muito baixa em todos os desfechos. E talvez o achado mais importante seja o que não encontramos: nenhum estudo avaliou diretamente câncer ou DPOC na equipe cirúrgica. Isso é um vazio de evidência, não evidência de ausência de risco.

NÚMEROS para decorar: 37,6% ocular; 41,7% respiratório; RR 13,9 metaplasia; RR 5,2 HPV; 0 estudos de câncer/DPOC.""")

# =====================================================================
# SLIDE 14 — DISCUSSÃO: INTERPRETAÇÃO
# =====================================================================
s = deck.content_slide("DISCUSSÃO", "O que os achados significam e como interpretá-los com cautela")
cols = [
    ("chart", "Carga de sintomas", [
        "Sintomas frequentes: ocular 37,6%, respiratório 41,7%, qualquer sintoma 55,6–73,2%.",
        "Coerente com a literatura prévia, que era transversal e sem síntese quantitativa (Mowbray 2013; Dixon 2023).",
        [("Contribuição: ", {"bold": True}), ("primeira estimativa combinada com intervalo de predição, subgrupo por país e "
                                              "GRADE para este corpo de literatura.", {})],
    ]),
    ("spiral", "Heterogeneidade: esperada, não ignorada", [
        "I² > 90% é típico em metanálise de prevalência → interpretar pelo intervalo de predição.",
        "Fontes plausíveis: definição do sintoma e recordatório, composição profissional, tempo de exposição, "
        "disponibilidade de exaustão e EPI, condições ambientais.",
        "País reduziu o I² intragrupo (Turquia 57%, Malásia 0%), mas com 2–3 estudos por estrato é geração de hipótese.",
    ]),
    ("biotech", "Sinais além do incômodo agudo", [
        [("A favor da causalidade: ", {"bold": True}), ("gradiente com o tempo de exposição (espirometria, HPV), temporalidade "
                                                       "(coorte) e plausibilidade biológica.", {})],
        [("Contra: ", {"bold": True}), ("um estudo por desfecho, intervalos amplos, especificidade comprometida por coexposições "
                                       "(gases anestésicos, radiação).", {})],
        "Metabólitos = exposição recente; metaplasia = resposta inespecífica; HPV-DNA = detecção, não infecção.",
    ]),
]
dcw = 5.87
for i, (ic, t, body) in enumerate(cols):
    x = L + i * (dcw + 0.3)
    card(s, x, 1.95, dcw, 5.35, title=t, body=body, icon_name=ic, fill=LIGHT, body_size=17, bullet=True, title_size=19,
         body_space_after=9)
rect(s, L, 7.6, 18.2, 2.3, fill=NAVY)
icon(s, "question", L + 0.35, 8.33, 0.85, color="gold")
tb(s, L + 1.5, 7.7, 16.6, 2.1, [
    [("O achado talvez mais relevante é o que não foi encontrado. ", {"bold": True, "color": GOLD}),
     ("Nenhum estudo elegível estimou câncer ou DPOC atribuíveis à fumaça. Relatos de caso de papilomatose laríngea e "
      "carcinoma orofaríngeo por HPV em cirurgiões (Hallmo; Naess, 1991; Rioux et al., 2013) reforçam a plausibilidade, mas "
      "não estimam risco. A controvérsia (Hurst; Stewart, 2024) não se resolve com os estudos existentes, e sim com estudos "
      "longitudinais ainda por realizar.", {})]], size=16, color=WHITE, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
deck.notes(s, """[7:20–7:50] DISCUSSÃO – INTERPRETAÇÃO (~30 s)
Três leituras. Primeira: a carga de sintomas é alta e coerente com a literatura; a novidade é ter uma estimativa combinada com intervalo de predição, subgrupo e GRADE. Segunda: a heterogeneidade acima de 90% é esperada em prevalência; em vez de escondê-la, mostramos o intervalo de predição e as fontes prováveis: definição do sintoma, composição da equipe, tempo de exposição e contexto, como exaustão e EPI. Terceira: os desfechos objetivos têm gradiente dose-resposta, temporalidade e plausibilidade, mas são um estudo por desfecho, com intervalos amplos e coexposições. São marcadores, não doença.
E o achado mais relevante é o que não foi encontrado: nenhum estudo de câncer ou DPOC. A controvérsia sobre o risco real só se resolve com estudos longitudinais que ainda não existem.""")

# =====================================================================
# SLIDE 15 — DISCUSSÃO: PONTOS FORTES E LIMITAÇÕES
# =====================================================================
s = deck.content_slide("DISCUSSÃO", "Pontos fortes e limitações")
card(s, L, 1.95, 7.4, 8.4, title="Pontos fortes", icon_name="thumbsup", badge_fill=GREEN, fill=GREEN_TINT, body_size=18,
     bullet=True, body_space_after=12, body=[
         "Busca abrangente: 7 bases, literatura cinzenta e busca por citação, sem filtro de idioma na busca.",
         "Protocolo registrado (PROSPERO) e relato PRISMA 2020 com checklist de 27 itens.",
         "Risco de viés padronizado com ferramentas JBI escolhidas pela função de cada estudo.",
         "Síntese com intervalo de predição, 3 modelos concordantes, leave-one-out, Baujat e subgrupo.",
         "Certeza graduada por desfecho (GRADE), com justificativa por domínio.",
         "Reprodutibilidade: código em Python, planilhas e figuras abertos no OSF.",
     ])
card(s, 8.95, 1.95, 10.5, 8.4, title="Limitações (declaradas no manuscrito)", icon_name="warning", badge_fill=RED,
     fill=RED_TINT, body_size=17, bullet=True, body_space_after=10, body=[
         [("Transversais, exposição por proxy (ocupação) e desfechos autorrelatados; ", {"bold": True}),
          ("viés de atribuição: o respondente sabe que o questionário é sobre fumaça.", {})],
         [("Sem grupo não exposto nos agrupamentos ", {"bold": True}), ("→ não se estima o excesso atribuível à exposição.", {})],
         [("Efeito do trabalhador sadio: ", {"bold": True}), ("quem adoece sai do centro cirúrgico → prevalência subestimada.", {})],
         [("Heterogeneidade alta; subgrupo exploratório; ", {"bold": True}), ("o maior inquérito (n = 672) ficou fora do agrupamento "
                                                                             "ocular; vários estudos em periódicos de indexação "
                                                                             "limitada.", {})],
         [("Sobreposição amostral ", {"bold": True}), ("tratada com 1 publicação por desfecho; 1 resumo de congresso na síntese.", {})],
         [("Revisor único ", {"bold": True}), ("na triagem, extração, JBI e GRADE; 6 relatórios não recuperados; elegibilidade em "
                                              "3 idiomas.", {})],
         [("A metanálise estima prevalência em expostos, não risco causal.", {"bold": True, "color": RED})],
     ])
deck.notes(s, """[7:50–8:15] PONTOS FORTES E LIMITAÇÕES (~25 s)
Como pontos fortes: busca ampla e sem filtro de idioma, protocolo registrado, risco de viés padronizado, síntese com intervalo de predição e três modelos concordantes, GRADE por desfecho e tudo reprodutível no OSF.
As limitações estão todas declaradas. As principais: os estudos são transversais, com exposição por ocupação e sintomas autorrelatados, e o respondente sabia que o questionário era sobre fumaça; não há grupo não exposto nos agrupamentos, então não estimamos o excesso atribuível; existe o efeito do trabalhador sadio, que subestima a prevalência; a heterogeneidade é alta; e a triagem, a extração e o risco de viés foram feitos por um único revisor, sem duplicata.

ATITUDE: fale as limitações com segurança. Banca valoriza quem conhece as fraquezas do próprio trabalho mais do que quem as esconde.""")

# =====================================================================
# SLIDE 16 — CONCLUSÃO
# =====================================================================
s = deck.content_slide("CONCLUSÃO", "Síntese da mensagem da revisão")
pic(s, IMG / "exaustao_n95.png", L, 1.95, w=8.0, name="Foto exaustão e N95")
tb(s, L, 6.5, 8.0, 0.35, ["Imagem ilustrativa (gerada por IA): exaustão local na fonte e respirador N95."], size=13,
   color=GRAY, space_after=0)
rect(s, L, 6.95, 8.0, 1.85, fill=NAVY_TINT)
tb(s, L + 0.3, 7.02, 7.4, 1.75, [
    {"runs": [("Proteção recomendada (NIOSH, 1996; NR-32)", {"bold": True, "color": NAVY})], "space_after": 3,
     "bullet": False},
    "Evacuação local da fumaça na fonte (medida principal);",
    "Respiradores N95/PFF2 (retêm partículas, não substituem a exaustão);",
    "Educação da equipe. Efetividade não avaliada nesta revisão.",
], size=14, color=INK, bullet=True, bullet_color=NAVY, space_after=2)
concl = [
    ("check", "O que se sabe", GREEN, GREEN_TINT,
     "Sintomas oculares e respiratórios são frequentemente relatados pela equipe exposta, com ampla variação entre contextos "
     "(ocular 37,6%, IP 7–83%; respiratório 41,7%, IP 15–74%). Desfechos objetivos (função pulmonar, biomarcadores, mucosa "
     "nasal, HPV) sinalizam alterações além do incômodo agudo."),
    ("question", "O que não se sabe", AMBER, GOLD_TINT,
     "Não há evidência direta de câncer ou DPOC atribuíveis à fumaça; a certeza é muito baixa; a exposição múltipla limita a "
     "atribuição causal; a evidência é heterogênea e majoritariamente transversal."),
    ("shield", "Implicação", NAVY, NAVY_TINT,
     "A proteção da equipe parece justificada pela carga sintomática e pelo princípio da precaução; a quantificação do risco "
     "de longo prazo depende de estudos longitudinais específicos."),
]
for i, (ic, t, col, tint, body) in enumerate(concl):
    y = 1.95 + i * 2.3
    rect(s, 9.75, y, 9.7, 2.1, fill=tint)
    icon_badge(s, ic, 10.3, y + 0.55, d=0.8, fill=col)
    tb(s, 10.95, y + 0.15, 8.3, 0.5, [t], size=19, color=col if col != AMBER else rgb("8A6D1F"), bold=True, space_after=0,
       anchor=MSO_ANCHOR.MIDDLE)
    tb(s, 10.0, y + 0.95, 9.2, 1.15, [body], size=14, color=INK, space_after=0, line_spacing=1.05)
rect(s, L, 9.05, 18.2, 1.6, fill=NAVY)
tb(s, L + 0.4, 9.1, 17.4, 1.5, [[("Mensagem final: ", {"bold": True, "color": GOLD}),
                                 ("a fumaça cirúrgica está associada a uma carga sintomática relevante e a sinais biológicos "
                                  "precoces; proteger a equipe hoje é prudente, e medir o risco crônico é a tarefa dos próximos "
                                  "estudos.", {})]], size=18, color=WHITE, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
deck.notes(s, """[8:15–8:40] CONCLUSÃO (~25 s)
Concluindo. O que se sabe: sintomas oculares e respiratórios são frequentes na equipe exposta, com grande variação entre contextos, e os desfechos objetivos sinalizam alterações além do incômodo agudo. O que não se sabe: não há evidência direta de câncer ou DPOC atribuíveis à fumaça, a certeza é muito baixa e as coexposições limitam a atribuição causal.
A implicação prática é clara: pelo princípio da precaução e pela carga de sintomas, a exaustão local na fonte, os respiradores N95 e a educação da equipe se justificam hoje. E medir o risco de longo prazo é tarefa de estudos longitudinais.""")

# =====================================================================
# SLIDE 17 — PERSPECTIVAS FUTURAS
# =====================================================================
s = deck.content_slide("PERSPECTIVAS FUTURAS", "Agenda de pesquisa e próximos passos deste trabalho")
rect(s, L, 1.95, 11.0, 8.7, fill=LIGHT)
tb(s, L + 0.3, 2.05, 10.4, 0.5, ["Para o campo: o que falta para responder à pergunta do risco crônico"], size=19, color=NAVY,
   bold=True, space_after=0)
agenda = [
    ("timeline", "Estudos longitudinais", "Coortes com aferição objetiva da exposição (PM2,5, COV, tempo de dispositivo) e controle "
                                          "de coexposições (gases anestésicos, radiação) e tabagismo."),
    ("list", "Definições padronizadas", "Sintoma-índice, período de recordatório e instrumentos validados, com taxa de resposta "
                                         "relatada, para reduzir a heterogeneidade entre inquéritos."),
    ("dna", "Desfechos crônicos", "Incidência de câncer e DPOC na equipe cirúrgica; seguimento de marcadores (mucosa nasal, "
                                  "HPV, função pulmonar) ao longo do tempo."),
    ("fan", "Efetividade das medidas", "Estudos de intervenção sobre exaustão local, respiradores N95/PFF2 e educação, com "
                                       "medição de exposição antes e depois."),
]
for i, (ic, t, body) in enumerate(agenda):
    y = 2.75 + i * 1.95
    icon_badge(s, ic, L + 0.75, y + 0.5, d=0.85, fill=NAVY)
    tb(s, L + 1.5, y, 9.5, 0.45, [t], size=18, color=NAVY, bold=True, space_after=0)
    tb(s, L + 1.5, y + 0.45, 9.5, 1.4, [body], size=15, color=INK, space_after=0, line_spacing=1.05)
rect(s, 12.55, 1.95, 6.9, 8.7, fill=GOLD_TINT)
tb(s, 12.85, 2.05, 6.3, 0.5, ["Para este trabalho"], size=19, color=NAVY, bold=True, space_after=0)
nxt = [("upload", "Submissão do manuscrito a periódico indexado (versão final v5 concluída)."),
       ("calendar", "Atualização da busca antes da publicação e vigilância dos 6 relatórios não recuperados."),
       ("people", "Replicação da triagem e extração em duplicata, com segundo revisor independente."),
       ("hospital", "Devolutiva institucional: proposta de protocolo de proteção à fumaça no centro cirúrgico."),
       ("graduation", "Formação do aluno em síntese de evidências: do protocolo ao GRADE, com código aberto.")]
for i, (ic, body) in enumerate(nxt):
    y = 2.75 + i * 1.55
    icon(s, ic, 12.85, y + 0.1, 0.55, color="navy")
    tb(s, 13.6, y, 5.6, 1.45, [body], size=15, color=INK, space_after=0, line_spacing=1.05)
deck.notes(s, """[8:40–8:55] PERSPECTIVAS FUTURAS (~15 s)
Para o campo, a agenda é clara: coortes com medição objetiva da exposição e controle de coexposições, definições padronizadas de sintoma, desfechos crônicos como câncer e DPOC, e estudos de efetividade da exaustão e das máscaras.
Para este trabalho: submeter o manuscrito, atualizar a busca, replicar a triagem em duplicata e levar uma proposta de proteção para o nosso centro cirúrgico.""")

# =====================================================================
# SLIDE 18 — REFERÊNCIAS
# =====================================================================
s = deck.content_slide("REFERÊNCIAS BIBLIOGRÁFICAS", "Principais referências metodológicas e dos estudos incluídos (lista completa no manuscrito)")
refs_left = [
    "PAGE, M. J. et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ, v. 372, n71, 2021.",
    "BARKER, T. H. et al. Conducting proportional meta-analysis in different types of systematic reviews: a guide for synthesisers of evidence. BMC Med Res Methodol, v. 21, p. 189, 2021.",
    "INTHOUT, J.; IOANNIDIS, J. P. A.; BORM, G. F. The Hartung-Knapp-Sidik-Jonkman method for random effects meta-analysis is straightforward and considerably outperforms the standard DerSimonian-Laird method. BMC Med Res Methodol, v. 14, p. 25, 2014.",
    "RILEY, R. D.; HIGGINS, J. P. T.; DEEKS, J. J. Interpretation of random effects meta-analyses. BMJ, v. 342, d549, 2011.",
    "AROMATARIS, E.; MUNN, Z. (Ed.). JBI Manual for Evidence Synthesis. Adelaide: JBI, 2020.",
    "MUNN, Z. et al. Methodological guidance for systematic reviews of observational epidemiological studies reporting prevalence and cumulative incidence data. Int J Evid Based Healthc, v. 13, n. 3, p. 147-153, 2015.",
    "BRASIL. Ministério da Saúde. Diretrizes metodológicas: Sistema GRADE. Brasília: Ministério da Saúde, 2014.",
    "HURST, R. D.; STEWART, C. L. Hazards of surgical smoke from electrocautery: a critical review of the data. Am J Surg, v. 233, p. 29-36, 2024.",
]
refs_right = [
    "BENAIM, E. H.; JASPERS, I. Surgical smoke and its components, effects, and mitigation: a contemporary review. Toxicol Sci, v. 198, n. 2, p. 157-168, 2024.",
    "DIXON, K.; DASGUPTA, P.; VASDEV, N. A systematic review of the harmful effects of surgical smoke inhalation on operating room personnel. Health Sci Rev, v. 6, 100077, 2023.",
    "İLÇE, A.; YUZDEN, G. E.; VAN GIERSBERGEN, M. Y. The examination of problems experienced by nurses and doctors associated with exposure to surgical smoke and the necessary precautions. J Clin Nurs, v. 26, p. 1555-1561, 2017.",
    "BIENIEK, A. A. et al. Risco ocupacional: sinais e sintomas relacionados à exposição à fumaça cirúrgica. Rev SOBECC, v. 27, 2022.",
    "HU, X. et al. Prevalence of HPV infections in surgical smoke exposed gynecologists. Int Arch Occup Environ Health, v. 94, n. 1, p. 107-115, 2021.",
    "IBRAHIM, J. B. et al. Evaluation of spirometric lung function among healthcare professionals working in operating theatres: a comparative cross-sectional study. Afr J Thorac Crit Care Med, v. 31, n. 2, e2639, 2025.",
    "NAVARRO, M. C. et al. Cambios en la mucosa nasal de los médicos por exposición al humo por electrocoagulación. Rev Fac Nac Salud Pública, v. 34, n. 2, p. 135-144, 2016.",
    "CANICOBA, A. R. B. Impacto da exposição ocupacional à fumaça cirúrgica sobre os marcadores biológicos de profissionais de saúde da sala operatória. Tese (Doutorado). EE-USP, 2025.",
]
tb(s, L, 1.95, 8.9, 8.7, refs_left, size=15, color=INK, space_after=9, line_spacing=1.0)
tb(s, 10.55, 1.95, 8.9, 8.7, refs_right, size=15, color=INK, space_after=9, line_spacing=1.0)
deck.notes(s, """[8:55–9:00] REFERÊNCIAS (~5 s)
Estas são as principais referências metodológicas e dos estudos incluídos; a lista completa, com mais de 60 itens, está no manuscrito. (Não leia; apenas mencione e avance.)""")

# =====================================================================
# SLIDE 19 — AGRADECIMENTOS
# =====================================================================
s = deck.content_slide("AGRADECIMENTOS")
icon(s, "handshake", 9.6, 2.0, 1.1, color="navy")
tb(s, L, 3.3, 18.2, 0.7, ["Muito obrigado"], size=36, color=NAVY, bold=True, align=PP_ALIGN.CENTER, space_after=0)
ag = [
    ("graduation", "Orientadora", "Profa. Lisie Tocci Justo, pela orientação, supervisão metodológica e revisão crítica."),
    ("people", "Coautores", "Luiz Henrique Ledesma Pereira (SLMandic Araras) e Dra. Mariana Matera Veras (LIM05, HC-FMUSP), "
                            "pela interpretação dos resultados e revisão crítica."),
    ("hospital", "Instituição", "Faculdade São Leopoldo Mandic Araras e Programa de Iniciação Científica (PIC), na modalidade "
                                "voluntária, pelo apoio institucional e metodológico; professores colaboradores do projeto."),
]
for i, (ic, t, body) in enumerate(ag):
    x = L + i * (5.87 + 0.3)
    rect(s, x, 4.4, 5.87, 3.6, fill=LIGHT)
    icon_badge(s, ic, x + 2.935, 5.1, d=0.95, fill=NAVY)
    tb(s, x + 0.3, 5.75, 5.27, 0.5, [t], size=19, color=NAVY, bold=True, align=PP_ALIGN.CENTER, space_after=0)
    tb(s, x + 0.35, 6.25, 5.17, 1.7, [body], size=15, color=INK, align=PP_ALIGN.CENTER, space_after=0, line_spacing=1.05)
rect(s, L, 8.4, 18.2, 2.0, fill=NAVY_TINT)
tb(s, L + 0.4, 8.5, 17.4, 1.85, [
    [("Registro PROSPERO: ", {"bold": True, "color": NAVY}), ("CRD420251238727   ·   ", {}),
     ("Dados, código e figuras: ", {"bold": True, "color": NAVY}), ("osf.io/jktmn", {})],
    [("Financiamento: ", {"bold": True, "color": NAVY}), ("nenhum.   ·   ", {}),
     ("Conflitos de interesse: ", {"bold": True, "color": NAVY}), ("nenhum.   ·   ", {}),
     ("Dispensa do CEP: ", {"bold": True, "color": NAVY}), ("protocolo 2025/0743 (Res. CNS 510/2016).", {})],
    [("Contato: ", {"bold": True, "color": NAVY}), ("theo.baccaro@med.slmandic.edu.br", {})],
], size=16, color=INK, space_after=6, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
deck.notes(s, """[9:00–9:10] AGRADECIMENTOS (~10 s)
Agradeço à Profa. Lisie pela orientação, ao Luiz Henrique e à Dra. Mariana pela revisão crítica, e à Faculdade São Leopoldo Mandic e ao PIC pelo apoio. O protocolo está no PROSPERO e todo o código e as planilhas estão abertos no OSF. Obrigado. Estou à disposição para perguntas.""")

# =====================================================================
# SLIDE 20 — ENCERRAMENTO (slide do modelo, movido para o fim)
# =====================================================================
deck.move_slide_to_end(1)
enc = prs.slides[len(prs.slides) - 1]
deck.notes(enc, """ENCERRAMENTO
Deixe este slide na tela durante as perguntas. Respire, ouça a pergunta inteira, repita-a em uma frase ("a pergunta é sobre…") e responda em no máximo 30–40 segundos. Se não souber, diga o que o estudo permite afirmar e o que seria necessário para responder.""")

deck.save(OUT)
print(f"OK: {OUT} ({len(prs.slides)} slides)")
