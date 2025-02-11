class Game:
    total_games = 0 # Variavel de classe para contar o número total de jogos
    def __init__(self, nome="", anoLancamento=0, multiJogador=0, nota=0):
        self.nome = nome
        self.anoLancamento = anoLancamento
        self.multijogador = multiJogador
        self.nota = nota
        self.totalAvaliacoes = 0
        self.numAvaliacoes = 0  # Renomeado de "avaliacao" para "numAvaliacoes"
        Game.total_games += 1

    def __str__(self):
        return f"Game: {self.nome}, Ano lançamento: {self.anoLancamento}, Multijogador: {self.multijogador}, Nota Final: {self.nota}\n"

    def ficha_tecnica(self):
        print(f"Nome do jogo: {self.nome}")
        print(f"Ano de lançamento do jogo {self.anoLancamento} ")
        print(f"Multi-Jogador: {self.multijogador}")
        print(f"Nota final do jogo: {self.nota}\n")

    def adicionar_avaliacao(self, nota):
        self.totalAvaliacoes += nota
        self.numAvaliacoes += 1

    def mediaAvaliacoes(self):
        if self.numAvaliacoes > 0:
            media = self.totalAvaliacoes / self.numAvaliacoes
            print(f'Média das avaliações do jogo {self.nome}: {media}')
        else:
            print(f'O jogo {self.nome} ainda não tem avaliações suficientes para calcular a média.')

# Criando os objetos
game1 = Game("Combat Arms", 2009, True, 9.5)
game2 = Game("Counter-Strike", 2000, True, 9.5)
game3 = Game("Warface", 2013, True, 9.0)

# Chamando os métodos
game1.ficha_tecnica()
game1.adicionar_avaliacao(9.0)
game1.adicionar_avaliacao(7.0)
game1.mediaAvaliacoes()

game2.ficha_tecnica()
game2.adicionar_avaliacao(5.0)
game2.adicionar_avaliacao(6.0)
game2.mediaAvaliacoes()

game3.ficha_tecnica()
game3.adicionar_avaliacao(5.0)
game3.adicionar_avaliacao(6.0)
game3.mediaAvaliacoes()


# Exibindo um número total de jogos criados
print(f"Total de jogos criados: {Game.total_games}")