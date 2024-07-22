import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Obter o caminho absoluto para a pasta "dados"
path = os.path.abspath('dados')

# Nome do arquivo Excel
file_name = 'dados_jp.xlsx'

# Combinar o caminho com o nome do arquivo para obter o caminho completo
excel_file = os.path.join(path, file_name)

# Exibir o caminho completo do arquivo
st.write("Caminho completo do arquivo Excel:", excel_file)

# Ler o Excel em um DataFrame
cesta = pd.read_excel(excel_file)