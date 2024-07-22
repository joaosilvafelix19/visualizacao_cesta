import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
import os

# Path to the Excel file in your GitHub repository
relative_path = 'arquivos/aplicativo/dados/dados_jp.xlsx'

# Construct the absolute path based on the current working directory
file_path = os.path.join(os.getcwd(), relative_path)

# Print the file path to verify it
st.write(f"File path: {file_path}")

# Function to load data
@st.cache_data
def load_data():
    try:
        # Attempt to read the Excel file
        data = pd.read_excel(file_path)
        return data
    except Exception as e:
        # Print error message if file reading fails
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
