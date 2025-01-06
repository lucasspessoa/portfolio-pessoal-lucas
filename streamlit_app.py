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
    - Desenvolvi dashboards interativos que demonstraram potencial de crescimento de cerca de 5% na receita média da empresa; 
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

    # Projeto 1: Dashboard Netflix 1997
    if st.button("Dashboard Netflix 1997"):
        st.write("Com dados fictícios, analisei Lucro e Produto da empresa de streaming Netflix, criada em 1997, baseada no aluguel de DVDs de filmes de sucesso do ano de 1998 (nostálgico?).")
        st.markdown("""
        Além da criatividade em demonstrar a importância da Análise de Dados muito antes de existir ferramentas como Power BI, utilizei o dashboard para exibir gráficos-chave para o tipo de análise que se propõe:
        - **Gráfico de Linha**: excelente para acompanhar tendências ao longo do tempo;
        - **Gráfico de Barras Agrupadas**: demonstra a relação de magnitude entre duas variáveis;
        - **Gráfico de Pizza**: embora exista limitação de elementos (recomendável não mais que 5), é útil para mostrar a composição de um todo;
        - **Mapa**: perfeito para visualizações geográficas.

        Plus: no Gráfico de Pizza, ainda foi inclusa a "Tooltip", ou Dica de Ferramenta, para mostrar a composição dos tipos de devoluções em relação aos filmes listados. Para visualizá-la, passe o mouse por cima de cada fatia.
        """)
        st.write("[Acesse o dashboard publicado no Power BI](https://app.powerbi.com/view?r=eyJrIjoiMTcxOTVkZjMtNTZmMS00OWVlLWI4ZGItMWFjZjJhZWY0ZjI2IiwidCI6ImI1OTFhZTU0LTMzYzItNDU4OS1iZTY2LTkwMjFhNDE5NmM3YyJ9&disablecdnExpiration=1728858578)")

    # Projeto 2: Dashboard Indicadores
    if st.button("Dashboard Indicadores"):
        st.write("Neste dashboard, pude me aprofundar no trabalho de Performance voltado a analisar indicadores de uma Promotora de Crédito Consignado, com DADOS FICTÍCIOS.")
        st.markdown("""
        Este exercício me permitiu se aprofundar em gráficos nativos e fórmulas do Power BI que são úteis para essa atividade tão fundamental voltada ao desempenho de uma empresa:
        - **Segmentações**: no topo, é possível realizar filtros de período, comercial e convênio. Essa ferramenta permite visualizar análises ainda mais detalhadas, pois altera o contexto dos gráficos exibidos no dashboard;
        - **Dados Relativos**: por vezes, informações como a participação em relação ao todo ou métricas de crescimento de um período em relação a outro ("Month-over-Month", por exemplo) são necessárias para premiar destaques individuais ou entender a saúde do negócio, por exemplo. O Power BI fornece meios de se calcular esses dados, que estão exibidos em gráficos de tabelas;
        - **KPI e Velocímetro**: gráficos muito populares para análise relativa e de metas. No dashboard, são duas excelentes alternativas para exibir a produção total realizada no período e a meta estipulada. E parabéns a equipe comercial, que ultrapassou a meta estipulada!;
        - **Treemap**: permite visualizar hierarquia. No dashboard, mostra a distribuição da produção de acordo com o convênio do negócio. Ainda no exemplo, demonstra a diferença de participação nas receitas da empresa;
        - **Campanha Específica**: suponha que a empresa crie uma meta específica a cada comercial; no último gráfico de tabela simples, mostra quem atingiu a meta específica (selo verdinho) de R$ 250 mil no convênio Privado.

        Embora nada extravagante, também foquei em ferramentas de estilização. Uso de símbolos, paleta de cores e a visualização "clean" são marcas que particulamente me encantam na parte de design.
        """)
        st.write("[Acesse o dashboard publicado no Power BI](https://app.powerbi.com/view?r=eyJrIjoiMjNlNzQzZWEtYzVmMi00NTJhLWIxZDctZWQ2OWVmMjRkYmZhIiwidCI6ImI1OTFhZTU0LTMzYzItNDU4OS1iZTY2LTkwMjFhNDE5NmM3YyJ9)")

    # Projeto 3: Dashboard Segmentação
    if st.button("Dashboard Segmentação"):
        st.write("Neste dashboard, destaco uma atividade fundamental a qualquer analista: a Segmentação de Clientes. Com a ajuda da biblioteca Faker, de Python, gerei base de dados fictícios para servir a esse exercício.") 
        st.markdown("""
        A segmentação é importante pois permite separar os clientes da empresa em diferentes grupos e assim obter insights valiosos que apoiem tomadas de decisões estratégicas, bem como campanhas de marketing, por exemplo.
        Dentre as segmentações que realizei, dividi clientes por Faixa Etária, Faixa de Renda - distribuição da renda mensal individual de acordo com o Salário Mínimo vigente - e Categoria do Cliente.
        Como principais conclusões e insights, pontuo:
        - **segmentação por Categoria de Produto e Renda**: por meio de uma medida, calculei o Valor Médio de Compra para verificar qual categoria, na média, melhor rentabiliza para a firma e como isso se distribui de acordo com a renda do cliente;
        - **segmentação por Categoria de Cliente**: dentre Novo, Recorrente e VIP, nota-se que a firma não possui um programa forte de fidelização, embora muitos clientes frequentes. Nessa situação, seria interessante programas de marketing que impulsionem clientes fiéis e evite perda de carteira;
        - **segmentação por Faixa Etária e relação com o Faturamento**: com o apoio fundamental do gráfico de dispersão, é possível perceber a relação positiva das duas variáveis. Quanto mais velho o cliente, mais em valor de transações são realizadas, com exceção da faixa entre 26 e 45, que é constante;
        - **Sazonalidade**: por meio de um gráfico de linhas, nota-se que os dados de faturamento seguem em linha até o mês de outubro, quando se registra queda abrupta até novembro. Divergente do esperado, né? Mas calma que nada como uma Black Friday para salvar o fim de ano (risos).

        Realizar esse trabalho exige tempo, muita capacidade analítica e entendimento do negócio, mas entrega resultados fundamentais às firmas para entender como cada cliente age.
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