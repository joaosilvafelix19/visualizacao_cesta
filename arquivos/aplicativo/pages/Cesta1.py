import streamlit as st
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go

# Importando os dados e fazendo algumas manipulações

# Define the full path to the Excel file
data_path = "C:\\Users\\joaos\\Documents\\GitHub\\visualizacao_cesta\\arquivos\\aplicativo\\dados\\dados_jp1.xlsx"  # Adjust backslashes for your OS

cesta = pd.read_excel(data_path)

