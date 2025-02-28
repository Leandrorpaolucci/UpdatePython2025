import streamlit as st
import sqlite3

# Conectando com o banco de dados SQLite
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

# Função para atualizar os dados no banco de dados
def atualizar_dados(id, login=None, senha=None, email_recuperacao=None):
    if login:
        cursor.execute('''
            UPDATE dados_acesso SET login = ? WHERE id = ?
        ''', (login, id))
    if senha:
        cursor.execute('''
            UPDATE dados_acesso SET senha = ? WHERE id = ?
        ''', (senha, id))
    if email_recuperacao:
        cursor.execute('''
            UPDATE dados_acesso SET email_recuperacao = ? WHERE id = ?
        ''', (email_recuperacao, id))
    conn.commit()

# Página de salvar dados
def pagina_salvar():
    st.title("💾 Salvar Dados de Acesso")
    st.markdown("""
        Preencha os campos abaixo para armazenar os dados de acesso ao seu site.
        Certifique-se de inserir todas as informações corretamente.
    """)

    with st.container():
        st.subheader("🔑 Informações de Acesso")
        
        site = st.text_input("📍 Nome do Site de Referência", placeholder='Digite o nome do site')
        
        if site:
            login = st.text_input(f"🔑 Login de Entrada para o Site: {site}", placeholder='Login do site')
            senha = st.text_input(f"🔒 Digite a Senha para o Site: {site}", placeholder='Senha do site', type="password")
            email_recuperacao = st.text_input(f"📧 E-mail de Recuperação do {site}", placeholder='Digite o e-mail de recuperação')

        if st.button("Salvar Dados"):
            salvar_dados(site, login, senha, email_recuperacao)
            st.success("Dados salvos com sucesso!")

# Página de atualizar dados
def pagina_atualizar():
    st.title("✏️ Atualizar Dados de Acesso")

    # Inserir ID para busca
    id_busca = st.number_input("Digite o ID do site a ser atualizado", min_value=1, step=1)
    
    if id_busca:
        cursor.execute("SELECT * FROM dados_acesso WHERE id = ?", (id_busca,))
        resultado = cursor.fetchone()
        
        if resultado:
            st.write(f"**Site:** {resultado[1]}")
            st.write(f"**Login:** {resultado[2]}")
            st.write(f"**Senha:** {'*' * len(resultado[3])}")  # Escondendo a senha
            st.write(f"**E-mail de Recuperação:** {resultado[4]}")
            
            # Atualizar campos
            novo_login = st.text_input(f"Novo Login (Deixe em branco para manter: {resultado[2]})")
            nova_senha = st.text_input(f"Nova Senha (Deixe em branco para manter)", type="password")
            novo_email = st.text_input(f"Novo E-mail de Recuperação (Deixe em branco para manter: {resultado[4]})")
            
            if st.button("Atualizar Dados"):
                atualizar_dados(id_busca, 
                                login=novo_login if novo_login else None, 
                                senha=nova_senha if nova_senha else None, 
                                email_recuperacao=novo_email if novo_email else None)
                st.success("Dados atualizados com sucesso!")
        else:
            st.error("ID não encontrado!")

# Menu para navegação entre as páginas
opcao = st.sidebar.selectbox("Escolha uma opção", ["Salvar Dados", "Atualizar Dados"])

if opcao == "Salvar Dados":
    pagina_salvar()
else:
    pagina_atualizar()
