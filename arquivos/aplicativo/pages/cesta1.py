import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import os

# URL of the Excel file on GitHub
url = "https://github.com/joaosilvafelix19/visualizacao_cesta/blob/main/arquivos/aplicativo/dados/cesta.csv"

# Importing the data directly from GitHub
cesta = pd.read_csv(url)

# Manipulating the data
#df = cesta.iloc[:, [6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50]]
#df30 = df.tail(1)