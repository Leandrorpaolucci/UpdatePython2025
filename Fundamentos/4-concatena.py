name = str(input('Digite o nome do filme:\n '))
yearLaunch = int(input('Digite o ano do lançamento do fime:\n'))
noteMovie = float(input('Digite a nota do filme:\n'))


# Alternativa 1

print(" Dados do filme - Alternativa - 1\n")
print("Nome do filme:", name)
print("Ano do Filme: ", yearLaunch)
print("Nota do filme: ", noteMovie)
print('\n')

# Alternativa 2
print('Alternativa 2 - Todas as informações em um print')
print("Nome do Filme:", name, "\nAno De Lançamento:", yearLaunch, "\nNota Do filme:", noteMovie)
print('\n')

# Alternativa 3
print(f'''
Alternativa - 3 (Mais utilizada)
Nome do Filme {name},
Ano do Filme {yearLaunch},
Nota do filme: {noteMovie}.
''')