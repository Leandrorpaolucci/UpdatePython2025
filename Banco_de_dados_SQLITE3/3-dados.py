import sqlite3


# 1 - Conectando no banco de dados
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - Inserindo Dados

cursor.execute(
    """
        INSERT INTO filmes(nome, ano, nota)
        VALUES ('Sonic', 2021, 8.0)

    """
)

conexao.commit()
conexao.close()
print('Dados inseridos na tabela.')