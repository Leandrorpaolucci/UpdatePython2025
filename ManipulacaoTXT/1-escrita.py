name = input('Digite o nome do aluno:\n')


"""
Arquivos - Modos de operação:
    1. Modo 'W' - Write  / Escrever
    2. Modo 'A' - Append / Adicionar
    3. Modo 'R' - Read / Leitura
"""

# Implementação 1 - Cria e escreve 'W'

caminho = r'C:\PythonUpdate2025\UpdatePython2025\ManipulacaoTXT'
#file = open(f'{caminho}/names.txt', 'w')
#file.write(f"{name}\n")
#file.close()


# Implementação 2 - Adiciona
# file = open(f'{caminho}/names.txt', 'a', encoding='utf-8')
# file.write(f"{name}\n")
# file.close()

# Implementação 3 -  utilizando with e apelidando com as file
with open(f"{caminho}/names.txt", 'a', encoding='utf-8') as arquivo:
    arquivo.write(f"{name}\n")
