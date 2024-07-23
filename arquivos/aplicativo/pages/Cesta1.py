import streamlit as st
import pandas as pd
import requests
import io
import plotly.express as px
import plotly.graph_objects as go


# URL to the raw Excel file on GitHub
data_url = "https://raw.githubusercontent.com/joaosilvafelix19/visualizacao_cesta/main/arquivos/aplicativo/dados/dados_jp1.xlsx"

try:
    # Download the file from GitHub
    response = requests.get(data_url)
    response.raise_for_status()  # Check that the request was successful
    
    # Read the Excel file into a DataFrame
    cesta = pd.read_excel(io.BytesIO(response.content))
    
    # Perform your data manipulations here
    # Example: Display the first few rows of the dataset
    st.write(cesta.head())

    # Your existing visualization code here
    # Example: Creating a simple plot
    fig = px.line(cesta, x="Date", y="Price", title="Price over Time")
    st.plotly_chart(fig)

except requests.exceptions.RequestException as e:
    st.error(f"Failed to download the file: {e}")
    st.stop()

except Exception as e:
    st.error(f"An error occurred: {e}")
    st.stop()