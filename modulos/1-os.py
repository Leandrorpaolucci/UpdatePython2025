import os

# Consultar funcionalidades do módulo os

# 1- retorna a pasta atual
print(os.getcwd())

# 2 - listar arquivos e pastas
print(os.listdir())

# 3 - listar a versão do sistema operacional
os.system('ver')

# 4 - Configurações da maquina
os.system('systeminfo')

# 5 - limpar o terminal
os.system('cls')

# 6 - desligar o computador
os.system('shutdown /s')

# 7 cancelar o desligamento
os.system('shutdown /a')

# 6 - desligar o computador imediatamente
#os.system('shutdown /s /t 0')

def turn_off_one_hour():
    os.system('shutdown /s /t 3600') # 1 hora o desligamento

def turn_off_an_hour():
    os.system('shutdown /s /t 1800')

def cancel_shutdown():
    os.system('shutdown /a')

turn_off_an_hour()
