filmsSet = {
    "Avatar a lenda de Ang",
    "Cavaleiros dos zodiacos",
    "Yugioh",
    "Bob Esponja",
    "Dragon Ball"
}

#print(type(filmsSet))

# 1 - Buscar o tamanho do set
print(f'#1 {len(filmsSet)}\n')

# 2 - True e 1 são considerados os mesmos valores.

exampleSet = {"Inception", True, 1, 8.7}
print(f'#2 {exampleSet}\n')

# 3 - Adcionar item de outro set
filmsSet.update(exampleSet)
print(f'#3 {filmsSet}\n')

# 4 - Remover item no set
filmsSet.remove(True)
filmsSet.remove(8.7)
print(f'#4 {filmsSet}\n')
