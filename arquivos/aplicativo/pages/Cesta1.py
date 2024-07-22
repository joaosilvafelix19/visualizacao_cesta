import streamlit as st
import openpyxl
import pandas as pd
import os

st.title("Cesta Básica em João Pessoa - *LABIMEC*")

# Define the relative path to the Excel file
relative_path = 'arquivos/aplicativo/dados/dados_jp.xlsx'

# Get the absolute path of the Excel file
file_path = os.path.join(os.getcwd(), relative_path)

# Check if the file exists
if os.path.exists(file_path):
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        st.write("Dados carregados com sucesso!")
        st.write(df.head())  # Display the first few rows of the dataframe
    except Exception as e:
        st.error(f"Ocorreu um erro ao carregar os dados: {e}")
else:
    st.error(f"O arquivo especificado não foi encontrado no caminho {file_path}.")
