import random

# 1 - Seleciona valor aleatorio de uma lista
list1 = [7, 6, 4, 3, 2, 1]
print(f'# 1 {random.choice(list1)}')

# 2 - Gera um número aleatorio em intervalo de valores
r1 = random.randint(1, 20)
print(f'# 2 {r1}')

# 3 - Seleciona caractere aleatorio de uma string
name = "Leandro"
r2 = random.choice(name)
print(f'# 3 {r2}')

# 4 - Seleciona mais de um valor aleatorio
# random.sample(sequencia, tamanho)
print(f'# 4{random.sample(list1, 2)}')
print(f'# 4 {random.sample(list1, 3)}')
s = "Olá mundo"
print(f'# 4{random.sample(s, 2)}')

# 5 - Programa de sorteio
done = False
while not done:
    print("O que você deseja fazer?")
    print("1. Adivinhar o número")
    print("2. sair")

    choice = input(">")
    if choice == "1":
        print("============== Adivinhe um número de  1 a 10 ======================")
        number = int(input("Digite um número de 1 a 10:\n"))
        result = random.randint(1, 10)
        if number == result:
            print(f"O Número que você selecionou foi {number} e o sorteio foi {result}")
            print("Você acertou!")
        else:
            print(f"O Número que você selecionou foi {number} e o sorteio foi {result}")
            print("Você errou!")
    elif choice == "2":
        done = True
    else:
        print("Opção inválida, escolha a opção '1' ou '2'.")

