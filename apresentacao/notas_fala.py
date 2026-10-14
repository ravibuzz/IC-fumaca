"""Notas do orador, slide a slide.

Cada nota tem duas partes:
  FALA  — o que dizer em voz alta, dimensionado para ~150 palavras/min no tempo do slide;
  APOIO — números, justificativas e respostas prontas; NÃO é para ler, só para consultar se perguntarem.
O cabeçalho "[m:ss–m:ss] TÍTULO (~N s · W palavras)" é preenchido por Deck.notes().
"""

NOTAS = {
    "capa": """CAPA
FALA:
Bom dia. Sou Theo Báccaro, aluno de Medicina da São Leopoldo Mandic, orientado pela Profa. Lisie Tocci Justo. Vou apresentar nossa revisão sistemática com metanálise de prevalência sobre os efeitos da fumaça cirúrgica na saúde da equipe do centro cirúrgico.

APOIO (não ler):
- Coautores: Luiz Henrique Ledesma Pereira e Dra. Mariana Matera Veras (LIM05, HC-FMUSP); cite-os se sobrar fôlego.
- Fale o título de forma natural, sem ler palavra por palavra. Respire e avance.""",

    "trajetoria": """TRAJETÓRIA
FALA:
Antes de começar, o caminho. Em julho de 2025 concluí o curso de revisão sistemática e metanálise da Unicamp, com distinção, e um de escrita científica; registrei o protocolo no PROSPERO e li, um a um, 10.910 títulos e resumos.

APOIO (não ler):
- Cursos: Revisão Sistemática e Metanálise (Unicamp, via Coursera), 40 h, com distinção (20/07/2025); Escrita Científica: Produção de Artigos de Alto Impacto (ZucoEscrita), 3,6 h (31/07/2025); Fiocruz: ABNT, 3 h (11/03/2026) e referências, 2 h (25/03/2026). Total ≈ 49 h.
- Capas (falam por si; não precisa citar): Diretrizes Metodológicas do Ministério da Saúde (estudos observacionais; Sistema GRADE) e os checklists do JBI usados (prevalência, transversal analítico, coorte).
- Busca final em 09/07/2026; triagem entre julho e agosto de 2026; depois extração, JBI, metanálise em Python, GRADE e manuscrito.
- A animação monta o slide sozinha (~3 s): comece a falar sem esperar. Não leia as legendas.""",

    "introducao": """INTRODUÇÃO
FALA:
Fumaça cirúrgica é o subproduto da destruição térmica dos tecidos pelo eletrocautério, pelo laser e pelo bisturi ultrassônico. Ela contém hidrocarbonetos aromáticos, compostos orgânicos voláteis como o benzeno, material particulado fino e ultrafino e até material genético viral, como o HPV.
Quem trabalha no centro cirúrgico relata com frequência irritação ocular, tosse, irritação de mucosas e cefaleia. Os efeitos crônicos são plausíveis, mas sem relação causal estabelecida, e o tema é controverso. Enquanto isso, exaustão de fumaça e máscaras de alta filtração ainda são pouco adotadas, e as revisões anteriores eram descritivas. Por isso propusemos uma síntese em camadas: metanálise da prevalência dos sintomas e síntese narrativa, com GRADE, dos desfechos objetivos.

APOIO (não ler):
- PM2,5 = fração fina (diâmetro aerodinâmico < 2,5 µm); ultrafina = < 0,1 µm. O manuscrito cita as duas.
- Controvérsia: Hurst; Stewart (2024) argumentam que o risco pode estar superestimado; Benaim; Jaspers (2024) revisam composição e mitigação.
- "Por que mais uma revisão?": as revisões que encontramos (Mowbray et al., 2013; Dixon; Dasgupta; Vasdev, 2023) não fizeram síntese quantitativa; aqui há estimativa combinada com intervalo de predição, subgrupo por país e GRADE.""",

    "objetivos": """OBJETIVOS
FALA:
O objetivo foi avaliar os desfechos de saúde da exposição ocupacional à fumaça cirúrgica, com ênfase na prevalência de sintomas, nos desfechos objetivos e nos biomarcadores. A pergunta seguiu o PECO e, para a prevalência, o CoCoPop, recomendado pelo JBI. Um alerta desde já: a metanálise de proporções estima frequência em expostos, não efeito causal.

APOIO (não ler):
- PECO e não PICO: é exposição, não intervenção alocada.
- O (desfecho) no protocolo = efeitos à saúde relacionados à exposição; os que apareceram foram sintomas, espirometria, biomarcadores urinários, mucosa nasal e HPV-DNA.
- CoCoPop = Condição, Contexto, População (Munn et al., 2015).
- Específicos: ocular como desfecho principal e respiratório exploratório; síntese narrativa dos desfechos objetivos; GRADE por desfecho.""",

    "mapa": """METODOLOGIA – MAPA
FALA:
O método é a parte de que mais me orgulho, e vou apresentá-lo como um passo a passo em sete etapas, seguindo o relato PRISMA 2020: protocolo, busca, seleção, extração, risco de viés, síntese e certeza da evidência. Usei Zotero, Rayyan, OpenAlex e análise em Python. Um assistente de IA teve só apoio operacional; elegibilidade, extração e interpretação foram decisões humanas, e o código está aberto no OSF.

APOIO (não ler):
- Protocolo no PROSPERO (CRD420251238727), registrado antes da extração; dispensa do CEP (protocolo 2025/0743; Res. CNS 510/2016).
- IA (julho–agosto de 2026): priorização da ordem de leitura, leitura assistida de resumos e organização do fluxo; nada gerado por IA entrou sem verificação humana. Declarada conforme a Portaria CNPq nº 2.664/2026.
- Ferramentas: Zotero 6 (referências), Rayyan (deduplicação e triagem), OpenAlex (metadados e citações), Python 3.13 com NumPy, SciPy e statsmodels.
- Não detalhe nada aqui: é só o mapa. As colunas aparecem sozinhas, uma a uma.""",

    "passos12": """PASSOS 1 E 2
FALA:
Incluímos estudos observacionais com profissionais de centro cirúrgico expostos à fumaça, com qualquer efeito à saúde ou marcador de exposição, em português, inglês ou espanhol, sem limite de data. Resumos de congresso só entraram com eventos e denominador extraíveis, numa decisão posterior ao registro e declarada. A busca foi feita para máxima sensibilidade: dois blocos, população e exposição, sem filtro de idioma ou data, em sete bases, literatura cinzenta e busca por citação. Foram 16.757 registros, mais 443 referências por citação.

APOIO (não ler):
- Exclusões: in vitro ou animais; fora do centro cirúrgico; desfecho só no paciente; só medição do ar; revisões, editoriais e cartas; exposição não atribuível à fumaça (gases, radiação).
- PubMed e Embase, juntos, trouxeram mais da metade dos registros (cerca de 55%).
- Cochrane CENTRAL = 0: indexa ensaios clínicos, e só incluímos observacionais; era esperado.
- Sem bloco de desfecho porque os desfechos eram heterogêneos (sintomas, espirometria, HPV...): um bloco de desfecho reduziria a sensibilidade.
- Literatura cinzenta: Google Scholar (4 × 50 resultados) e Catálogo CAPES. A busca não tem filtro de idioma, mas a elegibilidade é restrita a pt/en/es (limitação declarada).""",

    "passo3": """PASSO 3 – SELEÇÃO
FALA:
Os registros foram para o Rayyan, que removeu 5.839 duplicatas. Li título e resumo dos 10.910 registros únicos; um script e a IA ordenaram a fila e apoiaram a leitura, mas cada decisão foi minha. Trinta e dois relatórios foram buscados na íntegra, seis não foram recuperados, 26 foram avaliados e 22 incluídos. Um cuidado importante: sete publicações do mesmo grupo brasileiro tinham amostras sobrepostas, e cada análise usou um único representante, para não contar a mesma amostra duas vezes.

APOIO (não ler):
- Fluxo: 16.757 identificados → 16.749 importados (8 não exportados) → 5.839 duplicatas (DOI, PMID e similaridade de título) → 10.910 triados → 10.882 excluídos → 28 + 4 por citação = 32 buscados → 6 não recuperados → 26 avaliados → 4 excluídos (1 resumo sem dados; 3 por população ou contexto) → 22 incluídos.
- Representante do cluster (Paraná): Bieniek et al., 2022, definido antes da síntese.
- Os 6 não recuperados incluem 2 inquéritos de sintomas e 1 estudo de olho seco; tentativas: acesso institucional, repositórios, páginas dos autores, comutação e contato com autores.
- HONESTIDADE: triagem por revisor único, declarada como limitação. O PRISMA 2020 é guia de RELATO; a seleção em duplicata é recomendação METODOLÓGICA (JBI, Cochrane, Diretrizes do MS). A replicação em duplicata está nas perspectivas.""",

    "passos45": """PASSOS 4 E 5
FALA:
A extração usou planilha padronizada: desenho, população, dispositivo, comparador, definição do desfecho e, para a metanálise, eventos e denominador; por exemplo, 33 de 81 profissionais com lacrimejamento no İlçe 2017. O risco de viés usou as ferramentas do JBI, escolhidas pela função de cada estudo. No semáforo, nenhum estudo teve preocupação baixa, sobretudo por amostragem não probabilística, taxa de resposta não relatada e autorrelato.

APOIO (não ler):
- Listas JBI: prevalência (9 itens; os 7 estudos das metanálises), transversal analítico (8; comparativos e objetivos), coorte (11; 3 coortes).
- Julgamento global qualitativo pelos domínios críticos (amostragem, tamanho, validade da mensuração, taxa de resposta); "não" pesa mais que "incerto". Todos os estudos foram mantidos e a classificação alimentou o GRADE.
- Por que JBI e não Newcastle-Ottawa ou ROBINS-E: o JBI tem lista específica para prevalência, alinhada ao CoCoPop; NOS não cobre prevalência e ROBINS-E é para efeito de exposição comparativa.
- Mohd Fikri Rosely 2022 é resumo de congresso: itens incertos e preocupação alta.""",

    "passo6": """PASSO 6 – METANÁLISE ← o coração da apresentação
FALA:
A metanálise, em cinco passos. Um: cada estudo vira uma proporção, eventos sobre n. Dois: a transformação logito leva essa proporção para uma escala sem limites, mais próxima da normal, e garante resultados entre 0 e 100%. Três: modelo de efeitos aleatórios, porque a prevalência verdadeira varia entre hospitais e países; a variância entre estudos, o tau-quadrado, foi estimada por Paule-Mandel. Quatro: o ajuste de Hartung-Knapp torna o intervalo de confiança mais honesto com poucos estudos. Cinco: voltamos para porcentagem e relatamos o I² e o intervalo de predição, a faixa esperada para um novo estudo. A robustez foi testada com mais dois modelos, leave-one-out, Baujat e subgrupo por país.

APOIO (não ler):
- Peso de cada estudo = 1 ÷ (variância do estudo + τ²). IC95% individual pelo método de Wilson. Sem 0% ou 100%: não precisou de correção de continuidade.
- Hartung-Knapp: IC pela distribuição t com k − 1 graus de liberdade (IntHout; Ioannidis; Borm, 2014).
- Sem teste de Egger nem funil por erro-padrão: em proporções o erro-padrão depende da própria proporção (assimetria espúria) e os testes exigem ≥ 10 estudos. Há uma dispersão prevalência × tamanho amostral (Anexo G3, ocular), sem teste formal.
- Paule-Mandel: o DerSimonian-Laird tende a subestimar τ² quando a heterogeneidade é alta; com k = 6–7 todo estimador de τ² é impreciso. Sem metarregressão: poucos estudos por covariável. RR dos desfechos objetivos na escala log (Wald).
- Analogia: efeitos fixos = todos medem a mesma coisa com ruído; efeitos aleatórios = cada estudo tem a sua prevalência, e queremos a média e a dispersão delas.
- Os cinco cards aparecem sozinhos enquanto você fala.""",

    "passo7": """PASSO 7 – GRADE
FALA:
Por fim, a certeza da evidência pelo GRADE, em cinco domínios. Partimos de certeza baixa, por ser evidência observacional, e um domínio grave já leva a muito baixa. Dois cuidados: a evidência indireta não foi rebaixada nos sintomas, porque o sintoma relatado é o próprio desfecho, mas foi rebaixada nos desfechos objetivos, por coexposições e desfechos substitutos; e evitamos dupla contagem entre inconsistência e imprecisão.

APOIO (não ler):
- Intervalo de predição entra em inconsistência; amplitude do IC95% entra em imprecisão.
- "Se começasse em alta, mudaria?": não. Inconsistência muito grave + risco de viés grave + imprecisão grave levariam igualmente a muito baixa.
- Desfechos com um único estudo: inconsistência não aplicável; viés de publicação não avaliável.
- Decisões posteriores ao registro, todas declaradas: ocular principal e respiratório exploratório; modelo logito + Hartung-Knapp; uma publicação por desfecho no cluster; resumos de congresso com dados suficientes; regra do sintoma-índice e sensibilidade por definição.""",

    "selecao": """RESULTADOS – SELEÇÃO E CARACTERÍSTICAS
FALA:
Este é o fluxograma PRISMA. Ficaram 22 relatórios de nove países, 19 transversais e três coortes. Depois do controle de sobreposição, seis amostras, com 756 profissionais, entraram na metanálise ocular e sete, com 1.428, na respiratória. Nenhum estudo teve preocupação baixa com viés.

APOIO (não ler):
- Coortes prospectivas: Navarro 2016; Stanganelli 2019; Stanganelli Caus 2025.
- Só Mohd Fikri Rosely e Titi Rahmawati (2019) usaram amostragem aleatória estratificada.
- A busca por citação (443 referências) trouxe 4 relatórios, que entram em "Buscados na íntegra" (28 + 4 = 32).
- Países: Turquia, Malásia, Brasil, Paquistão, China, México, EUA, Sudão e Tailândia.""",

    "ocular": """RESULTADO PRINCIPAL – OCULAR ← dê tempo a este slide
FALA:
Este é o resultado principal: 37,6% de prevalência combinada de sintoma ocular, com intervalo de confiança de 21,9 a 56,5%, em seis amostras e 756 profissionais. Cada quadrado é um estudo e o losango, a estimativa combinada; a linha vermelha mais longa é o intervalo de predição, de 7 a 83%, a mensagem honesta do trabalho: com I² de 93%, os estudos vão de 19% na Malásia a 56% na Turquia. Então 37,6% é o centro de uma distribuição ampla, não "a" prevalência, e descreve a carga de sintomas, não um excesso atribuível.

APOIO (não ler):
- Tamanho do quadrado ∝ peso; linha preta = IC95% de Wilson. Não há grupo não exposto no agrupamento: é a proporção que relatou o sintoma.
- Na escala logito, a estimativa retrotransformada é o centro (mediana) da distribuição das prevalências verdadeiras, não a média aritmética.
- O maior inquérito (Van Giersbergen et al., 2019; n = 672) ficou fora do ocular por não ter numerador e denominador oculares extraíveis.
- "I² de 93% não invalida a metanálise?": em prevalência, I² alto é a regra (Barker et al., 2021); por isso relatamos o intervalo de predição e investigamos as fontes (país, definição) em vez de esconder a heterogeneidade num único número.
- Definições: lacrimejamento, irritação ocular ou escala do sistema ocular; o período de recordatório não é homogêneo entre estudos.""",

    "respiratorio": """RESPIRATÓRIO E ROBUSTEZ ← aponte a tabela, não leia linha por linha
FALA:
O desfecho respiratório, exploratório, deu 41,7%, com intervalo de predição de 15 a 74%. A tabela diz uma coisa só: trocar o modelo, retirar um estudo ou o resumo de congresso não muda a leitura. E, com definições específicas, o I² respiratório cai de 91 para 61%.

APOIO (não ler):
- Tabela: logito-HK 37,6/41,7; Freeman-Tukey 38,1/41,7; GLMM 37,5/42,0; leave-one-out 34,3–42,1 e 38,9–45,5; sem resumo de congresso 42,1 (I² 89%) e 42,4 (I² 90%); definições específicas 36,5 (I² 94%) e 35,8 (I² 61%).
- O mínimo respiratório do leave-one-out (38,9%) é sem Van Giersbergen 2019, a definição mais divergente.
- Subgrupo ocular: Turquia 50,5% (k = 3; n = 268; I² 57%); Malásia 19,8% (k = 2; n = 333; I² 0%); p < 0,001 entre subgrupos, mas exploratório (poucos estudos e um resumo na Malásia).
- Baujat: Mohd Fikri Rosely 2022 é o estudo mais influente; mesmo assim o I² ocular segue alto sem o resumo (89%) ou sem Bieniek (94%).""",

    "objetivos_bio": """DESFECHOS OBJETIVOS E GRADE
FALA:
Além dos sintomas, quatro estudos, um por desfecho, trouxeram medidas objetivas, todas na mesma direção. No Sudão, espirometria com valores menores nos expostos e gradiente pelo tempo de atuação. No Brasil, metabólitos urinários de benzeno e xileno e malondialdeído bem mais altos. No México, metaplasia nasal em 70% contra 5%, risco relativo de 13,9. Na China, DNA de HPV na mucosa nasal em 9% contra 1,7%, risco relativo de 5,2. A certeza foi muito baixa em todos, e nenhum estudo elegível avaliou câncer ou DPOC: isso é vazio de evidência, não ausência de risco.

APOIO (não ler):
- Ibrahim 2025 (92 vs 92 pareados): VEF1 2,78 vs 3,14 L; CVF 3,02 vs 3,45 L; PFE 327,5 vs 483,5 L/min; p = 0,001; VEF1/CVF ≈ 91% nos dois grupos; PFE depende de esforço.
- Canicoba 2025: 52 expostos vs 49 controles para os metabólitos (três amostras do controle se perderam) e 52 vs 52 para o perfil oxidativo; t,t-mucônico 202,9 vs 46,1 µg/L; metil-hipúrico 468,2 vs 184,4 µg/L; malondialdeído 9,33 vs 3,22 nmol/mg; sem IC95%; t,t-mucônico é inespecífico (dieta, tabagismo).
- Navarro 2016: 16/23 vs 1/20; RR 13,9 (IC95% 2,0–95,8), IC amplo por haver 1 evento no grupo não exposto.
- Hu 2021: 42/469 vs 4/231; RR 5,2 (IC95% 1,9–14,2); DNA ≠ infecção ou doença; o achado da N95 (0/196) não tem ajuste.
- Para decorar: 37,6% ocular; 41,7% respiratório; RR 13,9 metaplasia; RR 5,2 HPV; 0 estudos elegíveis de câncer ou DPOC.""",

    "discussao": """DISCUSSÃO – INTERPRETAÇÃO
FALA:
Três leituras. Primeira: a carga de sintomas é alta e coerente com a literatura, agora com estimativa combinada e GRADE. Segunda: heterogeneidade acima de 90% é esperada em prevalência; a definição do sintoma explicou parte dela, e tempo de exposição, exaustão e EPI são fontes plausíveis, não testadas. Terceira: os desfechos objetivos são marcadores, não doença. E o achado talvez mais relevante é o que não foi encontrado: estudos elegíveis sobre câncer ou DPOC.

APOIO (não ler):
- Literatura prévia sem síntese quantitativa: Mowbray et al., 2013; Dixon; Dasgupta; Vasdev, 2023.
- "Qualquer sintoma": 55,6% (Mohd Fikri Rosely, 2022) e 73,2% (Van Giersbergen et al., 2019), síntese narrativa.
- A favor da causalidade: gradiente com o tempo de exposição, temporalidade (coorte), plausibilidade. Contra: um estudo por desfecho, IC amplos, coexposições (gases anestésicos, radiação).
- Relatos de caso de papilomatose laríngea e carcinoma orofaríngeo por HPV em cirurgiões (Hallmo; Naess, 1991; Rioux et al., 2013) reforçam a plausibilidade, mas não estimam risco.""",

    "limitacoes": """PONTOS FORTES E LIMITAÇÕES
FALA:
Os pontos fortes são a busca ampla, o protocolo registrado, a síntese com três modelos concordantes, o GRADE por desfecho e a reprodutibilidade no OSF. As limitações estão declaradas: estudos transversais com autorrelato, sem grupo não exposto nos agrupamentos, efeito do trabalhador sadio, heterogeneidade alta e revisor único. Elas não invalidam a síntese; delimitam o que a evidência permite afirmar.

APOIO (não ler):
- Viés de atribuição: o respondente sabe que o questionário é sobre fumaça.
- Trabalhador sadio: quem adoece tende a sair do centro cirúrgico, o que subestima a prevalência.
- Elegibilidade restrita a português, inglês e espanhol; periódicos de indexação limitada (análise restrita ao MEDLINE não foi factível); 6 relatórios não recuperados.
- ATITUDE: fale as limitações com segurança. A banca valoriza quem conhece as fraquezas do próprio trabalho.""",

    "conclusao": """CONCLUSÃO
FALA:
Concluindo: sintomas oculares e respiratórios são frequentes na equipe exposta, com grande variação entre contextos, e estudos isolados sugerem alterações além do incômodo agudo. Nenhum estudo elegível avaliou câncer ou DPOC, o que não é ausência de risco, e a certeza é muito baixa. Pela carga de sintomas e por precaução, proteger a equipe hoje é prudente: exaustão na fonte, respiradores e educação.

APOIO (não ler):
- Proteção (NIOSH, 1996): evacuação local na fonte é a medida principal; N95/PFF2 não substituem a exaustão; educação da equipe. A efetividade das medidas não foi avaliada nesta revisão.
- NR-32: marco geral de gestão de riscos em serviços de saúde, mas não trata especificamente da fumaça cirúrgica.""",

    "perspectivas": """PERSPECTIVAS FUTURAS
FALA:
Para o campo, faltam coortes com medida objetiva da exposição, definições padronizadas, desfechos crônicos e estudos de efetividade da proteção. Para este trabalho: submeter o manuscrito, atualizar a busca e replicar a triagem em duplicata.

APOIO (não ler):
- Também: devolutiva institucional (proposta de protocolo de proteção no centro cirúrgico) e vigilância dos 6 relatórios não recuperados.""",

    "referencias": """REFERÊNCIAS
FALA:
As referências completas e os suplementos estão no QR code.

APOIO (não ler):
- Não leia a lista; mencione e avance.
- O QR code leva ao projeto público do OSF (osf.io/jktmn): hoje, suplementos, código e planilhas. As legendas dizem isso.
- Se você publicar o PDF do manuscrito no OSF (confira antes a política de preprint da revista escolhida), as legendas podem passar a citar o manuscrito: é uma troca de uma linha no gerador (MANUSCRITO_NO_OSF = True).""",

    "agradecimentos": """AGRADECIMENTOS
FALA:
Agradeço à Profa. Lisie, aos coautores Luiz Henrique e Dra. Mariana, e à São Leopoldo Mandic e ao PIC. Obrigado; estou à disposição para perguntas.

APOIO (não ler):
- PROSPERO CRD420251238727 · OSF osf.io/jktmn · sem financiamento · sem conflitos de interesse.
- Ao dizer "perguntas", AVANCE para o slide 21 (QR code grande do OSF) e deixe-o na tela durante a arguição.""",

    "encerramento": """ENCERRAMENTO
Deixe este slide na tela durante as perguntas: o QR code leva ao projeto do OSF. Ouça a pergunta inteira, repita-a em uma frase ("a pergunta é sobre…") e responda em 30 a 40 segundos. Se não souber, diga o que o estudo permite afirmar e o que seria necessário para responder.""",
}
