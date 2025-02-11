import gradio as gr

def somar(x, y):
    return x + y

print(somar(5, 6))

interface = gr.Interface(
    fn=somar,
    inputs=["number", "number"]
    outputs="number",
    title="Calculadora de soma",
    description="Insira dois números para obter a soma",
    theme="default",
)


interface.launch()