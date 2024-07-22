import streamlit as st
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go

# Path and file name
path = os.path.abspath('dados')
file_name = 'dados_jp.xlsx'
excel_file = os.path.join(path, file_name)

# Debugging output
print(f"Path: {path}")
print(f"File Name: {file_name}")
print(f"Full Path to File: {excel_file}")

# Reading the Excel file
cesta = pd.read_excel(excel_file)
