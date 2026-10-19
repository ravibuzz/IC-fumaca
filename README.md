# IC — Fumaça cirúrgica (VIII SEMICA 2025/2026)

Apresentação oral de 10 minutos e material de estudo da Iniciação Científica
"Sintomas, desfechos objetivos e biomarcadores em profissionais de centro cirúrgico
ocupacionalmente expostos à fumaça cirúrgica: revisão sistemática e metanálise de prevalência".

## Conteúdo

| Caminho | O que é |
|---|---|
| `apresentacao/SEMICA_Fumaca_Cirurgica_Baccaro.pptx` | Apresentação final (21 slides), sobre o modelo oficial do SEMICA, com notas de fala em todos os slides, transição de esmaecimento e animações automáticas nos slides-chave |
| `apresentacao/SEMICA_Fumaca_Cirurgica_Baccaro.pdf` | Versão PDF para o pen drive (plano B) |
| `resumo/Resumo_SEMICA_Baccaro.docx` | Resumo pronto para submissão ao SEMICA (Word), conforme as normas do evento; gerado por `resumo/gerar_docx.js` a partir de `resumo/RESUMO_SEMICA.md` |
| `guia/GUIA_DE_ESTUDO_E_DEFESA.md` / `.docx` | Guia de estudo: roteiro de fala, método explicado passo a passo, perguntas prováveis da banca com respostas, ficha de números e checklist |
| `apresentacao/build_deck.py` + `deck_lib.py` | Gerador da apresentação (python-pptx) a partir do modelo oficial |
| `apresentacao/assets/` | Modelo oficial, figuras do manuscrito, imagens geradas (Higgsfield), ícones e, em `trajetoria/`, miniaturas dos certificados, capas das diretrizes e o QR code do OSF |
| `apresentacao/auditar_layout.py` | Auditoria de layout: mede no PDF renderizado o respiro do texto dentro de cada card (bordas, transbordo, sobreposição, alinhamento) |
| `guia/montar_guia.py` + `guia/partes/` | Montagem do guia (Markdown → DOCX via pandoc) |
| `fonte/` | Manuscrito final (v5) usado como fonte de todos os números |

## Regenerar

```bash
cd apresentacao && python3 build_deck.py          # gera o PPTX
python3 auditar_layout.py SEMICA_Fumaca_Cirurgica_Baccaro.pptx SEMICA_Fumaca_Cirurgica_Baccaro.pdf  # confere o layout
cd ../guia && python3 montar_guia.py               # gera o guia (.md e .docx), com roteiro e cronograma a partir das notas
```

Dependências: Python 3 com `python-pptx`, `Pillow`, `lxml`, `segno` (QR code); `pandoc` para o DOCX do guia; `pdftotext` (poppler) para a auditoria.

## Versão enxuta (pedido da orientadora)

Slides mais limpos e tempo cronometrado: uma mensagem por slide (o subtítulo é a frase-chave), pouco texto e os números
de destaque grandes; o foco é mostrar como o trabalho foi feito e responder ao objetivo. A versão completa continua
igual e gerada por `build_deck.py`.

| Caminho | O que é |
|---|---|
| `apresentacao/SEMICA_Fumaca_Cirurgica_Baccaro_ENXUTA.pptx` / `.pdf` | 15 slides principais (fala de ~7:40, com folga para os 10 min) + 9 slides de apoio depois do encerramento |
| `apresentacao/ROTEIRO_VERSAO_ENXUTA.md` | Tempo por slide, relógio acumulado e a fala de cada slide |
| `apresentacao/build_deck_enxuto.py` + `notas_fala_enxuta.py` | Gerador e notas; capa, referências, agradecimentos, encerramento e apoio reaproveitam as funções `slide_*` de `build_deck.py` |

```bash
cd apresentacao && python3 build_deck_enxuto.py   # gera o PPTX e o ROTEIRO_VERSAO_ENXUTA.md
```

Os slides de apoio (16 a 24, título "APOIO · ...": trajetória, critérios e busca, PRISMA, extração e risco de viés,
metanálise, GRADE, respiratório e robustez, biomarcadores, discussão) só aparecem se a banca perguntar: no modo de
apresentação, digite o número do slide e Enter; para voltar ao encerramento, digite 15 e Enter. O aprendizado
(trajetória, slide 16) só se a banca der a oportunidade.
