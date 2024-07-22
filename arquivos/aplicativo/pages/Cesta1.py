import streamlit as st
import pandas as pd

st.title("Cesta Básica em João Pessoa - *LABIMEC*")

# Correct URL to the raw Excel file in GitHub
url = 'https://raw.githubusercontent.com/joaosilvafelix19/visualizacao_cesta/main/arquivos/aplicativo/dados/dados_jp.xlsx'

try:
    # Read the Excel file directly from GitHub
    df = pd.read_excel(url)
    st.write("Dados carregados com sucesso!")
    st.write(df.head())  # Display the first few rows of the dataframe
except Exception as e:
    st.error(f"Ocorreu um erro ao carregar os dados: {e}")
