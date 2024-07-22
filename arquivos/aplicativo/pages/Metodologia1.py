import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
import os

# Path to the Excel file in your GitHub repository
relative_path = 'arquivos/aplicativo/dados/dados_jp.xlsx'

# Construct the absolute path based on the current working directory
file_path = os.path.join(os.getcwd(), relative_path)

# Load the Excel file into a DataFrame
@st.cache_data
def load_data():
    return pd.read_excel(file_path)

# Load the data
data = load_data()

# Display the data using AgGrid
st.title('Data Viewer')
AgGrid(data)
