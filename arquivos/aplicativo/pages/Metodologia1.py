import streamlit as st
import numpy as np
import pandas as pd
from st_aggrid import AgGrid

import os

# Caminho relativo
relative_path = 'arquivos/aplicativo/dados/dados_jp.xlsx'

# Caminho absoluto
file_path = os.path.join(os.getcwd(), relative_path)

st.write(f"File path: {file_path}")

