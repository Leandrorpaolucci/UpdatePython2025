import gradio as gr

def customizar_texto(texto, cor_fundo, cor_texto, tamanho_fonte, 
                     estilo_fonte):
    # Configura o estilo do texto
    estilo = (
        f"color: {cor_texto}; "
        f"background-color: {cor_fundo}; "
        f"font-size: {tamanho_fonte}px; "
        f"font-family: {estilo_fonte};"
    )

    return f'<div style="{estilo}">{texto}</div>'

interface = gr.Interface(
    fn=customizar_texto,
    inputs=[
        gr.Textbox(label="Texto", placeholder="Digite o seu texto aqui..."),
        gr.ColorPicker(label="Cor de fundo"),
        gr.ColorPicker(label="Cor de texto"),
        gr.Slider(minimum=10, maximum=100, label="Tamanho da fonte", value=20),
        gr.Radio(
            choices=["Arial", "Courier New", "Georgia", "Times New Roman", "Verdana"],
            label="Estilo da fonte"
        )
    ],
    outputs=gr.HTML(label="Texto Customizado"),
    title="Customizador de texto",
    description="Customize o seu texto com cor, tamanho e estilo da fonte."
)

interface.launch()
