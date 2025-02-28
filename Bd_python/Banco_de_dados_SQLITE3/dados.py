import sqlite3

# 1 - Conectar ao banco de dados
def conecta_bd():
    conexao = sqlite3.connect('titulo.db')
    return conexao

# 2 - Criar a tabela (caso não exista)
def cria_tabela():
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ano INTEGER,
            nota REAL
        )
        """
    )
    conexao.commit()
    conexao.close()

# 3 - Inserir dados
def inserir_dados(nome, ano, nota):
    try:
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
    except sqlite3.Error as e:
        print(f"Erro ao inserir dados: {e}")
    finally:
        conexao.close()

# 4 - Listagem de dados
def obter_dados():
    try:
        conexao = conecta_bd()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM filmes")
        dados = cursor.fetchall()
        return dados
    except sqlite3.Error as e:
        print(f"Erro ao obter dados: {e}")
    finally:
        conexao.close()
