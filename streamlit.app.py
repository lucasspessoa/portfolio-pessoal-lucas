import streamlit as st

# Configurações da Página
st.set_page_config(page_title="Lucas da Silva Pessoa - Portfólio", layout="centered")

# Seção 1: Boas-Vindas
st.title("Lucas da Silva Pessoa")
st.subheader("Analista de Dados | Estudante de Ciências Econômicas")
st.write("""
    Olá! Eu sou o Lucas, um entusiasta em análise de dados, apaixonado por transformar dados em insights.
    Este é o meu portfólio, onde você pode encontrar meus projetos, experiência e objetivos de carreira.
""")

# Links para redes sociais
st.write("[LinkedIn](https://linkedin.com/in/01lucaspessoa) | [GitHub](https://github.com/seu-usuario)")

# Seção 2: Currículo (Resume)
st.header("Currículo")
st.write("Aqui estão alguns dos meus destaques profissionais:")
st.write("""
- **Experiência**: Assistente Administrativo Jr. na GFT, com foco em precificação e análise de dados.
- **Educação**: 5º semestre de Ciências Econômicas na UFC.
- **Habilidades**: Power BI, SQL Server, Python, Excel.
""")
# Opção para download do currículo
with open("Lucas_da_Silva_Pessoa_CV.pdf", "rb") as pdf_file:
    pdf_data = pdf_file.read()
st.download_button("Baixar Currículo", data=pdf_data, file_name="Lucas_da_Silva_Pessoa_CV.pdf")

# Seção 3: Projetos
st.header("Projetos")
st.write("Aqui estão alguns dos projetos em que trabalhei:")
st.write("""
- **[Netflix 1997 Dashboard](#)**: Análise de lucro e performance de uma empresa fictícia de streaming.
- **[Análise de Vendas](#)**: Insights detalhados sobre padrões de vendas e segmentação de consumidores.
- **[Portfolio de Análise de Dados](#)**: Uma série de projetos focados em SQL, Power BI e Python.
""")

# Seção 4: Objetivos Profissionais
st.header("Objetivos Profissionais")
st.write("""
Estou buscando oportunidades para:
- Continuar aprimorando minhas habilidades em **Power BI**, **SQL**, e **Python**.
- Trabalhar em projetos que envolvam **ciência de dados** e **automação de processos**.
- Contribuir para o desenvolvimento de estratégias baseadas em dados que impactem diretamente a tomada de decisão nas empresas.
""")

# Seção 5: Contato
st.header("Entre em Contato")
st.write("Se você quiser me contatar para colaborações ou oportunidades de trabalho, entre em contato via e-mail ou telefone.")
st.write("""
- **E-mail**: lucaspfc05@gmail.com
- **Telefone**: (85) 992398429
""")

# Opcional: Formulário de contato
st.text_input("Nome")
st.text_input("E-mail")
st.text_area("Mensagem")
st.button("Enviar")