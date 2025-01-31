# 1 - listar valores de 0 a 10 que sejam menores do que 4

listNumbers = [iteração for iteração in range(10) if iteração < 4 ]
print(listNumbers)


# Lista de filmes
moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]


# 2 - Filmes que possuem a letra 'e' no titulo
letra = 'k'
moviesWithE = [filme for filme in moviesList if letra in filme.lower()]
print(f'#2 Filmes que possuem a letra: {letra} : {moviesWithE}')

# 3 - Filmes que eu assisti
filme_nao_assistido = "Jurassic Park"
moviesWatched = [filme for filme in moviesList if filme != filme_nao_assistido]
print(f'#3 Filmes que eu NÃO assisti {filme_nao_assistido}: {moviesWatched}')

# 4 - Encontrando um filme pelo nome

while True:
    searchName = input("#4 Digite o nome do filme para buscar na lista (ou sair para encerrar):\n")
    if searchName.lower() == "sair":
        print('Programa encerrado!')
        break

    foundMovies = [filme for filme in moviesList if searchName.lower() in filme.lower()]
    if foundMovies:
        print(f'Filme(s) Encontrado(s) com o nome: {searchName}:')
        for foundMovies in foundMovies:
            print(foundMovies)
    else:
        print(f'Nenhum filme foi encontrado com o nome {searchName}. Tente novamente.')

    