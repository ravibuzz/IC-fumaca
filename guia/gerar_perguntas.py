"""Gera PERGUNTAS_DA_BANCA.pdf: as perguntas mais prováveis com resposta curta (~30 s) e o slide a mostrar na versão
enxuta, seguidas do banco completo de perguntas e respostas-modelo (partes/perguntas.json, já conferido contra o
manuscrito).

Uso:  python3 gerar_perguntas.py
"""
from __future__ import annotations

import html
import json
import re
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "PERGUNTAS_DA_BANCA.pdf"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

# (pergunta, resposta curta, slide da versão enxuta para mostrar). Condensadas das respostas-modelo conferidas.
TOP = [
    ("Esse 37,6% é 37,6% de quê, exatamente?",
     "É a proporção combinada de profissionais de centro cirúrgico que relataram sintoma ocular (irritação ou "
     "lacrimejamento), em seis amostras independentes, com 756 pessoas da Turquia, Malásia e Brasil. Não é o excesso "
     "causado pela fumaça, porque não há grupo não exposto. Os estudos vão de 19,4% a 56,1%; a síntese é 37,6% "
     "(IC95% 21,9–56,5), e num novo hospital a prevalência pode ficar entre 7 e 83%.", "8"),
    ("A metanálise não tem grupo controle. Como você fala em risco à saúde?",
     "A metanálise não fala em risco: estima a frequência de sintomas em expostos, a carga de sintomas, não o efeito "
     "causal. A comparação com não expostos vem da síntese narrativa: HPV nasal (RR 5,2), metaplasia nasal (RR 13,9), "
     "VEF1 menor e biomarcadores urinários elevados, todos desfavoráveis aos expostos, mas com um estudo por desfecho. "
     "Por isso falo em precaução, não em risco atribuível.", "10 e 11"),
    ("Com I² de 93%, para que serve combinar os estudos?",
     "O número importante não é só 37,6%, é o intervalo de predição de 7 a 83%. Em metanálise de prevalência, I² alto "
     "é esperado. Combinar serviu para estimar o centro, medir a dispersão e investigar a origem da variação: país e "
     "definição do sintoma. No respiratório, só com definições específicas, o I² cai de 91% para 61%.", "8 (apoio 23)"),
    ("O que significa o intervalo de predição de 7 a 83%?",
     "O IC (21,9–56,5%) diz onde está a média; o intervalo de predição diz onde deve cair a prevalência de um novo "
     "centro cirúrgico: 7 a 83% no ocular e 15 a 74% no respiratório. Com menos de dez estudos ele é instável, e eu "
     "registro isso nos métodos.", "8"),
    ("Por que efeitos aleatórios, e não efeito fixo?",
     "Porque a prevalência verdadeira muda entre hospitais e países, com instrumentos e definições diferentes. O "
     "modelo estima a média e a dispersão entre estudos (τ² por Paule-Mandel); com poucos estudos, o ajuste de "
     "Hartung-Knapp dá um IC mais honesto. O argumento é conceitual; o I² só confirmou.", "7 (apoio 21)"),
    ("O resultado depende do modelo ou de algum estudo?",
     "Não. Freeman-Tukey deu 38,1% e 41,7%; GLMM, 37,5% e 42,0%; tirando um estudo de cada vez, 34,3–42,1% (ocular) "
     "e 38,9–45,5% (respiratório); sem o resumo de congresso, 42,1% e 42,4%.", "9"),
    ("A inteligência artificial fez a triagem por você?",
     "Não. Li os 10.910 títulos e resumos e decidi cada um. A automação só ordenou a fila de leitura (um script em "
     "Python e um assistente de IA, declarados); nenhuma exclusão foi feita pela IA. A elegibilidade, a extração, a "
     "interpretação e a redação foram humanas, e o uso está declarado conforme a Portaria CNPq nº 2.664/2026.", "5"),
    ("Triagem por um único revisor não invalida a revisão?",
     "Não invalida, mas reduz a confiança, e eu declaro isso. Tornei cada decisão auditável: protocolo no PROSPERO "
     "antes da extração, motivos de exclusão registrados, dados e julgamentos nos anexos, código e planilhas no OSF. "
     "A busca por citação (443 referências) funcionou como rede de segurança. A primeira melhoria é a triagem em "
     "duplicata.", "11 (apoio 25)"),
    ("Por que incluir um resumo de congresso na metanálise?",
     "O critério admitia resumos com dados suficientes (eventos e denominador): um cumpriu, outro não e foi excluído. "
     "Classifiquei o resumo com preocupação alta de viés e refiz sem ele: ocular 42,1% e respiratório 42,4%, sem "
     "mudar a conclusão.", "9"),
    ("Certeza muito baixa em tudo: qual a utilidade prática?",
     "Dizer com honestidade quanto se pode confiar. Mesmo o estudo com menor prevalência teve 19,4% de sintoma "
     "ocular: a carga é relevante em qualquer cenário. A revisão também mapeou o vazio (nenhum estudo sobre câncer "
     "ou DPOC), e certeza baixa é justamente o terreno da precaução.", "12 (apoio 22)"),
    ("A fumaça cirúrgica causa câncer ou DPOC?",
     "Ninguém mediu isso diretamente: nenhum estudo elegível estimou câncer ou DPOC na equipe. Ausência de estudos "
     "não é ausência de risco. Há sinais em desfechos intermediários e plausibilidade biológica, mas o risco só se "
     "responde com coortes com medida objetiva da exposição.", "11 e 13"),
    ("O que protege mais: exaustor na fonte ou N95/PFF2?",
     "Um não substitui o outro: a exaustão na fonte é a medida principal; a N95/PFF2 complementa, porque retém "
     "partículas, mas não gases; e há a educação da equipe. Isso vem do NIOSH (1996) e da precaução: a efetividade "
     "das medidas não foi avaliada nesta revisão.", "12"),
    ("Por que o ocular é o desfecho principal, se o respiratório tem mais estudos?",
     "Pela homogeneidade da definição, não pelo tamanho: os seis estudos oculares mediram irritação ou lacrimejamento; "
     "no respiratório, as definições vão de tosse a qualquer sintoma de vias aéreas. Só com definições específicas, o "
     "respiratório vai a 35,8% e o I² cai de 91% para 61%.", "3 e 9"),
    ("São 22 relatórios, mas só 6 e 7 amostras nas metanálises. Por quê?",
     "Sete publicações do mesmo grupo do Paraná tinham amostras sobrepostas. A regra, definida antes da síntese, foi "
     "usar uma só por análise (Bieniek et al., 2022); outros relatórios não tinham o desfecho no formato combinável e "
     "entraram na síntese narrativa. Nenhum participante foi contado duas vezes.", "6 (apoio 19)"),
    ("Por que PECO, e não PICO? E o CoCoPop?",
     "PECO porque é exposição, não intervenção alocada; ele orientou a busca e os desfechos comparativos. Para a "
     "prevalência, usei o CoCoPop (condição, contexto, população), recomendado pelo JBI.", "4"),
    ("Resuma a mensagem do trabalho em uma frase.",
     "Quatro em cada dez profissionais expostos relatam sintomas oculares ou respiratórios; estudos isolados mostram "
     "alterações além do incômodo agudo; ninguém mediu câncer ou DPOC. Proteger a equipe é precaução justificada, e "
     "medir o risco de longo prazo é a pesquisa que falta.", "12"),
]

CSS = """
@page { size: A4; margin: 14mm 15mm 16mm 15mm; }
body { font-family: "Liberation Sans", Arial, sans-serif; color: #1f2430; font-size: 10.5pt; line-height: 1.4; }
h1 { color: #002060; font-size: 20pt; margin: 0 0 4px; }
h2 { color: #002060; font-size: 14pt; margin: 18px 0 8px; border-bottom: 2px solid #C9A227; padding-bottom: 3px; }
h2.novo { page-break-before: always; break-before: page; }
.sub { color: #555; margin: 0 0 12px; }
.box { background: #f3f5f9; border-left: 4px solid #002060; padding: 8px 12px; margin: 8px 0 12px; }
.q { page-break-inside: avoid; break-inside: avoid; margin: 0 0 12px; }
.q .p { font-weight: bold; color: #002060; font-size: 11pt; margin-bottom: 3px; }
.q .n { display: inline-block; min-width: 22px; background: #8B0000; color: #fff; border-radius: 3px;
        text-align: center; font-size: 9.5pt; margin-right: 6px; padding: 0 4px; }
.curta { background: #fff8e1; border-left: 4px solid #C9A227; padding: 6px 10px; }
.mostre { color: #0E7C86; font-weight: bold; font-size: 9.5pt; margin-top: 3px; }
.dica { color: #555; font-size: 9.5pt; margin-top: 4px; }
.dica b { color: #8A6D1F; }
ul { margin: 2px 0 6px 18px; padding: 0; }
"""

MAPA_APOIO = ("Slides de apoio da versão enxuta (digite o número + Enter; 16 + Enter volta ao encerramento): "
              "17 trajetória e aprendizado · 18 elegibilidade e busca · 19 fluxograma PRISMA · 20 extração e JBI · "
              "21 metanálise e robustez · 22 GRADE · 23 respiratório e subgrupo por país · 24 desfechos objetivos · "
              "25 pontos fortes e limitações.")


def md(texto):
    """Escapa e converte **negrito** do JSON em <b>."""
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", html.escape(texto))


def main():
    banco = json.loads((HERE / "partes" / "perguntas.json").read_text(encoding="utf-8"))
    partes = [
        "<h1>Perguntas da banca</h1>",
        '<p class="sub">VIII SEMICA · 21/10/2026 · Theo Báccaro · Fumaça cirúrgica e saúde da equipe de centro '
        "cirúrgico: revisão sistemática e metanálise de prevalência</p>",
        '<div class="box"><b>Como responder.</b> Deixe o slide de encerramento (QR code) na tela. Ouça a pergunta '
        "inteira, repita-a em uma frase e responda em 30 a 40 segundos, começando pela resposta direta. Se a pergunta "
        "apontar uma limitação, concorde com o que é verdade, diga o que fez para reduzi-la e o que faria a seguir. "
        "Nunca diga que a fumaça <b>causa</b> doença: diga carga de sintomas, sinais em desfechos intermediários e "
        "precaução.<br><br>" + MAPA_APOIO + "</div>",
        "<h2>Parte 1 · As 16 mais prováveis, com resposta de 30 segundos</h2>",
    ]
    for i, (p, r, sl) in enumerate(TOP, start=1):
        partes.append(f'<div class="q"><div class="p"><span class="n">{i}</span>{html.escape(p)}</div>'
                      f'<div class="curta">{html.escape(r)}</div><div class="mostre">Mostre: slide {sl}</div></div>')
    partes.append('<h2 class="novo">Parte 2 · Banco completo: respostas-modelo (30–60 s) e dicas</h2>'
                  '<p class="sub">Escritas em primeira pessoa e conferidas número a número contra o manuscrito. Onde há '
                  "colchetes, complete com a sua experiência.</p>")
    n = 0
    for k, grupo in enumerate(banco):
        partes.append(f'<h2{" class=novo" if k else ""}>{html.escape(grupo["nome"])}</h2>')
        for q in grupo["perguntas"]:
            if q["pergunta"].startswith("[Correções"):
                continue  # registro interno da verificação, não é pergunta
            n += 1
            dica = f'<div class="dica"><b>Dica:</b> {md(q["dica"])}</div>' if q.get("dica") else ""
            partes.append(f'<div class="q"><div class="p"><span class="n">{n}</span>{md(q["pergunta"])}</div>'
                          f'<div>{md(q["resposta"])}</div>{dica}</div>')
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "perguntas.html"
        page.write_text(f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><style>{CSS}</style></head>"
                        f"<body>{''.join(partes)}</body></html>", encoding="utf-8")
        subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={OUT}", page.as_uri()], check=True, capture_output=True)
    print(f"OK: {OUT} ({len(TOP)} perguntas curtas + {n} do banco completo)")


if __name__ == "__main__":
    main()
