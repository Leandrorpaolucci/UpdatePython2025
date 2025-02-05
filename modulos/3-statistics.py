import statistics

# 1 - Aplicando a média
print(statistics.mean([3, 2, 3, 8, 9])) # soma todos e divide pelo número de casas decimais

# 2 - aplicando mediana
print(statistics.median([1, 2, 4, 8, 9]))
print(statistics.median([1, 2, 3, 7, 8, 9]))

# 3 Aplicando a moda
print(statistics.mode([2, 5, 3, 2, 8, 3, 9, 4, 2, 5, 6]))

# 4 desvio padrão

"""
    Quanto mais próximo de 0 for o desvio padrão, significa que os dados
    do conjunto estão menos despersos.

"""

print(statistics.stdev([1, 1,5, 2, 2.5, 3, 3.5, 4, 4.5]))