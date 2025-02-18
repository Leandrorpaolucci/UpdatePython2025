import sqlite3

# 1 - conectar ao banco de dados
def conecta_bd():
    conexao = sqlite3.connect('titulo.db')
    return conexao

# 2 - Inserir dados
def inserir_dados(nome, ano, nota):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute(
        """
        INSERT INTO filmes(nome, ano, nota)
        VALUES (?, ?, ?)
        """,
        (nome, ano, nota)
    )

    conexao.commit()
    conexao.close()

# 3 - Listagem de dados
def obter_dados():
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM filmes")
    dados = cursor.fetchall()
    cursor.close()
    return dados
