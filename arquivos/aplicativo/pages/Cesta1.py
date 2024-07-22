import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Title of the app
st.title('Cesta Básica Data Visualization')

# File uploader
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    # Read the Excel file
    cesta = pd.read_excel(uploaded_file)
    
    # Display the first few rows of the dataframe
    st.write("First few rows of the dataset:")
    st.write(cesta.head())
    
    # Example Plotly visualization: Scatter plot of prices
    # Adjust columns based on your actual dataset
    if 'Product' in cesta.columns and 'Price' in cesta.columns:
        fig = px.scatter(cesta, x='Product', y='Price', title='Product Prices')
        st.plotly_chart(fig)
    else:
        st.write("Expected columns 'Product' and 'Price' not found in the dataset.")
else:
    st.write("Please upload an Excel file.")

# Debug information
st.write("Current Working Directory:", os.getcwd())
st.write("Uploaded File Path:", uploaded_file)
