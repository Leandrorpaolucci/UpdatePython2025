import psycopg2

try:
    # Estabelecer a conexão com o banco de dados
    conexao = psycopg2.connect(
        database='db_games',
        user='postgres',
        password='123456',
        host='localhost',
        port='5432'
    )

    # Criar um cursor a partir da conexão
    cursor_obj = conexao.cursor()

    # Dados a serem inseridos
    games = [
        ('Dragon Ball Z', 1986, 9.0),
        ('Os Cavaleiros dos Zodiaco', 1996, 9.5)
    ]

    # Inserir os dados
    for game in games:
        try:
            cursor_obj.execute(
                """
                    INSERT INTO games(name, ano, score)
                    VALUES (%s, %s, %s)
                """, game
            )
        except Exception as e:
            print(f"Ocorreu um erro ao inserir o jogo {game[0]}: {e}")
    
    # Salvar as alterações no banco
    conexao.commit()
    print('Dados inseridos com sucesso!')

except Exception as e:
    print(f"Ocorreu um erro na conexão ou na execução do código: {e}")
    
finally:
    # Garantir que a conexão seja fechada, independentemente de erros
    if conexao:
        conexao.close()
