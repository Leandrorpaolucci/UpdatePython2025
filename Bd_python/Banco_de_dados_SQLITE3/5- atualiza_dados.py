import sqlite3

conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()


# Atualizando dados


cursor.execute(
    f"""
        UPDATE filmes SET nota = {5}
        WHERE id = {1}

    """
)

conexao.commit()
print('Dados atualizados.')