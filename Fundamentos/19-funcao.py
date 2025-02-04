# 1 - função para imprimir uma mensagem
def welcome(message="Bem vindo ao sistema de filmes."):
    print(message)


# 2 Função para calcular a média de notas
def calculate_average():
    while True:
        try:
            num_ratings = int(input("Digite quantas avaliações deseja fazer para o filme:\n"))
            if num_ratings <= 0:
                print("Você precisa inserir um número positivo de avaliações.")
                continue
            break
        except ValueError:
            print("Por favor, insira um número inteiro válido para o número de avaliações.")

    ratings = []
    for i in range(num_ratings):
        while True:
            try:
                note = float(input(f"Digite a nota para o filme ({i + 1}/{num_ratings}):\n"))
                if 0 <= note <= 10:
                    ratings.append(note)
                    break
                else:
                    print("A nota deve estar entre 0 e 10. Tente novamente.")
            except ValueError:
                print("Por favor, insira um número válido para a nota.")

    average = sum(ratings) / num_ratings
    return average

print(f'A média é: {calculate_average():.2f}')

def create_movie():
    name = str(input('Digite o nome do filme:\n '))
    yearLaunch = int(input('Digite o ano do lançamento do fime:\n'))
    moviePrice = float(input("Digite o preço do filme:\n"))
    rating = float(input('Digite a nota do filme:\n'))
    print(f'{name}, ({yearLaunch}) - R$:{moviePrice} - nota: {rating}')

create_movie()