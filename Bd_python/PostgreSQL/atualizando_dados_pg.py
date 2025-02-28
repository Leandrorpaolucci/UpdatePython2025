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

    # Criar o cursor a partir da conexão usando 'with' para garantir o fechamento
    with conexao.cursor() as cursor_obj:
        # Verificar se o registro com o ID existe antes de atualizar
        cursor_obj.execute("SELECT 1 FROM games WHERE ID = %s", (2,))
        if cursor_obj.fetchone():
            # O registro foi encontrado, podemos atualizar
            cursor_obj.execute("""
                UPDATE games
                SET NAME = %s
                WHERE ID = %s
            """, ("Naruto", 2))
            conexao.commit()
            print("Dados atualizados com sucesso.")
        else:
            print("ID não encontrado, nenhum dado foi atualizado.")

except OperationalError as e:
    print(f"Erro de conexão ao banco de dados: {e}")
except DatabaseError as e:
    print(f"Erro ao executar a query: {e}")
finally:
    if conexao:
        conexao.close()
        print("Conexão fechada.")
