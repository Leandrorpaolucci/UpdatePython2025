import tkinter as tk


# 1 - Criando a nossa janela

janela = tk.Tk()
janela.geometry("550x350")
janela.title("Frases")

#2 Adicionando um frame
frame = tk.Frame(janela)
frame.pack(padx=10, pady=10, fill='x', expand=True)

#3 - adicionando o label
label = tk.Label(frame, text="Olá Mundo!")
label.pack(fill='x', expand=True)

# 4 - adicionar o input text
frase_lab = tk.Label(frame, text="Frase")
frase_lab.pack(fill='x', expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x', expand=True)

# 5 - Função para alterar o texto da label

def click():
    label.config(text=frase_inp.get())


# 6 - Adicionando Botão
button = tk.Button(frame, text="Enviar", command=click)
button.pack()


janela.mainloop()