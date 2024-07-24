import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder

url_cesta = "https://raw.githubusercontent.com/joaosilvafelix19/visualizacao_cesta/main/arquivos/aplicativo/dados/cesta.csv"
url_precos = "https://raw.githubusercontent.com/joaosilvafelix19/visualizacao_cesta/main/arquivos/aplicativo/dados/precos.csv"

# Importando os dados dos preços não ponderados
precos = pd.read_csv(url_precos).round(2)
precos['data'] = pd.to_datetime(precos['data'], errors='coerce')  # Convertendo para datetime com tratamento de erros
precos['data'] = precos['data'].apply(lambda x: x.strftime('%d-%m-%Y') if pd.notnull(x) else '')

precos_ponderados = pd.read_csv(url_cesta).round(2)
precos_ponderados['data'] = pd.to_datetime(precos_ponderados['data'], errors='coerce')  # Convertendo para datetime com tratamento de erros
precos_ponderados['data'] = precos_ponderados['data'].apply(lambda x: x.strftime('%d-%m-%Y') if pd.notnull(x) else '')

st.title("Download dos dados")

st.markdown("Abaixo, há a possibilidade de fazer o download dos dados não ponderados (Preços) e dos dados ponderados (Preços Ponderados). Os dados não ponderados referem-se ao preços coletados nos supermercados mas sem as ponderações definidas pelo decreto lei nº 399/1938, já os preços ponderados são os preços coletados e multiplicados pelos pesos descritos pelo decreto lei nº 399/1938. Para mais detalhes sobre a metodologia vá para a guia Metodologia.")

# Opção de escolha entre os dados
opcao = st.radio("Escolha uma opção para download dos dados", ('Preços', 'Preços Ponderados'))

#-------------------------------------------------------------------------------------------------------------------------
# Preços (Preços não ponderados)
#-------------------------------------------------------------------------------------------------------------------------

if opcao == "Preços":
    st.write("Você escolheu os preços não ponderados")
    
    # Dando a opção de se baixar os dados em csv
    @st.cache_data
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    csv = convert_df(precos)

    st.download_button(
        label="Baixe os preços como CSV",
        data=csv,
        file_name='precos.csv',
        mime='text/csv',
    )
    
    
# -------------------------------------------------------------------------------------------------------
# Preços Ponderados 
#--------------------------------------------------------------------------------------------------------
if opcao == "Preços Ponderados":
    st.write("Você escolheu os preços ponderados")
    
    # Dando a opção de se baixar os dados em csv
    @st.cache_data
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    csv = convert_df(precos_ponderados)

    st.download_button(
        label="Baixe os preços ponderados como CSV",
        data=csv,
        file_name='precos_ponderados.csv',
        mime='text/csv',
    )
    