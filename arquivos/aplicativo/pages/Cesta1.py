import streamlit as st
import pandas as pd
import requests

st.title("Cesta Básica em João Pessoa - *LABIMEC*")

# URL to the raw Excel file in GitHub using GitHub API
url = 'https://api.github.com/repos/joaosilvafelix19/visualizacao_cesta/contents/arquivos/aplicativo/dados/dados_jp.xlsx'

# Send request to GitHub API to get file content
response = requests.get(url)
if response.status_code == 200:
    file_content = response.json()['content']
    file_content = pd.io.common.get_handle(file_content, 'rb').read()
    
    # Load the content into a pandas DataFrame
    df = pd.read_excel(pd.io.common.BytesIO(file_content))
    st.write("Dados carregados com sucesso!")
    st.write(df.head())  # Display the first few rows of the dataframe
else:
    st.error(f"Ocorreu um erro ao carregar os dados: HTTP {response.status_code} - {response.reason}")
