import streamlit as st
import pandas as pd
import requests
import io
import plotly.express as px
import plotly.graph_objects as go


# URL to the raw Excel file on GitHub
data_url = "https://github.com/joaosilvafelix19/visualizacao_cesta/blob/main/arquivos/aplicativo/dados/dados_jp1.xlsx"

# Download the file from GitHub
response = requests.get(data_url)
response.raise_for_status()  # Check that the request was successful

# Read the Excel file into a DataFrame
cesta = pd.read_excel(io.BytesIO(response.content))

# Perform your data manipulations here
# Example: Display the first few rows of the dataset
st.write(cesta.head())