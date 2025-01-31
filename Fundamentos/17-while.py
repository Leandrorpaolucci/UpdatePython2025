# Lista de filmes

moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

# 1- iterando valores de uma lista de filmes usando while

index = 0
while index < len(moviesList):
    print(f'EX # 1 - item da lista: {index}, {moviesList[index]}')
    index += 1

# 2 - Quando a condição for atendida, o loop será encerrado [Utilizando Break]
print('--' * 20)
i = 0
while i < (len(moviesList)):
    if moviesList[i] == "Inception":
        break
    print(f'#EX 2 - item da lista: {i}, {moviesList[i]}')
    i += 1

print('--' * 20)

# 3 - Quando a condição for atendida, o loop via para próxima iteração
i = 0
while i < (len(moviesList)):
    if moviesList[i] == "Inception":
        i += 1
        continue
    print(f'#EX 3 - item da lista: {i}, {moviesList[i]}')
    i += 1

print('--' * 20)
# 4 - Avaliação do filme com While
movieName = input("Digite o nome do filme:\n ")
movieRating = int(input("Digite quantas avaliações deseja fazer:\n "))
total = 0
contador = 0

while contador < movieRating:
    nota = float(input("Digite a nota para o filme:\n "))
    total += nota
    contador +=1

if movieRating > 0:
    avarage = total / movieRating
else:
    avarage = 0
print(f'A média de avaliação do filme {movieName} é: {avarage:.2f}')


