import streamlit as st
from openpyxl import load_workbook
import pandas as pd
from st_aggrid import AgGrid

# Full local path to the Excel file
file_path = r'C:\Users\joaos\Documents\GitHub\visualizacao_cesta\arquivos\aplicativo\dados\dados_jp.xlsx'

# Function to load data using openpyxl
def load_data():
    try:
        # Load the workbook and select the active sheet
        wb = load_workbook(file_path, data_only=True)
        sheet = wb.active
        
        # Convert sheet to DataFrame
        data = pd.DataFrame(sheet.values)
        
        # Assuming the first row is the header
        data.columns = data.iloc[0]
        data = data[1:]
        
        return data
    except Exception as e:
        st.error(f"Error loading the Excel file: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

# Load the data
data = load_data()

# Check if data is loaded successfully
if not data.empty:
    # Display the data using AgGrid
    st.title('Data Viewer')
    AgGrid(data)
else:
    st.write("No data to display.")
