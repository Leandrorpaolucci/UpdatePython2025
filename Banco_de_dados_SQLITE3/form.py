import streamlit as st
from UpdatePython2025.

st.title("Filmes")

nome = st.text_input("Nome do filme")
ano = st.number_input("Ano do filme:", min_value=2010, max_value=2024)
nota = st.slider("Nota do filme", min_value=0, max_value=10)


if st.button('adicionar'):
    ...