import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Obter o caminho absoluto para a pasta "dados"
path = os.path.abspath('dados')

st.write(path)