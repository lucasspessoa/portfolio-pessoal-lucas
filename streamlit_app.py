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
    st.write("""
        Olá! Eu sou o Lucas, um entusiasta em análise de dados, apaixonado por transformar dados em insights.
        """
        """
        Este é o meu portfólio, onde você pode encontrar, nesta seção, informações pessoais/profissionais, contato e objetivos.
        """
        """
        Projetos e suas descrições você confere na seção Projetos Realizados, na barra de Navegação ao lado.
    """)

    # Links para redes sociais
    st.write("[LinkedIn](https://linkedin.com/in/01lucaspessoa) | [GitHub](https://github.com/lucasspessoa)")

    # Currículo
    st.header("Currículo")
    st.write("Aqui estão meus destaques profissionais:")
    st.write("""
    - **Experiência**: 
    """
    """
    Assistente Administrativo Jr. na GFT Promotora de Crédito Consignado.
    Ao longo de mais de dois anos, desempenhei atividades de Pricing e Inteligência de Mercado, com o objetivo de colocar o produto da empresa como destaque frente à concorrência;
    """
    """
    Foram realizadas validações de concorrência e comparação ao preço da empresa; engenharia de precificação; custos do produto; potenciais oportunidades; entre outras tarefas.
    """
    """ 
    Para tais atividades, foram necessárias habilidades típicas de um Analista de Dados: criação e manuseio de dashboards, realização de consultas complexas e engenharia em banco de dados relacionais (SQL) e conhecimento estatístico para tomada de decisão estratégica.
    """
    """
    Além disso, realizei automação de tarefas para otimização de tempo. Isso permitiu melhora significativa no tempo de trabalho do setor e menores riscos de erro humano.
    """
    """
    - **Educação**: cursando Ciências Econômicas na Universidade Federal do Ceará.
    - **Habilidades Técnicas**: Estatística; Microeconomia para Análise de Mercado; Power BI; SQL; Python para Tratamento de Dados; Cloud Computing; e Excel, com destaque em Power Query;
    - **Habilidades Interpessoais**: Comunicação Didática; Colaboração para Melhoria Contínua, sem medo de ouvir pontos negativos; Tranquilidade para Resolução de Problemas; Foco e Atenção em Resultados.
    """)

    # Opção para download do currículo
    with open("CV_Lucas.pdf", "rb") as pdf_file:
        pdf_data = pdf_file.read()
    st.download_button("Baixar Currículo", data=pdf_data, file_name="CV_Lucas.pdf")

    # Objetivos Profissionais
    st.header("Objetivos Profissionais")
    st.write("""
    Estou buscando oportunidades para:
    - Continuar aprimorando minhas habilidades em ferramentas como **Power BI**, **Excel**, **SQL** e **Python** com objetivo de crescer na área de dados.
    - Trabalhar em projetos que envolvam **Ciência de Dados** ou **Estatística** e **Automação de Processos**.
    - Contribuir para o desenvolvimento de estratégias baseadas em dados que impactem diretamente a tomada de decisão nas empresas.
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
        st.write("Neste dashboard, pude me aprofundar no trabalho de Performance, voltado a analisar indicadores de uma Promotora de crédito consignado, com DADOS FICTÍCIOS.") 
        st.markdown("""
        Este exercício me fez se aprofundar em gráficos nativos do Power BI que são úteis para essa área tão fundamental voltada ao desempenho de uma empresa:
        - **KPI**: muito popular para análise relativa. No dashboard, exibe a produção do último mês em relação à meta mensal da empresa;
        - **Velocímetro**: voltado a metas. No dashboard, exibe a produção total realizada no período e a meta estipulada;
        - **Treemap**: permite visualizar hierarquia. No dashboard, mostra a distribuição da produção de acordo com o convênio do negócio;
        - **Tabela Simples**: sempre bem-vinda. No dashboard, mostra quem atingiu a meta específica (selo verdinho) de R$ 250 mil no convênio Privado.

        Embora nada extravagante, também foquei em ferramentas de estilização. Uso de símbolos, paleta de cores e a visualização "clean" são marcas que particulamente me encantam na parte de design.
        """)
        st.write("[Acesse o dashboard publicado no Power BI](https://app.powerbi.com/view?r=eyJrIjoiMjNlNzQzZWEtYzVmMi00NTJhLWIxZDctZWQ2OWVmMjRkYmZhIiwidCI6ImI1OTFhZTU0LTMzYzItNDU4OS1iZTY2LTkwMjFhNDE5NmM3YyJ9)")

        # Projeto 3: Repositório GitHub
    if st.button("Projeto Função Professor"):
        st.write("O projeto visa realizar a validação mais esperada (e temida!) pelos alunos: verificação de aprovação.")
        st.markdown("""
        Resolver esse projeto me possibilitou se aprofundar na seguinte atividade:
        - **ETL** (Extrair, Transformar e Carregar) via Python, com uso da biblioteca queridinha dos analistas, o Pandas. A base de extração é via Planilha Excel. A "lib" Pandas possui ferramentas próprias para limpeza, manuseio e organização dos dados.  
        """)
        st.write("Veja o código completo no [GitHub](https://github.com/lucasspessoa/portfolio-dados).")