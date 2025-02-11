import gradio as gr

def processar_dados(texto, numero, imagem, lista_texto, cor, opcoes):
    texto_revertido = texto[::-1]
    dobro_numero = numero * 2
    mensagem_imagem =  "Imagem recebida" if imagem else "Não há imagem Recebida"
    lista_processada = [[item for item in lista_texto.splitlines()]] if lista_texto else []

    return (
        texto_revertido,
        dobro_numero,
        mensagem_imagem,
        lista_processada,
        f"Cor selecionada {cor}",
        opcoes        
    )


interface = gr.Interface(
    fn=processar_dados,
    inputs=[
        gr.Textbox(label="Texto", placeholder="Digite o texto aqui..."),
        gr.Slider(minimum=0, maximum=100, label="Número", value=0),
        gr.Image(type="pil", label="Imagem"),
        gr.Textbox(label="Lista de itens", lines=4, placeholder="Item1\nItem2\n"),
        gr.ColorPicker(label="Selecione uma cor"),
        gr.CheckboxGroup(
            choices=["Opção1", "Opção2", "Opção3"],
            label="Escolha suas opções"
        )
    ],

    outputs=[
        gr.Textbox(label="Texto Revertido"),
        gr.Number(label="Dobro do Número"),
        gr.Textbox(label="Mensagem sobre a imagem"),
        gr.DataFrame(label="Itens da lista", headers=["Itens"]),
        gr.Textbox(label="Cor selecionada"),
        gr.Textbox(label="Opções Selecionadas")     
    ],

    title="Verificador de tipos de entrada e saída",
    description="Insira um texto, um número, uma imagem, lista de itens, uma cor para ver como a entrada é processada"
)

interface.launch()