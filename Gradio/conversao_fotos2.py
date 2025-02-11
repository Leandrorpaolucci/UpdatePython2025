import gradio as gr
from PIL import Image
import os
from docx import Document
from fpdf import FPDF

def converter_imagem(input_image, tipo_conversao):
    # Obter o nome do arquivo original (sem a extensão)
    nome_original, _ = os.path.splitext(os.path.basename(input_image))
    
    # Abrir a imagem
    img = Image.open(input_image)
    
    # Definir a nova extensão
    extensao = tipo_conversao.split(' ')[-1].lower()
    output_image_path = f"{nome_original}_convertido.{extensao}"

    # Realizar a conversão
    if tipo_conversao == "JPG para JPEG":
        img.save(output_image_path, "JPEG")
    elif tipo_conversao == "PNG para JPG":
        img.convert("RGB").save(output_image_path, "JPEG")
    elif tipo_conversao == "JPEG para PNG":
        img.save(output_image_path, "PNG")
    elif tipo_conversao == "JPEG para JPG":
        img.save(output_image_path, "JPEG")
    
    return output_image_path

def converter_doc_para_pdf(input_doc):
    # Obter o nome do arquivo original (sem a extensão)
    nome_original, _ = os.path.splitext(os.path.basename(input_doc))
    
    # Abrir o arquivo DOCX
    doc = Document(input_doc)
    pdf_output_path = f"{nome_original}_convertido.pdf"
    
    # Criar o PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Adicionar conteúdo do DOCX ao PDF
    for para in doc.paragraphs:
        pdf.multi_cell(0, 10, para.text)
    
    # Salvar o PDF
    pdf.output(pdf_output_path)
    
    return pdf_output_path

# Função para gerenciar a interface de conversão
def interface_conversao(input_file, tipo_conversao):
    if input_file.endswith(('.jpg', '.jpeg', '.png')):
        return converter_imagem(input_file, tipo_conversao)
    elif input_file.endswith('.docx'):
        return converter_doc_para_pdf(input_file)

# Interface Gradio com tema válido
interface = gr.Interface(
    fn=interface_conversao,
    inputs=[
        gr.File(label="Escolha o arquivo para conversão", type="filepath"),
        gr.Radio(
            choices=[
                "JPG para JPEG", "PNG para JPG", "JPEG para PNG", "JPEG para JPG",
                "DOCX para PDF"
            ],
            label="Escolha o tipo de conversão"
        )
    ],
    outputs=gr.File(label="Baixar arquivo convertido"),
    title="Conversor de Arquivos",
    description="Este aplicativo permite converter imagens (JPG, PNG, JPEG) entre si e também documentos DOCX para PDF.",
    theme=gr.themes.Soft()  # Definindo um tema válido
)

# Executando a interface
interface.launch()
