import streamlit as st
import dados

# Garantir que a tabela 'filmes' exista antes de qualquer operação
dados.cria_tabela()

st.title("Filmes")

# Entradas de dados
nome = st.text_input("Nome do filme")
ano = st.number_input("Ano do filme:", min_value=2010, max_value=2024)
nota = st.slider("Nota do filme", min_value=0, max_value=10)

# Função para adicionar o filme
if st.button('Adicionar'):
    if not nome:
        st.error("Por favor, insira o nome do filme.")
    else:
        try:
            dados.inserir_dados(nome, ano, nota)
            st.success(f"Filme '{nome}' adicionado com sucesso!")
        except Exception as e:
            st.error(f"Ocorreu um erro ao adicionar o filme: {e}")

# Exibição de filmes cadastrados
if st.button('Mostrar filmes'):
    try:
        filmes = dados.obter_dados()
        if filmes:
            st.write("Filmes cadastrados:")
            for filme in filmes:
                st.write(f"{filme[1]} ({filme[2]}) - Nota: {filme[3]}")
        else:
            st.write("Nenhum filme cadastrado.")
    except Exception as e:
        st.error(f"Ocorreu um erro ao obter os filmes: {e}")
