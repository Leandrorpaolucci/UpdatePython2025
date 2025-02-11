#Classe Pai (Super Classe) - Generalista

class Game:
    total_games = 0 # Variável de classe para contar o número total de jogos
    def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0):
        self.name = name  
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        Game.total_games += 1
        self.totalEvaluation = 0
        self.evaluators = 0
        
    def __str__(self):
        return f"Game: {self.name}"
    
    def technical_sheet(self):
        print("###Dados do Jogo###")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de Lançamento: {self.yearLaunch}")
        print(f"Modo multiplayer?: {self.multiplayer}")
        print(f"Avaliação do Jogo: {self.note}\n")
        
    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1
        
    def average(self):
        print(f"Média do jogo {self.name}: {self.totalEvaluation / self.evaluators}")
        
# Classe derivada (SubClasse) - Especializada
class SinglePlayerGame(Game):
    def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0, storyline=""):
        super().__init__(name, yearLaunch, multiplayer, note)
        self.storyline = storyline

    def technical_sheet(self):
        super().technical_sheet()
        print(f"Enredo: {self.storyline}\n")

multi_game = Game("FortNite", 2017,  True, 8.0)
multi_game.technical_sheet()

single_player = SinglePlayerGame("The Last Of Us II", 2020, False, 9.5, "Emocionante historia de sobrevivencia.")
single_player.technical_sheet()