import hashlib

# - 1 Verificar os algoritmos disponiveis
print('#1\n' * 1)
print(hashlib.algorithms_available)

print('#2\n' * 1)
# - 2 Verificar algoritmos de acordo com o sistema operacional
print(hashlib.algorithms_guaranteed)

print('#3\n' * 1)
# - 3 Utilizando o SHA256
algorithm = hashlib.sha256()
print(algorithm.digest())
message = "A melhor forma de prever o futuro é criá-lo".encode()
algorithm.update(message)
print(algorithm.hexdigest())

print('#4\n' * 1)
# - 4 Utilizando o MD5

md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())