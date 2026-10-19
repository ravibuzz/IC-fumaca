"""Gera a apresentação do VIII SEMICA sobre o modelo oficial.

Uso:  python3 build_deck.py  [saida.pptx]

Grade de layout: conteúdo de x = 1,25" a 19,45" e de y = 1,95" a 10,65" (9,85" nos slides com a trilha de
passos); respiro interno de 0,35" nos cards e 0,3" entre blocos; blocos lado a lado com topo e base alinhados.
"""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches

from notas_fala import NOTAS
from deck_lib import (ASSETS, AMBER, GAP, GOLD, GOLD_TINT, GRAY, GREEN, GREEN_TINT, INK, L, LIGHT, NAVY, NAVY_TINT, PAD,
                      R, RED, RED_TINT, TEAL, TEAL_TINT, WHITE, Build, Deck, add_transition, bar_chart, card, circle, cols,
                      fill_text, icon, icon_badge, line, pic, rect, rgb, stat, table, tb)

FIG = ASSETS / "figuras"
IMG = ASSETS / "imagens"
TRJ = ASSETS / "trajetoria"
TEMPLATE = ASSETS / "modelo" / "modelo_oficial_semica.pptx"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent / "SEMICA_Fumaca_Cirurgica_Baccaro.pptx"

OSF_URL = "https://osf.io/jktmn/"          # QR code: projeto público do OSF
# Troque para True depois de publicar o PDF do manuscrito no OSF; as legendas dos slides 19–21 passam a prometê-lo.
MANUSCRITO_NO_OSF = False
QR_TITULO = "Manuscrito completo, anexos e suplementos" if MANUSCRITO_NO_OSF else "Suplementos, código e planilhas"
QR_CURTO = "Manuscrito e suplementos" if MANUSCRITO_NO_OSF else "Suplementos"
QR_DADOS = "Manuscrito, dados e código: " if MANUSCRITO_NO_OSF else "Dados e código: "
QR_PNG = TRJ / "qr_osf_jktmn.png"

TITULO = ("Sintomas, desfechos objetivos e biomarcadores em profissionais de centro cirúrgico "
          "ocupacionalmente expostos à fumaça cirúrgica: revisão sistemática e metanálise de prevalência")

Y0, YB, YBT = 1.95, 10.65, 9.85            # topo do conteúdo; base sem trilha; base com trilha
DARK_GOLD = rgb("8A6D1F")
HL = {"hl": True}                          # marca-texto


def make_qr():
    try:
        import segno
    except ImportError:
        return
    segno.make(OSF_URL, error="h").save(str(QR_PNG), scale=24, border=4, dark="#002060", light="#FFFFFF")


make_qr()
deck = Deck(TEMPLATE)
prs = deck.prs

# =====================================================================
# 1 — CAPA (slide do modelo)
# =====================================================================
capa = prs.slides[0]
shapes = {s.name: s for s in capa.shapes}
tit = shapes["CaixaDeTexto 5"]
aut = shapes["CaixaDeTexto 4"]
cab = shapes["CaixaDeTexto 6"]  # "VIII SEMICA – SEMINÁRIO DE INICIAÇÃO CIENTÍFICA": mesmo texto e fonte, só recentralizado
cab.left, cab.width = Inches(2.6), Inches(14.8)
for par in cab.text_frame.paragraphs:
    par.alignment = PP_ALIGN.CENTER
tit.left, tit.top, tit.width, tit.height = Inches(2.6), Inches(5.35), Inches(14.8), Inches(1.75)
tf = tit.text_frame
tf.clear()
tf.word_wrap = True
fill_text(tf, [{"runs": [(TITULO, {})], "align": PP_ALIGN.CENTER}], size=32, color=NAVY, bold=True,
          space_after=0, line_spacing=1.0, font="Calibri")
aut.left, aut.top, aut.width, aut.height = Inches(4.0), Inches(7.3), Inches(12.0), Inches(1.4)
tf = aut.text_frame
tf.clear()
tf.word_wrap = True
fill_text(tf, [  # modelo oficial: Tahoma 18 para autor(a) e orientador(a)
    {"runs": [("Autor: ", {"bold": True}), ("Theo Augusto Lopes de Moraes Báccaro", {})], "align": PP_ALIGN.CENTER},
    {"runs": [("Orientadora: ", {"bold": True}), ("Profa. Lisie Tocci Justo", {})], "align": PP_ALIGN.CENTER},
    {"runs": [("Coautores: Luiz Henrique Ledesma Pereira; Mariana Matera Veras (LIM05, HC-FMUSP)",
               {"size": 16, "color": GRAY})], "align": PP_ALIGN.CENTER, "space_before": 4},
], size=18, color=INK, space_after=3, font="Tahoma")
deck.notes(capa, NOTAS["capa"], dur=15)

deck.remove_slides(range(1, 10))  # remove os slides-modelo 2..10; o encerramento (11) é preservado

# =====================================================================
# 2 — TRAJETÓRIA (um ano de preparação)
# =====================================================================
s = deck.content_slide("TRAJETÓRIA", "Mais de um ano de preparação: formação, protocolo, leitura de 10.910 registros e análise")
b = Build(s)
marcos = [
    ("graduation", "Jul/2025", "RS e metanálise (Unicamp) e escrita científica"),
    ("clipboard", "2025", "Protocolo no PROSPERO e dispensa do CEP"),
    ("book", "Mar/2026", "Normalização ABNT e referências (Fiocruz)"),
    ("search", "Jul/2026", "Busca final em 7 bases (09/07) e projeto no OSF"),
    ("filter", "Jul–Ago/2026", "10.910 títulos e resumos lidos, um a um"),
    ("chart", "Até Out/2026", "Extração, JBI, metanálise, GRADE e manuscrito"),
]
seg = (R - L) / len(marcos)
ly = 2.4
line(s, L + seg / 2, ly, R - seg / 2, ly, color=rgb("C9CFDA"), width=4)
for i, (ic, quando, oque) in enumerate(marcos):
    cx = L + seg * (i + 0.5)
    with b.step():
        icon_badge(s, ic, cx, ly, d=0.8, fill=RED if i == len(marcos) - 1 else NAVY)
        tb(s, cx - seg / 2 + 0.1, 2.9, seg - 0.2, 0.4, [quando], size=18, color=NAVY, bold=True, align=PP_ALIGN.CENTER,
           space_after=0)
        tb(s, cx - seg / 2 + 0.2, 3.3, seg - 0.4, 0.75, [oque], size=15, color=INK, align=PP_ALIGN.CENTER, space_after=0)
PY = 4.2
PH = YB - PY
LW2 = 5.7                                   # certificados em grade 2 x 2 à esquerda; capas à direita
lx, lw, rx = L, LW2, L + LW2 + GAP
rw = R - rx
certs = [
    ("cert_unicamp_rs_metanalise.jpg", "RS e Metanálise", "Unicamp · 40 h", "com distinção"),
    ("cert_zuco_escrita.jpg", "Escrita científica", "ZucoEscrita · 3,6 h", None),
    ("cert_fiocruz_abnt.jpg", "Normas ABNT", "Fiocruz · 3 h", None),
    ("cert_fiocruz_referencias.jpg", "Referências (ABNT)", "Fiocruz · 2 h", None),
]
# (arquivo, linha 1, linha 2): obras usadas no trabalho — guias e ferramentas citados no manuscrito + manuais e livros estudados
guias = [
    ("capa_prisma2020.jpg", "PRISMA 2020", "Page et al."),
    ("capa_ms_observacionais.jpg", "MS 2014", "Observacionais"),
    ("capa_ms_grade.jpg", "MS 2014", "Sistema GRADE"),
    ("capa_jbi_prevalencia.jpg", "JBI", "Prevalência"),
    ("capa_jbi_transversal.jpg", "JBI", "Transversal"),
    ("capa_jbi_coorte.jpg", "JBI", "Coorte"),
]
livros = [
    ("capa_cochrane_handbook.jpg", "Cochrane", "Handbook, 2019"),
    ("capa_jbi_manual.jpg", "JBI Manual", "Síntese, 2020"),
    ("capa_borenstein.jpg", "Borenstein et al.", "Metanálise, 2021"),
    ("capa_harrer.jpg", "Harrer et al.", "Metanálise em R"),
]
TOP = PY + PAD + 0.7 + 0.2                 # abaixo do título do card
with b.step():
    card(s, lx, PY, lw, PH, title="Formação certificada · ≈ 49 h", icon_name="graduation", title_size=19, badge_d=0.7)
    CH = 1.5
    cw = (lw - 2 * PAD - 0.3) / 2
    row_h = (YB - PAD - TOP) / 2
    for k, (img, nome, meta, extra) in enumerate(certs):
        cx0 = lx + PAD + (k % 2) * (cw + 0.3)
        y0 = TOP + (k // 2) * row_h
        with Image.open(TRJ / img) as im:
            wi = min(cw, CH * im.size[0] / im.size[1])
        pic(s, TRJ / img, cx0 + (cw - wi) / 2, y0, w=wi, h=CH, border=rgb("C9CFDA"))
        par = [{"runs": [(nome, {"bold": True, "color": NAVY})], "space_after": 1}, {"runs": [(meta, {"color": GRAY})]}]
        if extra:
            par.append({"runs": [(extra, {"bold": True, "color": DARK_GOLD})]})
        tb(s, cx0, y0 + CH + 0.1, cw, 0.75, par, size=14, align=PP_ALIGN.CENTER, space_after=0)
COV_H = 1.5
NCOL = 6
colw = (rw - 2 * PAD) / NCOL
row2_h = (YB - PAD - TOP) / 2


def linha_capas(itens, y0, rotulo):
    tb(s, rx + PAD, y0, rw - 2 * PAD, 0.32, [rotulo], size=14, color=GRAY, bold=True, space_after=0)
    x0 = rx + PAD + (NCOL - len(itens)) * colw / 2      # linha mais curta fica centralizada
    for j, (img, l1, l2) in enumerate(itens):
        cx0 = x0 + j * colw
        pic(s, TRJ / img, cx0 + 0.1, y0 + 0.4, w=colw - 0.2, h=COV_H, border=rgb("C9CFDA"))
        tb(s, cx0, y0 + 0.4 + COV_H + 0.08, colw, 0.5, [{"runs": [(l1, {"bold": True, "color": NAVY})], "space_after": 1},
                                                          {"runs": [(l2, {"color": GRAY})]}],
           size=13, align=PP_ALIGN.CENTER, space_after=0)


with b.step():
    card(s, rx, PY, rw, PH, title="Base metodológica: guias, ferramentas e livros estudados", icon_name="book",
         title_size=19, badge_d=0.7)
    linha_capas(guias, TOP, "GUIA DE RELATO, DIRETRIZES DO MINISTÉRIO DA SAÚDE E FERRAMENTAS DE RISCO DE VIÉS")
with b.step():
    linha_capas(livros, TOP + row2_h, "MANUAIS E LIVROS DE REVISÃO SISTEMÁTICA E METANÁLISE")
b.apply()
deck.notes(s, NOTAS["trajetoria"], dur=25)

# =====================================================================
# 3 — INTRODUÇÃO
# =====================================================================
s = deck.content_slide("INTRODUÇÃO", "Fumaça cirúrgica: o que é e por que importa")
LW = 8.3
foto = pic(s, IMG / "centro_cirurgico_fumaca.png", L, Y0, w=LW, name="Foto centro cirúrgico")
fy = Y0 + foto.height / 914400
tb(s, L, fy + 0.1, LW, 0.35, ["Imagem ilustrativa (gerada por IA): pluma de fumaça do eletrocautério no campo cirúrgico."],
   size=14, color=GRAY, space_after=0)
SY = fy + 0.6
rect(s, L, SY, LW, YB - SY, fill=NAVY_TINT)
tb(s, L + PAD, SY + PAD, LW - 2 * PAD, 0.45, ["Sintomas agudos relatados pela equipe exposta"], size=19, color=NAVY,
   bold=True, space_after=0)
sint = [("eye", "Irritação ocular e lacrimejamento"), ("lungs", "Tosse e irritação das vias aéreas"),
        ("nose", "Irritação de mucosas"), ("exclaim", "Cefaleia e náusea")]
step_y = (YB - PAD - (SY + PAD + 0.6)) / len(sint)
for i, (ic, txt) in enumerate(sint):
    yy = SY + PAD + 0.6 + i * step_y
    icon(s, ic, L + PAD, yy + (step_y - 0.42) / 2, 0.42, color="navy")
    tb(s, L + PAD + 0.62, yy, LW - 2 * PAD - 0.62, step_y, [txt], size=18, color=INK, space_after=0,
       anchor=MSO_ANCHOR.MIDDLE)
RX = L + LW + 0.6
rows = [
    ("smoke", "O que é", [[("Subproduto da ", {}), ("destruição térmica dos tecidos", {"bold": True}),
                          (" por dispositivos de energia: eletrocautério, laser e bisturi ultrassônico "
                           "(Benaim; Jaspers, 2024).", {})]]),
    ("flask", "O que contém", [[("Hidrocarbonetos aromáticos policíclicos, ", {}), ("compostos orgânicos voláteis", {"bold": True}),
                               (" (benzeno, tolueno, xileno), ", {}), ("material particulado fino (PM2,5) e ultrafino", {"bold": True}),
                               (" e material genético viral, como o HPV.", {})]]),
    ("warning", "O que se sabe (e o que não se sabe)", [[("Sintomas agudos são frequentes. Efeitos crônicos (neoplasias, doença "
                                                         "respiratória) são plausíveis, mas ", {}),
                                                        ("sem relação causal estabelecida", {"bold": True, **HL}),
                                                        ("; o tema é controverso (Hurst; Stewart, 2024).", {})]]),
    ("shield", "Por que importa", [[("Exaustão de fumaça e máscaras de alta filtração ainda são ", {}),
                                    ("pouco adotadas", {"bold": True}),
                                    (" e não há diretrizes harmonizadas. As revisões anteriores eram descritivas, sem síntese "
                                     "quantitativa.", {})]]),
]
LAC_H = 1.45
row_h = (YB - LAC_H - GAP - Y0) / len(rows)
for i, (ic, t, body) in enumerate(rows):
    yy = Y0 + i * row_h
    icon_badge(s, ic, RX + 0.45, yy + 0.45, d=0.9, fill=NAVY)
    tb(s, RX + 1.2, yy, R - RX - 1.2, 0.45, [t], size=20, color=NAVY, bold=True, space_after=0)
    tb(s, RX + 1.2, yy + 0.48, R - RX - 1.2, row_h - 0.55, body, size=17, color=INK, space_after=0, line_spacing=1.02)
rect(s, RX, YB - LAC_H, R - RX, LAC_H, fill=GOLD_TINT)
tb(s, RX + PAD, YB - LAC_H + 0.2, R - RX - 2 * PAD, LAC_H - 0.4,
   [[("Lacuna → ", {"bold": True, "color": RED}), ("síntese em camadas: ", {"bold": True}),
     ("metanálise da prevalência de sintomas + síntese narrativa, com GRADE, dos desfechos objetivos e biomarcadores.", {})]],
   size=17, color=INK, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
deck.notes(s, NOTAS["introducao"], dur=45)

# =====================================================================
# 4 — OBJETIVOS
# =====================================================================
s = deck.content_slide("OBJETIVOS", "Pergunta estruturada: PECO para os desfechos comparativos e CoCoPop para a prevalência")
rect(s, L, Y0, R - L, 1.35, fill=NAVY)
tb(s, L + 0.45, Y0 + 0.15, R - L - 0.9, 1.05, [[("Objetivo geral: ", {"bold": True, "color": GOLD}),
                                               ("avaliar os desfechos de saúde associados à exposição ocupacional à fumaça "
                                                "cirúrgica na equipe de centro cirúrgico, com ênfase na prevalência de sintomas, "
                                                "nos desfechos objetivos e nos biomarcadores de exposição ou de possível efeito.", {})]],
   size=21, color=WHITE, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
peco = [
    ("P", "População", "Equipe de centro cirúrgico: cirurgiões, residentes, enfermagem, instrumentadores e anestesia."),
    ("E", "Exposição", "Fumaça gerada por dispositivos de energia (eletrocautério, laser, bisturi ultrassônico)."),
    ("C", "Comparador", "Não expostos, pouco expostos ou protegidos (exaustão local, máscaras de alta filtração)."),
    ("O", [("Outcome", {}), (" (desfecho)", {"bold": False, "size": 17})],
     "Efeitos à saúde relacionados à exposição: sintomas, medidas objetivas e biomarcadores."),
]
PE_Y, PE_H = 3.6, 2.65
for (x, w), (letter, name, body) in zip(cols(4), peco):
    rect(s, x, PE_Y, w, PE_H, fill=LIGHT)
    circle(s, x + PAD + 0.375, PE_Y + PAD + 0.375, 0.75, fill=NAVY, text=letter, size=26)
    tb(s, x + PAD + 1.0, PE_Y + PAD, w - 2 * PAD - 1.0, 0.75, [name], size=20, color=NAVY, bold=True, space_after=0,
       anchor=MSO_ANCHOR.MIDDLE)
    tb(s, x + PAD, PE_Y + PAD + 0.95, w - 2 * PAD, PE_H - 2 * PAD - 0.95, [body], size=16, color=INK, space_after=0,
       line_spacing=1.05)
CL_Y = PE_Y + PE_H + 0.25
tb(s, L, CL_Y, R - L, 0.4, [[("Para a prevalência (metanálise de proporções): ", {"bold": True, "color": NAVY}),
                            ("esquema CoCoPop (Munn et al., 2015)", {"color": GRAY})]], size=18, space_after=0)
coco = [("Condição", "Sintomas oculares e respiratórios autorrelatados, relacionados à exposição"),
        ("Contexto", "Centro cirúrgico com uso de dispositivos de energia"),
        ("População", "Equipe de centro cirúrgico")]
CC_Y, CC_H = CL_Y + 0.5, 1.5
for (x, w), (name, body) in zip(cols(3), coco):
    rect(s, x, CC_Y, w, CC_H, fill=TEAL_TINT)
    tb(s, x + PAD, CC_Y + 0.27, w - 2 * PAD, 0.38, [name], size=18, color=TEAL, bold=True, space_after=0)
    tb(s, x + PAD, CC_Y + 0.7, w - 2 * PAD, CC_H - 0.95, [body], size=16, color=INK, space_after=0)
OB_Y = CC_Y + CC_H + GAP
(ox, ow), (ax, aw) = (L, 11.2), (L + 11.2 + GAP, R - L - 11.2 - GAP)
rect(s, ox, OB_Y, ow, YB - OB_Y, fill=GOLD_TINT)
tb(s, ox + PAD, OB_Y + 0.28, ow - 2 * PAD, YB - OB_Y - 0.5, [
    {"runs": [("Objetivos específicos", {"bold": True, "color": NAVY, "size": 17})], "space_after": 4},
    {"runs": [("Metanálise da prevalência de sintoma ", {}), ("ocular (principal)", {"bold": True}),
              (" e respiratório (exploratório);", {})], "bullet": "1."},
    {"runs": [("Síntese narrativa dos ", {}), ("desfechos objetivos e biomarcadores", {"bold": True}), (";", {})], "bullet": "2."},
    {"runs": [("Certeza da evidência por desfecho (", {}), ("GRADE", {"bold": True}), (").", {})], "bullet": "3."},
], size=16, color=INK, space_after=3)
rect(s, ax, OB_Y, aw, YB - OB_Y, fill=RED_TINT)
icon(s, "warning", ax + PAD, OB_Y + (YB - OB_Y - 0.55) / 2, 0.55, color="red")
tb(s, ax + PAD + 0.8, OB_Y + 0.25, aw - 2 * PAD - 0.8, YB - OB_Y - 0.5,
   [[("Atenção: ", {"bold": True, "color": RED}), ("a metanálise de proporções ", {}),
     ("estima a frequência de sintomas em expostos", {"bold": True, **HL}),
     (", não o efeito causal da fumaça; a causalidade depende dos estudos comparativos.", {})]],
   size=16, color=INK, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
deck.notes(s, NOTAS["objetivos"], dur=23)

# =====================================================================
# 5 — METODOLOGIA: MAPA DOS 7 PASSOS
# =====================================================================
s = deck.content_slide("METODOLOGIA", "Mapa da revisão: 7 passos, do protocolo à certeza da evidência (PRISMA 2020)")
b = Build(s)
steps = [
    ("Protocolo", ["PECO e CoCoPop", "PRISMA 2020 e Diretrizes do MS", "PROSPERO CRD420251238727",
                              "Dispensa do CEP 2025/0743"]),
    ("Busca", ["7 bases + literatura cinzenta", "Busca por citação (OpenAlex)", "Sem filtro de idioma ou data",
               "Última busca: 09/07/2026"]),
    ("Seleção", ["Zotero → Rayyan", "Deduplicação automática", "Triagem e leitura na íntegra", "Controle de sobreposição"]),
    ("Extração", ["Planilha padronizada", "Eventos e denominadores", "Definição do desfecho", "Taxa de resposta"]),
    ("Risco de viés", ["Ferramentas JBI", "Prevalência (9 itens)", "Transversal (8) e coorte (11)", "Domínios críticos"]),
    ("Síntese", ["Metanálise de proporções", "Logito + efeitos aleatórios", "Hartung-Knapp", "Predição (IP) e sensibilidade"]),
    ("Certeza (GRADE)", ["GRADE adaptado à prevalência", "5 domínios", "Ponto de partida: baixa", "Justificativa por domínio"]),
]
step_cols = cols(len(steps), L, R, gap=0.15)  # bordas externas rente à faixa de ferramentas
cy = 2.45
line(s, step_cols[0][0] + step_cols[0][1] / 2, cy, step_cols[-1][0] + step_cols[-1][1] / 2, cy, color=rgb("C9CFDA"),
     width=4)
CY0, CH = 3.85, 3.05
for i, ((x0, w0), (t, body)) in enumerate(zip(step_cols, steps), start=1):
    cx = x0 + w0 / 2
    with b.step():
        circle(s, cx, cy, 0.95, fill=RED if i == 6 else NAVY, text=str(i), size=28)
        tb(s, x0, 3.08, w0, 0.7, [t], size=19, color=NAVY, bold=True, align=PP_ALIGN.CENTER, space_after=0)
        rect(s, x0, CY0, w0, CH, fill=LIGHT)
        tb(s, x0 + 0.22, CY0 + 0.25, w0 - 0.44, CH - 0.5, body, size=16, color=INK, space_after=10, line_spacing=1.0)
TS_Y, TS_H = CY0 + CH + GAP, 1.4
with b.step():
    rect(s, L, TS_Y, R - L, TS_H, fill=NAVY_TINT)
    tb(s, L + PAD, TS_Y + 0.2, 2.05, TS_H - 0.4, [[("Ferramentas", {"bold": True, "color": NAVY, "size": 19})],
                                               "(função operacional)"], size=14, color=GRAY, space_after=2,
       anchor=MSO_ANCHOR.MIDDLE)
    tools = [("database", "Zotero 6", "gestão de referências"), ("filter", "Rayyan", "deduplicação e triagem"),
             ("link", "OpenAlex", "metadados e citações"), ("code", "Python 3.13", "NumPy, SciPy, statsmodels"),
             ("robot", "Assistente de IA", "apoio operacional")]
    # posições a partir da largura medida de cada rótulo: ~0,35 pol. entre um grupo e o ícone seguinte
    for x, lw_, (ic, name, desc) in zip([3.65, 6.73, 9.95, 13.04, 16.58], [2.05, 2.20, 2.05, 2.75, 1.90], tools):
        icon(s, ic, x, TS_Y + (TS_H - 0.55) / 2, 0.55, color="navy")
        tb(s, x + 0.7, TS_Y + 0.25, lw_, 0.4, [name], size=17, color=NAVY, bold=True, space_after=0)
        tb(s, x + 0.7, TS_Y + 0.65, lw_, 0.55, [desc], size=15, color=INK, space_after=0)
NB_Y = TS_Y + TS_H + GAP
with b.step():
    for (x, w), body in zip(cols(2), [
        [[("Uso de IA (declarado, Portaria CNPq nº 2.664/2026): ", {"bold": True, "color": NAVY}),
          ("apoio operacional na priorização da leitura, na leitura assistida de resumos e na organização do fluxo. ", {}),
          ("Elegibilidade, extração, interpretação e redação: decisões humanas.", {"bold": True})]],
        [[("Transparência e reprodutibilidade: ", {"bold": True, "color": NAVY}),
          ("checklist PRISMA 2020 (27 itens), estratégias completas (Anexo A), extração, JBI e GRADE em anexos; ", {}),
          ("código, figuras e planilhas abertos no OSF.", {"bold": True})]],
    ]):
        rect(s, x, NB_Y, w, YB - NB_Y, fill=LIGHT)
        tb(s, x + PAD, NB_Y + 0.22, w - 2 * PAD, YB - NB_Y - 0.44, body, size=15, color=INK, space_after=0,
           anchor=MSO_ANCHOR.MIDDLE)
b.apply()
deck.notes(s, NOTAS["mapa"], dur=30)

# =====================================================================
# 6 — PASSOS 1 e 2: ELEGIBILIDADE E BUSCA
# =====================================================================
s = deck.content_slide("METODOLOGIA", "Passos 1 e 2 · Critérios de elegibilidade e busca de alta sensibilidade", track={1, 2})
LW6 = 8.4
rect(s, L, Y0, LW6, YBT - Y0, fill=LIGHT)
tb(s, L + PAD, Y0 + PAD, LW6 - 2 * PAD, 0.45, ["Critérios de elegibilidade e ajustes posteriores declarados"], size=19,
   color=NAVY, bold=True, space_after=0)
icon(s, "check", L + PAD, Y0 + 0.95, 0.4, color="teal")
tb(s, L + PAD + 0.55, Y0 + 0.95, 6.0, 0.4, ["Incluímos"], size=18, color=TEAL, bold=True, space_after=0,
   anchor=MSO_ANCHOR.MIDDLE)
tb(s, L + PAD, Y0 + 1.4, LW6 - 2 * PAD, 2.85, [
    "Estudos observacionais (transversais, caso-controle, coorte);",
    "Profissionais de centro cirúrgico expostos à fumaça cirúrgica;",
    "Efeitos à saúde ou marcadores de exposição como desfecho;",
    "Português, inglês ou espanhol; sem restrição de data;",
    [("Resumos de congresso com eventos e denominador extraíveis (preocupação alta; ", {}),
     ("ajuste posterior ao registro, declarado", {"color": DARK_GOLD, "bold": True}), (").", {})],
], size=18, color=INK, bullet=True, bullet_color=TEAL, space_after=9)
EX_Y = Y0 + 4.55
icon(s, "xmark", L + PAD, EX_Y + 0.05, 0.4, color="red")
tb(s, L + PAD + 0.55, EX_Y + 0.05, 6.0, 0.4, ["Excluímos"], size=18, color=RED, bold=True, space_after=0,
   anchor=MSO_ANCHOR.MIDDLE)
tb(s, L + PAD, EX_Y + 0.5, LW6 - 2 * PAD, YBT - EX_Y - 0.5 - PAD, [
    "Estudos in vitro ou em animais;",
    "População fora do centro cirúrgico (ex.: ambulatórios);",
    "Desfecho apenas no paciente;",
    "Medição físico-química do ar sem desfecho humano;",
    "Revisões, editoriais, cartas e comentários;",
    "Exposição não atribuível à fumaça (gases, radiação).",
], size=18, color=INK, bullet=True, bullet_color=RED, space_after=9)
RX6 = L + LW6 + GAP
CHART_B = 6.85
rect(s, RX6, Y0, R - RX6, CHART_B - Y0, fill=WHITE, line=rgb("C9CFDA"))
tb(s, RX6 + PAD, Y0 + PAD - 0.05, R - RX6 - 2 * PAD, 0.4, ["Registros recuperados por fonte (busca em 09/07/2026)"],
   size=18, color=NAVY, bold=True, space_after=0)
bar_chart(s, RX6 + 0.15, Y0 + 0.8, 6.45, CHART_B - Y0 - 0.95,
          ["PubMed/MEDLINE", "Embase", "Web of Science", "Scopus", "BVS (LILACS/IBECS)", "Google Scholar", "SciELO",
           "Cochrane CENTRAL", "Catálogo CAPES"],
          [4522, 4660, 3629, 2639, 1229, 50, 28, 0, 0], color=NAVY, font_size=14,
          labels=["4.522", "4.660", "3.629", "2.639", "1.229", "50", "28", "0", "0"])
SX6 = RX6 + 6.75
SW6 = R - PAD - SX6
stat(s, SX6, Y0 + 0.85, SW6, "16.757", "registros identificados", h=1.45, num_size=40, lab_size=16, num_color=RED)
stat(s, SX6, Y0 + 2.45, SW6, "+ 443", "referências na busca por citação (OpenAlex)", h=1.55, num_size=32, lab_size=15,
     num_color=NAVY)
tb(s, SX6, CHART_B - PAD - 0.75, SW6, 0.75, ["Cinzenta: Google Scholar (4 × 50 resultados) e Catálogo CAPES"],
   size=14, color=GRAY, space_after=0)
ST_Y = CHART_B + GAP
rect(s, RX6, ST_Y, R - RX6, YBT - ST_Y, fill=GOLD_TINT)
tb(s, RX6 + PAD, ST_Y + PAD - 0.05, R - RX6 - 2 * PAD, 0.4, ["Como a estratégia foi construída"], size=18, color=NAVY,
   bold=True, space_after=0)
tb(s, RX6 + PAD, ST_Y + 0.85, R - RX6 - 2 * PAD, YBT - ST_Y - 0.85 - PAD, [
    [("Dois blocos: ", {"bold": True}), ("(equipe cirúrgica) AND (fumaça OR dispositivos de energia); MeSH/Emtree e texto "
                                        "livre; sem bloco de desfecho.", {})],
    [("Sem filtro de idioma ou data na busca", {"bold": True, **HL}), (" → alta sensibilidade (Anexo A).", {})],
    [("Busca por citação (OpenAlex): ", {"bold": True}), ("referências dos incluídos e quem os cita.", {})],
], size=16, color=INK, bullet=True, bullet_color=GOLD, space_after=6)
deck.notes(s, NOTAS["passos12"], dur=35)

# =====================================================================
# 7 — PASSO 3: SELEÇÃO
# =====================================================================
s = deck.content_slide("METODOLOGIA", "Passo 3 · Seleção dos estudos: do registro bruto ao relatório incluído", track=3)
b = Build(s)
flow = [("16.757", ["registros identificados", "nas bases e", "na literatura cinzenta"], NAVY),
        ("10.910", ["registros únicos"], NAVY),
        ("32", ["buscados na íntegra", "(28 da triagem +", "4 por citação)"], NAVY),
        ("26", ["avaliados para", "elegibilidade"], NAVY),
        ("22", ["relatórios incluídos"], RED)]
between = [["5.839", "duplicatas", "+ 8 não", "exportados"], ["10.882", "excluídos", "na triagem"], ["6 não", "recuperados"],
           ["4 excluídos", "na íntegra"]]
FB_Y, FB_H = Y0, 2.2
bw, bg = 2.6, (R - L - 5 * 2.6) / 4
for i, (num, lab, col) in enumerate(flow):
    x = L + i * (bw + bg)
    with b.step():
        if i > 0:
            px = x - bg
            line(s, px + 0.08, FB_Y + 0.8, x - 0.08, FB_Y + 0.8, color=NAVY, width=2.5, arrow=True)
            tb(s, px + 0.04, FB_Y + 1.0, bg - 0.08, 1.0, between[i - 1], size=14, color=GRAY, align=PP_ALIGN.CENTER,
               space_after=0, line_spacing=0.95)
        rect(s, x, FB_Y, bw, FB_H, fill=RED_TINT if col == RED else LIGHT)
        tb(s, x + 0.2, FB_Y + 0.2, bw - 0.4, 0.75, [num], size=40, color=col, bold=True, align=PP_ALIGN.CENTER,
           space_after=0)
        tb(s, x + 0.25, FB_Y + 1.0, bw - 0.5, FB_H - 1.25, lab, size=15, color=INK, align=PP_ALIGN.CENTER, space_after=0)
cards = [
    ("filter", "Deduplicação e triagem", [
        [("Zotero → Rayyan: ", {"bold": True}), ("duplicatas por DOI, PMID e similaridade de título.", {})],
        [("10.910 títulos e resumos ", {"bold": True}), ("lidos por um único revisor.", {})],
        [("Script em Python e IA: apoio operacional ", {}), ("(ordem de leitura, leitura assistida, fluxo); ", {}),
         ("elegibilidade decidida por humano.", {"bold": True})],
    ]),
    ("book", "Leitura na íntegra", [
        [("Critérios definitivos; ", {"bold": True}), ("motivo de exclusão registrado (Anexo C).", {})],
        [("Excluídos: ", {"bold": True}), ("1 resumo sem dados e 3 por população ou contexto.", {})],
        [("Sintoma-índice: ", {"bold": True}), ("o mais específico de cada via (lacrimejamento ou irritação ocular; tosse "
                                               "ou irritação de vias aéreas).", {})],
    ]),
    ("people", "Sobreposição amostral", [
        [("7 publicações do mesmo grupo ", {"bold": True}), ("(Paraná) com amostras sobrepostas.", {})],
        [("1 representante por desfecho, ", {"bold": True}), ("definido antes da síntese: Bieniek et al., 2022.", {})],
        [("Nenhuma sobreposição documentada dentro de cada agrupamento.", {"bold": True, **HL})],
    ]),
]
CA_Y = FB_Y + FB_H + GAP
BN_H = 1.15
CA_H = YBT - BN_H - GAP - CA_Y
for (x, w), (ic, t, body) in zip(cols(3), cards):
    with b.step():
        card(s, x, CA_Y, w, CA_H, title=t, body=body, icon_name=ic, body_size=16, bullet=True, fill=LIGHT,
             body_space_after=7)
with b.step():
    rect(s, L, YBT - BN_H, R - L, BN_H, fill=GOLD_TINT)
    icon(s, "exclaim", L + PAD, YBT - BN_H + (BN_H - 0.55) / 2, 0.55, color="navy")
    tb(s, L + PAD + 0.8, YBT - BN_H + 0.15, R - L - 2 * PAD - 0.8, BN_H - 0.3, [
        [("6 relatórios não recuperados ", {"bold": True, "color": NAVY}),
         ("apesar de acesso institucional, repositórios, páginas dos autores, comutação e contato com autores; entre eles, "
          "2 inquéritos de sintomas e 1 estudo de olho seco → possível impacto, declarado como limitação.", {})]],
       size=15, color=INK, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
b.apply()
deck.notes(s, NOTAS["passo3"], dur=35)

# =====================================================================
# 8 — PASSOS 4 e 5: EXTRAÇÃO E RISCO DE VIÉS
# =====================================================================
s = deck.content_slide("METODOLOGIA", "Passos 4 e 5 · Extração padronizada e avaliação do risco de viés (JBI)", track={4, 5})
LW8 = 7.3
card(s, L, Y0, LW8, YBT - Y0, title="Extração dos dados", icon_name="table", fill=LIGHT, body_size=18, bullet=True,
     body_space_after=8, body=[
         [("Planilha padronizada: ", {"bold": True}), ("autor, ano, país; desenho; população; dispositivo; comparador; "
                                                      "instrumento e definição do desfecho; taxa de resposta; resultados.", {})],
         [("Para a metanálise: ", {"bold": True}), ("eventos e denominador de cada grupo (Anexo D).", {})],
         [("Recordatório, validação e taxa de resposta ", {"bold": True}),
          ("raramente informados → “não relatado”.", {})],
         [("Sem contato com autores; ", {"bold": True}), ("planilha completa pública no OSF.", {})],
     ])
TB_ROWS = [
    ["Estudo", "Eventos", "n", "Prev.", "Definição"],
    ["İlçe et al., 2017", "33", "81", "40,7%", "lacrimejamento"],
    ["Usta et al., 2019", "57", "105", "54,3%", "lacrimejamento"],
    ["Cinar; Sanlier, 2022", "46", "82", "56,1%", "irritação ocular"],
    ["Bieniek et al., 2022", "67", "155", "43,2%", "escala ocular"],
]
TBL_Y = YBT - PAD - 0.44 * 5 - 0.06
tb(s, L + PAD, TBL_Y - 0.5, LW8 - 2 * PAD, 0.4, ["Exemplo de linhas extraídas (Anexo D, sintoma ocular)"], size=15,
   color=NAVY, bold=True, space_after=0)
table(s, L + PAD, TBL_Y, LW8 - 2 * PAD, TB_ROWS, col_widths=[2.3, 1.0, 0.65, 0.9, 1.75], size=14, row_h=0.44,
      align_cols={1: PP_ALIGN.CENTER, 2: PP_ALIGN.CENTER, 3: PP_ALIGN.CENTER})
RX8 = L + LW8 + GAP
tb(s, RX8, Y0, R - RX8, 0.45, ["Risco de viés: ferramenta JBI escolhida pela função de cada estudo"], size=18,
   color=NAVY, bold=True, space_after=0)
jbi = [("Prevalência", "9 itens", "estudos das metanálises (k = 7)", NAVY),
       ("Transversal analítico", "8 itens", "comparativos e objetivos", TEAL),
       ("Coorte", "11 itens", "3 coortes prospectivas", DARK_GOLD)]
JT_Y, JT_H = Y0 + 0.6, 1.5
for (x, w), (t, items, who, col) in zip(cols(3, RX8, R, gap=0.25), jbi):
    rect(s, x, JT_Y, w, JT_H, fill=LIGHT)
    tb(s, x + 0.25, JT_Y + 0.2, w - 0.5, 0.35, [t], size=16, color=col, bold=True, space_after=0)
    tb(s, x + 0.25, JT_Y + 0.55, w - 0.5, 0.45, [items], size=22, color=INK, bold=True, space_after=0)
    tb(s, x + 0.25, JT_Y + 1.02, w - 0.5, 0.3, [who], size=14, color=GRAY, space_after=0)
tb(s, RX8, JT_Y + JT_H + 0.22, R - RX8, 0.95, [
    [("Julgamento global: ", {"bold": True, "color": NAVY}),
     ("qualitativo, pelos domínios críticos (amostragem, tamanho amostral, validade da mensuração, taxa de resposta), "
      "não por corte percentual; “não” pesou mais que “incerto”. Todos os estudos foram mantidos e a classificação "
      "alimentou o GRADE.", {})]], size=15, color=INK, space_after=0)
FIG_Y = JT_Y + JT_H + 1.3
CAP_H = 0.82
# Figura E1 redesenhada com formas nativas (nítida em qualquer projetor): itens 1–9 da lista JBI de prevalência
JBI_ROWS = [
    ("İlçe et al., 2017", "+??++-++?", "A"),
    ("Cinar; Sanlier, 2022", "+??+++++?", "M"),
    ("Usta et al., 2019", "+??++-++?", "A"),
    ("Mohd Fikri Rosely; Titi Rahmawati, 2019", "+++++-++?", "M"),
    ("Van Giersbergen et al., 2019", "+-?++-++?", "A"),
    ("Bieniek et al., 2022", "+??+++++?", "M"),
    ("Mohd Fikri Rosely, 2022", "?????????", "A"),
]
SYM = {"+": ("+", GREEN), "?": ("?", AMBER), "-": ("−", RED)}
NW = 4.05
gx0 = RX8 + NW + 0.15
gcw = (R - gx0) / 10
HDR_H = 0.38
grow = (YBT - CAP_H - 0.12 - FIG_Y - HDR_H) / len(JBI_ROWS)
for j, lab in enumerate([str(k) for k in range(1, 10)] + ["Geral"]):
    tb(s, gx0 + j * gcw, FIG_Y, gcw, HDR_H, [lab], size=14, color=NAVY, bold=True, align=PP_ALIGN.CENTER,
       space_after=0, anchor=MSO_ANCHOR.MIDDLE)
for i, (nome, itens, geral) in enumerate(JBI_ROWS):
    ry = FIG_Y + HDR_H + i * grow
    if i % 2 == 0:
        rect(s, RX8, ry, R - RX8, grow, fill=LIGHT, radius=0, name="Faixa zebrada")
    tb(s, RX8 + 0.1, ry, NW - 0.1, grow, [nome], size=14, color=INK, align=PP_ALIGN.RIGHT, space_after=0,
       anchor=MSO_ANCHOR.MIDDLE)
    for j, ch in enumerate(itens):
        sym, col = SYM[ch]
        circle(s, gx0 + (j + 0.5) * gcw, ry + grow / 2, min(0.36, grow - 0.08), fill=col, text=sym, size=14)
    circle(s, gx0 + 9.5 * gcw, ry + grow / 2, min(0.36, grow - 0.08), fill=RED if geral == "A" else AMBER)
tb(s, RX8, YBT - CAP_H, R - RX8, CAP_H, [
    [("Figura E1. ", {"bold": True}), ("+ sim  ", {"color": GREEN, "bold": True}), ("? incerto  ", {"color": AMBER, "bold": True}),
     ("− não", {"color": RED, "bold": True}), ("  ·  Geral: ", {"bold": True}), ("● alta  ", {"color": RED, "bold": True}),
     ("● moderada", {"color": AMBER, "bold": True}), ("  →  ", {}),
     ("nenhum com preocupação baixa.", {"bold": True, **HL})],
    [("Itens: ", {"bold": True, "color": NAVY}),
     ("1\u00a0marco amostral · 2\u00a0amostragem · 3\u00a0tamanho · 4\u00a0sujeitos/cenário · 5\u00a0cobertura · "
      "6\u00a0validade · 7\u00a0padronização · 8\u00a0análise · 9\u00a0taxa de resposta", {"color": GRAY})],
], size=14, color=INK, space_after=2)
deck.notes(s, NOTAS["passos45"], dur=29)

# =====================================================================
# 9 — PASSO 6: METANÁLISE DE PREVALÊNCIA
# =====================================================================
s = deck.content_slide("METODOLOGIA", "Passo 6 · Metanálise de prevalência explicada: de 6–7 proporções a uma estimativa combinada",
                       track=6)
b = Build(s)
pipe = [
    ("Proporção de cada estudo", "p = eventos ÷ n", [
        [("Ex.: ", {}), ("33/81 = 40,7%", {"bold": True}), (".", {})],
        [("IC95% de cada estudo pelo ", {}), ("método de Wilson", {"bold": True}), (".", {})],
    ]),
    ("Transformação logito", "ln[ p ÷ (1 − p) ]", [
        [("Leva a proporção (0 a 1) para a escala ", {}), ("−∞ a +∞", {"bold": True}), (".", {})],
        "Aproxima da normal e mantém estimativa e IC entre 0 e 100%.",
        "Sem 0% ou 100% → sem correção de continuidade.",
    ]),
    ("Modelo de efeitos aleatórios", "τ² por Paule-Mandel", [
        [("A prevalência verdadeira ", {}), ("varia entre estudos", {"bold": True}), (".", {})],
        [("τ² = variância entre estudos; ", {"bold": True}), ("peso = 1 ÷ (variância + τ²).", {})],
        "Subestima τ² menos que DerSimonian-Laird com poucos estudos.",
    ]),
    ("Ajuste de Hartung-Knapp", "IC pela distribuição t", [
        [("Usa t com ", {}), ("k − 1 graus de liberdade", {"bold": True}), (".", {})],
        "IC mais honesto (em geral mais largo) com poucos estudos e alta heterogeneidade (IntHout; Ioannidis; Borm, 2014).",
    ]),
    ("Voltar para % e interpretar", "I² + predição", [
        "Retrotransformação para porcentagem.",
        [("I² = % da variação ", {}), ("devida à heterogeneidade", {"bold": True}), (".", {})],
        [("Intervalo de predição: ", {}), ("faixa esperada para um novo estudo", {"bold": True, **HL}),
         ("; instável com k < 10.", {})],
    ]),
]
PC_Y, PC_H = Y0, 4.65
pc = cols(len(pipe))
for i, ((x, w), (t, formula, body)) in enumerate(zip(pc, pipe), start=1):
    with b.step():
        if i > 1:
            line(s, x - GAP + 0.03, PC_Y + 2.25, x - 0.03, PC_Y + 2.25, color=NAVY, width=2.5, arrow=True)
        rect(s, x, PC_Y, w, PC_H, fill=LIGHT)
        circle(s, x + PAD + 0.3, PC_Y + PAD + 0.3, 0.6, fill=RED, text=str(i), size=20)
        tb(s, x + PAD + 0.75, PC_Y + PAD - 0.05, w - 2 * PAD - 0.75, 0.7, [t], size=16, color=NAVY, bold=True,
           space_after=0, anchor=MSO_ANCHOR.MIDDLE)
        rect(s, x + 0.25, PC_Y + 1.2, w - 0.5, 0.6, fill=WHITE, line=rgb("C9CFDA"))
        tb(s, x + 0.35, PC_Y + 1.2, w - 0.7, 0.6, [formula], size=16, color=RED, bold=True, align=PP_ALIGN.CENTER,
           space_after=0, anchor=MSO_ANCHOR.MIDDLE)
        tb(s, x + 0.25, PC_Y + 2.0, w - 0.5, PC_H - 2.0 - PAD, body, size=16, color=INK, bullet=True, bullet_color=NAVY,
           space_after=4)
RB_Y = PC_Y + PC_H + 0.22
BN9 = 1.0
CH_Y = RB_Y + 0.45
CH_H = YBT - BN9 - GAP - CH_Y
with b.step():
    tb(s, L, RB_Y, R - L, 0.4, [[("Verificando a robustez ", {"bold": True, "color": NAVY}),
                                ("(sensibilidade, influência e subgrupo)", {"color": GRAY})]], size=17, space_after=0)
    chips = [("Freeman-Tukey", "duplo-arcoseno (DerSimonian-Laird)"), ("GLMM logístico", "intercepto aleatório por estudo"),
             ("Leave-one-out", "retira 1 estudo por vez"), ("Gráfico de Baujat", "quem puxa a heterogeneidade"),
             ("Subgrupo por país", "exploratório; teste Q"), ("Sensibilidade extra", "sem resumo; definições específicas")]
    for (x, w), (t, d) in zip(cols(len(chips), gap=0.2), chips):
        rect(s, x, CH_Y, w, CH_H, fill=TEAL_TINT)
        tb(s, x + 0.25, CH_Y + 0.2, w - 0.5, 0.35, [t], size=16, color=TEAL, bold=True, space_after=0)
        tb(s, x + 0.25, CH_Y + 0.58, w - 0.5, CH_H - 0.78, [d], size=14, color=INK, space_after=0)
with b.step():
    rect(s, L, YBT - BN9, R - L, BN9, fill=GOLD_TINT)
    icon(s, "question", L + PAD, YBT - BN9 + (BN9 - 0.6) / 2, 0.6, color="navy")
    tb(s, L + PAD + 0.85, YBT - BN9 + 0.15, R - L - 2 * PAD - 0.85, BN9 - 0.3, [
        [("Sem teste de Egger nem funil por erro-padrão: ", {"bold": True, "color": NAVY}),
         ("em proporções o erro-padrão depende da própria proporção (assimetria espúria) e os testes exigem ≥ 10 estudos; "
          "viés de relato apreciado qualitativamente. ", {}),
         ("Sem metarregressão ", {"bold": True}), ("(poucos estudos por covariável). ", {}),
         ("RR ", {"bold": True}), ("na escala log (Wald).", {})]],
       size=15, color=INK, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
b.apply()
deck.notes(s, NOTAS["passo6"], dur=50)

# =====================================================================
# 10 — PASSO 7: GRADE
# =====================================================================
s = deck.content_slide("METODOLOGIA", "Passo 7 · Certeza da evidência: GRADE adaptado a desfechos de prevalência", track=7)
dom = [
    ("balance", "Risco de viés", "Do JBI: amostragem não probabilística, taxa de resposta não relatada, autorrelato; nos "
                                 "objetivos, sem ajuste para confundidores."),
    ("spiral", "Inconsistência", "I² acima de 90%, prevalências de 19% a 56% e intervalo de predição amplo → muito grave "
                                 "na prevalência."),
    ("compass", "Evidência indireta", "Não rebaixada na prevalência (o sintoma é o próprio desfecho); rebaixada nos "
                                      "desfechos objetivos (coexposições, desfechos substitutos)."),
    ("target", "Imprecisão", "IC95% amplo ou ausente no estudo original (ex.: 21,9\u00a0a\u00a056,5); poucos eventos nos desfechos "
                             "objetivos."),
    ("search", "Viés de publicação", "Busca ampla, mas poucos estudos, em geral pequenos, e 6 não recuperados → viés não "
                                     "excluível; sem base para rebaixar."),
]
DM_H = 3.45
for (x, w), (ic, t, body) in zip(cols(len(dom)), dom):
    card(s, x, Y0, w, DM_H, title=t, body=[body], icon_name=ic, fill=LIGHT, body_size=16, title_size=17, pad=0.3,
         badge_d=0.75, body_gap=0.2)
GB_Y = Y0 + DM_H + GAP
(gx, gw), (dx, dw) = (L, 10.6), (L + 10.6 + GAP, R - L - 10.6 - GAP)
rect(s, gx, GB_Y, gw, YBT - GB_Y, fill=NAVY_TINT)
tb(s, gx + PAD, GB_Y + PAD - 0.05, gw - 2 * PAD, YBT - GB_Y - 2 * PAD + 0.05, [
    {"runs": [("Como a certeza foi graduada", {"bold": True, "color": NAVY, "size": 18})], "space_after": 6, "bullet": False},
    [("Ponto de partida: certeza BAIXA ", {"bold": True}), ("para evidência observacional (decisão dos autores; parte da "
                                                            "literatura sugere iniciar em alta para prevalência).", {})],
    [("Regra: ", {"bold": True}), ("um domínio grave já leva a MUITO BAIXA", {"bold": True, **HL}),
     ("; a certeza final não muda com o ponto de partida alternativo.", {})],
    [("Sem dupla contagem: ", {"bold": True}), ("intervalo de predição em inconsistência; IC95% em imprecisão.", {})],
    [("Desfechos de estudo único: ", {"bold": True}), ("inconsistência não aplicável; viés de publicação não avaliável.", {})],
    {"runs": [("●●●● alta   ●●●○ moderada   ●●○○ baixa   ●○○○ muito baixa", {"color": NAVY, "bold": True})],
     "space_before": 4, "bullet": False},
], size=16, color=INK, bullet=True, bullet_color=NAVY, space_after=12)
rect(s, dx, GB_Y, dw, YBT - GB_Y, fill=GOLD_TINT)
tb(s, dx + PAD, GB_Y + PAD - 0.05, dw - 2 * PAD, YBT - GB_Y - 2 * PAD + 0.05, [  # mesma receita do painel da esquerda
    {"runs": [("Decisões posteriores ao registro", {"bold": True, "color": NAVY, "size": 18})], "space_after": 6,
     "bullet": False},
    "Ocular principal; respiratório exploratório (definição variável);",
    "Modelo principal: logito, efeitos aleatórios e Hartung-Knapp;",
    "1 publicação por desfecho no cluster com sobreposição; análises por país e de influência exploratórias;",
    "Resumos de congresso incluídos (preocupação alta);",
    "Na análise: regra do sintoma-índice e sensibilidade por definição, independentes dos resultados.",
], size=16, color=INK, bullet=True, bullet_color=GOLD, space_after=12)
deck.notes(s, NOTAS["passo7"], dur=30)

# =====================================================================
# 11 — RESULTADOS: SELEÇÃO E CARACTERÍSTICAS
# =====================================================================
s = deck.content_slide("RESULTADOS", "Seleção (PRISMA 2020) e características dos 22 relatórios incluídos")
b = Build(s)
MX, MW = 2.25, 5.2
SX, SW = MX + MW + 0.4, 10.55 - (MX + MW + 0.4)
heights = [1.3, 1.0, 1.0, 1.0, 1.05, 1.4]
gapv = 0.28
ys = [Y0]
for h in heights[:-1]:
    ys.append(ys[-1] + h + gapv)
prisma = [
    ([[("Registros identificados (n = 16.757)", {"bold": True})], "Bases: 16.707 · Literatura cinzenta: 50"],
     [[("Busca por citação", {"bold": True})], "443 referências →", "4\u00a0relatórios buscados", "na íntegra"], GOLD_TINT),
    ([["Importados: 16.749 (8 não exportados)"], [("Duplicatas removidas: 5.839", {"bold": True})]], None, None),
    ([[("Triados (título e resumo): 10.910", {"bold": True})], "revisor único; IA como apoio"],
     [[("Excluídos na triagem", {"bold": True})], "n = 10.882"], LIGHT),
    ([[("Buscados na íntegra: 32", {"bold": True})], "28 da triagem + 4 por citação"],
     [[("Não recuperados", {"bold": True})], "n = 6"], LIGHT),
    ([[("Avaliados para elegibilidade: 26", {"bold": True})]],
     [[("Excluídos (n = 4)", {"bold": True})], "1 resumo; 3 população ou contexto"], LIGHT),
    ([[("Relatórios incluídos (n = 22)", {"bold": True, "size": 17, "color": GREEN})],
      "Metanálise: 6 (ocular) e 7 (respiratório)", "Narrativa + GRADE: desfechos objetivos"], None, None),
]
for i, ((main, side, side_fill), y, h) in enumerate(zip(prisma, ys, heights)):
    last = i == len(prisma) - 1
    with b.step():
        if i > 0:
            line(s, MX + MW / 2, ys[i - 1] + heights[i - 1], MX + MW / 2, y - 0.02, color=NAVY, width=2, arrow=True)
        rect(s, MX, y, MW, h, fill=GREEN_TINT if last else LIGHT, radius=0.08)
        tb(s, MX + 0.3, y + 0.12, MW - 0.6, h - 0.24, main, size=15, color=INK, space_after=2, anchor=MSO_ANCHOR.MIDDLE)
        if side:
            rect(s, SX, y, SW, h, fill=side_fill, radius=0.08)
            tb(s, SX + 0.25, y + 0.12, SW - 0.5, h - 0.24, side, size=14, color=INK, space_after=0,
               anchor=MSO_ANCHOR.MIDDLE)
            if i > 0:  # a busca por citação fica sem seta, como na Figura 1: os 4 relatórios entram em "Buscados na íntegra"
                line(s, MX + MW, y + h / 2, SX - 0.02, y + h / 2, color=NAVY, width=2, arrow=True)
for lab, a, z in [("Identificação", 0, 1), ("Triagem", 2, 3), ("Elegibilidade", 4, 4), ("Incluídos", 5, 5)]:
    cy = (ys[a] + ys[z] + heights[z]) / 2
    tb(s, MX - 0.5 - 1.1, cy - 0.2, 2.2, 0.4, [lab], size=15, color=NAVY, bold=True, align=PP_ALIGN.CENTER,
       space_after=0, rotation=270, anchor=MSO_ANCHOR.MIDDLE)
tb(s, MX, ys[-1] + heights[-1] + 0.1, 10.55 - MX, 0.35,
   ["Fluxograma PRISMA 2020 (Figura 1 do manuscrito); não recuperados e excluídos no Anexo C."], size=14, color=GRAY,
   space_after=0)
SX2 = 10.85
tiles = cols(2, SX2, R)
TH = 1.95
with b.step():
    stat(s, tiles[0][0], Y0, tiles[0][1], "22", "relatórios de estudos observacionais", h=TH, fill=LIGHT,
         num_size=44, lab_size=14)
    stat(s, tiles[1][0], Y0, tiles[1][1], "9", "países: Turquia, Malásia, Brasil, Paquistão, China, México, EUA, Sudão e "
                                               "Tailândia", h=TH, fill=LIGHT, num_size=44, lab_size=14)
    stat(s, tiles[0][0], Y0 + TH + GAP, tiles[0][1], "19 + 3", "transversais + coortes prospectivas", h=TH, fill=LIGHT,
         num_size=40, lab_size=14)
    stat(s, tiles[1][0], Y0 + TH + GAP, tiles[1][1], "6 | 7", "amostras independentes: ocular\u00a0(n\u00a0=\u00a0756) | "
                                                               "respiratória\u00a0(n\u00a0=\u00a01.428)", h=TH, fill=RED_TINT, num_size=40,
         lab_size=14, num_color=RED)
RK_Y = Y0 + 2 * TH + 2 * GAP
with b.step():
    card(s, SX2, RK_Y, R - SX2, ys[-1] + heights[-1] - RK_Y, title="Risco de viés (JBI): resumo", icon_name="balance", fill=LIGHT,
         body_size=15, bullet=True, body_space_after=6, badge_d=0.7, title_size=20, body=[
             [("Prevalência: ", {"bold": True}), ("preocupação moderada a alta (amostragem não probabilística, taxa de "
                                                 "resposta não informada, autorrelato); só 1 estudo com amostragem aleatória.", {})],
             [("Resumo de congresso: ", {"bold": True}), ("alta preocupação por relato incompleto.", {})],
             [("Comparativos e objetivos: ", {"bold": True}),
              ("preocupação moderada (exposição pela ocupação, sem ajuste para confundidores).", {})],
             [("Nenhum estudo com preocupação baixa ", {"bold": True, "color": RED}),
              ("→ análise restrita a baixo risco não foi factível.", {})],
         ])
b.apply()
deck.notes(s, NOTAS["selecao"], dur=18)

# =====================================================================
# 12 — RESULTADOS: SINTOMA OCULAR
# =====================================================================
s = deck.content_slide("RESULTADOS", "Desfecho principal · Prevalência combinada de sintoma ocular (irritação ou lacrimejamento)")
b = Build(s)
FW = 12.3
with b.step():
    fp = pic(s, FIG / "fig2_forest_ocular_slide.png", L, Y0, w=FW, name="Figura 2 forest plot ocular")
    fb = Y0 + fp.height / 914400
    tb(s, L, fb + 0.08, FW, 0.5, [[("Figura 2. ", {"bold": True}),
                                   ("Logito, Paule-Mandel e Hartung-Knapp. Quadrado = prevalência do estudo (tamanho ∝ peso); "
                                    "linha preta = IC95% de Wilson; losango = estimativa combinada; linha vermelha = intervalo "
                                    "de predição (IP).", {})]], size=14, color=GRAY, space_after=0)
SRX = L + FW + GAP
with b.step():
    rect(s, SRX, Y0, R - SRX, 3.55, fill=RED_TINT)
    tb(s, SRX + PAD, Y0 + 0.22, R - SRX - 2 * PAD, 1.25, ["37,6%"], size=72, color=RED, bold=True, space_after=0)
    tb(s, SRX + PAD, Y0 + 1.47, R - SRX - 2 * PAD, 0.4, ["prevalência combinada de sintoma ocular"], size=16, color=GRAY,
       space_after=0)
    tb(s, SRX + PAD, Y0 + 2.0, R - SRX - 2 * PAD, 1.25, [
        [("IC95% ", {"bold": True}), ("21,9–56,5", {})],
        [("Intervalo de predição ", {"bold": True}), ("7–83%", {})],
        [("I² = 93% · k = 6 · n = 756", {"bold": True})],
    ], size=17, color=INK, space_after=3)
CR_Y = Y0 + 3.55 + GAP
LR_Y = 9.0
with b.step():
    card(s, SRX, CR_Y, R - SRX, YB - CR_Y, title="Características do agrupamento", fill=LIGHT, body_size=18, bullet=True,
         title_size=19, body_space_after=16, body=[
             "6 inquéritos transversais: Turquia (3), Malásia (2) e Brasil (1).",
             "Preocupação com viés moderada ou alta em todos.",
             "Definições: lacrimejamento, irritação ocular ou escala do sistema ocular.",
             [("O maior inquérito (n = 672) ", {"bold": True}), ("não entrou: sem numerador e denominador ocular "
                                                                "extraíveis.", {})],
         ])
    rect(s, L, LR_Y, FW, YB - LR_Y, fill=NAVY_TINT)
    tb(s, L + PAD, LR_Y + 0.15, FW - 2 * PAD, YB - LR_Y - 0.3, [
        [("Como ler: ", {"bold": True, "color": NAVY}),
         ("cerca de 4 em cada 10 profissionais relataram irritação ou lacrimejamento ocular; os estudos variam de 19% "
          "(Malásia) a 56% (Turquia), e ", {}),
         ("um novo estudo poderia encontrar qualquer valor entre 7% e 83%", {"bold": True, **HL}), (". ", {}),
         ("É a proporção que relatou o sintoma, não uma prevalência com recordatório homogêneo.", {"color": GRAY})]],
       size=16, color=INK, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
b.apply()
deck.notes(s, NOTAS["ocular"], dur=50)

# =====================================================================
# 13 — RESULTADOS: RESPIRATÓRIO + ROBUSTEZ
# =====================================================================
s = deck.content_slide("RESULTADOS", "Desfecho exploratório · Sintoma respiratório ou de vias aéreas, e robustez das estimativas")
FW3 = 10.2
fp = pic(s, FIG / "fig3_forest_resp_slide.png", L, Y0, w=FW3, name="Figura 3 forest plot respiratório")
fb = Y0 + fp.height / 914400
tb(s, L, fb + 0.08, FW3, 0.5, [[("Figura 3. ", {"bold": True}),
                                ("Sete amostras independentes (n = 1.428). Definições variam: tosse, ardência de garganta, "
                                 "irritação ou qualquer sintoma de vias aéreas superiores, escala por sistema.", {})]], size=14, color=GRAY,
   space_after=0)
LOW_Y = 8.6
rect(s, L, LOW_Y, FW3, YB - LOW_Y, fill=NAVY_TINT)
tb(s, L + PAD, LOW_Y + PAD - 0.05, FW3 - 2 * PAD, YB - LOW_Y - 2 * PAD + 0.05, [
    {"runs": [("Subgrupo por país (sintoma ocular; exploratório)", {"bold": True, "color": NAVY, "size": 17})],
     "space_after": 5},
    [("Turquia 50,5% ", {"bold": True, "color": RED}), ("(k = 3; I² = 57%)  ·  ", {}),
     ("Malásia 19,8% ", {"bold": True, "color": RED}), ("(k = 2; I² = 0%)  ·  ", {}),
     ("Brasil 43,2% ", {"bold": True}), ("(k = 1)", {})],
    [("Teste entre subgrupos p < 0,001, mas: ", {"bold": True}), ("poucos estudos por país e um resumo de congresso na "
                                                                   "Malásia → gera hipótese, não prova moderação causal.", {})],
], size=15, color=INK, space_after=4)
RX13 = L + FW3 + GAP
RW13 = R - RX13
rect(s, RX13, Y0, RW13, 2.35, fill=RED_TINT)
tb(s, RX13 + PAD, Y0 + 0.2, RW13 - 2 * PAD, 0.9, ["41,7%"], size=50, color=RED, bold=True, space_after=0)
tb(s, RX13 + PAD, Y0 + 1.08, RW13 - 2 * PAD, 0.38, ["prevalência combinada de sintoma respiratório"], size=16, color=GRAY,
   space_after=0)
tb(s, RX13 + PAD, Y0 + 1.5, RW13 - 2 * PAD, 0.6, [
    [("IC95% ", {"bold": True}), ("30,4–53,9  ·  ", {}), ("Intervalo de predição ", {"bold": True}), ("15–74%", {})],
    [("I² = 91% · k = 7 · n = 1.428", {"bold": True})],
], size=15, color=INK, space_after=2)
tb(s, RX13, Y0 + 2.6, RW13, 0.4, ["Robustez: estável entre modelos e estudos"], size=16, color=NAVY, bold=True,
   space_after=0)
table(s, RX13, Y0 + 3.05, RW13, [
    ["Análise", "Ocular", "Respiratório"],
    ["Logito + Hartung-Knapp (principal)", "37,6%", "41,7%"],
    ["Freeman-Tukey (DerSimonian-Laird)", "38,1%", "41,7%"],
    ["GLMM logístico (intercepto aleatório)", "37,5%", "42,0%"],
    ["Leave-one-out (faixa)", "34,3–42,1%", "38,9–45,5%"],
    ["Sem o resumo de congresso", "42,1%", "42,4%"],
    ["Só definições específicas", "36,5% (I² 94%)", "35,8% (I² 61%)"],
], col_widths=[RW13 - 3.3, 1.55, 1.75], size=14, row_h=0.44, align_cols={1: PP_ALIGN.CENTER, 2: PP_ALIGN.CENTER},
      bold_rows=(1,))
rect(s, RX13, LOW_Y, RW13, YB - LOW_Y, fill=GOLD_TINT)
tb(s, RX13 + PAD, LOW_Y + PAD - 0.05, RW13 - 2 * PAD, YB - LOW_Y - 2 * PAD + 0.05, [
    {"runs": [("O que a sensibilidade ensina", {"bold": True, "color": NAVY, "size": 17})], "space_after": 5,
     "bullet": False},
    [("Definições específicas: ", {}), ("I² respiratório 91% → 61%", {"bold": True, **HL}),
     (" (a definição explica parte da heterogeneidade).", {})],
    [("Ocular: I² segue alto sem o resumo (89%) ou sem Bieniek (94%): ", {}),
     ("não\u00a0depende de um único estudo.", {"bold": True})],
], size=15, color=INK, bullet=True, bullet_color=GOLD, space_after=4)
deck.notes(s, NOTAS["respiratorio"], dur=25)

# =====================================================================
# 14 — RESULTADOS: DESFECHOS OBJETIVOS E GRADE
# =====================================================================
s = deck.content_slide("RESULTADOS", "Desfechos objetivos e biomarcadores: sinais além do incômodo agudo (1 estudo por desfecho)")
b = Build(s)
obj = [
    ("lungs", "Função pulmonar (espirometria)", "Ibrahim et al., 2025 · Sudão · 92 expostos vs 92 não expostos pareados", [
        [("VEF1 ", {}), ("2,78 vs 3,14 L", {"bold": True}), (" · CVF ", {}), ("3,02 vs 3,45 L", {"bold": True}),
         (" · PFE ", {}), ("327,5 vs 483,5 L/min", {"bold": True})],
        "p = 0,001; gradiente: mais tempo em centro cirúrgico → valores menores.",
        [("Cautela: ", {"bold": True, "color": RED}), ("VEF1/CVF ≈ 91% nos dois grupos; PFE depende do esforço.", {})],
    ]),
    ("vial", "Biomarcadores urinários", "Canicoba, 2025 · Brasil · 52 vs 49 (metabólitos); 52 vs 52 (oxidativo)", [
        [("Ác. t,t-mucônico (benzeno): ", {}), ("202,9 vs 46,1 µg/L", {"bold": True})],
        [("Ác. metil-hipúrico (xileno): ", {}), ("468,2 vs 184,4 µg/L", {"bold": True})],
        [("Malondialdeído: ", {}), ("9,33 vs 3,22 nmol/mg", {"bold": True}), ("; todos p < 0,001", {})],
        [("Cautela: ", {"bold": True, "color": RED}), ("sem IC95%; t,t-mucônico inespecífico (dieta, tabagismo).", {})],
    ]),
    ("biotech", "Mucosa nasal (biópsia)", "Navarro et al., 2016 · México · coorte de 4 anos · 23 vs 20 residentes", [
        [("Metaplasia ou hiperplasia: ", {}), ("70% (16/23) vs 5% (1/20)", {"bold": True})],
        [("RR 13,9 (IC95% 2,0–95,8)", {"bold": True, "color": RED}), (": 1 evento no grupo não exposto → IC amplo", {})],
        [("Cautela: ", {"bold": True, "color": RED}), ("resposta inespecífica a irritantes; exposição por proxy.", {})],
    ]),
    ("virus", "HPV-DNA na mucosa nasal", "Hu et al., 2021 · China · 469 com eletrocirurgia vs 231 sem", [
        [("8,96% vs 1,73%", {"bold": True}), (" (42/469 com eletrocirurgia vs 4/231 sem)", {})],
        [("RR 5,2 (IC95% 1,9–14,2)", {"bold": True, "color": RED}), (" · maior com mais tempo de eletrocirurgia", {})],
        [("Cautela: ", {"bold": True, "color": RED}), ("DNA ≠ infecção ou doença; achado da N95 (0/196) sem ajuste.", {})],
    ]),
]
OH = 3.0
oc = cols(2)
for i, (ic, t, src, body) in enumerate(obj):
    x, w = oc[i % 2]
    y = Y0 + (i // 2) * (OH + GAP)
    with b.step():
        rect(s, x, y, w, OH, fill=LIGHT)
        icon_badge(s, ic, x + PAD + 0.4, y + PAD + 0.4, d=0.8, fill=NAVY)
        tb(s, x + PAD + 1.05, y + PAD - 0.08, w - 2 * PAD - 1.05, 0.45, [t], size=18, color=NAVY, bold=True, space_after=0)
        tb(s, x + PAD + 1.05, y + PAD + 0.4, w - 2 * PAD - 1.05, 0.4, [src], size=14, color=GRAY, space_after=0)
        tb(s, x + PAD, y + 1.35, w - 2 * PAD, OH - 1.35 - PAD, body, size=17, color=INK, bullet=True, bullet_color=NAVY,
           space_after=5)
GY = Y0 + 2 * OH + 2 * GAP
with b.step():
    rect(s, L, GY, R - L, YB - GY, fill=NAVY)
    for (x, w), (t, body) in zip(cols(3, L + PAD, R - PAD, gap=0.45), [
        ("●○○○  Certeza MUITO BAIXA", "em todos os desfechos (GRADE); comparações não combinadas (desenhos e "
                                     "desfechos heterogêneos)."),
        ("0 estudos elegíveis: câncer ou DPOC", ["vazio de evidência:", "ausência de estudos ≠ ausência de risco."]),
        ("Direção consistente, mas…", "coexposições (gases anestésicos, radiação), 1 estudo por desfecho e IC amplos: "
                                     "marcadores, não doença crônica atribuível."),
    ]):
        tb(s, x, GY + PAD, w, 0.45, [t], size=20, color=GOLD, bold=True, space_after=0)
        tb(s, x, GY + PAD + 0.55, w, YB - GY - 2 * PAD - 0.55, body if isinstance(body, list) else [body], size=16,
           color=WHITE, space_after=0)
b.apply()
deck.notes(s, NOTAS["objetivos_bio"], dur=40)

# =====================================================================
# 15 — DISCUSSÃO: INTERPRETAÇÃO
# =====================================================================
s = deck.content_slide("DISCUSSÃO", "O que os achados significam e como interpretá-los com cautela")
dcols = [
    ("chart", "Carga de sintomas", [
        [("Sintomas frequentes: ", {"bold": True}), ("ocular 37,6%, respiratório 41,7%, qualquer sintoma entre 55,6% e "
                                                    "73,2%.", {})],
        [("Coerente com a literatura prévia", {"bold": True}),
         (", sem síntese quantitativa (Mowbray et al., 2013; Dixon; Dasgupta; Vasdev, 2023).", {})],
        [("Contribuição: ", {"bold": True}), ("estimativa combinada com intervalo de predição, subgrupo por país e GRADE, "
                                              "para uma literatura antes descritiva.", {})],
    ]),
    ("spiral", "Heterogeneidade esperada", [
        [("I² > 90% é típico ", {"bold": True}), ("em prevalência → ler pelo intervalo de predição.", {})],
        [("Fontes plausíveis: ", {"bold": True}), ("definição do sintoma e recordatório, composição profissional, tempo de "
                                                  "exposição, exaustão e EPI.", {})],
        [("País reduziu o I² ", {"bold": True}), ("intragrupo (Turquia 57%, Malásia 0%), mas com 2–3 estudos por estrato "
                                                 "é hipótese.", {})],
    ]),
    ("biotech", "Sinais além do incômodo agudo", [
        [("A favor da causalidade: ", {"bold": True}), ("gradiente com o tempo de exposição, temporalidade (coorte) e "
                                                       "plausibilidade biológica.", {})],
        [("Contra: ", {"bold": True}), ("um estudo por desfecho, intervalos amplos, coexposições (gases anestésicos, "
                                       "radiação).", {})],
        [("Metabólitos: ", {"bold": True}), ("exposição recente · ", {}), ("metaplasia: ", {"bold": True}),
         ("resposta inespecífica · ", {}), ("DNA\u00a0de\u00a0HPV: ", {"bold": True}), ("detecção, não infecção.", {})],
    ]),
]
DB_H = 2.1
DC_H = YB - DB_H - GAP - Y0
chaves = [("37,6% | 41,7%", "prevalência ocular | respiratória"),
          ("IP 7–83%", "faixa esperada para um novo estudo (ocular)"),
          ("RR 13,9 | RR 5,2", "metaplasia nasal | DNA de HPV (1 estudo cada)")]
KC_H = 1.15
for (x, w), (ic, t, body), (num, lab) in zip(cols(3), dcols, chaves):
    card(s, x, Y0, w, DC_H, title=t, body=body, icon_name=ic, fill=LIGHT, body_size=17, bullet=True, title_size=19,
         body_space_after=10)
    ky = Y0 + DC_H - PAD - KC_H
    rect(s, x + PAD, ky, w - 2 * PAD, KC_H, fill=WHITE, line=rgb("C9CFDA"), name="Faixa zebrada chave")
    tb(s, x + PAD, ky + 0.12, w - 2 * PAD, 0.55, [num], size=28, color=RED, bold=True, align=PP_ALIGN.CENTER,
       space_after=0)
    tb(s, x + PAD + 0.15, ky + 0.68, w - 2 * PAD - 0.3, 0.35, [lab], size=14, color=GRAY, align=PP_ALIGN.CENTER,
       space_after=0)
rect(s, L, YB - DB_H, R - L, DB_H, fill=NAVY)
icon(s, "question", L + PAD + 0.05, YB - DB_H + (DB_H - 0.85) / 2, 0.85, color="gold")
tb(s, L + PAD + 1.2, YB - DB_H + PAD, R - L - 2 * PAD - 1.2, DB_H - 2 * PAD, [
    [("O achado talvez mais relevante é o que não foi encontrado. ", {"bold": True, "color": GOLD}),
     ("Nenhum estudo elegível estimou câncer ou DPOC atribuíveis à fumaça. Relatos de caso de papilomatose laríngea e "
      "carcinoma orofaríngeo por HPV em cirurgiões (Hallmo; Naess, 1991; Rioux et al., 2013) reforçam a plausibilidade, mas "
      "não estimam risco. A controvérsia (Hurst; Stewart, 2024) se resolve com estudos longitudinais ainda por realizar.", {})]],
   size=18, color=WHITE, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
deck.notes(s, NOTAS["discussao"], dur=30)

# =====================================================================
# 16 — DISCUSSÃO: PONTOS FORTES E LIMITAÇÕES
# =====================================================================
s = deck.content_slide("DISCUSSÃO", "Pontos fortes e limitações")
LB_H = 1.6
LC_H = YB - LB_H - GAP - Y0
card(s, L, Y0, 7.4, LC_H, title="Pontos fortes", icon_name="thumbsup", badge_fill=GREEN, fill=GREEN_TINT, body_size=18,
     bullet=True, body_space_after=18, body=[
         [("Busca abrangente: ", {"bold": True}), ("7 bases, literatura cinzenta e citação, sem filtro de idioma na busca.", {})],
         [("Protocolo registrado ", {"bold": True}), ("(PROSPERO) e relato PRISMA\u00a02020 (27\u00a0itens).", {})],
         [("Risco de viés padronizado ", {"bold": True}), ("com ferramentas JBI.", {})],
         [("Síntese robusta: ", {"bold": True}), ("intervalo de predição, 3 modelos concordantes, leave-one-out, Baujat.", {})],
         [("Certeza por desfecho ", {"bold": True}), ("(GRADE), justificada por domínio.", {})],
         [("Sobreposição amostral e uso de IA ", {"bold": True}), ("declarados.", {})],
         [("Reprodutível: ", {"bold": True}), ("código, planilhas e figuras no OSF.", {})],
     ])
card(s, L + 7.4 + GAP, Y0, R - L - 7.4 - GAP, LC_H, title="Limitações (declaradas no manuscrito)", icon_name="warning",
     badge_fill=RED, fill=RED_TINT, body_size=18, bullet=True, body_space_after=14, body=[
         [("Transversais, exposição por proxy e autorrelato; ", {"bold": True}),
          ("viés de atribuição (o\u00a0respondente sabe que o tema é fumaça).", {})],
         [("Sem grupo não exposto nos agrupamentos ", {"bold": True}), ("→ não se estima o excesso atribuível.", {})],
         [("Efeito do trabalhador sadio: ", {"bold": True}), ("quem adoece sai do centro cirúrgico → subestima.", {})],
         [("Heterogeneidade alta; ", {"bold": True}), ("subgrupo exploratório; maior inquérito fora do ocular.", {})],
         [("Sobreposição amostral ", {"bold": True}), ("tratada; 1 resumo de congresso na síntese.", {})],
         [("Revisor único ", {"bold": True}), ("na triagem, extração, JBI e GRADE; 6 relatórios não recuperados.", {})],
         [("Instrumentos sem validação relatada; ", {"bold": True}), ("recordatório e resposta pouco informados.", {})],
         [("Elegibilidade só em português, inglês e espanhol; ", {"bold": True}),
          ("periódicos pouco indexados.", {})],
         [("A metanálise estima prevalência em expostos, não risco causal.", {"bold": True, "color": RED})],
     ])
rect(s, L, YB - LB_H, R - L, LB_H, fill=NAVY)
icon(s, "balance", L + PAD + 0.05, YB - LB_H + (LB_H - 0.7) / 2, 0.7, color="gold")
tb(s, L + PAD + 1.05, YB - LB_H + 0.2, R - L - 2 * PAD - 1.05, LB_H - 0.4, [
    [("Limitações declaradas e testadas por sensibilidade quando possível: ", {"bold": True, "color": GOLD}),
     ("não invalidam a síntese; delimitam o que a evidência permite afirmar.", {})]],
   size=18, color=WHITE, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
deck.notes(s, NOTAS["limitacoes"], dur=25)

# =====================================================================
# 17 — CONCLUSÃO
# =====================================================================
s = deck.content_slide("CONCLUSÃO", "Síntese da mensagem da revisão")
b = Build(s)
CW = 7.6
FB_H = 1.5
TOP_B = YB - FB_H - GAP
cr_x = L + CW + GAP + 0.2
cr_w = R - cr_x
with b.step():
    ph = pic(s, IMG / "exaustao_n95.png", L, Y0, w=CW, name="Foto exaustão e N95")
    py_ = Y0 + ph.height / 914400
    tb(s, L, py_ + 0.08, CW, 0.35, ["Imagem ilustrativa (gerada por IA): exaustão local na fonte e respirador N95."],
       size=14, color=GRAY, space_after=0)
    PR_Y = py_ + 0.55
    rect(s, L, PR_Y, CW, TOP_B - PR_Y, fill=NAVY_TINT)
    # título e corpo com os mesmos deslocamentos do card "Implicação", ao lado
    tb(s, L + PAD, PR_Y + PAD - 0.05, CW - 2 * PAD, 0.45, ["Proteção recomendada (NIOSH, 1996)"], size=19, color=NAVY,
       bold=True, space_after=0)
    tb(s, L + PAD, PR_Y + PAD + 0.45, CW - 2 * PAD, TOP_B - PR_Y - 2 * PAD - 0.45, [
        [("Evacuação local na fonte ", {"bold": True}), ("(medida principal);", {})],
        [("Respiradores N95/PFF2 ", {"bold": True}), ("(não substituem a exaustão);", {})],
        [("Educação da equipe. ", {"bold": True}), ("Efetividade das medidas não avaliada.", {})],
    ], size=17, color=INK, bullet=True, bullet_color=NAVY, space_after=3)
concl = [
    ("check", "O que se sabe", GREEN, GREEN_TINT, GREEN,
     [[("Sintomas oculares (37,6%; IP 7–83%) e respiratórios (41,7%; IP 15–74%) são ", {}), ("frequentes", {"bold": True}),
       (", com ampla variação entre contextos; desfechos objetivos sinalizam alterações além do incômodo agudo.", {})]]),
    ("question", "O que não se sabe", AMBER, GOLD_TINT, DARK_GOLD,
     [[("Entre os estudos elegíveis, ", {}), ("não há evidência direta de câncer ou DPOC atribuíveis à fumaça", {"bold": True}),
       ("; certeza muito baixa; a exposição múltipla limita a atribuição causal.", {})]]),
    ("shield", "Implicação", NAVY, NAVY_TINT, NAVY,
     [[("A proteção da equipe ", {}), ("parece justificada", {"bold": True}),
       (" pela carga sintomática e pelo princípio da precaução; o risco de longo prazo depende de estudos longitudinais.", {})]]),
]
h12 = (PR_Y - Y0 - 2 * GAP) / 2           # cards 1 e 2 acima; o 3º começa junto da caixa de proteção
card_ys = [(Y0, h12), (Y0 + h12 + GAP, h12), (PR_Y, TOP_B - PR_Y)]
for i, (ic, t, badge, tint, tcol, body) in enumerate(concl):
    y, card_h = card_ys[i]
    with b.step():
        rect(s, cr_x, y, cr_w, card_h, fill=tint)
        if i < 2:  # cards de cima: conteúdo centrado na vertical
            icon_badge(s, ic, cr_x + PAD + 0.4, y + card_h / 2, d=0.8, fill=badge)
            tb(s, cr_x + PAD + 1.05, y + PAD - 0.1, cr_w - 2 * PAD - 1.05, card_h - 2 * PAD + 0.2,
               [{"runs": [(t, {"size": 19, "color": tcol, "bold": True})], "space_after": 6}, *body], size=17, color=INK,
               space_after=0, line_spacing=1.02, anchor=MSO_ANCHOR.MIDDLE)
        else:
            icon_badge(s, ic, cr_x + PAD + 0.4, y + PAD + 0.4, d=0.8, fill=badge)
            tb(s, cr_x + PAD + 1.05, y + PAD - 0.05, cr_w - 2 * PAD - 1.05, 0.45, [t], size=19, color=tcol, bold=True,
               space_after=0)
            tb(s, cr_x + PAD + 1.05, y + PAD + 0.45, cr_w - 2 * PAD - 1.05, card_h - 2 * PAD - 0.45, body, size=17,
               color=INK, space_after=0, line_spacing=1.02)
with b.step():
    rect(s, L, YB - FB_H, R - L, FB_H, fill=NAVY)
    tb(s, L + 0.45, YB - FB_H + 0.2, R - L - 0.9, FB_H - 0.4, [[("Mensagem final: ", {"bold": True, "color": GOLD}),
                                                              ("na equipe exposta, sintomas oculares e respiratórios são "
                                                               "frequentes e estudos isolados sugerem alterações além do "
                                                               "incômodo agudo; proteger a equipe hoje é prudente, e medir o "
                                                               "risco crônico é tarefa dos próximos estudos.", {})]],
       size=18, color=WHITE, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
b.apply()
deck.notes(s, NOTAS["conclusao"], dur=25)

# =====================================================================
# 18 — PERSPECTIVAS FUTURAS
# =====================================================================
s = deck.content_slide("PERSPECTIVAS FUTURAS", "Agenda de pesquisa e próximos passos deste trabalho")
PW_L = 11.0
rect(s, L, Y0, PW_L, YB - Y0, fill=LIGHT)
tb(s, L + PAD, Y0 + PAD - 0.05, PW_L - 2 * PAD, 0.5, ["Para o campo: o que falta para responder ao risco crônico"],
   size=22, color=NAVY, bold=True, space_after=0)
agenda = [
    ("hourglass", "Estudos longitudinais", [[("Coortes com ", {}), ("aferição objetiva da exposição", {"bold": True}),
                                            (" (PM2,5, COV, tempo de dispositivo) e controle de coexposições e tabagismo.", {})]]),
    ("list", "Definições padronizadas", [[("Sintoma-índice, recordatório e ", {}), ("instrumentos validados", {"bold": True}),
                                          (", com taxa de resposta relatada.", {})]]),
    ("lungs", "Desfechos crônicos", [[("Incidência de ", {}), ("câncer e DPOC", {"bold": True}),
                                    ("; seguimento de mucosa nasal, HPV e função pulmonar.", {})]]),
    ("fan", "Efetividade das medidas", [[("Intervenção com ", {}), ("exaustão local, N95/PFF2 e educação", {"bold": True}),
                                         (", medindo a exposição antes e depois.", {})]]),
]
AG_Y0 = Y0 + 1.05
ITEM_L = 1.12  # altura de um item (título + 2 linhas)
ag_h = (YB - PAD - 0.15 - AG_Y0 - ITEM_L) / (len(agenda) - 1)
for i, (ic, t, body) in enumerate(agenda):
    y = AG_Y0 + i * ag_h
    icon_badge(s, ic, L + PAD + 0.425, y + 0.45, d=0.85, fill=NAVY)
    tb(s, L + PAD + 1.15, y, PW_L - 2 * PAD - 1.15, 0.45, [t], size=19, color=NAVY, bold=True, space_after=0)
    tb(s, L + PAD + 1.15, y + 0.47, PW_L - 2 * PAD - 1.15, ITEM_L - 0.4, body, size=18, color=INK, space_after=0,
       line_spacing=1.05)
PX = L + PW_L + GAP
rect(s, PX, Y0, R - PX, YB - Y0, fill=GOLD_TINT)
tb(s, PX + PAD, Y0 + PAD - 0.05, R - PX - 2 * PAD, 0.5, ["Para este trabalho"], size=22, color=NAVY, bold=True,
   space_after=0)
nxt = [("upload", [("Submissão ", {"bold": True}), ("do manuscrito para publicação em periódico indexado.", {})]),
       ("calendar", [("Atualização da busca ", {"bold": True}), ("e vigilância dos 6 relatórios não recuperados.", {})]),
       ("people", [("Duplicata: ", {"bold": True}), ("triagem e extração com segundo revisor independente.", {})]),
       ("hospital", [("Devolutiva institucional: ", {"bold": True}), ("protocolo de proteção no centro cirúrgico.", {})]),
       ("graduation", [("Formação ", {"bold": True}), ("em síntese de evidências, do protocolo ao GRADE.", {})])]
ITEM_R = 0.66  # altura de um item (2 linhas)
nx_h = (YB - PAD - 0.15 - AG_Y0 - ITEM_R) / (len(nxt) - 1)
for i, (ic, body) in enumerate(nxt):
    y = AG_Y0 + i * nx_h
    icon(s, ic, PX + PAD, y + 0.06, 0.55, color="navy")
    tb(s, PX + PAD + 0.8, y, R - PX - 2 * PAD - 0.8, ITEM_R + 0.1, [body], size=18, color=INK, space_after=0,
       line_spacing=1.05)
deck.notes(s, NOTAS["perspectivas"], dur=15)

# =====================================================================
# 19 — REFERÊNCIAS + QR
# =====================================================================
s = deck.content_slide("REFERÊNCIAS BIBLIOGRÁFICAS", "Principais referências metodológicas e dos estudos incluídos (lista completa no manuscrito)")
REFS = [  # (antes da fonte, fonte em negrito, depois)
    ("AROMATARIS, E.; MUNN, Z. (Ed.). ", "JBI Manual for Evidence Synthesis", ". Adelaide: JBI, 2020."),
    ("BARKER, T. H. et al. Conducting proportional meta-analysis in different types of systematic reviews: a guide for "
     "synthesisers of evidence. ", "BMC Med Res Methodol", ", v. 21, p. 189, 2021."),
    ("BENAIM, E. H.; JASPERS, I. Surgical smoke and its components, effects, and mitigation: a contemporary review. ",
     "Toxicol Sci", ", v. 198, n. 2, p. 157-168, 2024."),
    ("BIENIEK, A. A. et al. Risco ocupacional: sinais e sintomas relacionados à exposição à fumaça cirúrgica. ",
     "Rev SOBECC", ", v. 27, 2022."),
    ("BRASIL. Ministério da Saúde. ", "Diretrizes metodológicas: Sistema GRADE", ". Brasília: Ministério da Saúde, 2014."),
    ("CANICOBA, A. R. B. ", "Impacto da exposição ocupacional à fumaça cirúrgica sobre os marcadores biológicos de "
     "profissionais de saúde da sala operatória", ". Tese (Doutorado). EEUSP, 2025."),
    ("DIXON, K.; DASGUPTA, P.; VASDEV, N. A systematic review of the harmful effects of surgical smoke inhalation on "
     "operating room personnel. ", "Health Sci Rev", ", v. 6, 100077, 2023."),
    ("HU, X. et al. Prevalence of HPV infections in surgical smoke exposed gynecologists. ",
     "Int Arch Occup Environ Health", ", v. 94, n. 1, p. 107-115, 2021."),
    ("HURST, R. D.; STEWART, C. L. Hazards of surgical smoke from electrocautery: a critical review of the data. ",
     "Am J Surg", ", v. 233, p. 29-36, 2024."),
    ("IBRAHIM, J. B. et al. Evaluation of spirometric lung function among healthcare professionals working in operating "
     "theatres: a comparative cross-sectional study. ", "Afr J Thorac Crit Care Med", ", v. 31, n. 2, e2639, 2025."),
    ("İLÇE, A.; YUZDEN, G. E.; VAN GIERSBERGEN, M. Y. The examination of problems experienced by nurses and doctors "
     "associated with exposure to surgical smoke and the necessary precautions. ", "J Clin Nurs",
     ", v. 26, n. 11-12, p. 1555-1561, 2017."),
    ("INTHOUT, J.; IOANNIDIS, J. P. A.; BORM, G. F. The Hartung-Knapp-Sidik-Jonkman method for random effects "
     "meta-analysis is straightforward and considerably outperforms the standard DerSimonian-Laird method. ",
     "BMC Med Res Methodol", ", v. 14, p. 25, 2014."),
    ("MUNN, Z. et al. Methodological guidance for systematic reviews of observational epidemiological studies reporting "
     "prevalence and cumulative incidence data. ", "Int J Evid Based Healthc", ", v. 13, n. 3, p. 147-153, 2015."),
    ("NAVARRO, M. C. et al. Cambios en la mucosa nasal de los médicos por exposición al humo por electrocoagulación. ",
     "Rev Fac Nac Salud Pública", ", v. 34, n. 2, p. 135-144, 2016."),
    ("PAGE, M. J. et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. ", "BMJ",
     ", v. 372, n71, 2021."),
    ("RILEY, R. D.; HIGGINS, J. P. T.; DEEKS, J. J. Interpretation of random effects meta-analyses. ", "BMJ",
     ", v. 342, d549, 2011."),
]
refs_par = [[(a, {}), (b, {"bold": True}), (c, {})] for a, b, c in REFS]
refs_left, refs_right = refs_par[:9], refs_par[9:]  # colunas de altura parecida
QB_H = 2.4
RF_B = YB - QB_H - GAP
(r1x, r1w), (r2x, r2w) = cols(2, gap=0.6)
tb(s, r1x, Y0, r1w, RF_B - Y0, refs_left, size=15, color=INK, space_after=8, line_spacing=1.0)
tb(s, r2x, Y0, r2w, RF_B - Y0, refs_right, size=15, color=INK, space_after=8, line_spacing=1.0)
QY = YB - QB_H
rect(s, L, QY, R - L, QB_H, fill=NAVY_TINT)
QS = QB_H - 2 * PAD
pic(s, QR_PNG, R - PAD - QS, QY + PAD, w=QS, h=QS, name="QR code OSF")
icon(s, "file", L + PAD, QY + (QB_H - 0.7) / 2, 0.7, color="navy")
tb(s, L + PAD + 1.0, QY + 0.25, R - L - 2 * PAD - 1.0 - QS - 0.3, QB_H - 0.5, [
    {"runs": [(QR_TITULO, {"bold": True, "color": NAVY, "size": 22})], "space_after": 6},
    [("Aponte a câmera do celular para o QR code  ·  ", {}), ("osf.io/jktmn", {"bold": True, "color": NAVY})],
    {"runs": [("Planilhas de extração, código em Python, figuras em alta resolução e material complementar.",
               {"color": GRAY})]},
], size=17, color=INK, space_after=3, anchor=MSO_ANCHOR.MIDDLE)
deck.notes(s, NOTAS["referencias"], dur=5)

# =====================================================================
# 20 — AGRADECIMENTOS
# =====================================================================
s = deck.content_slide("AGRADECIMENTOS")
icon(s, "handshake", 10.35 - 0.55, Y0 + 0.3, 1.1, color="navy")
tb(s, L, Y0 + 1.55, R - L, 0.7, ["Muito obrigado"], size=36, color=NAVY, bold=True, align=PP_ALIGN.CENTER, space_after=0)
ag = [
    ("graduation", "Orientadora", "Profa. Lisie Tocci Justo, pela orientação, supervisão metodológica e revisão crítica."),
    ("people", "Coautores", "Luiz Henrique Ledesma Pereira (SLMandic\u00a0Araras) e Dra.\u00a0Mariana Matera Veras "
                            "(LIM05,\u00a0HC-FMUSP), pela interpretação dos resultados e revisão crítica."),
    ("hospital", "Instituição", "Faculdade São Leopoldo Mandic Araras e Programa de Iniciação Científica (PIC), na modalidade "
                                "voluntária, pelo apoio institucional\u00a0e\u00a0metodológico."),
]
AG_Y, AG_H = Y0 + 2.6, 3.75
for (x, w), (ic, t, body) in zip(cols(3), ag):
    rect(s, x, AG_Y, w, AG_H, fill=LIGHT)
    icon_badge(s, ic, x + w / 2, AG_Y + PAD + 0.475, d=0.95, fill=NAVY)
    tb(s, x + PAD, AG_Y + 1.45, w - 2 * PAD, 0.45, [t], size=19, color=NAVY, bold=True, align=PP_ALIGN.CENTER,
       space_after=0)
    tb(s, x + PAD, AG_Y + 1.95, w - 2 * PAD, AG_H - 1.95 - PAD, [body], size=17, color=INK, align=PP_ALIGN.CENTER,
       space_after=0, line_spacing=1.05)
IB_Y = AG_Y + AG_H + GAP
rect(s, L, IB_Y, R - L, YB - IB_Y, fill=NAVY_TINT)
tb(s, L + PAD, IB_Y + 0.2, R - L - 2 * PAD, YB - IB_Y - 0.4, [
    [("Registro PROSPERO: ", {"bold": True, "color": NAVY}), ("CRD420251238727   ·   ", {}),
     (QR_DADOS, {"bold": True, "color": NAVY}), ("osf.io/jktmn", {})],
    [("Financiamento: ", {"bold": True, "color": NAVY}), ("nenhum   ·   ", {}),
     ("Conflitos de interesse: ", {"bold": True, "color": NAVY}), ("nenhum   ·   ", {}),
     ("Dispensa do CEP: ", {"bold": True, "color": NAVY}), ("protocolo 2025/0743 (Res. CNS 510/2016)", {})],
    [("Contato: ", {"bold": True, "color": NAVY}), ("theo.baccaro@med.slmandic.edu.br", {})],
], size=17, color=INK, space_after=6, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
deck.notes(s, NOTAS["agradecimentos"], dur=10)

# =====================================================================
# 21 — ENCERRAMENTO (slide do modelo, movido para o fim) + QR
# =====================================================================
deck.move_slide_to_end(1)
enc = prs.slides[len(prs.slides) - 1]
QE = 2.4  # grande o bastante para ler do fundo da sala durante as perguntas
QCX = 12.83 + 6.42 / 2
pic(enc, QR_PNG, QCX - QE / 2, 5.85, w=QE, h=QE, name="QR code OSF")
tb(enc, QCX - 3.2, 5.85 + QE + 0.1, 6.4, 0.4, [[(QR_CURTO + "  ·  ", {}),
                                             ("osf.io/jktmn", {"bold": True, "color": NAVY})]],
   size=16, color=GRAY, align=PP_ALIGN.CENTER, space_after=0)
deck.notes(enc, NOTAS["encerramento"])

for sl in prs.slides:
    add_transition(sl)

deck.save(OUT)
print(f"OK: {OUT} ({len(prs.slides)} slides; roteiro de {deck.clock // 60}:{deck.clock % 60:02d})")
