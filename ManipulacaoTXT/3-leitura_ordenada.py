names = []

"""
Arquivos - Modos de operação:
    1. Modo 'W' - Write  / Escrever
    2. Modo 'A' - Append / Adicionar
    3. Modo 'R' - Read / Leitura
"""

caminho = r'C:\PythonUpdate2025\UpdatePython2025\ManipulacaoTXT'

with open(f"{caminho}/names.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        names.append(linha.rstrip())

for name in sorted(names):
    print(f'Olá {name}')