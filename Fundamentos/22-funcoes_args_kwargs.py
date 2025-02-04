"""
1. *args: Utilizamos ele quando não temos certeza
    de quantos argumentos queremos em uma função

2. Os argumentos são passados com uma tupla

3. **kwargs - Além dos valores, podemos passar também as respectivas chaves para cada argumento

"""

def sum(*args):
    sum_total = 0
    for n in args:
        sum_total += n
        print(f'A soma é: {sum_total}')



# 2 - apresentação de Cursos
def presentation(**data):
    for key, value in data.items():
        print(f'{key} - {value}')

print(' # 2 Lista de cursos:\n')
presentation(Name="Python", Category="Backend", Level="Iniciante")
presentation(Name="Visão Computacional Python", Category="IA", Level="Avançado")
presentation(Name="Dashboards com Dash", Category="Data Science", Level="Intermediario")