import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Definindo diretório
root = os.getcwd()
if root[0] == '/':
    root = '/GitHub/visualizacao_cesta/'
else:
    root = os.path.abspath('../..')
path = '/arquivos/aplicativo/dados'

# Importando os dados dos preços não ponerados
cesta = pd.read_excel(f"{root}{path}/dados_jp.xlsx", sheet_name="cesta")
