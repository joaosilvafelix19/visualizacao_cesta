import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Importando os dados e fazendo algumas manipulações
file_path = "C:/Users/joaos/Documents/GitHub/visualizacao_cesta/arquivos/aplicativo/dados/dados_jp1.xlsx"

# Check if the file exists
if os.path.exists(file_path):
    # Load the data from the Excel file
    df = pd.read_excel(file_path)
else:
    st.error("The file was not found. Please check the file path.")

