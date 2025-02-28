import psycopg2
from psycopg2 import OperationalError, DatabaseError

try:
    # Estabelecer conexão com o banco de dados
    conexao = psycopg2.connect(
        database='db_games',
        user='postgres',
        password='123456',
        host='localhost',
        port='5432'
    )

    # Criar o cursor a partir da conexão usando 'with' para garantir fechamento
    with conexao.cursor() as objeto_cursor:
        # Verificar se o registro existe antes de tentar excluir
        objeto_cursor.execute("SELECT * FROM games WHERE ID = %s", (2,))
        if objeto_cursor.fetchone():
            # O registro foi encontrado, então deletamos
            objeto_cursor.execute("DELETE FROM games WHERE ID = %s", (2,))
            conexao.commit()
            print("Dados deletados com sucesso!")
        else:
            print("ID não encontrado, nada foi excluído.")

except OperationalError as e:
    print(f"Erro de conexão ao banco de dados: {e}")
except DatabaseError as e:
    print(f"Erro ao executar a query: {e}")
finally:
    if conexao:
        conexao.close()
        print("Conexão fechada.")
