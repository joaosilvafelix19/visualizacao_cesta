import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Define o caminho para o diretório onde o arquivo Excel está localizado
# Certifique-se de ajustar o caminho conforme a estrutura do seu projeto
path = 'C:/Users/joaos/Documents/GitHub/visualizacao_cesta'
file_name = 'dados_jp.xlsx'
excel_file = os.path.join(path, file_name)

# Verifica o diretório atual e o caminho do arquivo para depuração
st.write("Diretório atual:", os.getcwd())
st.write("Caminho do arquivo:", excel_file)

# Verifica se o arquivo existe no caminho especificado
if not os.path.exists(excel_file):
    st.error(f'O arquivo {excel_file} não foi encontrado.')
else:
    try:
        # Lê o arquivo Excel para um DataFrame
        df = pd.read_excel(excel_file)
        st.write(df)

        # Exemplo de visualização com Plotly Express
        if not df.empty:
            st.subheader("Visualização dos Dados")
            # Ajuste os nomes das colunas conforme a estrutura dos seus dados
            fig = px.line(df, x=df.columns[0], y=df.columns[1], title="Gráfico dos Dados")
            st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Ocorreu um erro ao processar o arquivo: {e}")
