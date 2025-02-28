import sqlite3

conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - Leitura de dados
dados = cursor.execute("SELECT * FROM filmes")

print(dados.fetchall())