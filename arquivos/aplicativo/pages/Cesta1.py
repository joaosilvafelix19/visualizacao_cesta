import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os

st.title("Cesta Básica em João Pessoa - *LABIMEC*")

# Importando os dados 
os.chdir("C:/Users/joaos/Documents/GitHub/visualizacao_cesta/arquivos/aplicativo/dados")