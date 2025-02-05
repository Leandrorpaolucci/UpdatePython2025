import re

text = "Udemy - uma plataforma com muitos cursos."
# 1 - índice inicial e final de palavras
# O r significa uma raw string (string bruta)

match = re.search(r'Udemy', text)
print(f'índice inicial: {match.start()}')
print(f'índice inicial: {match.end()}')

# 2 - Buscando o índice que possui o ponto
site = "https://udemy.com"
match1 = re.search(r'\.', site)
print(match1)

# 3 - Buscando uma lista de caracteres dentro de uma frase
pattern = "[a-f]"
result = re.findall(pattern, text)
print(result)

# 4 Verificando o inicio de uma string
rule = r'^A'
phrases = ['A casa está suja', 'O dia está lindo', 'Vamos passear']
for f in phrases:
    if re.match(rule, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não corresponde: {f}")

# 5 Verificando o final de uma string
rule_end = r'!$'
phrases2 = "O dia está lindo"
match3 = re.search(rule_end, phrases2)
if match3:
    print("Sim, corresponde.")
else:
    print("Não corresponde.")