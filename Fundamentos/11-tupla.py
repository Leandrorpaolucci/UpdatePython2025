filmsTuple = ("Avatar a lenda de Ang", "Cavaleiros dos zodiacos", "Yugioh", "Bob Esponja", "Dragon Ball")
print(type(filmsTuple))

''''
Alguns métodos da lista podem ser reaproveitados na tupla...
'''

# 1 - Buscar os dois primeiros itens da tupla
print(filmsTuple[:2])

# 2 Buscar o último item da tupla
print(filmsTuple[-1])

# 3 buscar itens até uma determinada posição
print(filmsTuple[:3])

# 4 Buscar filmes de uma posição em diante
print(filmsTuple[2:])

# 5 Recuperar um item da tupla pelo nome
print(filmsTuple.index("Yugioh"))