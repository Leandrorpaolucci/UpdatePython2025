import gradio as gr

# Função que será chamada ao enviar o formulário
def cadastrar_candidato(nome, idade, sexo, setor, escolaridade, rua, numero, bairro, cep, cidade, estado):
    return f"""
    **📋 Dados Cadastrados:**  
    - **Nome:** {nome.title()}  
    - **Idade:** {idade}  
    - **Sexo:** {sexo}  
    - **Setor:** {setor}  
    - **Escolaridade:** {escolaridade}  

    **📍 Endereço:**  
    - **Rua:** {rua.title()}, Nº {numero}  
    - **Bairro:** {bairro.title()}  
    - **CEP:** {cep}  
    - **Cidade:** {cidade.title()} - {estado.title()}  
    """

# Interface do Gradio
interface = gr.Interface(
    fn=cadastrar_candidato,  # Função que será chamada
    title="Cadastro - Funcionários",
    description="Preencha os campos abaixo para cadastrar um candidato à vaga desejada.",
    inputs=[

        # Campo para o nome
        gr.Textbox(label="Nome do Candidato"),  

        # Campo para a idade com validação de 0 a 100
        gr.Number(label="Idade", precision=0, minimum=0, maximum=100),               

        # Campo para Seleção do sexo
        gr.Radio(choices=["Masculino", "Feminino", "Outros"], label="Sexo"), 

        # Campo para seleção do setor
        gr.Radio(choices=[ 
            "Vendas", "Cobrança", "RH", "Departamento Pessoal",
            "TI", "Pós-vendas", "Análise de Crédito", "Telefonia", "Manutenção"
        ], label="Setor da Vaga Desejada"),

        # Campo para seleção da escolaridade
        gr.Radio(choices=[ 
            "Ensino Médio - Incompleto",
            "Ensino Médio - Completo",
            "Cursando Superior",
            "Curso Superior - Completo",
            "Outros",
        ], label="Escolaridade"),

        # Campos para endereço
        gr.Textbox(label="Rua"),
        gr.Textbox(label="Número"),
        gr.Textbox(label="Bairro"),
        gr.Textbox(label="CEP"),
        gr.Textbox(label="Cidade"),
        gr.Textbox(label="Estado")
    ],

    outputs="markdown",  # O resultado será exibido em formato Markdown
    live=True  # Atualizar os resultados automaticamente
)

# Lançar a interface
interface.launch()
