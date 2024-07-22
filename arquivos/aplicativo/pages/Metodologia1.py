import streamlit as st
import numpy as np
import pandas as pd
from st_aggrid import AgGrid
import os

# Definindo o diretório onde o arquivo está localizado
root = os.getcwd()  # Obtém o diretório de trabalho atual
path = os.path.join(root, 'arquivos', 'aplicativo', 'dados', 'dados_jp.xlsx')

# Importando os dados dos preços
try:
    cesta = pd.read_excel(path, sheet_name="cesta")
except FileNotFoundError:
    st.error(f"O arquivo {path} não foi encontrado.")
except Exception as e:
    st.error(f"Ocorreu um erro ao importar o arquivo: {e}")

# Exibindo os dados em uma tabela interativa usando AgGrid
if 'cesta' in locals():
    st.write("Dados da cesta de produtos:")
    AgGrid(cesta)