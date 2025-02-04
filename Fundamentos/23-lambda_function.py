# Função de potencia de um número
power = lambda num: num ** 2

print(f"# 1 - A elevação é {power(5)}")

# Função que verifica se o número é par
is_even = lambda x: x % 2 == 0
print(f"# 2 - Disião Impar/Par = True or False: {is_even(27)}")

# Função que divide um número por outro
div_num = lambda x, y: x / y
print(f'A divisão é: {div_num(10, 2)}')

# Função que inverte uma string

reverse_string = lambda s: s[::-1]
print(reverse_string('Cecilia Oliveira Paolucci'))

# Funcionalidades relacionadas aos filmes
movie_list = ["Titanic", "The GodFather", "inception", "Jurassic Park", "The Matrix"]
ratings = {
    "Titanic":[8.5, 9.0, 7.5],
    "The GodFather":[9.5, 8.0, 6.5],
    "inception":[7.5, 4.0, 4.5],
    "Jurassic Park":[5.5, 5.0, 6.5],
    "The Matrix":[9.5, 10.0, 8.5],
}

# Função para calcular a média de avaliações de um filme
average_rating = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])

print(f'Média de avaliação do filme The Matrix: {average_rating("The Matrix")}')

# Função para verificar se um filme está na lista
check_movie = lambda movie_name: movie_name in movie_list
print(f'Inception está na lista? {check_movie("Inception")}')

# Função para recomendar um filme com base na sua avaliação
recomended_movie = lambda movie_name: f"Recomendo assistir {movie_name} com media de {average_rating(movie_name):.2f}"
print(f'{recomended_movie("Titanic")}')
