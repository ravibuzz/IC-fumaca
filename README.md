# IC — Fumaça cirúrgica (VIII SEMICA 2025/2026)

Apresentação oral de 10 minutos e material de estudo da Iniciação Científica
"Sintomas, desfechos objetivos e biomarcadores em profissionais de centro cirúrgico
ocupacionalmente expostos à fumaça cirúrgica: revisão sistemática e metanálise de prevalência".

## Conteúdo

| Caminho | O que é |
|---|---|
| `apresentacao/SEMICA_Fumaca_Cirurgica_Baccaro.pptx` | Apresentação final (20 slides), sobre o modelo oficial do SEMICA, com notas de fala em todos os slides |
| `apresentacao/SEMICA_Fumaca_Cirurgica_Baccaro.pdf` | Versão PDF para o pen drive (plano B) |
| `guia/GUIA_DE_ESTUDO_E_DEFESA.md` / `.docx` | Guia de estudo: roteiro de fala, método explicado passo a passo, perguntas prováveis da banca com respostas, ficha de números e checklist |
| `apresentacao/build_deck.py` + `deck_lib.py` | Gerador da apresentação (python-pptx) a partir do modelo oficial |
| `apresentacao/assets/` | Modelo oficial, figuras do manuscrito, imagens geradas (Higgsfield) e ícones |
| `guia/montar_guia.py` + `guia/partes/` | Montagem do guia (Markdown → DOCX via pandoc) |
| `fonte/` | Manuscrito final (v5) usado como fonte de todos os números |

## Regenerar

```bash
cd apresentacao && python3 build_deck.py          # gera o PPTX
cd ../guia && python3 montar_guia.py               # gera o guia (.md e .docx)
```

Dependências: Python 3 com `python-pptx`, `Pillow`, `lxml`; `pandoc` para o DOCX do guia.
