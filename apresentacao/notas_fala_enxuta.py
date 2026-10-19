"""Notas do orador da VERSÃO ENXUTA (15 slides principais, ~7 min 40 s, mais slides de apoio para as perguntas).

Mesmo formato de notas_fala.py:
  FALA  — o que dizer em voz alta; dimensionada para ~120 palavras/min, com folga para apontar a figura e respirar;
  APOIO — números e respostas prontas; NÃO é para ler, só para consultar se perguntarem.
O cabeçalho "[m:ss–m:ss] TÍTULO (~N s · W palavras)" é preenchido por Deck.notes().
"""

NOTAS = {
    "capa": """CAPA
FALA:
Bom dia. Sou Theo Báccaro, de Medicina da São Leopoldo Mandic, orientado pela Profa. Lisie. Apresento nossa revisão sistemática sobre a fumaça cirúrgica e a saúde da equipe do centro cirúrgico.

APOIO (não ler):
- Coautores: Luiz Henrique Ledesma Pereira e Dra. Mariana Matera Veras (LIM05, HC-FMUSP).
- Fale o título de forma natural, sem ler palavra por palavra. Respire e avance.""",

    "introducao": """INTRODUÇÃO
FALA:
Sempre que o eletrocautério, o laser ou o bisturi ultrassônico cortam tecido, formam fumaça. Ela contém benzeno e outros compostos voláteis, partículas ultrafinas e até DNA viral, como o do HPV. A equipe do centro cirúrgico está exposta a essa fumaça no trabalho e relata irritação nos olhos e nas vias aéreas; os efeitos crônicos são plausíveis, mas sem relação causal estabelecida. E as revisões anteriores eram majoritariamente descritivas: faltava combinar os estudos numa estimativa e graduar a certeza. Essa é a lacuna.

APOIO (não ler):
- Composição: hidrocarbonetos aromáticos policíclicos, compostos orgânicos voláteis (benzeno, tolueno, xileno), material particulado fino (PM2,5) e ultrafino (< 0,1 µm), material genético viral (Benaim; Jaspers, 2024).
- Controvérsia: Hurst; Stewart (2024) argumentam que o risco pode estar superestimado.
- Revisões anteriores sem síntese quantitativa: Mowbray et al., 2013; Dixon; Dasgupta; Vasdev, 2023.
- A imagem é ilustrativa, gerada por IA (a legenda diz isso).""",

    "objetivos": """OBJETIVO
FALA:
O objetivo foi avaliar os desfechos de saúde associados à exposição ocupacional à fumaça cirúrgica na equipe de centro cirúrgico, em três frentes: a prevalência de sintomas, por metanálise; os desfechos objetivos e biomarcadores, por síntese narrativa; e a certeza da evidência, pelo GRADE.

APOIO (não ler):
- PECO, e não PICO, porque é exposição, não intervenção alocada. Para a prevalência, o esquema CoCoPop (Condição, Contexto, População; Munn et al., 2015), recomendado pelo JBI.
- Ocular é o desfecho principal; respiratório é exploratório (definições mais variáveis).
- A conclusão responde a estes três itens, na mesma ordem (1, 2, 3).""",

    "metodo": """MÉTODO EM 7 PASSOS
FALA:
Para responder, segui sete passos, conforme o PRISMA 2020. Registrei o protocolo no PROSPERO antes da extração. Busquei em sete bases, na literatura cinzenta e por citação, sem filtro de idioma. Li, um a um, 10.910 títulos e resumos. Extraí os dados numa planilha padronizada, avaliei o risco de viés pelo JBI, combinei as prevalências em metanálise e graduei a certeza pelo GRADE. O código e as planilhas estão abertos no OSF, e a IA foi apenas apoio operacional: as decisões foram humanas.

APOIO (não ler):
- PROSPERO CRD420251238727; dispensa do CEP (protocolo 2025/0743; Res. CNS 510/2016).
- 7 bases: PubMed/MEDLINE, Embase, Web of Science, Scopus, BVS (LILACS/IBECS), SciELO e Cochrane CENTRAL; cinzenta: Google Scholar (4 × 50 resultados) e Catálogo CAPES; citação: OpenAlex.
- Ferramentas: Zotero 6, Rayyan, OpenAlex, Python 3.13 (NumPy, SciPy, statsmodels).
- IA (declarada, Portaria CNPq nº 2.664/2026): priorização da ordem de leitura, leitura assistida de resumos e organização do fluxo; elegibilidade, extração, interpretação e redação foram decisões humanas.
- Detalhes de elegibilidade e busca: slide de apoio 17.
- As colunas aparecem sozinhas, uma a uma: comece a falar sem esperar.""",

    "selecao": """BUSCA E SELEÇÃO
FALA:
A busca trouxe 16.757 registros. Sem as duplicatas, li 10.910 títulos e resumos; 32 relatórios foram buscados na íntegra, seis não foram recuperados, 26 foram avaliados e 22 incluídos, de nove países. Um cuidado importante: sete publicações do mesmo grupo tinham amostras sobrepostas, e cada análise usou uma só, para não contar as mesmas pessoas duas vezes.

APOIO (não ler):
- Fluxo: 16.757 identificados → 16.749 importados (8 não exportados) → 5.839 duplicatas → 10.910 triados → 10.882 excluídos → 28 + 4 por citação = 32 buscados → 6 não recuperados → 26 avaliados → 4 excluídos (1 resumo sem dados; 3 por população ou contexto) → 22 incluídos.
- 19 transversais e 3 coortes prospectivas; países: Turquia, Malásia, Brasil, Paquistão, China, México, EUA, Sudão e Tailândia.
- Representante do grupo com sobreposição (Paraná): Bieniek et al., 2022, definido antes da síntese.
- Triagem por revisor único: limitação declarada; replicar em duplicata está nas perspectivas.
- Fluxograma PRISMA completo: slide de apoio 18.""",

    "metanalise": """COMO OS ESTUDOS FORAM COMBINADOS
FALA:
Como combinar estudos tão diferentes? Em quatro passos. Primeiro, cada estudo vira uma proporção: no İlçe, 33 de 81 profissionais, 40,7%. Segundo, a escala logito, que mantém o resultado entre zero e cem por cento. Terceiro, um modelo de efeitos aleatórios, porque a prevalência verdadeira muda de um hospital para outro, com ajuste de Hartung-Knapp, mais honesto com poucos estudos. Quarto, o intervalo de predição: o que esperar num novo hospital. Antes, o risco de viés de cada estudo foi avaliado pelo JBI; depois, a certeza de cada desfecho, pelo GRADE.

APOIO (não ler):
- Logito = ln[p ÷ (1 − p)]; IC95% de cada estudo pelo método de Wilson; sem 0% ou 100%, não houve correção de continuidade.
- Efeitos aleatórios: τ² (variância entre estudos) por Paule-Mandel; peso = 1 ÷ (variância + τ²). Hartung-Knapp: IC pela distribuição t com k − 1 graus de liberdade (IntHout; Ioannidis; Borm, 2014).
- Intervalo de predição com t (k − 2); instável com menos de 10 estudos.
- Sem teste de Egger nem funil: em proporções o erro-padrão depende da própria proporção, e os testes pedem ≥ 10 estudos.
- GRADE: ponto de partida baixa (observacional); um domínio grave já leva a muito baixa.
- Detalhes: slides de apoio 19 (extração e JBI), 20 (metanálise) e 21 (GRADE).""",

    "ocular": """RESULTADO PRINCIPAL – OCULAR ← dê tempo a este slide
FALA:
Este é o resultado principal. Em seis estudos, com 756 profissionais, a prevalência combinada de sintoma ocular foi de 37,6%: cerca de quatro em cada dez relataram irritação ou lacrimejamento. Cada quadrado é um estudo; o losango, a estimativa combinada. Os estudos vão de 19%, na Malásia, a 56%, na Turquia, e o I² de 93% mostra que a variação entre estudos vai além do acaso. Por isso, a mensagem mais honesta é o intervalo de predição: num novo hospital, a prevalência pode ficar entre 7 e 83%, conforme o contexto.

APOIO (não ler):
- IC95% 21,9–56,5. O intervalo de confiança é sobre a média; o intervalo de predição é sobre um novo estudo.
- É a proporção de expostos que relatou o sintoma, não um efeito causal: não há grupo não exposto no agrupamento.
- O maior inquérito (Van Giersbergen et al., 2019; n = 672) ficou fora do ocular: sem numerador e denominador oculares extraíveis.
- "I² de 93% invalida?": em metanálise de prevalência, I² alto é esperado; por isso o intervalo de predição e a investigação das fontes (país, definição).
- Subgrupo por país (exploratório): Turquia 50,5%; Malásia 19,8%; p < 0,001 entre subgrupos.""",

    "respiratorio": """SINTOMA RESPIRATÓRIO E ROBUSTEZ ← aponte a tabela, não leia linha por linha
FALA:
O sintoma respiratório, exploratório, teve prevalência de 41,7%, em sete estudos e 1.428 profissionais. E os resultados são robustos: com três modelos estatísticos diferentes, quase não mudam, no ocular e no respiratório. Com as definições mais específicas, o I² respiratório cai de 91 para 61%: parte da variação vem de como cada estudo definiu o sintoma.

APOIO (não ler):
- IC95% 30,4–53,9; intervalo de predição 15–74%; I² = 91%.
- Leave-one-out: ocular 34,3–42,1%; respiratório 38,9–45,5%. Sem o resumo de congresso: 42,1% e 42,4%.
- Só definições específicas: ocular 36,5% (I² 94%); respiratório 35,8% (I² 61%).
- Tabela completa e subgrupo por país: slide de apoio 22.""",

    "objetivos_bio": """DESFECHOS OBJETIVOS E BIOMARCADORES
FALA:
Além dos sintomas, quatro estudos mediram alterações objetivas, e todos apontam na mesma direção. No Sudão, função pulmonar menor nos expostos. No Brasil, o metabólito urinário do benzeno foi mais de quatro vezes maior. No México, metaplasia ou hiperplasia nasal em 70% dos residentes expostos, contra 5%. Na China, DNA de HPV na mucosa nasal cerca de cinco vezes mais frequente. Mas é um estudo por desfecho, a certeza é muito baixa, e nenhum estudo elegível estimou câncer ou DPOC.

APOIO (não ler):
- Ibrahim 2025 (92 vs 92 pareados; medianas): VEF1 2,78 vs 3,14 L; CVF 3,02 vs 3,45 L; PFE 327,5 vs 483,5 L/min; p = 0,001; VEF1/CVF ≈ 91% nos dois grupos (não é padrão obstrutivo); gradiente com o tempo de atuação.
- Canicoba 2025 (52 vs 49): ácido t,t-mucônico 202,9 vs 46,1 µg/L (benzeno); metil-hipúrico 468,2 vs 184,4 µg/L (xileno); malondialdeído 9,33 vs 3,22 nmol/mg; sem IC95%; t,t-mucônico é inespecífico (dieta, tabagismo).
- Navarro 2016: 16/23 vs 1/20; RR 13,9 (IC95% 2,0–95,8), IC amplo por 1 evento no grupo não exposto.
- Hu 2021: 42/469 vs 4/231; RR 5,2 (IC95% 1,9–14,2); DNA ≠ infecção ou doença; achado da N95 (0/196) sem ajuste.
- Coexposições (gases anestésicos, radiação) limitam a atribuição. Detalhes: slide de apoio 23.""",

    "discussao": """DISCUSSÃO
FALA:
O que o trabalho acrescenta: uma estimativa combinada, com intervalo de predição e certeza graduada, onde antes havia revisões descritivas, com protocolo registrado e análise reproduzível. Como ler: é prevalência em expostos, a carga de sintomas, não o excesso causado pela fumaça. E os limites, todos declarados: estudos transversais, sintomas autorrelatados, heterogeneidade alta e triagem por um único revisor.

APOIO (não ler):
- Viés de atribuição: o respondente sabe que o tema é fumaça. Trabalhador sadio: quem adoece sai do centro cirúrgico (subestima).
- Heterogeneidade: definição do sintoma e recordatório, composição profissional, tempo de exposição, exaustão e EPI.
- A favor da causalidade: gradiente com o tempo de exposição, temporalidade (coorte), plausibilidade. Contra: um estudo por desfecho, IC amplos, coexposições.
- Lista completa de pontos fortes e limitações: slide de apoio 24.
- ATITUDE: fale as limitações com segurança; a banca valoriza quem conhece as fraquezas do próprio trabalho.""",

    "conclusao": """CONCLUSÃO – RESPOSTA AO OBJETIVO
FALA:
Respondendo ao objetivo: um, sintomas oculares e respiratórios foram frequentemente relatados, por cerca de quatro em cada dez profissionais, com grande variação entre contextos. Dois, estudos isolados sugerem alterações além do incômodo agudo, sem demonstrar doença crônica. Três, a certeza é muito baixa. Ainda assim, pela carga de sintomas e por precaução, proteger a equipe parece justificado: exaustão na fonte, respiradores e educação.

APOIO (não ler):
- Proteção (NIOSH, 1996): a evacuação local na fonte é a medida principal; N95/PFF2 não substituem a exaustão. A efetividade das medidas não foi avaliada nesta revisão.
- NR-32: marco geral de riscos em serviços de saúde, sem regra específica para a fumaça cirúrgica.""",

    "perspectivas": """PERSPECTIVAS FUTURAS
FALA:
Faltam coortes com medida objetiva da exposição, estudos sobre câncer e DPOC e sobre a efetividade da proteção. Para este trabalho: submeter o manuscrito e replicar a triagem em duplicata.

APOIO (não ler):
- Também: definições padronizadas de sintoma e recordatório, atualização da busca e vigilância dos 6 relatórios não recuperados.""",

    "referencias": """REFERÊNCIAS
FALA:
As referências e os suplementos estão no QR code.

APOIO (não ler):
- Não leia a lista; mencione e avance.
- O QR code leva ao projeto público do OSF (osf.io/jktmn): suplementos, código e planilhas.""",

    "agradecimentos": """AGRADECIMENTOS
FALA:
Agradeço à Profa. Lisie, aos coautores e à São Leopoldo Mandic. Obrigado; estou à disposição para perguntas.

APOIO (não ler):
- Ao dizer "perguntas", AVANCE para o slide 15 (QR code grande) e deixe-o na tela durante a arguição.""",

    "encerramento": """ENCERRAMENTO
Deixe este slide na tela durante as perguntas. Ouça a pergunta inteira, repita-a em uma frase e responda em 30 a 40 segundos.
SLIDES DE APOIO (depois deste; no modo de apresentação, digite o número e Enter para ir direto, e 15 + Enter para voltar):
16 Trajetória e aprendizado (se perguntarem como foi a formação ou o que aprendeu)
17 Elegibilidade e busca por base
18 Fluxograma PRISMA completo e características dos estudos
19 Extração e risco de viés (JBI)
20 Metanálise passo a passo e verificações de robustez
21 GRADE: domínios e decisões
22 Sintoma respiratório: tabela de robustez e subgrupo por país
23 Desfechos objetivos em detalhe
24 Pontos fortes e limitações""",
}

# Slides de apoio: mostrados só se perguntarem. As notas são para consulta, sem tempo de fala.
APOIO = {
    "trajetoria": """APOIO 16 – TRAJETÓRIA E APRENDIZADO (mostre só se perguntarem sobre a formação ou o aprendizado)
Se derem a oportunidade, em 20 a 30 segundos:
Em julho de 2025 concluí o curso de revisão sistemática e metanálise da Unicamp, com distinção. Estudei o PRISMA 2020, o Cochrane Handbook, o manual do JBI e os livros de Borenstein e de Harrer; registrei o protocolo no PROSPERO e li, um a um, 10.910 títulos e resumos.
(Feche com o seu aprendizado, nas suas palavras; por exemplo: ler a heterogeneidade com honestidade, relatando o intervalo de predição em vez de um número único.)

PONTOS-CHAVE:
- Cursos: Unicamp (40 h, com distinção, 20/07/2025); ZucoEscrita (3,6 h); Fiocruz ABNT (3 h) e referências (2 h). Total ≈ 49 h.
- Cochrane Handbook, Borenstein e Harrer foram material de estudo; o manuscrito cita os trabalhos específicos de cada método (Barker 2021, IntHout 2014, Riley 2011, Munn 2015).""",

    "passos12": """APOIO 17 – ELEGIBILIDADE E BUSCA
- Incluídos: observacionais com profissionais de centro cirúrgico expostos; qualquer efeito à saúde ou marcador de exposição; português, inglês ou espanhol; sem limite de data; resumos de congresso só com eventos e denominador (decisão posterior ao registro, declarada).
- Excluídos: in vitro ou animais; fora do centro cirúrgico; desfecho só no paciente; só medição do ar; revisões, editoriais e cartas; exposição não atribuível à fumaça.
- Busca em dois blocos (população AND exposição), sem bloco de desfecho, para máxima sensibilidade. Cochrane CENTRAL = 0 era esperado (indexa ensaios clínicos).""",

    "selecao": """APOIO 18 – FLUXOGRAMA PRISMA E CARACTERÍSTICAS
- Fluxograma da Figura 1 do manuscrito; não recuperados e excluídos no Anexo C.
- A busca por citação (443 referências) trouxe 4 relatórios, que entram em "Buscados na íntegra" (28 + 4 = 32).
- Entre os 7 estudos das metanálises, só Mohd Fikri Rosely e Titi Rahmawati (2019) usaram amostragem aleatória; nenhum estudo com preocupação baixa de viés.""",

    "passos45": """APOIO 19 – EXTRAÇÃO E RISCO DE VIÉS (JBI)
- Listas JBI por função do estudo: prevalência (9 itens), transversal analítico (8), coorte (11).
- Julgamento global qualitativo pelos domínios críticos (amostragem, tamanho, validade da mensuração, taxa de resposta); "não" pesa mais que "incerto". Todos os estudos foram mantidos e a classificação alimentou o GRADE.
- Por que JBI: tem lista específica para prevalência, alinhada ao CoCoPop; Newcastle-Ottawa não cobre prevalência e o ROBINS-E é para efeito comparativo de exposição.""",

    "passo6": """APOIO 20 – METANÁLISE PASSO A PASSO E ROBUSTEZ
- Proporção → logito → efeitos aleatórios (Paule-Mandel) → Hartung-Knapp → retrotransformação, I² e intervalo de predição.
- Robustez: Freeman-Tukey (DerSimonian-Laird), GLMM logístico, leave-one-out, Baujat, subgrupo por país, sem o resumo de congresso e só definições específicas.
- Analogia: efeitos fixos = todos medem a mesma coisa com ruído; efeitos aleatórios = cada estudo tem a sua prevalência, e queremos a média e a dispersão delas.""",

    "passo7": """APOIO 21 – GRADE
- Ponto de partida baixa (observacional); um domínio grave já leva a muito baixa. Começar em alta não mudaria a certeza final.
- Evidência indireta não rebaixada nos sintomas (o sintoma é o próprio desfecho); rebaixada nos objetivos (coexposições, desfechos substitutos).
- Sem dupla contagem: intervalo de predição em inconsistência; IC95% em imprecisão.""",

    "respiratorio": """APOIO 22 – TABELA DE ROBUSTEZ E SUBGRUPO POR PAÍS
- Subgrupo ocular: Turquia 50,5% (k = 3; I² 57%); Malásia 19,8% (k = 2; I² 0%); Brasil 43,2% (k = 1); p < 0,001, mas exploratório (poucos estudos e um resumo de congresso na Malásia).
- Baujat: no ocular, Mohd Fikri Rosely 2022 é o mais influente; o I² ocular segue alto sem ele (89%) ou sem Bieniek (94%).""",

    "objetivos_bio": """APOIO 23 – DESFECHOS OBJETIVOS EM DETALHE
- Cada desfecho vem de um único estudo; comparações não combinadas (desenhos e desfechos heterogêneos).
- Cautelas: VEF1/CVF ≈ 91% nos dois grupos e PFE depende do esforço; t,t-mucônico inespecífico; metaplasia é resposta inespecífica a irritantes; DNA de HPV ≠ infecção ou doença.""",

    "limitacoes": """APOIO 24 – PONTOS FORTES E LIMITAÇÕES
- Fortes: busca ampla, protocolo registrado, PRISMA 2020, JBI, intervalo de predição, 3 modelos concordantes, GRADE por desfecho, OSF.
- Limitações: transversais e autorrelato; sem grupo não exposto nos agrupamentos; trabalhador sadio; heterogeneidade; revisor único; 6 não recuperados; elegibilidade em 3 idiomas.""",
}
