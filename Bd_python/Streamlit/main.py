import streamlit as st
import sqlite3

# Conectando ao banco de dados SQLite (ele será criado se não existir)
conn = sqlite3.connect('dados_site.db')
cursor = conn.cursor()

# Criando a tabela, caso não exista
cursor.execute('''
    CREATE TABLE IF NOT EXISTS dados_acesso (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        site TEXT NOT NULL,
        login TEXT NOT NULL,
        senha TEXT NOT NULL,
        email_recuperacao TEXT NOT NULL
    )
''')
conn.commit()

# Função para salvar os dados no banco de dados
def salvar_dados(site, login, senha, email_recuperacao):
    cursor.execute('''
        INSERT INTO dados_acesso (site, login, senha, email_recuperacao)
        VALUES (?, ?, ?, ?)
    ''', (site, login, senha, email_recuperacao))
    conn.commit()

# Título
st.title("💾 Salvar Dados de Acesso")

# Descrição com uma explicação rápida
st.markdown("""
    Preencha os campos abaixo para armazenar os dados de acesso ao seu site.
    Certifique-se de inserir todas as informações corretamente.
""")

# Usando containers para organizar o layout
with st.container():
    # Criando uma seção com campos
    st.subheader("🔑 Informações de Acesso")
    
    site = st.text_input("📍 Nome do Site de Referência", placeholder='Digite o nome do site')
    
    if site:
        login = st.text_input(f"🔑 Login de Entrada para o Site: {site}", placeholder='Login do site')
        senha = st.text_input(f"🔒 Digite a Senha para o Site: {site}", placeholder='Senha do site', type="password")
        email_recuperacao = st.text_input(f"📧 E-mail de Recuperação do {site}", placeholder='Digite o e-mail de recuperação')

    # Botão para salvar os dados
    if st.button("Salvar Dados"):
        if site and login and senha and email_recuperacao:
            salvar_dados(site, login, senha, email_recuperacao)
            st.success("Dados salvos com sucesso!")
        else:
            st.warning("Por favor, preencha todos os campos antes de salvar.")

    # Seção de ajuda ou observações extras
    st.markdown("""
        **Dica:** Use senhas fortes e nunca compartilhe suas informações de login com terceiros.
    """)
