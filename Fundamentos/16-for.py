# Lista de filmes

moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]
numeros = [10, 20, 30, 40]

# 1 - iterar valores de uma lista
for movie in moviesList:
    print(f'#1 Filme: {movie}')

print('--' * 35)

# 2 - Quando a condição for atendida será encerrado

for movie in moviesList:
    if movie == "Inception":
        break
    print(f'#2 Filme: {movie}')

print('--' * 35)

# 3 - Quando a condição for atendida, o Loop vai para próxima iteração
for movie in moviesList:
    if movie == "Inception":
        continue
    print(f'#3 Filme: {movie}')

# 4 - Avaliação do filme:
movieName = input("Digite o nome do filme:\n ")
movieRating = int(input("Digite quantas avaliações deseja fazer:\n "))
total = 0

for i in range(movieRating):
    note = float(input("Digite a nota para o filme:\n "))
    total += note

if movieRating > 0:
    avarage = total / movieRating
else:
    avarage = 0

print(f'A media de avaliação do filme {movieName} é:{avarage:.2f}')



