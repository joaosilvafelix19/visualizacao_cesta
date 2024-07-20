import streamlit as st
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go

# Definindo diretório
root = r'C:\Users\joaos\Documents\GitHub\visualizacao_cesta'
path = r'arquivos\aplicativo\dados'

# Montando o caminho do arquivo
file_path = os.path.join(root, path, 'dados_jp.xlsx')
print(f"Attempting to read file from: {file_path}")

# Importando os dados da cesta
try:
    cesta = pd.read_excel(file_path)
except Exception as e:
    st.error(f"Error reading the file: {e}")
    st.stop()

df = cesta.iloc[:,[6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50]]
df30 = df.tail(1)

carne = df30['media_carne'].mean().round(2)
leite = df30['media_leite'].mean().round(2)
feijao = df30['media_feijao'].mean().round(2)
arroz = df30['media_arroz'].mean().round(2)
farinha = df30['media_farinha'].mean().round(2)
tomate = df30['media_tomate'].mean().round(2)
pao = df30['media_pao'].mean().round(2)
cafe = df30['media_cafe'].mean().round(2)
banana = df30['media_banana'].mean().round(2)
acucar = df30['media_acucar'].mean().round(2)
oleo = df30['media_oleo'].mean().round(2)
manteiga = df30['media_manteiga'].mean().round(2)

st.title("Cesta Básica em João Pessoa - *LABIMEC*")

st.markdown("Abaixo, no gráfico à esquerda, encontra-se a evolução diária do custo da cesta básica na cidade João Pessoa. No gráfico da direita é mostrado quanto cada produto ponderado pelo decreto lei nº 399 de 1938 representa no dia atual, ou seja, este gráfico é atualizado diariamente")

# Seleciona as colunas data e média cesta
cesta = cesta.iloc[:,[1, 54]]

Produtos = pd.DataFrame(dict(
    produtos = ["4,5KG-Carne","6L-Leite","4,5KG-Feijão","3,6KG-Arroz","3KG-Farinha",
                "12KG-Tomate","6KG-Pão","300GR-Café","11,25KG-Banana", "3KG-Açúcar",
                "750ML-Óleo", "750GR-Manteiga"],
    custo = [carne, leite, feijao, arroz, farinha, tomate, pao, cafe, banana, acucar, oleo, manteiga])) 

col_a, col_b = st.columns(2)

with col_a:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=cesta['data'], y=cesta['media_cesta'], name='', line=dict(color='royalblue', width=4)))
    fig.update_layout(title='Evolução diária custo da cesta básica',
                   xaxis_title='Período',
                   yaxis_title='Custo (R$)')
    st.plotly_chart(fig, use_container_width=True)

with col_b:
    fig_peso = px.bar(Produtos, y='produtos', x='custo', text_auto='.5s',
                title="Custo ponderado por produto",
                orientation="h",
                text = 'custo')
    fig_peso.update_layout(yaxis={'categoryorder':'total ascending'},
                    xaxis_title='Custo (R$)',
                    yaxis_title='Produto ponderado')

    st.plotly_chart(fig_peso, use_container_width=True)

#-------------------------------------------------------------------
