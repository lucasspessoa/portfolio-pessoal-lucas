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
    st.write("Aqui estão alguns dos meus destaques profissionais:")
    st.write("""
    - **Experiência**: Assistente Administrativo Jr. na GFT Promotora de Crédito Consignado.
    Ao longo de mais de dois anos, desempenhei atividades de Pricing e Inteligência de Mercado, com o objetivo de colocar o produto da empresa como destaque frente à concorrência;
    """
    """ 
    Para atender ao objetivo descrito acima, atividades de análise de dados internos da empresa em Banco de Dados Relacionais foram necessários;
    """
    """
    Além disso, realizei atividades de automação de tarefas para otimização de tempo.
    """
    """
    - **Educação**: cursando Ciências Econômicas na Universidade Federal do Ceará.
    - **Habilidades**: Estatística; Microeconomia; Power BI; SQL; Python; e Excel, com destaque em Power Query.
    """)

    # Opção para download do currículo
    with open("CV_Analista_Lucas.pdf", "rb") as pdf_file:
        pdf_data = pdf_file.read()
    st.download_button("Baixar Currículo", data=pdf_data, file_name="CV_Analista_Lucas.pdf")

    # Objetivos Profissionais
    st.header("Objetivos Profissionais")
    st.write("""
    Estou buscando oportunidades para:
    - Continuar aprimorando minhas habilidades em ferramentas como **Power BI**, **Excel**, **SQL**, e **Python**.
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

    # Projeto 1: Netflix 1997 Dashboard
    if st.button("Netflix 1997 Dashboard"):
        st.write("Análise de lucro e performance, com dados fictícios, da empresa de streaming Netflix, criada em 1997, baseada no aluguel de DVDs de filmes de sucesso do ano de 1998.")
        st.write("[Acesse o dashboard publicado no Power BI](https://app.powerbi.com/view?r=eyJrIjoiMTcxOTVkZjMtNTZmMS00OWVlLWI4ZGItMWFjZjJhZWY0ZjI2IiwidCI6ImI1OTFhZTU0LTMzYzItNDU4OS1iZTY2LTkwMjFhNDE5NmM3YyJ9&disablecdnExpiration=1728858578)")