import pprint
filmsDict = {
    "Yugioh": {
        "Ano Lançamento": 1996,
        "Nota Anime": 9.0,
        "Genero": ["Desenho", "Anime"]
},
    "Cavaleiros dos zodiaco": {
        "Ano Lançamento": 1985,
        "Nota Anime": 9.8,
        "Genero": ["Desenho", "Anime"]
    },
    
    "Dragon Ball Z":{
        "Ano Lançamento": 1989,
        "Nota Anime": 9.5,
        "Genero": ["Desenho", "Anime"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)

print("--" * 40)
# 1 - buscar uma informação dentro de um dicionário aninhado
print(f'#1 {filmsDict["Yugioh"]["Genero"]}\n')

# 2 - Adicionar novo item
filmsDict["Yugioh"]["criador"] = "Kazuki Takahashi"
print(f'#2 {filmsDict["Yugioh"]}\n')

# 3 - excluir um dicionário
del filmsDict["Yugioh"]
pp.pprint(filmsDict)