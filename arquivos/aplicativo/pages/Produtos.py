import streamlit as st
import numpy as np
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go
import time
from st_aggrid import AgGrid
import os


# Importando os dados e fazendo algumas manipulações
root = os.getcwd()
if root[0] == '/':
    root = '/GitHub/visualizacao_cesta/'
else:
    root = os.path.abspath('../..')
path = '/arquivos/aplicativo/dados'

# Importando os dados dos preços não ponerados
precos = pd.read_excel(f"{root}{path}/dados_jp.xlsx", sheet_name="precos")
precos['data'] = precos['data'].apply(lambda x: x.strftime('%d-%m-%Y'))
dff = pd.read_excel(f"{root}{path}/dados_jp.xlsx", sheet_name="precos")

# Selecionando apenas a data e os valores referentes as médias dos produtos
df = precos.iloc[:,[1,2,6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50]]

# Selecionando os últimos 30 dias
df = df.tail(30)

# Título da página
st.title("Visualização dos produtos de forma individual")

# Criando uma caixa de seleção
escolha = st.selectbox(
    'Qual produto você deseja visualizar',
    ('Selecione um produto','Carne', 'Leite', 'Feijão', 'Arroz', 'Farinha', 'Tomate', 'Pão', 'Café', 'Banana', 'Açúcar', 'Óleo', 'Manteiga'))


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Carne
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Gráfico de linha evolução do KG da carne
if escolha == "Carne":
    st.markdown("O Gráfico a seguir mostra a evolução diária do custo médio do KG da carne na cidade de João Pessoa, são considerados para o cálculo da carne o coxão mole (chã de dentro), coxão duro (chã de fora) e patinho.")
    fig_carne = go.Figure()
    fig_carne.add_trace(go.Scatter(x=dff['data'], y=dff['media_carne'], name='', line=dict(color='royalblue', width=4)))
    fig_carne.update_layout(title='Evolução diária do KG da carne',
                    xaxis_title='Período',
                    yaxis_title='Custo (R$)')
    st.plotly_chart(fig_carne, use_container_width=True)
    
    # Mostrando estatísticas descritivas por meio da função st.metric() nos últimos 30 dias
    st.markdown("As informações abaixo mostram quais são os preços mínimo, médio, mediana e preço máximo do KG da carne relativo ao custo médio estimado diário nos últimos 30 dias na cidade de João Pessoa.")
    col1, col2, col3, col4 = st.columns(4)

    min_carne=df['media_carne'].min().round(2); media_carne=df['media_carne'].mean().round(2); mediana_carne=df['media_carne'].median().round(2); 
    max_carne=df['media_carne'].max().round(2)
    
    col1.metric("Mínimo", f'R$ {min_carne}')
    col2.metric("Média", f'R$ {media_carne}')
    col3.metric("Mediana", f'R$ {mediana_carne}')
    col4.metric("Máximo", f'R$ {max_carne}')
    
    # box plot custo do quilograma da carne por dia da semana
    st.markdown("Já o boxplot abaixo mostra como tem se comportado o preço do KG da carne relativo ao custo médio estimado diário nos últimos 30 dias por dia da semana.")
    box_carne = px.box(df, x="dia_semana", y="media_carne", points="all")
    box_carne.update_layout(title='Custo médio por dia da semana',
                   xaxis_title='Dia da semana',
                   yaxis_title='Custo (R$)')
    box_carne.update_xaxes(categoryorder='array', categoryarray= ['Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo'])
    st.plotly_chart(box_carne, use_container_width=True)
    
    # Tabela contendo osúltimos sete dias
    st.markdown("Por fim, mostra-se os preços médios observados dos últimos 7 dias de coleta na cidade de João Pessoa.")
    table_carne = precos.tail(7).round(2)
    table_carne = table_carne[['data', 'media_carne']]
    table_carne = table_carne.rename(columns = {'data':'Data', 'media_carne':'Média Carne'})
    table_carne = table_carne.pivot_table(index=["Data"], 
                    values='Média Carne')
    table_carne = table_carne.T
    st.table(table_carne)
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Leite
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Gráfico de linha evolução de 1 litro de leite
if escolha == "Leite":
    st.markdown("O Gráfico a seguir mostra a evolução diária do custo médio do litro do leite na cidade de João Pessoa, é considerado para o cálculo o leite do tipo integral.")
    fig_leite = go.Figure()
    fig_leite.add_trace(go.Scatter(x=dff['data'], y=dff['media_leite'], name='', line=dict(color='royalblue', width=4)))
    fig_leite.update_layout(title='Evolução diária de 1L de leite',
                    xaxis_title='Período',
                    yaxis_title='Custo (R$)')
    st.plotly_chart(fig_leite, use_container_width=True)
    
    # Mostrando estatísticas descritivas por meio da função st.metric() nos últimos 30 dias
    st.markdown("As informações abaixo mostram quais são os preços mínimo, médio, mediana e preço máximo do litro do leite relativo ao custo médio estimado diário nos últimos 30 dias na cidade de João Pessoa.")
    col1_leite, col2_leite, col3_leite, col4_leite = st.columns(4)

    min_leite=df['media_leite'].min().round(2); media_leite=df['media_leite'].mean().round(2); mediana_leite=df['media_leite'].median().round(2); 
    max_leite=df['media_leite'].max().round(2)
    
    col1_leite.metric("Mínimo", f'R$ {min_leite}')
    col2_leite.metric("Média", f'R$ {media_leite}')
    col3_leite.metric("Mediana", f'R$ {mediana_leite}')
    col4_leite.metric("Máximo", f'R$ {max_leite}')
    
    # box plot custo do litro do leite por dia da semana
    st.markdown("Já o boxplot abaixo mostra como tem se comportado o preço do litro do leite relativo ao custo médio estimado diário nos últimos 30 dias por dia da semana.")
    box_leite = px.box(df, x="dia_semana", y="media_leite", points="all")
    box_leite.update_layout(title='Custo médio por dia da semana',
                   xaxis_title='Dia da semana',
                   yaxis_title='Custo (R$)')
    box_leite.update_xaxes(categoryorder='array', categoryarray= ['Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo'])
    st.plotly_chart(box_leite, use_container_width=True)
    
    # Tabela contendo osúltimos sete dias
    st.markdown("Por fim, mostra-se os preços médios observados dos últimos 7 dias de coleta na cidade de João Pessoa.")
    table_leite = precos.tail(7).round(2)
    table_leite = table_leite[['data', 'media_leite']]
    table_leite = table_leite.rename(columns = {'data':'Data', 'media_leite':'Média Leite'})
    table_leite= table_leite.pivot_table(index=["Data"], 
                    values='Média Leite')
    table_leite = table_leite.T
    st.table(table_leite)
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Feijão
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Gráfico de linha evolução de 1 KG de feijão
if escolha == "Feijão":
    st.markdown("O Gráfico a seguir mostra a evolução diária do custo médio de 1 KG de feijão na cidade de João Pessoa, é considerado para o cálculo o feijão carioca do tipo 1.")
    fig_feijao = go.Figure()
    fig_feijao.add_trace(go.Scatter(x=dff['data'], y=dff['media_feijao'], name='', line=dict(color='royalblue', width=4)))
    fig_feijao.update_layout(title='Evolução diária de 1 KG de feijão',
                    xaxis_title='Período',
                    yaxis_title='Custo (R$)')
    st.plotly_chart(fig_feijao, use_container_width=True)

    # Mostrando estatísticas descritivas por meio da função st.metric() nos últimos 30 dias
    st.markdown("As informações abaixo mostram quais são os preços mínimo, médio, mediana e preço máximo do quilograma do feijão relativo ao custo médio estimado diário nos últimos 30 dias na cidade de João Pessoa.")
    col1_feijao, col2_feijao, col3_feijao, col4_feijao = st.columns(4)

    min_feijao=df['media_feijao'].min().round(2); media_feijao=df['media_feijao'].mean().round(2); mediana_feijao=df['media_feijao'].median().round(2); 
    max_feijao=df['media_feijao'].max().round(2)
    
    col1_feijao.metric("Mínimo", f'R$ {min_feijao}')
    col2_feijao.metric("Média", f'R$ {media_feijao}')
    col3_feijao.metric("Mediana", f'R$ {mediana_feijao}')
    col4_feijao.metric("Máximo", f'R$ {max_feijao}')
    
    # box plot custo do quilograma do feijão por dia da semana
    st.markdown("Já o boxplot abaixo mostra como tem se comportado o preço do quilograma do feijão relativo ao custo médio estimado diário nos últimos 30 dias por dia da semana.")
    box_feijao = px.box(df, x="dia_semana", y="media_feijao", points="all")
    box_feijao.update_layout(title='Custo médio por dia da semana',
                   xaxis_title='Dia da semana',
                   yaxis_title='Custo (R$)')
    box_feijao.update_xaxes(categoryorder='array', categoryarray= ['Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo'])
    st.plotly_chart(box_feijao, use_container_width=True)
    
    # Tabela contendo o súltimos sete dias
    st.markdown("Por fim, mostra-se os preços médios observados dos últimos 7 dias de coleta na cidade de João Pessoa.")
    table_feijao = precos.tail(7).round(2)
    table_feijao = table_feijao[['data', 'media_feijao']]
    table_feijao = table_feijao.rename(columns = {'data':'Data', 'media_feijao':'Média Feijão'})
    table_feijao= table_feijao.pivot_table(index=["Data"], 
                    values='Média Feijão')
    table_feijao = table_feijao.T
    st.table(table_feijao)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Arroz
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Gráfico de linha evolução de 1 KG de Arroz
if escolha == "Arroz":
    st.markdown("O Gráfico a seguir mostra a evolução diária do custo médio de 1 KG de arroz na cidade de João Pessoa, é considerado para o cálculo o arroz parboilizado do tipo 1.")
    fig_arroz = go.Figure()
    fig_arroz.add_trace(go.Scatter(x=dff['data'], y=dff['media_arroz'], name='', line=dict(color='royalblue', width=4)))
    fig_arroz.update_layout(title='Evolução diária de 1 KG de arroz',
                    xaxis_title='Período',
                    yaxis_title='Custo (R$)')
    st.plotly_chart(fig_arroz, use_container_width=True)
    
    # Mostrando estatísticas descritivas por meio da função st.metric() nos últimos 30 dias
    st.markdown("As informações abaixo mostram quais são os preços mínimo, médio, mediana e preço máximo do quilograma do arroz relativo ao custo médio estimado diário nos últimos 30 dias na cidade de João Pessoa.")
    col1_arroz, col2_arroz, col3_arroz, col4_arroz = st.columns(4)

    min_arroz=df['media_arroz'].min().round(2); media_arroz=df['media_arroz'].mean().round(2); mediana_arroz=df['media_arroz'].median().round(2); 
    max_arroz=df['media_arroz'].max().round(2)
    
    col1_arroz.metric("Mínimo", f'R$ {min_arroz}')
    col2_arroz.metric("Média", f'R$ {media_arroz}')
    col3_arroz.metric("Mediana", f'R$ {mediana_arroz}')
    col4_arroz.metric("Máximo", f'R$ {max_arroz}')
    
    # box plot custo do arroz por dia da semana
    st.markdown("Já o boxplot abaixo mostra como tem se comportado o preço do quilograma do arroz relativo ao custo médio estimado diário nos últimos 30 dias por dia da semana.")
    box_arroz = px.box(df, x="dia_semana", y="media_arroz", points="all")
    box_arroz.update_layout(title='Custo médio por dia da semana',
                   xaxis_title='Dia da semana',
                   yaxis_title='Custo (R$)')
    box_arroz.update_xaxes(categoryorder='array', categoryarray= ['Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo'])
    st.plotly_chart(box_arroz, use_container_width=True)
    
    # Tabela contendo o súltimos sete dias
    st.markdown("Por fim, mostra-se os preços médios observados dos últimos 7 dias de coleta na cidade de João Pessoa.")
    table_arroz = precos.tail(7).round(2)
    table_arroz = table_arroz[['data', 'media_arroz']]
    table_arroz = table_arroz.rename(columns = {'data':'Data', 'media_arroz':'Média Arroz'})
    table_arroz = table_arroz.pivot_table(index=["Data"], 
                    values='Média Arroz')
    table_arroz = table_arroz.T
    st.table(table_arroz)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Farinha
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Gráfico de linha evolução de 1 KG de Farinha
if escolha == "Farinha":
    st.markdown("O Gráfico a seguir mostra a evolução diária do custo médio de 1 KG de farinha na cidade de João Pessoa.")
    fig_farinha = go.Figure()
    fig_farinha.add_trace(go.Scatter(x=dff['data'], y=dff['media_farinha'], name='', line=dict(color='royalblue', width=4)))
    fig_farinha.update_layout(title='Evolução diária de 1 KG de farinha',
                    xaxis_title='Período',
                    yaxis_title='Custo (R$)')
    st.plotly_chart(fig_farinha, use_container_width=True)
    
    # Mostrando estatísticas descritivas por meio da função st.metric() nos últimos 30 dias
    st.markdown("As informações abaixo mostram quais são os preços mínimo, médio, mediana e preço máximo do quilograma da farinha relativo ao custo médio estimado diário nos últimos 30 dias na cidade de João Pessoa.")
    col1_farinha, col2_farinha, col3_farinha, col4_farinha = st.columns(4)

    min_farinha=df['media_farinha'].min().round(2); media_farinha=df['media_farinha'].mean().round(2); mediana_farinha=df['media_farinha'].median().round(2); 
    max_farinha=df['media_farinha'].max().round(2)
    
    col1_farinha.metric("Mínimo", f'R$ {min_farinha}')
    col2_farinha.metric("Média", f'R$ {media_farinha}')
    col3_farinha.metric("Mediana", f'R$ {mediana_farinha}')
    col4_farinha.metric("Máximo", f'R$ {max_farinha}')
    
    # box plot custo da farinha por dia da semana
    st.markdown("Já o boxplot abaixo mostra como tem se comportado o preço do quilograma da farinha relativo ao custo médio estimado diário nos últimos 30 dias por dia da semana.")
    box_farinha = px.box(df, x="dia_semana", y="media_farinha", points="all")
    box_farinha.update_layout(title='Custo médio por dia da semana',
                   xaxis_title='Dia da semana',
                   yaxis_title='Custo (R$)')
    box_farinha.update_xaxes(categoryorder='array', categoryarray= ['Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo'])
    st.plotly_chart(box_farinha, use_container_width=True)
    
    # Tabela contendo o súltimos sete dias
    st.markdown("Por fim, mostra-se os preços médios observados dos últimos 7 dias de coleta na cidade de João Pessoa.")
    table_farinha = precos.tail(7).round(2)
    table_farinha = table_farinha[['data', 'media_farinha']]
    table_farinha = table_farinha.rename(columns = {'data':'Data', 'media_farinha':'Média Farinha'})
    table_farinha = table_farinha.pivot_table(index=["Data"], 
                    values='Média Farinha')
    table_farinha = table_farinha.T
    st.table(table_farinha)
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Tomate
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Gráfico de linha evolução de 1 KG de Tomate
if escolha == "Tomate":
    st.markdown("O Gráfico a seguir mostra a evolução diária do custo médio de 1 KG de tomate na cidade de João Pessoa.")
    fig_tomate = go.Figure()
    fig_tomate.add_trace(go.Scatter(x=dff['data'], y=dff['media_tomate'], name='', line=dict(color='royalblue', width=4)))
    fig_tomate.update_layout(title='Evolução diária de 1 KG de tomate',
                    xaxis_title='Período',
                    yaxis_title='Custo (R$)')
    st.plotly_chart(fig_tomate, use_container_width=True)
    
    # Mostrando estatísticas descritivas por meio da função st.metric() nos últimos 30 dias
    st.markdown("As informações abaixo mostram quais são os preços mínimo, médio, mediana e preço máximo do quilograma do tomate relativo ao custo médio estimado diário nos últimos 30 dias na cidade de João Pessoa.")
    col1_tomate, col2_tomate, col3_tomate, col4_tomate = st.columns(4)

    min_tomate=df['media_tomate'].min().round(2); media_tomate=df['media_tomate'].mean().round(2); mediana_tomate=df['media_tomate'].median().round(2); 
    max_tomate=df['media_tomate'].max().round(2)
    
    col1_tomate.metric("Mínimo", f'R$ {min_tomate}')
    col2_tomate.metric("Média", f'R$ {media_tomate}')
    col3_tomate.metric("Mediana", f'R$ {mediana_tomate}')
    col4_tomate.metric("Máximo", f'R$ {max_tomate}')
    
    # box plot custo do tomate por dia da semana
    st.markdown("Já o boxplot abaixo mostra como tem se comportado o preço do quilograma do tomate relativo ao custo médio estimado diário nos últimos 30 dias por dia da semana.")
    box_tomate = px.box(df, x="dia_semana", y="media_tomate", points="all")
    box_tomate.update_layout(title='Custo médio por dia da semana',
                   xaxis_title='Dia da semana',
                   yaxis_title='Custo (R$)')
    box_tomate.update_xaxes(categoryorder='array', categoryarray= ['Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo'])
    st.plotly_chart(box_tomate, use_container_width=True)

    # Tabela contendo o súltimos sete dias
    st.markdown("Por fim, mostra-se os preços médios observados dos últimos 7 dias de coleta na cidade de João Pessoa.")
    table_tomate = precos.tail(7).round(2)
    table_tomate = table_tomate[['data', 'media_tomate']]
    table_tomate = table_tomate.rename(columns = {'data':'Data', 'media_tomate':'Média Tomate'})
    table_tomate = table_tomate.pivot_table(index=["Data"], 
                    values='Média Tomate')
    table_tomate = table_tomate.T
    st.table(table_tomate)
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Pão
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Gráfico de linha evolução de 1 KG de pão
if escolha == "Pão":
    st.markdown("O Gráfico a seguir mostra a evolução diária do custo médio de 1 KG de pão na cidade de João Pessoa.")
    fig_pao = go.Figure()
    fig_pao.add_trace(go.Scatter(x=dff['data'], y=dff['media_pao'], name='', line=dict(color='royalblue', width=4)))
    fig_pao.update_layout(title='Evolução diária de 1 KG de pão',
                    xaxis_title='Período',
                    yaxis_title='Custo (R$)')
    st.plotly_chart(fig_pao, use_container_width=True)
    
    # Mostrando estatísticas descritivas por meio da função st.metric() nos últimos 30 dias
    st.markdown("As informações abaixo mostram quais são os preços mínimo, médio, mediana e preço máximo do quilograma do pão relativo ao custo médio estimado diário nos últimos 30 dias na cidade de João Pessoa.")
    col1_pao, col2_pao, col3_pao, col4_pao = st.columns(4)

    min_pao=df['media_pao'].min().round(2); media_pao=df['media_pao'].mean().round(2); mediana_pao=df['media_pao'].median().round(2); 
    max_pao=df['media_pao'].max().round(2)
    
    col1_pao.metric("Mínimo", f'R$ {min_pao}')
    col2_pao.metric("Média", f'R$ {media_pao}')
    col3_pao.metric("Mediana", f'R$ {mediana_pao}')
    col4_pao.metric("Máximo", f'R$ {max_pao}')
    
    # box plot custo do pão por dia da semana
    st.markdown("Já o boxplot abaixo mostra como tem se comportado o preço do quilograma do pão relativo ao custo médio estimado diário nos últimos 30 dias por dia da semana.")
    box_pao = px.box(df, x="dia_semana", y="media_pao", points="all")
    box_pao.update_layout(title='Custo médio por dia da semana',
                   xaxis_title='Dia da semana',
                   yaxis_title='Custo (R$)')
    box_pao.update_xaxes(categoryorder='array', categoryarray= ['Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo'])
    st.plotly_chart(box_pao, use_container_width=True)
    
    # Tabela contendo o súltimos sete dias
    st.markdown("Por fim, mostra-se os preços médios observados dos últimos 7 dias de coleta na cidade de João Pessoa.")
    table_pao = precos.tail(7).round(2)
    table_pao = table_pao[['data', 'media_pao']]
    table_pao = table_pao.rename(columns = {'data':'Data', 'media_pao':'Média Pão'})
    table_pao = table_pao.pivot_table(index=["Data"], 
                    values='Média Pão')
    table_pao = table_pao.T
    st.table(table_pao)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Café
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Gráfico de linha evolução de 250 gramas de café
if escolha == "Café":
    st.markdown("O Gráfico a seguir mostra a evolução diária do custo médio de 250 gramas de café na cidade de João Pessoa.")
    fig_cafe = go.Figure()
    fig_cafe.add_trace(go.Scatter(x=dff['data'], y=dff['media_cafe'], name='', line=dict(color='royalblue', width=4)))
    fig_cafe.update_layout(title='Evolução diária de 250 gramas de café',
                    xaxis_title='Período',
                    yaxis_title='Custo (R$)')
    st.plotly_chart(fig_cafe, use_container_width=True)
    
    # Mostrando estatísticas descritivas por meio da função st.metric() nos últimos 30 dias
    st.markdown("As informações abaixo mostram quais são os preços mínimo, médio, mediana e preço máximo de 250 gramas de café relativo ao custo médio estimado diário nos últimos 30 dias na cidade de João Pessoa.")
    col1_cafe, col2_cafe, col3_cafe, col4_cafe = st.columns(4)

    min_cafe=df['media_cafe'].min().round(2); media_cafe=df['media_cafe'].mean().round(2); mediana_cafe=df['media_cafe'].median().round(2); 
    max_cafe=df['media_cafe'].max().round(2)
    
    col1_cafe.metric("Mínimo", f'R$ {min_cafe}')
    col2_cafe.metric("Média", f'R$ {media_cafe}')
    col3_cafe.metric("Mediana", f'R$ {mediana_cafe}')
    col4_cafe.metric("Máximo", f'R$ {max_cafe}')
    
    # box plot custo do café por dia da semana
    st.markdown("Já o boxplot abaixo mostra como tem se comportado o preço de 250 gramas de cfé relativo ao custo médio estimado diário nos últimos 30 dias por dia da semana.")
    box_cafe = px.box(df, x="dia_semana", y="media_cafe", points="all")
    box_cafe.update_layout(title='Custo médio por dia da semana',
                   xaxis_title='Dia da semana',
                   yaxis_title='Custo (R$)')
    box_cafe.update_xaxes(categoryorder='array', categoryarray= ['Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo'])
    st.plotly_chart(box_cafe, use_container_width=True)
    
    # Tabela contendo o súltimos sete dias
    st.markdown("Por fim, mostra-se os preços médios observados dos últimos 7 dias de coleta na cidade de João Pessoa.")
    table_cafe = precos.tail(7).round(2)
    table_cafe = table_cafe[['data', 'media_cafe']]
    table_cafe = table_cafe.rename(columns = {'data':'Data', 'media_cafe':'Média Café'})
    table_cafe = table_cafe.pivot_table(index=["Data"], 
                    values='Média Café')
    table_cafe = table_cafe.T
    st.table(table_cafe)
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Banana
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Gráfico de linha evolução de 1 kg de banana
if escolha == "Banana":
    st.markdown("O Gráfico a seguir mostra a evolução diária do custo médio do quilograma da banana na cidade de João Pessoa.")
    fig_banana = go.Figure()
    fig_banana.add_trace(go.Scatter(x=dff['data'], y=dff['media_banana'], name='', line=dict(color='royalblue', width=4)))
    fig_banana.update_layout(title='Evolução diária do KG da banana',
                    xaxis_title='Período',
                    yaxis_title='Custo (R$)')
    st.plotly_chart(fig_banana, use_container_width=True)
    
    # Mostrando estatísticas descritivas por meio da função st.metric() nos últimos 30 dias
    st.markdown("As informações abaixo mostram quais são os preços mínimo, médio, mediana e preço máximo do quilograma da banana relativo ao custo médio estimado diário nos últimos 30 dias na cidade de João Pessoa.")
    col1_banana, col2_banana, col3_banana, col4_banana = st.columns(4)

    min_banana=df['media_banana'].min().round(2); media_banana=df['media_banana'].mean().round(2); mediana_banana=df['media_banana'].median().round(2); 
    max_banana=df['media_banana'].max().round(2)
    
    col1_banana.metric("Mínimo", f'R$ {min_banana}')
    col2_banana.metric("Média", f'R$ {media_banana}')
    col3_banana.metric("Mediana", f'R$ {mediana_banana}')
    col4_banana.metric("Máximo", f'R$ {max_banana}')
    
    # box plot custo da banana por dia da semana
    st.markdown("Já o boxplot abaixo mostra como tem se comportado o preço do quilograma da banana relativo ao custo médio estimado diário nos últimos 30 dias por dia da semana.")
    box_banana = px.box(df, x="dia_semana", y="media_banana", points="all")
    box_banana.update_layout(title='Custo médio por dia da semana',
                   xaxis_title='Dia da semana',
                   yaxis_title='Custo (R$)')
    box_banana.update_xaxes(categoryorder='array', categoryarray= ['Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo'])
    st.plotly_chart(box_banana, use_container_width=True)
    
    # Tabela contendo o súltimos sete dias
    st.markdown("Por fim, mostra-se os preços médios observados dos últimos 7 dias de coleta na cidade de João Pessoa.")
    table_banana = precos.tail(7).round(2)
    table_banana = table_banana[['data', 'media_banana']]
    table_banana = table_banana.rename(columns = {'data':'Data', 'media_banana':'Média Banana'})
    table_banana = table_banana.pivot_table(index=["Data"], 
                    values='Média Banana')
    table_banana = table_banana.T
    st.table(table_banana)
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Açúcar
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Gráfico de linha evolução de 1 kg de açúcar
if escolha == "Açúcar":
    st.markdown("O Gráfico a seguir mostra a evolução diária do custo médio do quilograma do açúcar na cidade de João Pessoa.")
    fig_acucar = go.Figure()
    fig_acucar.add_trace(go.Scatter(x=dff['data'], y=dff['media_acucar'], name='', line=dict(color='royalblue', width=4)))
    fig_acucar.update_layout(title='Evolução diária do KG do açúcar',
                    xaxis_title='Período',
                    yaxis_title='Custo (R$)')
    st.plotly_chart(fig_acucar, use_container_width=True)
    
    # Mostrando estatísticas descritivas por meio da função st.metric() nos últimos 30 dias
    st.markdown("As informações abaixo mostram quais são os preços mínimo, médio, mediana e preço máximo do quilograma do açúcar relativo ao custo médio estimado diário nos últimos 30 dias na cidade de João Pessoa.")
    col1_acucar, col2_acucar, col3_acucar, col4_acucar = st.columns(4)

    min_acucar=df['media_acucar'].min().round(2); media_acucar=df['media_acucar'].mean().round(2); mediana_acucar=df['media_acucar'].median().round(2); 
    max_acucar=df['media_acucar'].max().round(2)
    
    col1_acucar.metric("Mínimo", f'R$ {min_acucar}')
    col2_acucar.metric("Média", f'R$ {media_acucar}')
    col3_acucar.metric("Mediana", f'R$ {mediana_acucar}')
    col4_acucar.metric("Máximo", f'R$ {max_acucar}')
    
    # box plot custo do açúcar por dia da semana
    st.markdown("Já o boxplot abaixo mostra como tem se comportado o preço do quilograma do açúcar relativo ao custo médio estimado diário nos últimos 30 dias por dia da semana.")
    box_acucar = px.box(df, x="dia_semana", y="media_acucar", points="all")
    box_acucar.update_layout(title='Custo médio por dia da semana',
                   xaxis_title='Dia da semana',
                   yaxis_title='Custo (R$)')
    box_acucar.update_xaxes(categoryorder='array', categoryarray= ['Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo'])
    st.plotly_chart(box_acucar, use_container_width=True)
    
    # Tabela contendo o súltimos sete dias
    st.markdown("Por fim, mostra-se os preços médios observados dos últimos 7 dias de coleta na cidade de João Pessoa.")
    table_acucar = precos.tail(7).round(2)
    table_acucar = table_acucar[['data', 'media_acucar']]
    table_acucar = table_acucar.rename(columns = {'data':'Data', 'media_acucar':'Média Açúcar'})
    table_acucar = table_acucar.pivot_table(index=["Data"], 
                    values='Média Açúcar')
    table_acucar = table_acucar.T
    st.table(table_acucar)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Óleo
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Gráfico de linha evolução de 90 ml de óleo
if escolha == "Óleo":
    st.markdown("O Gráfico a seguir mostra a evolução diária do custo médio de 900 ML de óleo na cidade de João Pessoa, o óleo considerado para o cálculo da média é o de soja")
    fig_oleo = go.Figure()
    fig_oleo.add_trace(go.Scatter(x=dff['data'], y=dff['media_oleo'], name='', line=dict(color='royalblue', width=4)))
    fig_oleo.update_layout(title='Evolução diária de 900 ML de óleo',
                    xaxis_title='Período',
                    yaxis_title='Custo (R$)')
    st.plotly_chart(fig_oleo, use_container_width=True)
    
    # Mostrando estatísticas descritivas por meio da função st.metric() nos últimos 30 dias
    st.markdown("As informações abaixo mostram quais são os preços mínimo, médio, mediana e preço máximo de 900 ML de óleo relativo ao custo médio estimado diário nos últimos 30 dias na cidade de João Pessoa.")
    col1_oleo, col2_oleo, col3_oleo, col4_oleo = st.columns(4)

    min_oleo=df['media_oleo'].min().round(2); media_oleo=df['media_oleo'].mean().round(2); mediana_oleo=df['media_oleo'].median().round(2); 
    max_oleo=df['media_oleo'].max().round(2)
    
    col1_oleo.metric("Mínimo", f'R$ {min_oleo}')
    col2_oleo.metric("Média", f'R$ {media_oleo}')
    col3_oleo.metric("Mediana", f'R$ {mediana_oleo}')
    col4_oleo.metric("Máximo", f'R$ {max_oleo}')
    
    # box plot custo do óleo por dia da semana
    st.markdown("Já o boxplot abaixo mostra como tem se comportado o preço de 900 ML de óleo relativo ao custo médio estimado diário nos últimos 30 dias por dia da semana.")
    box_oleo = px.box(df, x="dia_semana", y="media_oleo", points="all")
    box_oleo.update_layout(title='Custo médio por dia da semana',
                   xaxis_title='Dia da semana',
                   yaxis_title='Custo (R$)')
    box_oleo.update_xaxes(categoryorder='array', categoryarray= ['Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo'])
    st.plotly_chart(box_oleo, use_container_width=True)
    
    # Tabela contendo o súltimos sete dias
    st.markdown("Por fim, mostra-se os preços médios observados dos últimos 7 dias de coleta na cidade de João Pessoa.")
    table_oleo = precos.tail(7).round(2)
    table_oleo = table_oleo[['data', 'media_oleo']]
    table_oleo = table_oleo.rename(columns = {'data':'Data', 'media_oleo':'Média Óleo'})
    table_oleo = table_oleo.pivot_table(index=["Data"], 
                    values='Média Óleo')
    table_oleo = table_oleo.T
    st.table(table_oleo)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Manteiga
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Gráfico de linha evolução de 200 gramas de manteiga
if escolha == "Manteiga":
    st.markdown("O Gráfico a seguir mostra a evolução diária do custo médio de 200 gramas de manteiga na cidade de João Pessoa.")
    fig_manteiga = go.Figure()
    fig_manteiga.add_trace(go.Scatter(x=dff['data'], y=dff['media_manteiga'], name='', line=dict(color='royalblue', width=4)))
    fig_manteiga.update_layout(title='Evolução diária de 200 gramas de manteiga',
                    xaxis_title='Período',
                    yaxis_title='Custo (R$)')
    st.plotly_chart(fig_manteiga, use_container_width=True)
    
    # Mostrando estatísticas descritivas por meio da função st.metric() nos últimos 30 dias
    st.markdown("As informações abaixo mostram quais são os preços mínimo, médio, mediana e preço máximo de 200 gramas de manteiga relativo ao custo médio estimado diário nos últimos 30 dias na cidade de João Pessoa.")
    col1_manteiga, col2_manteiga, col3_manteiga, col4_manteiga = st.columns(4)

    min_manteiga=df['media_manteiga'].min().round(2); media_manteiga=df['media_manteiga'].mean().round(2); mediana_manteiga=df['media_manteiga'].median().round(2); 
    max_manteiga=df['media_manteiga'].max().round(2)
    
    col1_manteiga.metric("Mínimo", f'R$ {min_manteiga}')
    col2_manteiga.metric("Média", f'R$ {media_manteiga}')
    col3_manteiga.metric("Mediana", f'R$ {mediana_manteiga}')
    col4_manteiga.metric("Máximo", f'R$ {max_manteiga}')
    
    # box plot custo da manteiga por dia da semana
    st.markdown("Já o boxplot abaixo mostra como tem se comportado o preço de 200 gramas de manteiga relativo ao custo médio estimado diário nos últimos 30 dias por dia da semana.")
    box_manteiga = px.box(df, x="dia_semana", y="media_manteiga", points="all")
    box_manteiga.update_layout(title='Custo médio por dia da semana',
                   xaxis_title='Dia da semana',
                   yaxis_title='Custo (R$)')
    box_manteiga.update_xaxes(categoryorder='array', categoryarray= ['Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo'])
    st.plotly_chart(box_manteiga, use_container_width=True)
    
    # Tabela contendo o súltimos sete dias
    st.markdown("Por fim, mostra-se os preços médios observados dos últimos 7 dias de coleta na cidade de João Pessoa.")
    table_manteiga = precos.tail(7).round(2)
    table_manteiga = table_manteiga[['data', 'media_manteiga']]
    table_manteiga = table_manteiga.rename(columns = {'data':'Data', 'media_manteiga':'Média Manteiga'})
    table_manteiga = table_manteiga.pivot_table(index=["Data"], 
                    values='Média Manteiga')
    table_manteiga = table_manteiga.T
    st.table(table_manteiga)
