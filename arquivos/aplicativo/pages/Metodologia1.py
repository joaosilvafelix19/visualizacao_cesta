import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
import os

# Definindo o caminho absoluto do arquivo
file_path = r"C:/Users/joaos/Documents/GitHub/visualizacao_cesta/arquivos/aplicativo/dados/dados_jp.xlsx"

# Imprimindo o caminho do arquivo para depuração
st.write(f"Caminho do arquivo: {file_path}")

# Verificando se o arquivo existe
if not os.path.isfile(file_path):
    st.error(f"Arquivo não encontrado: {file_path}")
else:
    # Importando os dados dos preços não ponderados
    cesta = pd.read_excel(file_path, sheet_name="cesta")

    # Selecionando apenas as colunas das médias
    cesta = cesta.iloc[:, [6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50]]

    # Obtendo as médias
    carne = cesta['media_carne'].mean()
    leite = cesta['media_leite'].mean()
    feijao = cesta['media_feijao'].mean()
    arroz = cesta['media_arroz'].mean()
    farinha = cesta['media_farinha'].mean()
    tomate = cesta['media_tomate'].mean()
    pao = cesta['media_pao'].mean()
    cafe = cesta['media_cafe'].mean()
    banana = cesta['media_banana'].mean()
    acucar = cesta['media_acucar'].mean()
    oleo = cesta['media_oleo'].mean()
    manteiga = cesta['media_manteiga'].mean()

    # Criando um data frame
    tabela = pd.DataFrame(dict(
        Produtos = ["Carne", "Leite", "Feijão", "Arroz", "Farinha", "Legumes (Tomate)", "Pão Francês", "Café em Pó", "Frutas (Banana) ", "Açúcar", "Óleo", "Manteiga"],
        Peso     = ["4,5 KG","6,0 L", "4,5 KG", "3,6 KG","3,0 KG" ," 12,0 KG","6,0 KG", "300 GR","90 unid.","3,0 KG ","750 ML", "750 GR"],
        Coleta = ["1,0 KG", "1,0 L", "1,0 KG", "1,0 KG", "1,0 KG", "1,0 KG", "1,0 KG", "250 GR", "1,0 KG", "1,0 KG", "900 ML","200 GR"],
        Média = [round(carne,2), round(leite,2), round(feijao, 2), round(arroz,2), round(farinha,2), round(tomate,2), round(pao,2), round(cafe,2), round(banana,2), round(acucar,2), round(oleo,2), round(manteiga,2)]
    ))

    # Título da guia
    st.title("Metodologia")

    col1, col2 = st.columns(2)

    # Metodologia
    with col1:
        st.markdown("Neste aplicativo os dados foram coletados em supermercados varejistas que ofertam seus produtos de forma on-line na região metropolitana de João Pessoa. Os produtos pesquisados foram os indicados pelo Decreto Lei n° 399/1938 para a região 2, na qual a Paraíba faz parte. Os dados sobre o custo da cesta básica, com a frequência de coleta diária teve início no dia 09 de novembro de 2020 e vem sendo coletado de forma ininterrupta.")
                
        st.markdown("A tabela ao lado mostra as quantidades mínimas indicadas pelo decreto lei n° 399, na coluna Peso. A coluna Coleta mostra qual a medida de peso e volume que é considerada para o cálculo do valor médio de cada item, por exemplo, para o produto Carne, após a coleta dos dados, apenas os itens que tenham como medida de peso igual a 1 KG (quilograma) são considerados. Após isso, calcula-se a média de todos os itens com 1,0 KG de carne e multiplica-se por 4,5 kg, que dará o valor médio em reais do produto ponderado pelo peso. Para o item manteiga, multiplica-se o valor médio de cada item com 200 gramas e multiplica-se por 3,75 (750 gramas dividido por 200 gramas).")
    
        st.markdown("As especificidades dos produtos considerados são as seguintes: Para a Carne coxão mole (chã de dentro), coxão duro (chã de fora) e patinho, o leite considerado é o do tipo integral, o tipo de feijão coletado é o carioca tipo 1, para frutas são consideradas banana prata e nanica, o arroz considerado é o do tipo parboilizado tipo 1, e o óleo considerado é o de soja.")

    # Melhorando a estética dos dados mostrados
    with col2:
        AgGrid(tabela)
