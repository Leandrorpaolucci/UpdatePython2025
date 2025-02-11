import gradio as g

def somar(x, y):
    return x + y


iface = g.Interface(
    fn=somar,
    inputs=["number", "number"],
    outputs="number",
    title="Calculadora",
    description="Insira dois números para obter a soma",
    theme="default"
)

iface.launch()