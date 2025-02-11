import gradio as gr

def reverter_texto(texto):
    texto_revertido = texto[::-1]
    return texto_revertido, len(texto_revertido)

# print(reverter_texto("Olá mundo"))
interface = gr.Interface(
    fn=reverter_texto,
    inputs="text",
    outputs=["text", "number"],
    title="Reversor de Texto",
    description="Insira um texto para revertê-lo e contar os caracteres"
)

interface.launch()