import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Function to get the file path for the Excel file
def get_file_path(filename):
    try:
        # Obtain the absolute path for the "dados" folder
        path = os.path.abspath('dados')
        # Combine path and filename for the complete Excel file path
        file_path = os.path.join(path, filename)
        return file_path
    except Exception as e:
        st.error(f"Error while constructing file path: {e}")
        return None

# Name of the Excel file
file_name = 'dados_jp.xlsx'

# Get the complete file path
excel_file = get_file_path(file_name)

if excel_file and os.path.exists(excel_file):
    # Read the data from the Excel file
    try:
        cesta = pd.read_excel(excel_file)
        # Display the first 10 rows of the DataFrame as a table
        st.subheader("Data from 'dados_jp.xlsx'")
        st.dataframe(cesta.head(10))
    except Exception as e:
        st.error(f"Error reading the Excel file: {e}")
else:
    st.error("Error: Excel file not found. Please ensure 'dados_jp.xlsx' is in the 'dados' folder.")
