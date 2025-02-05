from collections import Counter, namedtuple, deque
from operator import itemgetter
"""
ótimo para tuplas nomeadas
"""


# 1 - Lista de Frutas (Contagem)
fruits = ["Maça", "Banana", "Uva", "Pêra", "Banana"
          "Uva", "Maça", "Laranja", "Banana",
          "Abacaxi", "Tangerina", "Uva", "Pêra", "Banana"]

print(fruits)
print(Counter(fruits))

print('--' * 30)
# 2 - Utilizando tupla nomeada
game = namedtuple('game', ['game', 'price', 'note'])
g1 = game("Fifa 25", 90.50, 8.5)
g2 = game("Resident Evil 4 - Remake", 300, 10.0)
print(g1)
print(g2)

print('--' * 30)
# 3 - Ordenando Dicionários
students = {"Leandro": 29, "Cecilia": 0.8, "Camila": 23}

a = sorted(students.items(), key = itemgetter(1)) #0 - chave  #1 valor print(a)

print('--' * 30)
# 4 - Utilizando uma fila em abas extremidades
deq = deque([20, 40, 60, 80])
deq.appendleft(10)
print(deq)

deq.append(90)
deq.popleft()
deq.pop()
print(deq)