import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Define the path to the "dados" folder and the Excel file name
path = os.path.abspath('dados')
file_name = 'dados_jp.xlsx'

# Combine the path and file name to get the full file path
excel_file = os.path.join(path, file_name)

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file)

# Display the DataFrame in the Streamlit app
st.write(df)