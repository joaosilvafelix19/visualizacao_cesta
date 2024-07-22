import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os

st.title("Cesta Básica em João Pessoa - *LABIMEC*")

# Importando os dados
data_path = "C:/Users/joaos/Documents/GitHub/visualizacao_cesta/arquivos/aplicativo/dados"  # Relative path

try:
    os.chdir(data_path)
    # Load your data here, for example:
    df = pd.read_csv("dados_jp.xlsx")
    st.write("Dados carregados com sucesso!")
except FileNotFoundError:
    st.error("O caminho especificado não foi encontrado. Verifique se o diretório 'dados' existe no caminho relativo.")

# Your plotting code here
