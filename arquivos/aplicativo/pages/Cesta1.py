import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

st.title("Cesta Básica em João Pessoa - *LABIMEC*")

# Importando os dados
data_path = "C:/Users/joaos/Documents/GitHub/visualizacao_cesta/arquivos/aplicativo/dados/dados_jp.xlsx"

try:
    # Load the data directly using the full path
    df = pd.read_excel(data_path)
    st.write("Dados carregados com sucesso!")
    st.write(df.head())  # Display the first few rows of the dataframe
except FileNotFoundError:
    st.error(f"O arquivo especificado não foi encontrado. Verifique se o caminho {data_path} está correto.")
except Exception as e:
    st.error(f"Ocorreu um erro ao carregar os dados: {e}")
