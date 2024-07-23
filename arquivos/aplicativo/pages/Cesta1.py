import streamlit as st
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go

# Importando os dados e fazendo algumas manipulações

# Define the full path to the Excel file
data_path = "C:\\Users\\joaos\\Documents\\GitHub\\visualizacao_cesta\\arquivos\\aplicativo\\dados\\dados_jp1.xlsx"  # Adjust backslashes for your OS

# Load the Excel file using the full path
try:
  cesta = pd.read_excel(data_path)
  print("File loaded successfully!")
except FileNotFoundError:
  print(f"File not found: {data_path}")
  print("Make sure the file exists at the specified location.")
except Exception as e:
  print(f"An error occurred: {e}")

# Importando os dados da cesta
df = cesta.iloc[:,[6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50]]
df30 = df.tail(1)