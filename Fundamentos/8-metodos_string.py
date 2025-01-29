movieName = "Toop Gun"

movieDescription = '''
    Top Gun Maverick, é um filme de aviação e aventura,
    muito consagrado na industria.
'''

print(movieName.upper()) # letras maiúsculas
print(movieName.lower()) # letras minusculas
print(movieName.capitalize()) # primeira letra maiúscula
print(movieName.title()) # primeira letra maiúscula
print(movieName.center(10, '-')) # retorna a string centralizada com caractere de preenchimento
print(movieName.find('u')) # procura um caractere e retorna o índice
print(movieName.count("o")) # conta quantas letras possuem na string com o mesmo nome solicitado
print(movieName.replace('Top', "Matrix")) # replace altera um nome desde que seja True
print(movieDescription.split(','))
