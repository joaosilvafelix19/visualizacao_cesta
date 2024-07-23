import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import os

# Define a test path
test_path = 'C:\\Users\\joaos\\Documents\\GitHub\\visualizacao_cesta\\arquivos\\aplicativo\\dados\\test_file.xlsx'

# Check if the test file exists
print(os.path.exists(test_path))