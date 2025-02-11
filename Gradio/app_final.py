import gradio as gr
from collections import Counter
import string

def converter_temperatura(temperatura, escala):
    if escala == "Celsius":
        return (temperatura * 9/5) + 32
    else:
        return (temperatura - 32) * 5/9
    
def analisar_texto(texto):
    texto_limpo = texto.translate(str.maketrans("", "", string.punctuation))
    palavras = texto_limpo.split()
    num_palavras = len(palavras)
    num_caracteres = len(texto)
    
    frequencia = Counter(palavras)
    frequencia_html = "<br>".join([f"{palavra}: {contagem}" for palavra, contagem in frequencia.items()])
    
    return num_palavras, num_caracteres, frequencia_html

def criar_relatorio(temperatura, escala, condicao, texto):
    temperatura_convertida = converter_temperatura(temperatura, escala)
    num_palavras, num_caracteres, frequencia = analisar_texto(texto)
    
    relatorio = (
        f"**Relatório de Clima**\n\n"
        f"Temperatura: {temperatura_convertida:.2f}{'F' if escala=='Celsius' else 'C'}\n"
        f"Condição: {condicao}\n"
        f"Descrição: {texto}\n\n"
        f"Número de Palavras: {num_palavras}\n"
        f"Número de Caracteres: {num_caracteres}\n"
        f"Frequência de Palavras: {frequencia}\n"   
    )
    
    return relatorio

iface = gr.Interface(
    fn=criar_relatorio,
    inputs=[
        gr.Number(label="Temperatura", precision=2),
        gr.Radio(choices=["Celsius", "Fahrenheit"], label="Converter de"),
        gr.Dropdown(
            choices=["Ensolarado", "Nublado", "Chuvoso", "Frio", "Quente"],
            label="Condição do Clima"
        ),
        gr.Textbox(label="Descrição do Dia", lines=4, placeholder="Descreva o dia")
    ],
    outputs=gr.Markdown(label="Relatório do CLima"),
    title="Relatório de CLima",
    description="Crie um relatório de clima com temperatura"
)

iface.launch()