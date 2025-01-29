filmslist = ["Avatar a lenda de Ang", "Cavaleiros dos zodiacos", "Yugioh", "Bob Esponja", "Dragon Ball"]

# 1 - Tamanho da lista - Método Len
print(len(filmslist))

# 2 - Recuperar um item da lista pelo seu nome
print(filmslist.index("Yugioh")) # retorna o número do item na lista

# 3 - Adcionar um item ao final da lista
filmslist.append("One Piece")
print(f" #3 {filmslist}")

# 4 - Ordenar lista
filmslist.sort()
print(f" #4 {filmslist}")

# 5 - Copiar os itens de uma lista para outra
filmesCopy = filmslist.copy()
filmesCopy.remove("Avatar a lenda de Ang")
print(f" #5 {filmesCopy}")

# 6 Remove todos os itens da lista
filmesCopy.clear()
print(f" #6 {filmesCopy}")