"""Monta o guia de estudo (Markdown + DOCX) a partir das partes em guia/partes/.

Uso: python3 montar_guia.py
"""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

import gerar_roteiro

HERE = Path(__file__).resolve().parent
PARTES = HERE / "partes"
OUT_MD = HERE / "GUIA_DE_ESTUDO_E_DEFESA.md"
OUT_DOCX = HERE / "GUIA_DE_ESTUDO_E_DEFESA.docx"


def read(name: str) -> str:
    p = PARTES / name
    return p.read_text(encoding="utf-8").strip() + "\n" if p.exists() else ""


def perguntas_md(data: list[dict]) -> tuple[str, str]:
    """Retorna (seção de perguntas, apêndice com o registro das verificações)."""
    out = ["## Parte 5 — Perguntas prováveis da banca e respostas-modelo\n",
           "As respostas estão em primeira pessoa, no tamanho de uma resposta oral (30–60 s). Cada bloco foi escrito "
           "por um revisor e depois conferido, número a número, contra o manuscrito por um segundo revisor independente; "
           "o registro dessas conferências está no Apêndice. Onde a resposta depende de algo que só você sabe (tempo "
           "gasto em cada etapa, dificuldades pessoais), há colchetes para você preencher.\n"]
    apx = ["## Apêndice — Registro das verificações das respostas\n",
           "Resumo do que o segundo revisor corrigiu em cada bloco de perguntas ao conferir as respostas contra o "
           "manuscrito. Serve como lista de pontos sensíveis: se a correção foi necessária aqui, a banca também pode "
           "tropeçar nela.\n"]
    n = 0
    for bloco in data:
        out.append(f"### Lente: {bloco['nome']}\n")
        for q in bloco["perguntas"]:
            if q["pergunta"].strip().startswith("[Correções"):
                apx.append(f"### {bloco['nome']}\n")
                apx.append(q["resposta"].strip() + "\n")
                continue
            n += 1
            out.append(f"**P{n}. {q['pergunta'].strip()}**\n")
            out.append(q["resposta"].strip() + "\n")
            if q.get("dica"):
                out.append(f"> Dica: {q['dica'].strip()}\n")
    return "\n".join(out), "\n".join(apx)


def main():
    gerar_roteiro.main()  # roteiro e cronograma sempre a partir das notas atuais do PPTX
    explic = json.loads((PARTES / "explicacoes.json").read_text(encoding="utf-8"))
    pergs = json.loads((PARTES / "perguntas.json").read_text(encoding="utf-8"))
    ordem = {"passos-1-3": "Parte 2", "passos-4-5-7": "Parte 3", "passo-6": "Parte 4"}
    partes_metodo = []
    for key in ("passos-1-3", "passo-6", "passos-4-5-7"):
        e = next(x for x in explic if x["key"] == key)
        md = e["markdown"].strip()
        # renomeia o título principal da seção para incluir a numeração da parte
        md = re.sub(r"^##\s+", f"## {ordem[key]} — ", md, count=1)
        partes_metodo.append(md + "\n")
    # ordem final das partes: 2 = passos 1-3, 3 = passo 6 (metanálise), 4 = passos 4, 5 e 7
    partes_metodo[1] = partes_metodo[1].replace("## Parte 4 — ", "## Parte 3 — ", 1)
    partes_metodo[2] = partes_metodo[2].replace("## Parte 3 — ", "## Parte 4 — ", 1)
    perg_md, apendice_md = perguntas_md(pergs)
    doc = "\n\n".join([
        read("00_intro.md"),
        "## Parte 1 — Roteiro de fala, slide a slide\n\n" + re.sub(r"^# .*\n", "", read("01_roteiro.md"), count=1)
        .replace("## Slide", "### Slide"),
        *partes_metodo,
        perg_md,
        read("06_numeros_e_checklist.md"),
        apendice_md,
    ])
    OUT_MD.write_text(doc, encoding="utf-8")
    subprocess.run(["pandoc", str(OUT_MD), "-o", str(OUT_DOCX), "--toc", "--toc-depth=2",
                    "-M", "lang=pt-BR", "-M", "toc-title=Sumário",
                    "-M", "title=Guia de estudo e defesa — VIII SEMICA"], check=True)
    print("OK:", OUT_MD, OUT_DOCX, f"({len(doc.split())} palavras)")


if __name__ == "__main__":
    main()
