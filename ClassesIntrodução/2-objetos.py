class Game:
    nome = ""
    AnoLancamento = 0
    multiJogadores = False
    nota = 0
    
# Primeiro Jogo
game1 = Game()
game1.name = "Counter-Strike"
game1.AnoLancamento = 2000
game1.multiJogadores = True
game1.nota = 9.5

print("### Dados do jogo ###")
print(f"Nome do jogo: {game1.name}\nAno Lançamento:{game1.AnoLancamento}")

# Segundo Jogo
game2 = Game()
game2.name = "Combat Arms"
game2.AnoLancamento = 2009
game2.multiJogadores = True
game2.nota = 8.0

print("### Dados do jogo ###")
print(f"Nome do jogo: {game2.name}\nAno Lançamento:{game2.AnoLancamento}")