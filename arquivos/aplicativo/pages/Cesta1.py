import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Define the full path to the Excel file
data_path = "C:\\Users\\joaos\\Documents\\GitHub\\visualizacao_cesta\\arquivos\\aplicativo\\dados\\dados_jp1.xlsx"  # Adjust backslashes for your OS

# Load the Excel file using the full path
try:
    cesta = pd.read_excel(data_path)
    st.write("File loaded successfully!")
    st.write(cesta.head())  # Print the first 5 rows of the DataFrame
except FileNotFoundError:
    print(f"File not found: {data_path}")
    print("Make sure the file exists at the specified location.")
except Exception as e:
    print(f"An error occurred: {e}")
