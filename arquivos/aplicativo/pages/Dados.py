import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from datetime import datetime, timezone

# Definindo diretório
streaos.chdir("C:\\Users\\joaos\\Dropbox\\Dados\\1_coleta_jp")

# Importando os dados dos preços não ponerados
precos = pd.read_excel("dados_jp.xlsx", sheet_name="precos").round(2)
precos['data'] = precos['data'].apply(lambda x: x.strftime('%d-%m-%Y'))
precos_ponderados = pd.read_excel("dados_jp.xlsx", sheet_name="cesta").round(2)
precos_ponderados['data'] = precos_ponderados['data'].apply(lambda x: x.strftime('%d-%m-%Y'))

st.title("Download dos dados")

st.markdown("Abaixo, há a possibilidade de fazer o download dos dados não ponderados (Preços) e dos dados ponderados (Preços Ponderados). Os dados não ponderados referem-se ao preços coletados nos supermercados mas sem as ponderações definidas pelo decreto lei nº 399/1938, já os preços ponderados são os preços coletados e multiplicados pelos pesos descritos pelo decreto lei nº 399/1938. Para mais detalhes sobre a metodologia vá para a guia Metodologia.")

# Opção de escolha entre os dados
Opção = st.radio("Escolha uma opção para download dos dados",
                 ('Preços', 'Preços Ponderados'))

#-------------------------------------------------------------------------------------------------------------------------
# Preços (Preços não ponderados)
#-------------------------------------------------------------------------------------------------------------------------

if Opção == "Preços":
    st.write("Você escolheu os preços não ponderados")
    
    # Dando a opção de se baixar os dados em csv
    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return precos.to_csv().encode('utf-8')

    csv = convert_df(precos)

    st.download_button(
        label="Baixe os preços como CSV",
        data=csv,
        file_name='precos.csv',
        mime='text/csv',
    )
    
    # Melhorando a estética dos dados mostrados
    gb = GridOptionsBuilder.from_dataframe(precos)
    gb.configure_pagination(enabled=True)
    gb.configure_default_column(editable=True, groupable=True)
    gridoptions = gb.build()
    AgGrid(precos, gridOptions=gridoptions,
           allow_unsafe_jscode=True)
    
# -------------------------------------------------------------------------------------------------------
# Preços Ponderados 
#--------------------------------------------------------------------------------------------------------
if Opção == "Preços Ponderados":
    st.write("Você escolheu os preços ponderados")
    
    # Dando a opção de se baixar os dados em csv
    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return precos_ponderados.to_csv().encode('utf-8')

    csv = convert_df(precos_ponderados)

    st.download_button(
        label="Baixe os preços ponderados como CSV",
        data=csv,
        file_name='precos_ponderados.csv',
        mime='text/csv',
    )
    
    # Melhorando a estética dos dados mostrados
    gb = GridOptionsBuilder.from_dataframe(precos_ponderados)
    gb.configure_pagination(enabled=True)
    gb.configure_default_column(editable=True, groupable=True)
    gridoptions = gb.build()
    AgGrid(precos_ponderados, gridOptions=gridoptions,
           allow_unsafe_jscode=True)
    