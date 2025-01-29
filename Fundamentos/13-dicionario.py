filmInception = {
    "Titulo": "Yugioh",
    "Ano Lançamento": 1998,
    "Nota Anime": 8.8,
    "Genero": ["Desenho", "Anime"]
}

# 1 - print
print(f'#1 {filmInception}\n')
# 2 - tamanho do dicionario
print(f'#2 tamanho: {len(filmInception)}\n')
# 3 - tipo do dicionario
print(f'#3 {type(filmInception)}\n')

# 4 - Recuperar um elemento do dicionario
print(filmInception["Genero"]) # via colchete
print(filmInception.get("Genero")) # via método get

# 5 - Buscar apenas as chaves do dicionario
print(filmInception.keys())

# 6 - buscar apenas os valores do dicionario
print(filmInception.values())

# 7 - Buscar itens do dicionario com chave e valor
print(filmInception.items()) # tuple (tupla)

# 8 - adicionar itens ao dicionário
filmInception["criador"] = "Kazuki Takahashi" #verifica se existe e cria a chave e valor
print(f'#8 {filmInception}\n')

# 9 - Atualizar itens ao dicionario
filmInception.update({"Nota Anime": 9.0})
print(f'#9 {filmInception}\n')

# 10 - Remover itens do dicionario

filmInception.pop("criador")
print(f'#10 {filmInception}\n')