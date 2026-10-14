# Roteiro de fala, slide a slide (notas do orador)

Tempo-alvo total: ~9 min 20 s, deixando folga para os 10 minutos. Os colchetes indicam o relógio acumulado.

## Slide 1 — Capa

[0:00–0:15] CAPA (~15 s)
Bom dia a todos. Meu nome é Theo Báccaro, sou aluno de Medicina da São Leopoldo Mandic de Araras. Vou apresentar a Iniciação Científica que desenvolvi ao longo de um ano, sob orientação da Profa. Lisie Tocci Justo, com a colaboração do Luiz Henrique Ledesma Pereira e da Dra. Mariana Matera Veras, do LIM05 da USP.
O trabalho é uma revisão sistemática com metanálise de prevalência sobre os efeitos à saúde da exposição ocupacional à fumaça cirúrgica na equipe de centro cirúrgico.

DICA: fale o título de forma natural, sem ler palavra por palavra. Respire e vá para o próximo slide.

## Slide 2 — TRAJETÓRIA: Um ano de preparação: formação, protocolo, leitura de 10.910 registros e análise

[0:15–0:35] TRAJETÓRIA (~20 s)
Antes do conteúdo, um ano de trabalho em uma imagem. Em julho de 2025 fiz o curso de Revisão Sistemática e Metanálise da Unicamp, 40 horas, concluído com distinção, e um curso de escrita científica. Estudei as Diretrizes Metodológicas do Ministério da Saúde e as ferramentas de risco de viés do JBI, registrei o protocolo no PROSPERO e obtive a dispensa do CEP. Em março de 2026 fiz os cursos de normalização da Fiocruz. Em julho rodei a busca final nas sete bases e li, um a um, 10.910 títulos e resumos; depois vieram a extração, o risco de viés, a metanálise em Python, o GRADE e o manuscrito.

DICA: este slide é contexto; não leia as legendas. Aponte a linha do tempo e siga. A animação monta o slide sozinha (cerca de 3 s).

## Slide 3 — INTRODUÇÃO: Fumaça cirúrgica: o que é e por que importa

[0:35–1:20] INTRODUÇÃO (~45 s)
Fumaça cirúrgica é o subproduto da destruição térmica dos tecidos pelo eletrocautério, pelo laser e pelo bisturi ultrassônico. Ela não é só "fumaça": contém hidrocarbonetos aromáticos policíclicos, compostos orgânicos voláteis como benzeno, tolueno e xileno, material particulado fino, o PM2,5, e partículas ultrafinas, que chegam às vias aéreas inferiores, e até material genético viral, como o HPV.
(Se perguntarem: PM2,5 é a fração fina, com diâmetro aerodinâmico abaixo de 2,5 µm; "ultrafina" é abaixo de 0,1 µm. O manuscrito cita as duas.)
Quem trabalha no centro cirúrgico relata com frequência irritação ocular, tosse, irritação de mucosas, cefaleia e náusea. O que não sabemos é o efeito de longo prazo: há plausibilidade biológica para câncer e doença respiratória, mas a relação causal nunca foi estabelecida, e revisões recentes chegam a dizer que o risco pode estar superestimado.
Enquanto isso, exaustão de fumaça e máscaras de alta filtração ainda são pouco adotadas. E a literatura prévia era descritiva, sem metanálise. Por isso desenhamos uma síntese em camadas: metanálise de prevalência dos sintomas e síntese narrativa, com GRADE, dos desfechos objetivos.

PONTO-CHAVE: a palavra "controvérsia" justifica a revisão. Se a banca perguntar "por que mais uma revisão?", a resposta é: nenhuma anterior quantificou a prevalência com intervalo de predição e GRADE.

## Slide 4 — OBJETIVOS: Pergunta estruturada: PECO para os desfechos comparativos e CoCoPop para a prevalência

[1:20–1:45] OBJETIVOS (~25 s)
O objetivo foi avaliar os desfechos de saúde associados à exposição ocupacional à fumaça cirúrgica na equipe de centro cirúrgico, com ênfase em três coisas: prevalência de sintomas, desfechos objetivos e biomarcadores.
A pergunta foi estruturada em PECO: população é a equipe de centro cirúrgico; exposição é a fumaça dos dispositivos de energia; comparador são os não expostos ou protegidos; desfecho são os efeitos à saúde. Para a parte de prevalência usamos o esquema CoCoPop, condição, contexto e população, que é o recomendado pelo JBI para metanálises de proporção.
Um ponto que gosto de deixar claro desde o início: metanálise de proporção estima frequência, não efeito causal. Isso vai ser importante na hora de interpretar.

SE PERGUNTAREM "por que PECO e não PICO?": porque é exposição, não intervenção; não houve alocação de intervenção.

## Slide 5 — METODOLOGIA: Mapa da revisão: 7 passos, do protocolo à certeza da evidência (PRISMA 2020)

[1:45–2:15] METODOLOGIA – MAPA (~30 s)
A parte que mais me orgulho é o método, então vou apresentá-lo como um passo a passo, do jeito que o PRISMA 2020 recomenda. São sete passos.
Um: a pergunta e o protocolo, registrado no PROSPERO antes da extração de dados, e a dispensa do Comitê de Ética, por ser revisão de literatura. Dois: a busca em sete bases, mais literatura cinzenta e busca por citação. Três: a seleção, com deduplicação, triagem e leitura na íntegra. Quatro: a extração padronizada. Cinco: o risco de viés com as ferramentas do JBI. Seis: a síntese, que é a metanálise de proporções. Sete: a certeza da evidência pelo GRADE.
Tudo foi feito com ferramentas abertas: Zotero, Rayyan, OpenAlex e análise em Python. Um assistente de IA teve função só operacional: ajudou a priorizar a ordem de leitura na triagem, na leitura assistida de resumos e na organização do fluxo de trabalho. Toda decisão de elegibilidade, a extração, a interpretação e a redação foram minhas, e nada gerado por IA entrou sem verificação humana; isso está declarado conforme a Portaria do CNPq. O código e as planilhas estão públicos no OSF.

DICA: não detalhe nada aqui; é só o mapa. Os próximos cinco slides percorrem os passos. As colunas aparecem sozinhas, uma a uma.

## Slide 6 — METODOLOGIA: Passos 1 e 2 · Critérios de elegibilidade e busca de alta sensibilidade

[2:15–2:50] PASSOS 1 E 2 (~35 s)
Os critérios de elegibilidade foram definidos no protocolo, e os ajustes feitos depois do registro estão declarados no manuscrito. Incluímos estudos observacionais primários com profissionais de centro cirúrgico expostos, com qualquer efeito à saúde ou marcador de exposição como desfecho, em português, inglês ou espanhol, sem restrição de data. Resumos de congresso só entraram quando traziam população, cenário, definição do desfecho, eventos e denominador; essa admissão foi uma decisão posterior ao registro, declarada, e esses resumos receberam preocupação alta com viés e análise de sensibilidade. Excluímos estudos em animais, populações fora do centro cirúrgico, desfechos só no paciente, medições de ar sem desfecho humano e exposições não atribuíveis à fumaça.
A busca foi desenhada para sensibilidade máxima: dois blocos, população e exposição, sem bloco de desfecho, sem filtro de idioma nem de data. Rodamos em sete bases, mais literatura cinzenta e busca por citação automatizada no OpenAlex. Resultado: 16.757 registros, mais 443 referências rastreadas por citação. PubMed e Embase trouxeram quase metade.

SE PERGUNTAREM por que a Cochrane CENTRAL deu zero: ela indexa ensaios clínicos e a revisão só incluiu observacionais; era esperado.
SE PERGUNTAREM por que sem bloco de desfecho: porque os desfechos eram heterogêneos (sintomas, espirometria, HPV...) e um bloco de desfecho reduziria a sensibilidade.

## Slide 7 — METODOLOGIA: Passo 3 · Seleção dos estudos: do registro bruto ao relatório incluído

[2:50–3:25] PASSO 3 – SELEÇÃO (~35 s)
Da esquerda para a direita: 16.757 registros entraram no Zotero e foram importados no Rayyan, que removeu 5.839 duplicatas por DOI, PMID e similaridade de título. Sobraram 10.910 registros únicos, e eu li o título e o resumo de todos eles. Um script em Python com regras por palavras-chave e um assistente de IA tiveram papel operacional: reordenaram a fila de leitura, apoiaram a leitura assistida de resumos e a organização do fluxo. Quem decidia a elegibilidade era eu, com os critérios.
Vinte e oito foram para texto completo, mais quatro vindos da busca por citação, total de 32; seis não foram recuperados apesar de tentativas por acesso institucional e contato com autores; 26 foram avaliados na íntegra e 22 incluídos.
Um cuidado importante: sete publicações vêm do mesmo grupo brasileiro, com amostras sobrepostas. Para não contar ninguém duas vezes, cada agrupamento recebeu só um representante desse cluster, o Bieniek 2022, que era o relato mais completo.

HONESTIDADE METODOLÓGICA: a triagem foi feita por um único revisor. Isso está declarado como limitação. Cuidado com a terminologia: o PRISMA 2020 é um guia de RELATO (diz o que deve constar no texto); a seleção independente por dois revisores é uma recomendação METODOLÓGICA importante (manuais do JBI e da Cochrane; Diretrizes do MS). Se perguntarem, diga que as decisões foram registradas com justificativa e que a replicação em duplicata está nas perspectivas.

## Slide 8 — METODOLOGIA: Passos 4 e 5 · Extração padronizada e avaliação do risco de viés (JBI)

[3:25–3:55] PASSOS 4 E 5 (~30 s)
A extração foi feita em planilha padronizada: identificação, desenho, população, dispositivo gerador, comparador, instrumento e definição do desfecho, taxa de resposta e, para a metanálise, o número de eventos e o denominador de cada estudo. Por exemplo, no İlçe 2017, 33 de 81 profissionais relataram lacrimejamento.
O risco de viés foi avaliado com as ferramentas do Joanna Briggs Institute, escolhidas pela função de cada estudo: a lista de prevalência, com nove itens, para os sete estudos das metanálises; a de transversal analítico para os comparativos; e a de coorte para os três longitudinais. O julgamento global foi qualitativo, guiado pelos domínios críticos: amostragem, tamanho amostral, validade da mensuração e taxa de resposta.
O semáforo resume: a preocupação foi moderada ou alta em todos, principalmente por amostragem não probabilística, taxa de resposta não relatada e desfecho autorrelatado. Nenhum estudo teve preocupação baixa, e isso vai pesar no GRADE.

SE PERGUNTAREM por que JBI e não Newcastle-Ottawa ou ROBINS-E: o JBI tem lista específica para estudos de prevalência, alinhada ao CoCoPop; NOS não cobre prevalência e ROBINS-E é para exposição comparativa.

## Slide 9 — METODOLOGIA: Passo 6 · Metanálise de prevalência explicada: de 7 proporções a uma estimativa combinada

[3:55–4:45] PASSO 6 – METANÁLISE (~50 s)  ← o coração da apresentação
Vou explicar a metanálise em cinco passos. Primeiro, cada estudo vira uma proporção: eventos dividido pelo n. Segundo, aplicamos a transformação logito, o logaritmo da chance: isso tira a proporção da escala de zero a um, aproxima da distribuição normal e garante que a estimativa combinada e os intervalos fiquem entre 0 e 100%. Terceiro, usamos modelo de efeitos aleatórios, porque não faz sentido supor uma única prevalência verdadeira em hospitais da Turquia, da Malásia e do Brasil; a variância entre estudos, o tau-quadrado, foi estimada por Paule-Mandel. Quarto, o intervalo de confiança da estimativa combinada recebeu o ajuste de Hartung-Knapp, que usa a distribuição t e é mais honesto quando há poucos estudos e muita heterogeneidade. Quinto, voltamos para porcentagem e reportamos o I² e o intervalo de predição, que diz onde cairia a prevalência de um novo estudo.
Para testar a robustez, repetimos tudo com a transformação de Freeman-Tukey e com um modelo logístico misto, fizemos leave-one-out, gráfico de Baujat e subgrupo por país.
Não fizemos gráfico de funil nem Egger, porque em proporções o erro-padrão depende da própria proporção, o que cria assimetria falsa, e seriam necessários dez estudos.

ANALOGIA se precisar: efeitos fixos = "todos os estudos medem a mesma coisa com ruído"; efeitos aleatórios = "cada estudo mede a sua prevalência, e queremos a média dessas prevalências e a dispersão delas".
Os cinco cards aparecem sozinhos, um a um, enquanto você fala.

## Slide 10 — METODOLOGIA: Passo 7 · Certeza da evidência: GRADE adaptado a desfechos de prevalência

[4:45–5:15] PASSO 7 – GRADE (~30 s)
O último passo foi graduar a certeza da evidência pelo GRADE, nos cinco domínios: risco de viés, inconsistência, evidência indireta, imprecisão e viés de publicação. Como não existe adaptação universal do GRADE para prevalência, explicitamos os critérios em cada domínio.
Partimos de certeza baixa, por ser evidência observacional, e qualquer domínio grave leva a muito baixa. Um detalhe que mostra cuidado: a evidência indireta não foi rebaixada nos sintomas, porque o sintoma autorrelatado é exatamente o desfecho da pergunta de frequência; já nos biomarcadores foi rebaixada, por coexposição e desfecho substituto. E evitamos dupla contagem: o intervalo de predição entrou em inconsistência, e a largura do IC em imprecisão.
À direita estão as decisões tomadas depois do registro no PROSPERO, todas declaradas no manuscrito.

SE PERGUNTAREM "se começasse em alta, mudaria?": não. Com inconsistência muito grave, risco de viés grave e imprecisão grave, a certeza cairia três níveis e chegaria igualmente a muito baixa.

## Slide 11 — RESULTADOS: Seleção (PRISMA 2020) e características dos 22 relatórios incluídos

[5:15–5:35] RESULTADOS – SELEÇÃO E CARACTERÍSTICAS (~20 s)
Este é o fluxograma PRISMA completo, que vocês já viram em números. Ficaram 22 relatórios de estudos observacionais, de nove países, a maioria transversal; três eram coortes prospectivas (Navarro 2016; Stanganelli 2019; Stanganelli Caus 2025).
Depois do controle de sobreposição, seis amostras independentes, com 756 profissionais, entraram na metanálise ocular, e sete amostras, com 1.428, na respiratória.
No risco de viés, a preocupação foi moderada a alta nos inquéritos de prevalência, e moderada nos estudos de desfechos objetivos. Nenhum estudo teve preocupação baixa; só Mohd Fikri Rosely e Titi Rahmawati (2019) usaram amostragem aleatória estratificada.

## Slide 12 — RESULTADOS: Desfecho principal · Prevalência combinada de sintoma ocular (irritação ou lacrimejamento)

[5:35–6:25] RESULTADO PRINCIPAL – OCULAR (~50 s)  ← dê tempo a este slide; é o que mais mostra análise crítica
Este é o resultado principal. A prevalência combinada de sintoma ocular, irritação ou lacrimejamento, foi de 37,6%, com intervalo de confiança de 21,9 a 56,5%. São seis amostras independentes, 756 profissionais.
No gráfico de floresta, cada quadrado é a prevalência de um estudo, com o tamanho proporcional ao peso; a linha preta é o intervalo de confiança de Wilson; o losango vermelho é a estimativa combinada e a linha vermelha mais longa é o intervalo de predição, de 7 a 83%.
Essa linha longa é a mensagem honesta do trabalho. A heterogeneidade é de 93%, os estudos vão de 19% na Malásia a 56% na Turquia, e um novo estudo, em outro hospital, poderia encontrar quase qualquer valor. Por isso eu não apresento o 37,6% como "a prevalência", e sim como a média de uma distribuição ampla, que o intervalo de predição descreve melhor do que o intervalo de confiança.
Dois cuidados de interpretação: isto é a proporção de profissionais que relataram o sintoma e o atribuíram à fumaça, conforme a definição de cada estudo, não uma prevalência com período de recordatório homogêneo; e não há grupo não exposto no agrupamento, então o número descreve a carga de sintomas, não um excesso atribuível.
(O maior inquérito, Van Giersbergen 2019, n = 672, ficou fora do agrupamento ocular por não reportar numerador e denominador extraíveis.)

SE PERGUNTAREM "I² de 93% não invalida a metanálise?": em prevalência, I² alto é a regra, não a exceção (Barker et al., 2021). Por isso reportamos o intervalo de predição e investigamos as fontes (país, definição), em vez de esconder a heterogeneidade num único número.

## Slide 13 — RESULTADOS: Desfecho exploratório · Sintoma respiratório ou de vias aéreas, e robustez das estimativas

[6:25–6:50] RESPIRATÓRIO E ROBUSTEZ (~25 s)  ← aponte a tabela, não leia linha por linha
O desfecho respiratório, tratado como exploratório porque as definições variam muito, deu 41,7%, com intervalo de predição de 15 a 74%, em sete amostras e 1.428 profissionais.
A tabela resume a robustez, e a mensagem é uma só: três modelos diferentes, retirar um estudo por vez ou excluir o resumo de congresso não mudam a leitura. O achado mais interessante é que, restringindo a definições específicas de sintoma respiratório, o I² cai de 91 para 61%: boa parte da heterogeneidade vem de como cada estudo definiu o sintoma.
Na análise por país, Turquia e Malásia diferem bastante, mas com dois ou três estudos por país isso é hipótese, não conclusão.

SE PEDIREM DETALHE DA TABELA: logito-HK 37,6/41,7; Freeman-Tukey 38,1/41,7; GLMM 37,5/42,0; leave-one-out 34,3–42,1 e 38,9–45,5; sem resumo de congresso 42,1/42,4; definições específicas 36,5 (I² 94%)/35,8 (I² 61%). Subgrupo ocular: Turquia n = 268; Malásia n = 333. No gráfico de Baujat, Mohd Fikri Rosely 2022 é o estudo mais influente.

## Slide 14 — RESULTADOS: Desfechos objetivos e biomarcadores: sinais além do incômodo agudo (1 estudo por desfecho)

[6:50–7:30] DESFECHOS OBJETIVOS E GRADE (~40 s)
Além dos sintomas, quatro estudos, um por desfecho, trouxeram medidas objetivas, e todos apontam na mesma direção, desfavorável aos expostos.
Espirometria no Sudão: VEF1, CVF e pico de fluxo menores nos expostos, com gradiente pelo tempo de atuação; mas a relação VEF1/CVF foi normal e o pico de fluxo depende de esforço, então lemos com cautela. Biomarcadores urinários no Brasil: metabólitos de benzeno e xileno e malondialdeído muito mais altos nos expostos; note que os denominadores diferem: 52 expostos contra 49 controles para os metabólitos, porque três amostras do grupo controle se perderam, e 52 contra 52 para o perfil oxidativo. Biópsia nasal numa coorte mexicana de quatro anos: metaplasia em 70% dos expostos contra 5%, risco relativo de 13,9, com intervalo muito amplo. E DNA de HPV na mucosa nasal de ginecologistas chineses: 9% contra 1,7%, risco relativo de 5,2.
Pelo GRADE, a certeza foi muito baixa em todos os desfechos. E talvez o achado mais importante seja o que não encontramos: nenhum estudo avaliou diretamente câncer ou DPOC na equipe cirúrgica. Isso é um vazio de evidência, não evidência de ausência de risco.

NÚMEROS para decorar: 37,6% ocular; 41,7% respiratório; RR 13,9 metaplasia; RR 5,2 HPV; 0 estudos de câncer/DPOC.

## Slide 15 — DISCUSSÃO: O que os achados significam e como interpretá-los com cautela

[7:30–8:00] DISCUSSÃO – INTERPRETAÇÃO (~30 s)
Três leituras. Primeira: a carga de sintomas é alta e coerente com a literatura; a novidade é ter uma estimativa combinada com intervalo de predição, subgrupo e GRADE. Segunda: a heterogeneidade acima de 90% é esperada em prevalência; em vez de escondê-la, mostramos o intervalo de predição e as fontes prováveis: definição do sintoma, composição da equipe, tempo de exposição e contexto, como exaustão e EPI. Terceira: os desfechos objetivos têm gradiente dose-resposta (espirometria e HPV), temporalidade e plausibilidade, mas são um estudo por desfecho, com intervalos amplos e coexposições. São marcadores, não doença.
E o achado mais relevante é o que não foi encontrado: nenhum estudo de câncer ou DPOC. A controvérsia sobre o risco real só se resolve com estudos longitudinais que ainda não existem.

## Slide 16 — DISCUSSÃO: Pontos fortes e limitações

[8:00–8:25] PONTOS FORTES E LIMITAÇÕES (~25 s)
Como pontos fortes: busca ampla e sem filtro de idioma, protocolo registrado, risco de viés padronizado, síntese com intervalo de predição e três modelos concordantes, GRADE por desfecho e tudo reprodutível no OSF.
As limitações estão todas declaradas. As principais: os estudos são transversais, com exposição por ocupação e sintomas autorrelatados, e o respondente sabia que o questionário era sobre fumaça; não há grupo não exposto nos agrupamentos, então não estimamos o excesso atribuível; existe o efeito do trabalhador sadio, que subestima a prevalência; a heterogeneidade é alta; e a triagem, a extração e o risco de viés foram feitos por um único revisor, sem duplicata.
Elas não invalidam a síntese: delimitam o que a evidência permite afirmar.

ATITUDE: fale as limitações com segurança. Banca valoriza quem conhece as fraquezas do próprio trabalho mais do que quem as esconde.

## Slide 17 — CONCLUSÃO: Síntese da mensagem da revisão

[8:25–8:50] CONCLUSÃO (~25 s)
Concluindo. O que se sabe: sintomas oculares e respiratórios são frequentes na equipe exposta, com grande variação entre contextos, e os desfechos objetivos sinalizam alterações além do incômodo agudo. O que não se sabe: não há evidência direta de câncer ou DPOC atribuíveis à fumaça, a certeza é muito baixa e as coexposições limitam a atribuição causal.
A implicação prática é clara: pelo princípio da precaução e pela carga de sintomas, a exaustão local na fonte, os respiradores N95 e a educação da equipe se justificam hoje. E medir o risco de longo prazo é tarefa de estudos longitudinais.

## Slide 18 — PERSPECTIVAS FUTURAS: Agenda de pesquisa e próximos passos deste trabalho

[8:50–9:05] PERSPECTIVAS FUTURAS (~15 s)
Para o campo, a agenda é clara: coortes com medição objetiva da exposição e controle de coexposições, definições padronizadas de sintoma, desfechos crônicos como câncer e DPOC, e estudos de efetividade da exaustão e das máscaras.
Para este trabalho: submeter o manuscrito, atualizar a busca, replicar a triagem em duplicata e levar uma proposta de proteção para o nosso centro cirúrgico.

## Slide 19 — REFERÊNCIAS BIBLIOGRÁFICAS: Principais referências metodológicas e dos estudos incluídos (lista completa no manuscrito)

[9:05–9:10] REFERÊNCIAS (~5 s)
Estas são as principais referências metodológicas e dos estudos incluídos; a lista completa está no manuscrito, e o QR code leva ao projeto público no OSF, com o manuscrito, os anexos e os suplementos. (Não leia; apenas mencione e avance.)

ANTES DO DIA: confira que o PDF do manuscrito está publicado no OSF (osf.io/jktmn); hoje o projeto tem o suplemento (zip) e as referências do banner.

## Slide 20 — AGRADECIMENTOS

[9:10–9:20] AGRADECIMENTOS (~10 s)
Agradeço à Profa. Lisie pela orientação, ao Luiz Henrique e à Dra. Mariana pela revisão crítica, e à Faculdade São Leopoldo Mandic e ao PIC pelo apoio. O protocolo está no PROSPERO e o manuscrito, os dados e o código estão no OSF. Obrigado. Estou à disposição para perguntas.

## Slide 21 — Encerramento

ENCERRAMENTO
Deixe este slide na tela durante as perguntas: o QR code leva ao manuscrito e aos suplementos no OSF. Respire, ouça a pergunta inteira, repita-a em uma frase ("a pergunta é sobre…") e responda em no máximo 30–40 segundos. Se não souber, diga o que o estudo permite afirmar e o que seria necessário para responder.
