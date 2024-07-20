import streamlit as st
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go

# Define the relative path to the data file
relative_path = 'arquivos/aplicativo/dados/dados_jp.xlsx'

# Get the absolute path of the data file
cesta_path = os.path.join(os.getcwd(), relative_path)

# Print the path to check if it is correct
st.write(f"Full path to data file: {cesta_path}")

# Check if the file exists
if not os.path.exists(cesta_path):
    st.error(f"File not found: {cesta_path}")
else:
    # Importing data and performing manipulations
    cesta = pd.read_excel(cesta_path)
    df = cesta.iloc[:, [6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50]]
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
    cesta = cesta.iloc[:, [1, 54]]

    Produtos = pd.DataFrame(dict(
        produtos=["4,5KG-Carne", "6L-Leite", "4,5KG-Feijão", "3,6KG-Arroz", "3KG-Farinha",
                  "12KG-Tomate", "6KG-Pão", "300GR-Café", "11,25KG-Banana", "3KG-Açúcar",
                  "750ML-Óleo", "750GR-Manteiga"],
        custo=[carne, leite, feijao, arroz, farinha, tomate, pao, cafe, banana, acucar, oleo, manteiga]))

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
                         text='custo')
        fig_peso.update_layout(yaxis={'categoryorder': 'total ascending'},
                               xaxis_title='Custo (R$)',
                               yaxis_title='Produto ponderado')

        st.plotly_chart(fig_peso, use_container_width=True)

    # Estatísticas Descritivas
    last7 = cesta.tail(7)
    last7_mean = last7['media_cesta'].mean()
    last14 = cesta.tail(14)
    mean14 = last14['media_cesta'].mean()
    dif14_7 = mean14 - last7_mean

    last15 = cesta.tail(15)
    last15_mean = last15['media_cesta'].mean()

    last30 = cesta.tail(30)
    mean30 = last30['media_cesta'].mean()
    dif30_15 = mean30 - last15_mean

    min_last30 = last30['media_cesta'].min()
    medi_last30 = last30['media_cesta'].median()
    max_last30 = last30['media_cesta'].max()

    last60 = cesta.tail(60)
    mean60 = last60['media_cesta'].mean()
    dif60_30 = mean60 - mean30

    st.markdown("As estatísticas a seguir mostram qual o valor da cesta básica nos últimos 7, 15 e 30 dias respectivamente, abaixo encontram-se as variações em reais dos últimos 14, 30 e 60 dias respectivamente")

    col1, col2, col3 = st.columns(3)
    col1.metric("Média 7 dias", f'R$ {last7_mean.round(2)}', dif14_7.round(2))
    col2.metric("Média 15 dias", f'R$ {last15_mean.round(2)}', dif30_15.round(2))
    col3.metric("Média 30 dias", f'R$ {mean30.round(2)}', dif60_30.round(2))

    st.markdown("Adiante é mostrado qual os valores mínimo, da mediana e o valor máximo do custo estimado da cesta básica em João Pessoa nos últimos 30 dias")

    col4, col5, col6 = st.columns(3)
    col4.metric("Mínimo 30 dias", f"R$ {min_last30.round(2)}")
    col5.metric("Mediana 30 dias", f"R$ {medi_last30.round(2)}")
    col6.metric("Máximo 30 dias", f"R$ {max_last30.round(2)}")
