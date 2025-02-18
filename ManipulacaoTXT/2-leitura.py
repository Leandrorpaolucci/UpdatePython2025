"""
Arquivos - Modos de operação:
    1. Modo 'W' - Write  / Escrever
    2. Modo 'A' - Append / Adicionar
    3. Modo 'R' - Read / Leitura
"""

caminho = r'C:\PythonUpdate2025\UpdatePython2025\ManipulacaoTXT'
with open(f"{caminho}/names.txt", "r", encoding="utf-8") as arquivo:
#    print(arquivo.read())
    for linha in arquivo:
        print(f"Olá, {linha.rstrip()}")