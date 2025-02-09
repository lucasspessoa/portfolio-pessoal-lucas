import streamlit as st

# Configurações da Página
st.set_page_config(page_title="Portfólio: Lucas da Silva Pessoa", layout="centered")

# Navegação Simples com Sidebar
st.sidebar.title("Navegação")
page = st.sidebar.selectbox("Escolha uma seção", ["Currículo", "Projetos Realizados"])

# Seção 1: Currículo
if page == "Currículo":
    st.title("Lucas da Silva Pessoa")
    st.subheader("Analista de Dados | Estudante de Ciências Econômicas")
    st.markdown("""
        Olá! Eu sou o Lucas, tenho 23 anos e, nas horas vagas, sou fã em catalogar filmes de sucesso. Apaixonado por aprender, sempre estou em busca de aperfeiçoar minhas habilidades.

        Este é o meu portfólio! Nesta seção, você encontra informações pessoais/profissionais, contato e objetivos.

        Projetos e suas descrições você confere na seção Projetos Realizados, na barra de Navegação ao lado.
        """)

    # Links para redes sociais
    st.write("[LinkedIn](https://linkedin.com/in/01lucaspessoa) | [GitHub](https://github.com/lucasspessoa)")

    # Currículo
    st.header("Currículo")
    st.write("Aqui estão meus destaques profissionais:")
    st.markdown("""
    **Experiência**: Assistente Administrativo/Dados na GFT Promotora de Crédito Consignado.
    - Realizei pesquisas de mercado para identificar oportunidades e mapear a concorrência, contribuindo para estratégias de precificação eficazes;
    - Desenvolvi dashboards interativos que demonstraram potencial de crescimento médio de 5% na receita marginal da empresa; 
    - Utilizei SQL para consultas complexas, extraindo dados críticos para análises estratégicas de desempenho;
    - Uso avançado de Excel (tabelas dinâmicas, gráficos e fórmulas complexas) para armazenar e tabular dados e apoiar decisões comerciais;
    - Automatizei fluxos de trabalho repetitivos com Power Query que reduziram minha carga de banco de horas em mais de 50%;
    - Realizei apresentações frequentes para demonstrar os principais insights e apresentar oportunidades de melhora no Lucro da empresa.

    **Educação**: graduando em Ciências Econômicas na Universidade Federal do Ceará.
    
    **Habilidades Técnicas**: Data Analytics, Economics, Machine Learning, Power BI, Excel, SQL, Python e Power Query;

    **Habilidades Interpessoais**: Comunicação Didática; Colaboração para Melhoria Contínua, sem medo de ouvir opiniões negativas construtivas; Tranquilidade para Resolução de Problemas; Foco e Atenção em Resultados.
    """)

    # Opção para download do currículo
    with open("CVLucasPessoa.pdf", "rb") as pdf_file:
        pdf_data = pdf_file.read()
    st.download_button("Baixar Currículo", data=pdf_data, file_name="CVLucasPessoa.pdf")

    # Objetivos Profissionais
    st.header("Objetivos Profissionais")
    st.write("""
    Estou buscando oportunidades para:
    - Continuar aprimorando minhas habilidades em ferramentas como **Power BI**, **Excel**, **SQL** e **Python** com objetivo de crescer na área de dados;
    - Aprender novas ferramentas que possam ampliar meu horizonte de trabalho;
    - Trabalhar em projetos que envolva a **Área de Dados**/**Estatística** e **Automação de Processos**;
    - Contribuir para o desenvolvimento de estratégias baseadas em dados que impactem diretamente a tomada de decisão da empresa;
    - Previsão de dados para maior acertividade nas decisões de negócio.
    """)

    # Contato
    st.header("Entre em Contato")
    st.write("Se você quiser me contatar para colaborações ou oportunidades de trabalho, entre em contato via e-mail ou telefone.")
    st.write("""
    - **E-mail**: lucaspfc05@gmail.com
    - **Telefone**: (85) 99239-8429
    """)

# Seção 2: Projetos
elif page == "Projetos Realizados":
    st.header("Projetos")
    st.write("Aqui estão alguns dos projetos em que trabalhei:")

    # Projeto 1:
    if st.button("Análise Financeira do Negócio de Aluguel de DVDs - Netflix 1997"):
        st.markdown("""
        **1. Visão Geral dos Indicadores Financeiros**:
        
        - Lucro Total: \\$12,4 milhões  
        - Receita Total: \\$39 milhões  
        - Custo Total: \\$27 milhões
         
        Os valores indicam uma margem de lucro de aproximadamente 31,9\\%, o que é um desempenho sólido para o setor de aluguel de DVDs. No entanto, a distribuição dos custos e a performance de filmes individuais precisam ser analisadas para otimizar os resultados.
        
        **2. Análise da Evolução do Lucro Total por Ano e Mês**:
        
        O gráfico de Lucro Total ao longo do tempo mostra uma trajetória ascendente, com um crescimento mais acelerado nos últimos meses de 1998. Esse comportamento pode indicar uma expansão da base de clientes, aumento no volume de aluguéis ou melhorias na precificação dos filmes.

        Oportunidade de melhoria: Explorar ações promocionais, ao considerar campanhas para maximizar a receita em meses com menor crescimento.
                    
        **3. Receita e Custo Total por Filme**:
        
        A análise por filme revela que títulos como "Armageddon" e "The Waterboy" geraram as maiores receitas, mas também possuem custos elevados. Já filmes como "A Bug’s Life" e "Saving Private Ryan" apresentam menor faturamento, mas custos proporcionalmente altos.

        Possíveis ações:

        - Otimizar precificação de filmes com alta demanda: testar aumento de preço para títulos mais populares;  
        - Negociar melhores condições com fornecedores: reduzir custos de aquisição de filmes que não apresentam margens atrativas;  
        - Reavaliar catálogo de filmes menos rentáveis: pode ser mais lucrativo focar em títulos com melhor relação receita/custo.  
                    
        **4. Motivo das Devoluções e Impacto no Financeiro**:
 
        O gráfico de Quantidade de Devoluções por Motivo destaca que 85,28\\% das devoluções ocorrem porque os clientes não gostaram do filme. Isso pode indicar um problema com as expectativas do público ou com a recomendação dos filmes.

        Impacto financeiro:

        - A alta taxa de devoluções pode gerar custos operacionais adicionais (ex.: logística, reembolsos);  
        - Clientes insatisfeitos podem reduzir a recorrência de aluguéis, impactando a receita no longo prazo.  
        
        Soluções possíveis:

        - Criar um sistema de avaliações e recomendações personalizadas para evitar aluguéis indesejados;  
        - Oferecer créditos ou descontos em futuros aluguéis para clientes que devolveram filmes insatisfeitos, incentivando novas transações.  
                    
        **5. Análise Geográfica dos Aluguéis**:
          
        O mapa de Total de Aluguéis por Cidade Destino indica que algumas cidades concentram a maior parte das locações. Isso pode significar que certas regiões possuem um mercado mais consolidado, enquanto outras podem estar subexploradas.

        Sugestões estratégicas:

        - Expandir a presença em cidades de baixa penetração por meio de campanhas regionais ou parcerias locais;  
        - Ajustar a distribuição do catálogo com base na demanda de cada região, otimizando a logística de envio e reduzindo custos operacionais.
        
        A análise financeira do negócio revela um crescimento sólido!
        """)
        st.write("[Acesse o dashboard publicado no Power BI](https://app.powerbi.com/view?r=eyJrIjoiMTcxOTVkZjMtNTZmMS00OWVlLWI4ZGItMWFjZjJhZWY0ZjI2IiwidCI6ImI1OTFhZTU0LTMzYzItNDU4OS1iZTY2LTkwMjFhNDE5NmM3YyJ9&disablecdnExpiration=1728858578)")

    # Projeto 2:
    if st.button("Análise de Produção Comercial e Estratégias para Otimização de Resultados"):
        st.write("Problema de negócio: A empresa precisa avaliar o desempenho da equipe comercial e dos convênios para entender se a produção está atingindo as metas estabelecidas e onde há oportunidades de crescimento. Apesar do crescimento expressivo nos últimos meses, é essencial identificar quais estratégias impulsionaram esse aumento e como manter essa trajetória ascendente.")
        st.markdown("""
        **1. Análise dos Gráficos e Dados**:
        
        1.1 Produção Comercial Individual:
        O gráfico de Produção Comercial destaca os colaboradores com maior contribuição para o total produzido. Bianca Pereira Souza e Alex Borba Severo (fictícios) representam enorme fatia (54%) da produção, indicando que uma parte significativa dos resultados está concentrada neles. Esse dado sugere a necessidade de incentivar outros colaboradores a aumentar sua participação.

        1.2 Crescimento da Produção Mensal:
        A tabela de Crescimento da Produção evidencia um aumento expressivo em novembro (+192,28%) e um crescimento contínuo em dezembro (+71,86%). Isso pode estar atrelado a campanhas, sazonalidade ou ações específicas de incentivo comercial. Identificar os fatores responsáveis permitirá replicar essas estratégias nos próximos períodos.

        1.3 Meta Anual e Performance:
        O gráfico de Produção Comercial vs. Meta da Empresa mostra que a produção atingiu 27,94 milhões de reais, superando a meta de 22 milhões de reais em 26,98%. Esse resultado indica um desempenho acima do esperado, porém é necessário entender se foi um crescimento sustentável ou se dependeu de fatores sazonais.

        1.4 Distribuição de Operações por Convênio:
        A análise do Valor de Operação Total por Convênio revela a segmentação por fontes de receita, como Federal, Governo Estadual, Prefeitura e INSS. Essa visualização ajuda a identificar quais convênios mais contribuíram para o crescimento e onde há oportunidades de melhoria.

        1.5 Produção no Convênio Privado Acima de 250K reais:
        A tabela de Campanha Convênio Privado > 250K destaca os colaboradores que mais produziram nesse segmento. O total de 1,19 milhão de reais indica que esse nicho pode ser explorado ainda mais com estratégias específicas.
        
        **2. Melhorias e Oportunidades de Negócio**:
        
        2.1 Estratégias de Expansão e Incentivos Internos:
        - Desenvolver treinamentos específicos para os colaboradores com menor produção, visando nivelar o desempenho da equipe;
        - Criar um programa de incentivos para motivar os comerciais a aumentar suas vendas e melhorar a distribuição da produção;
        - Implementar um acompanhamento contínuo de KPIs individuais para fornecer feedbacks estratégicos e ajustes em tempo real.

        2.2 Sustentabilidade do Crescimento:
        - Analisar os fatores que impulsionaram o crescimento exponencial em novembro e dezembro para replicar as estratégias em outros períodos;
        - Criar um calendário de ações comerciais alinhado a períodos de maior demanda, promovendo campanhas específicas nos meses historicamente mais fracos;
        - Monitorar a sazonalidade dos convênios para evitar quedas bruscas na produção.

        2.3 Expansão no Mercado Privado:
        - O convênio privado representou uma produção relevante (R$ 1,19M), indicando que há espaço para expandir esse segmento;
        - Desenvolver parcerias estratégicas com empresas privadas e oferecer condições especiais para atrair mais clientes;
        - Criar campanhas exclusivas para esse nicho, explorando oportunidades fora dos setores governamentais.

        2.4 Otimização dos Convênios:
        - Avaliar quais convênios geram maior rentabilidade e estabilidade para direcionar esforços de captação;
        - Negociar melhorias contratuais com os convênios menos rentáveis, aumentando a lucratividade das operações;
        - Criar segmentação por convênio no dashboard para analisar padrões de crescimento e identificar os mais promissores.

        Os gráficos do dashboard permitem identificar padrões de crescimento, analisar a performance individual dos colaboradores e entender quais segmentos do negócio apresentam maior potencial. A partir dessas análises, é possível criar estratégias para aumentar a eficiência da equipe comercial, expandir a atuação no mercado privado e garantir um crescimento sustentável da produção.

        Com ações baseadas em dados, a empresa pode maximizar seus resultados e fortalecer sua posição no mercado.
        """)
        st.write("[Acesse o dashboard publicado no Power BI](https://app.powerbi.com/view?r=eyJrIjoiMjNlNzQzZWEtYzVmMi00NTJhLWIxZDctZWQ2OWVmMjRkYmZhIiwidCI6ImI1OTFhZTU0LTMzYzItNDU4OS1iZTY2LTkwMjFhNDE5NmM3YyJ9)")

    # Projeto 3:
    if st.button("Segmentação de Clientes e Estratégias para Aumento de Receita"):
        st.write("Problema de negócio: A empresa deseja entender melhor o comportamento dos clientes para otimizar suas estratégias de venda e fidelização. Com base na segmentação de renda, faixa etária e categoria de cliente, o objetivo é identificar oportunidades de crescimento e retenção, além de ajustar estratégias sazonais para maximizar o faturamento.")
        st.markdown("""
        **1. Análise dos Gráficos e Dados**:
        
        1.1 Segmentação por Categoria e Faixa de Renda:
        A tabela de Faturamento por Categoria e Faixa de Renda mostra que os clientes gastam valores relativamente próximos, independentemente da renda. Contudo, categorias como Esportes e Vestuário possuem ticket médio um pouco superior. Isso pode indicar que o poder de compra influencia menos do que outros fatores, como necessidade e preferência pessoal.

        1.2 Quantidade de Transações por Categoria de Cliente:
        O gráfico mostra que clientes Novos representam o maior volume de transações, seguidos pelos Recorrentes e, por último, pelos VIPs. Isso sugere um desafio na retenção de clientes, pois a base de clientes recorrentes não está crescendo na mesma proporção dos novos. Além disso, o número reduzido de clientes VIPs indica que poucos consumidores realizam compras de alto valor.

        1.3 Faturamento por Faixa Etária:
        O gráfico destaca que as faixas 26-35 anos e 36-45 anos geram o maior faturamento, enquanto a faixa 18-25 anos tem um volume mais baixo, e os consumidores acima de 60 anos apresentam um faturamento menor. Isso sugere que as estratégias de marketing podem ser ajustadas para atrair públicos mais jovens e idosos.

        1.4 Faturamento por Mês (Sazonalidade):
        O gráfico revela uma estabilidade no faturamento durante o ano, com uma queda acentuada em novembro. Essa queda pode indicar um problema com estratégias sazonais ou a necessidade de reforçar promoções no período.

        **2. Melhorias e Oportunidades de Negócio**:

        2.1 Estratégias para Aumentar a Retenção de Clientes:
        - Criar um programa de fidelidade para incentivar compras recorrentes, oferecendo descontos progressivos ou benefícios exclusivos;
        - Implementar estratégias personalizadas para clientes VIPs, como atendimento exclusivo e ofertas premium para aumentar a retenção desse grupo;
        - Analisar por que muitos clientes novos não retornam e ajustar a experiência pós-compra, como e-mails de acompanhamento ou cupons para futuras compras.

        2.2 Expansão para Faixas Etárias com Menor Faturamento:
        - Criar campanhas específicas para o público 18-25 anos, utilizando estratégias voltadas para redes sociais, influenciadores e preços mais acessíveis;
        - Explorar a base de clientes 60+, oferecendo produtos adaptados às suas necessidades e promoções específicas para essa faixa etária.

        2.3 Ajuste de Estratégia Sazonal:
        - Avaliar a queda de faturamento em novembro e criar campanhas promocionais antecipadas, como aquecimento para a Black Friday;
        - Explorar datas comemorativas menos utilizadas ao longo do ano para incentivar compras em meses de menor faturamento.

        O dashboard revela oportunidades claras para aumentar a retenção de clientes, melhorar a personalização das estratégias de marketing e ajustar campanhas sazonais. A segmentação por faixa etária e renda permite uma abordagem mais eficiente para cada público, otimizando a experiência do consumidor e impulsionando o crescimento sustentável do negócio.
        """)
        st.write("[Acesse o dashboard publicado no Power BI](https://app.powerbi.com/view?r=eyJrIjoiNDI1NDhjMGEtMThiNS00NzI3LTgyZTgtMmEyYTY1YjZlOWQ1IiwidCI6ImI1OTFhZTU0LTMzYzItNDU4OS1iZTY2LTkwMjFhNDE5NmM3YyJ9)")

        # Projeto 4: Repositório GitHub
    if st.button("K-means - Clusterização"):
        st.write("De uma base de dados com valores de venda de diversos clientes, criei a seguinte missão: por meio da clusterização, conseguimos agrupar esses dados para realizar campanhas específicas?")
        st.markdown("""
        Para concluir essa atividade, separei as seguintes etapas:
        - **Carregamento e tratamento de dados**: elimine valores nulos e normalize sua base de dados para resultados finais robustos;
        - **Métodos para encontrar o "k" ideal**: o "k" significa a quantidade de grupos (clusters) ideal para a base de dados. Por meio de Método de Cotovelo e Índice de Silhueta, encontramos esse valor;
        - **Uso de gráficos para visualização**: utilize gráficos para a visualização e interpretação dos resultados. Em Python, recomendo biblioteca Matplotlib;
        - **Rótulo da base original**: com o agrupamento feito, rotule cada observação da base original de acordo com a separação realizada. A partir disso encontramos insights valiosos ao negócio.

        Interpretação dos resultados: neste exemplo, o "k" ideal, encontrado por meio do Índice de Silhueta, é igual a 2. Portanto, para campanhas específicas de acordo com o valor de venda feito pelo cliente, esse trabalho de marketing precisa ser direcionado a dois grupos.

        Por exemplo, podemos retirar o valioso insight de que os grupos podem ser divididos entre clientes que adquirem produtos a valores alto ou baixo de vendas.
        """)
        st.write("Veja o código completo no [GitHub](https://github.com/lucasspessoa/projeto-k-means).")

        # Projeto 5: Repositório GitHub
    if st.button("Projeto Biblioteca Faker"):
        st.write("Por meio desse projeto, me aventurei na diversidade de bibliotecas que o Python oferece. A 'lib' Faker consegue gerar dados falsos em larga escala, sendo amplamente utilizada em testes de software, geração de dados para desenvolvimento de protótipos e em projetos de ciência de dados onde dados reais não estão disponíveis.")
        st.markdown("""
        Para empresas que estão interessadas em realizar testes técnicos sem expor dados internos de clientes, por exemplo, essa biblioteca permite essa alternativa ao:
        - **Gerar Dados Personalizáveis**: Faker possui provedores de dados para uma variedade de informações, como: Nome, Endereço, Data e Hora, Dados Financeiros;
        - **Localização e Linguagem**: Faker suporta dados localizados em várias línguas e formatos regionais;
        - **Gerar Dados em Lote**: Faker permite gerar grandes quantidades de dados com facilidade;
        - **Personalir Provedores de Dados**: É possível criar provedores personalizados se você precisar de tipos de dados que não estão disponíveis por padrão.
        """)
        st.write("Veja o código completo no [GitHub](https://github.com/lucasspessoa/biblioteca-faker).")