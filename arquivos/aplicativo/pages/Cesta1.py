import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os

st.title("Cesta Básica em João Pessoa - *LABIMEC*")

# Importando os dados
data_path = "C:/Users/joaos/Documents/GitHub/visualizacao_cesta/arquivos/aplicativo/dados"  # Absolute path

# Check if the path exists
if not os.path.exists(data_path):
    st.error(f"O caminho especificado não foi encontrado. Verifique se o diretório {data_path} existe.")
else:
    try:
        os.chdir(data_path)
        # Check if the file exists
        if os.path.exists("dados_jp.xlsx"):
            df = pd.read_excel("dados_jp.xlsx")  # Corrected to read Excel file
            st.write("Dados carregados com sucesso!")
            st.write(df.head())  # Display the first few rows of the dataframe
        else:
            st.error("O arquivo 'dados_jp.xlsx' não foi encontrado no diretório especificado.")
    except Exception as e:
        st.error(f"Ocorreu um erro ao carregar os dados: {e}")
