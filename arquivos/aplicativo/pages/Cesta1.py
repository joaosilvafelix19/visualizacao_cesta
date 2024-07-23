import streamlit as st
import pandas as pd

data_path = "C:\\Users\\joaos\\Documents\\GitHub\\visualizacao_cesta\\arquivos\\aplicativo\\dados\\dados_jp1.xlsx"

st.write("Attempting to load file...")

try:
    cesta = pd.read_excel(data_path)
    st.write("File loaded successfully!")
    st.write(cesta.head())
except FileNotFoundError:
    st.error(f"File not found: {data_path}")
except Exception as e:
    st.error(f"An error occurred: {e}")

st.write("Code executed.")
