import tkinter as tk
from tkinter import messagebox
import sqlite3

class GerenciadorDeFilmes:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Filmes")
        self.root.geometry("400x300")  # Define o tamanho da janela

        # Conectar ao banco de dados SQLite (ou criar um novo arquivo, se não existir)
        self.conexao = sqlite3.connect('filmes.db')
        self.cursor = self.conexao.cursor()

        # Criar a tabela se ela não existir
        self.criar_tabela()

        # Rótulos e campos de entrada
        self.criar_widgets()

    def criar_tabela(self):
        # Cria a tabela de filmes, caso não exista
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS filmes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                ano INTEGER NOT NULL,
                nota REAL NOT NULL
            )
        ''')
        self.conexao.commit()

    def criar_widgets(self):
        # Label e Entry para ID
        self.label_id = tk.Label(self.root, text="ID:")
        self.label_id.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_id = tk.Entry(self.root, width=50)
        self.entry_id.grid(row=0, column=1, padx=10, pady=5)

        # Label e Entry para Nome
        self.label_nome = tk.Label(self.root, text="Nome:")
        self.label_nome.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_nome = tk.Entry(self.root, width=50)
        self.entry_nome.grid(row=1, column=1, padx=10, pady=5)

        # Label e Entry para Ano
        self.label_ano = tk.Label(self.root, text="Ano:")
        self.label_ano.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_ano = tk.Entry(self.root, width=50)
        self.entry_ano.grid(row=2, column=1, padx=10, pady=5)

        # Label e Entry para Nota
        self.label_nota = tk.Label(self.root, text="Nota:")
        self.label_nota.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_nota = tk.Entry(self.root, width=50)
        self.entry_nota.grid(row=3, column=1, padx=10, pady=5)

        # Botões
        self.botao_salvar = tk.Button(self.root, text="Salvar", command=self.salvar)
        self.botao_salvar.grid(row=4, column=0, padx=10, pady=10)

        self.botao_cancelar = tk.Button(self.root, text="Cancelar", command=self.cancelar)
        self.botao_cancelar.grid(row=4, column=1, padx=10, pady=10)

    def salvar(self):
        # Validação de entrada
        try:
            nome = self.entry_nome.get().strip()
            ano = int(self.entry_ano.get().strip())  # Verifica se o ano é um número
            nota = float(self.entry_nota.get().strip())  # Verifica se a nota é um número

            if nome == "":
                raise ValueError("O nome não pode estar vazio.")
            
            if not (0 <= nota <= 10):
                raise ValueError("A nota deve ser entre 0 e 10.")

            # Salvar no banco de dados
            self.cursor.execute('''
                INSERT INTO filmes (nome, ano, nota) 
                VALUES (?, ?, ?)
            ''', (nome, ano, nota))
            self.conexao.commit()

            messagebox.showinfo("Sucesso", f"Filme '{nome}' salvo com sucesso!")
            self.limpar_campos()

        except ValueError as e:
            messagebox.showerror("Erro", f"Entrada inválida: {e}")
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Erro ao salvar no banco de dados: {e}")

    def cancelar(self):
        # Limpar campos
        self.limpar_campos()

    def limpar_campos(self):
        # Limpa todos os campos de entrada
        self.entry_id.delete(0, tk.END)
        self.entry_nome.delete(0, tk.END)
        self.entry_ano.delete(0, tk.END)
        self.entry_nota.delete(0, tk.END)

    def __del__(self):
        # Fecha a conexão com o banco de dados quando o aplicativo for fechado
        self.conexao.close()

# Cria a janela principal
root = tk.Tk()
app = GerenciadorDeFilmes(root)

# Inicia o loop principal da interface gráfica
root.mainloop()
