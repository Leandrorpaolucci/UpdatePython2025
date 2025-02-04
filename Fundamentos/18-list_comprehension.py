# 1 - Listando valores de 0 a 10 que sejam menores que 4
numbersLessThanFour = [i for i in range(11) if i < 4]
print(f'1 - Números menores que 4: {numbersLessThanFour}\n')

# 2 - Lista de filmes
movieList = ['Titanic', 'The Godfather', 'Inception', 'Jurassic Park']
print(f'1 - Lista de filmes: {movieList}\n')

# 3 - Filmes com a letra 'k' no título (poderia ser qualquer letra)
movieWithK = [movie for movie in movieList if 'k' in movie.lower()]
print(f'2 - Filmes com a letra "k" no título: {movieWithK}\n')

# 4 - Filmes que você já assistiu (excluindo "Jurassic Park")
moviesWatched = [movie for movie in movieList if movie != "Jurassic Park"]
print(f'3 - Filmes que eu já assisti: {moviesWatched}\n')

# 5 - Função para buscar filmes por nome
def buscar_filme(nome):
    foundMovies = [movie for movie in movieList if nome.lower() in movie.lower()]
    if foundMovies:
        print(f'4 - Filmes encontrados com o nome "{nome}":')
        for movie in foundMovies:
            print(movie)
    else:
        print(f'Nenhum filme encontrado com o nome "{nome}".')

# 6 - Loop para buscar filmes
while True:
    searchMovie = input("Digite o nome do filme para buscar na lista (ou 'sair' para encerrar):\n")
    if searchMovie.lower() == "sair":
        print('Programa encerrado')
        break
    buscar_filme(searchMovie)
