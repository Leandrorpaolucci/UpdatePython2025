class Biblioteca:
    bibliotecas = []

    def __init__(self, nome):
        self.nome = nome
        self._ativo = False #Atributo Privado com "_"
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome
    
    def listar_bibliotecas():
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome} | {biblioteca.ativo}")

    def alterna_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return "Ativada" if self._ativo else "Desativada"
    

biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_cidade.alterna_estado()
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

print(biblioteca_cidade)
print(biblioteca_shopping)

Biblioteca.listar_bibliotecas()
