import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# URL to the raw Excel file on GitHub
data_url = "https://github.com/joaosilvafelix19/visualizacao_cesta/blob/main/arquivos/aplicativo/dados/dados_jp1.xlsx"

# Read the Excel file
cesta = pd.read_excel(data_url)

# Perform your data manipulations here
# Example: Display the first few rows of the dataset
st.write(cesta.head())

