import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Obtain the absolute path for the "dados" folder
path = os.path.abspath('dados')

# Name of the Excel file
file_name = 'dados_jp'

# Combine path and filename for the complete Excel file path
excel_file = os.path.join(path, file_name)

# Read the data from the Excel file
try:
  cesta = pd.read_excel(excel_file)
except FileNotFoundError:
  st.error("Error: Excel file not found. Please ensure 'dados_jp.xlsx' is in the 'dados' folder.")
else:
  # Display the first 10 rows of the DataFrame as a table
  st.subheader("Data from 'dados_jp.xlsx'")
  st.dataframe(cesta.head(10))