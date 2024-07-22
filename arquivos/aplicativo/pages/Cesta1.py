import streamlit as st
import pandas as pd
import os

# Obter o caminho absoluto para a pasta "dados"
path = os.path.abspath('dados')


# Importando os dados da cesta
cesta = pd.read_excel(f"{root}{path}/dados_jp.xlsx")
df = cesta.iloc[:,[6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50]]
df30 = df.tail(1)