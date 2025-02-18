import os

caminho = r'C:\PythonUpdate2025\UpdatePython2025\ManipulacaoTXT'

def adicionar_contato():
    nome = input('Informe o nome do contato:\n')
    endereco = input('Informe o endereço:\n')
    telefone = input('Informe o telefone:\n')

    contato = f"Nome: {nome} \nEndereço: {endereco} \nTelefone: {telefone}\n"
    
    # Garante que o arquivo exista antes de escrever
    if not os.path.exists(f'{caminho}/contatos.txt'):
        with open(f'{caminho}/contatos.txt', "w", encoding="utf-8") as arquivo:
            pass  # Apenas cria o arquivo vazio se não existir

    with open(f'{caminho}/contatos.txt', "a", encoding="utf-8") as arquivo:
        arquivo.write(contato)


def visualizar_contatos():
    if not os.path.exists(f"{caminho}/contatos.txt"):
        print("Lista de contatos está vazia")
        return 
    
    try:
        with open(f"{caminho}/contatos.txt", "r", encoding="utf-8") as arquivo:
            contatos = arquivo.read()
            print("Lista de contatos:")
            print(contatos)
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")


def deletar_todos_os_contato():
    if not os.path.exists(f"{caminho}/contatos.txt"):
        print("Lista de contatos está vazia")
        return 
    
    try:
        with open(f"{caminho}/contatos.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("")  # Apaga todos os contatos

        print("Contatos excluídos com sucesso!")
    except Exception as e:
        print(f"Erro ao excluir os contatos: {e}")
