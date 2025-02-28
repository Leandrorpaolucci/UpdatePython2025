import sqlite3

# 1- Criando o banco de dados
conexao = sqlite3.connect('titulo.db')


"""
Se a tabela já existir, ele faz a conexão (sem substituir o que já foi criado com o mesmo nome)
"""

