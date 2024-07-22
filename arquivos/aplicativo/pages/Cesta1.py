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
try:
    cesta = pd.read_excel(excel_file)
    print("File read successfully")
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

# Check if cesta is not empty and has enough columns
if not cesta.empty and cesta.shape[1] > 50:
    try:
        df = cesta.iloc[:,[6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50]]
        df30 = df.tail(1)
        print("Data processed successfully")
    except IndexError as e:
        print(f"IndexError: {e}")
    except Exception as e:
        print(f"An error occurred while processing data: {e}")
else:
    print("DataFrame is empty or does not have enough columns")
