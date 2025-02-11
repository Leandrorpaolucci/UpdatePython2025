class Game:
    def __init__(self, nome="", anoLancamento=0, multiJogador=0, nota=0):
        self.nome = nome
        self.anoLancamento = anoLancamento
        self.multijogador = multiJogador
        self.nota = nota

    def __str__(self):
        return f"Game: {self.nome}, Ano lançamento: {self.anoLancamento}, Multijogador: {self.multijogador}, Nota Final: {self.nota}"

    
game1 = Game("Combat Arms", 2009, True, 9.5)
game2 = Game("Counter-Strike", 2000, True, 9.5)
print(game1)
print(game2)

