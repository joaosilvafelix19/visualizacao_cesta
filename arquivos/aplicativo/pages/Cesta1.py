import streamlit as st
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go

# Importando os dados e fazendo algumas manipulações

# Definindo diretório
root = os.getcwd()
if root[0] == '/':
    root = '/GitHub/visualizacao_cesta/'
else:
    root = os.path.abspath('../..')
path = '/arquivos/aplicativo/dados'

# Importando os dados da cesta
cesta = pd.read_excel(f"{root}{path}/dados_jp.xlsx")
df = cesta.iloc[:,[6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50]]
df30 = df.tail(1)