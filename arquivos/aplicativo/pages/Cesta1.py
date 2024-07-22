import streamlit as st
import pandas as pd
import os

# Obter o caminho absoluto para a pasta "dados"
path = os.path.abspath('dados')

# Nome do arquivo Excel
file_name = 'dados_jp.xlsx'

# Combinar o caminho com o nome do arquivo para obter o caminho completo
excel_file = os.path.join(path, file_name)

# Ler o Excel em um DataFrame
cesta = pd.read_excel(excel_file)

# Importando os dados
cesta = pd.read_excel(excel_file)


# Importando os dados da cesta
##cesta = pd.read_excel(f"{root}{path}/dados_jp.xlsx")
##df = cesta.iloc[:,[6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50]]
#f30 = df.tail(1)