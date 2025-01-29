num1 = int(input('Digite o primeiro número:\n'))
num2 = int(input('Digite o segundo número:\n'))

# Aritméticos
sum = num1 + num2
sub = num1 - num2  #
div = num1 / num2  # divisão
mult = num1 * num2 # multiplicação
mod =  num1 % num2 # resto da divisão
exp = num1 ** num2 # exponenciação

print(f"""
* * * * * * * * Resultado * * * * * * * * 

Soma: {num1} + {num2} = {sum}
Subtração: {num1} - {num2} = {sub}
Divisão: {num1} / {num2} = {div}
Multiplicação: {num1} * {num2} = {mult}
Mod (Resto da divisão): {num1} % {num2} = {mod}
Exp (Exponenciação): {num1} ** {num2} = {exp}    
\n""")
# Operadores de Comparação
print('Operadores de Comparação\n')
bigger = num1 > num2
print(f'O 1º número digitado {num1} é maior que o 2º número digitado {num2} = {bigger}') 
smaller = num1 < num2
print(f'O 1º número digitado {num1} é menor que 2º número digitado {num2} = {smaller}') 
equal = num1 == num2
print(f'O 1º número digitado {num1} é igual o 2º número digitado {num2} = {equal}') 
different = num1 != num2
print(f'O 1º número digitado {num1} é diferente do 2º número digitado {num2} = {different}') 
bigger_equal = num1 >= num2
print(f'O 1º número digitado {num1} é maior ou igual ao  2º número digitado {num2} = {bigger_equal}') 
smaller_equal = num1 <= num2
print(f'O 1º número digitado {num1} é menor ou igual ao 2º número digitado {num2} = {smaller_equal}') 


