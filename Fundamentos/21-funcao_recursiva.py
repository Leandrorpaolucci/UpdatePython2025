"""
    Fatorial de um número
    1 -> 1 * 1
    2 -> 2 * 1
    3 -> 3 * 2 * 1
    
"""
# 1 - Fatorial de um número
def factorial(number):
    if number == 1:
        return 1
    return (number * factorial(number - 1))

number = int(input("#1 - Digite o número para calcular o fatorial:\n"))
print(f'O fatorial de {number} é {factorial(number)}')

print('\n')
# 2 - Soma total de um número

def total_sum(num):
    if num == 1:
        return 1
    else:
        return (num + total_sum(num - 1))
    
num = int(input("#2 - Digite o número para a soma:\n"))
print(f"A soma total {num} é {total_sum(num)}")
