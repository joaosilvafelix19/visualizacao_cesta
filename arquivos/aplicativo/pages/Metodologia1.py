import streamlit as st
import numpy as np
import pandas as pd
from st_aggrid import AgGrid

import os

# Caminho relativo
relative_path = 'arquivos/aplicativo/dados/dados_jp.xlsx'

# Caminho absoluto
file_path = os.path.join(os.getcwd(), relative_path)

# Checa se o caminho existe
if os.path.exists(file_path):
    file = Image.open(file_path)
else:
    st.error(f"Image file not found at {file_path}")
    file = None

