import streamlit as st

# Configurações da Página
st.set_page_config(page_title="Portfólio: Lucas da Silva Pessoa", layout="centered")

# Navegação Simples com Sidebar
st.sidebar.title("Navegação")
page = st.sidebar.selectbox("Escolha uma seção", ["Início / Currículo / Objetivos / Contato", "Projetos"])

# Seção 1: Início, Currículo, Objetivos Profissionais, Contato
if page == "Início / Currículo / Objetivos / Contato":
    st.title("Lucas da Silva Pessoa")
    st.subheader("Analista de Dados | Estudante de Ciências Econômicas")
    st.write("""
        Olá! Eu sou o Lucas, um entusiasta em análise de dados, apaixonado por transformar dados em insights.
        Este é o meu portfólio, onde você pode encontrar meus projetos, experiência e objetivos de carreira.
    """)

    # Links para redes sociais
    st.write("[LinkedIn](https://linkedin.com/in/01lucaspessoa) | [GitHub](https://github.com/lucasspessoa)")

    # Currículo
    st.header("Currículo")
    st.write("Aqui estão alguns dos meus destaques profissionais:")
    st.write("""
    - **Experiência**: Assistente Administrativo Jr. na GFT, com destaque em precificação, análise de dados e automação de tarefas.
    - **Educação**: cursando Ciências Econômicas na UFC.
    - **Habilidades**: Power BI, SQL, Python, Excel.
    """)

    # Opção para download do currículo
    with open("CV_Analista_Lucas.pdf", "rb") as pdf_file:
        pdf_data = pdf_file.read()
    st.download_button("Baixar Currículo", data=pdf_data, file_name="CV_Analista_Lucas.pdf")

    # Objetivos Profissionais
    st.header("Objetivos Profissionais")
    st.write("""
    Estou buscando oportunidades para:
    - Continuar aprimorando minhas habilidades em **Power BI**, **SQL**, e **Python**.
    - Trabalhar em projetos que envolvam **ciência de dados** e **automação de processos**.
    - Contribuir para o desenvolvimento de estratégias baseadas em dados que impactem diretamente a tomada de decisão nas empresas.
    """)

    # Contato
    st.header("Entre em Contato")
    st.write("Se você quiser me contatar para colaborações ou oportunidades de trabalho, entre em contato via e-mail ou telefone.")
    st.write("""
    - **E-mail**: lucaspfc05@gmail.com
    - **Telefone**: (85) 992398429
    """)

    # Formulário de contato opcional
    nome = st.text_input("Nome")
    email = st.text_input("E-mail")
    mensagem = st.text_area("Mensagem")
    if st.button("Enviar"):
        st.write(f"Obrigado pela mensagem, {nome}! Entraremos em contato em breve.")

# Seção 2: Projetos
elif page == "Projetos":
    st.header("Projetos")
    st.write("Aqui estão alguns dos projetos em que trabalhei:")

    # Projeto 1: Netflix 1997 Dashboard
    if st.button("Netflix 1997 Dashboard"):
        st.write("Análise de lucro e performance de uma empresa fictícia de streaming baseada no aluguel de DVDs.")
        st.image("caminho_para_imagem_netflix.png")
    
    # Projeto 2: Análise de Vendas
    if st.button("Análise de Vendas"):
        st.write("Insights detalhados sobre padrões de vendas e segmentação de consumidores.")
    
    # Projeto 3: Portfolio de Análise de Dados
    if st.button("Portfolio de Análise de Dados"):
        st.write("Projetos focados em SQL, Power BI e Python, voltados para análise de dados.")