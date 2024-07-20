import streamlit as st
import os
from PIL import Image

#root = os.getcwd()
#if root[0] == '/':
#    root = '/app/visualizacao_cesta/'
##else:
#    root = os.path.abspath('../..')
#path = '/arquivos/aplicativo/imagens'

# Determine the root directory
root = os.getcwd()
if root[0] == '/':
    root = '/app/visualizacao_cesta/'
else:
    root = 'C:/Users/joaos/Documents/GitHub/visualizacao_cesta'


# Set the path to the image
path = os.path.join(root, 'arquivos', 'aplicativo', 'imagens', 'labimec.jpg')

#from PIL import Image
img = Image.open(f'{root}{path}/labimec.jpg')

print(f'{root}{path}/labimec.jpg')

st.set_page_config(
    page_title = "Cesta Básica LABIMEC",
    layout="wide",
    initial_sidebar_state="auto",
   page_icon = img
)


st.title('Introdução')

st.markdown("A coleta de informações de forma automática por meio de dados disponíveis na internet vem crescendo continuamente e rapidamente para uma ampla gama de produtos e serviços, incluindo a coleta de preços de produtos alimentícios. Junto a esta maior disponibilidade de preços sobre produtos em aplicativos ou em web pages, também há novas formas de coleta de dados por meio de tecnologias como web scraping, criando-se, desta forma, possibilidades para que se possa construir novos índices de preços ou seguir metodologias de órgãos estatísticos oficiais com dados disponíveis on-line.")

st.markdown("Dada esta possibilidade, esse aplicativo tem o propósito de acompanhar e exibir algumas informações sobre os custos de uma cesta de produtos alimentícios para o município de João Pessoa, sendo atualizado diariamente e de forma automática. Inicialmente, o acompanhamento das alterações nos preços desta cesta de bens será limitado a região metropolitana da capital do Estado da Paraíba, podendo ter sua análise ampliada em um momento futuro para mais capitais brasileiras e mais itens.")

st.markdown("Os bens escolhidos para o acompanhamento e estimação do custo da cesta básica são os indicados pelo decreto lei n° 399/1938 que, entre outras coisas, estabelece quais itens serão considerados para a composição da cesta em cada região do país e a quantidade mínima que cada adulto deve consumir por mês.")

col1, col2 = st.columns(2)

with col1:
    st.write("""
             Por fim, ressalta-se que este aplicativo foi desenvolvido pelo Laboratório de Inteligência Artificial e Macroeconomia Computacional (LABIMEC-UFPB), fruto da dissertação intitulada: "Coleta de preços on-line de forma automática e estimação do custo da cesta básica: uma aplicação para o município de João Pessoa". Em março de 2022 o Instituto Nacional da Propriedade Industrial (INPI) expediu o certificado de registro de programa de computador, válido por 50 anos a partir de 1° de janeiro subsequente à data de 08/11/2020, em conformidade com o §2°, art. 2° da Lei 9.609, de 19 de Fevereiro de 1998 para o aplicativo intitulado: Coletor e analisador de dados de alta frequência para o custo da cesta básica..
             
             Além de dados atualizados sobre o custo da cesta básica, também desenvolvemos indicadores e outras informações sobre assuntos econômicos. Mais detalhes podem ser obtidos nas nossas redes sociais ou solicitado por e-mail: 
             
             **Instagram:** https://www.instagram.com/labimec/ 
             
             **Twitter:** https://twitter.com/labimec
             
             **E-mail:** labimecufpb@gmail.com
             """)
    
with col2:
    st.image(f'{root}{path}/labimec.jpg')
            
st.caption("Compreende a região metropolitana de João pessoa: Bayeux, Cabedelo, Conde, Cruz do Espírito Santo, João Pessoa, Lucena, Mamanguape, Rio Tinto, Santa Rita, Alhandra, Caaporã e Pitimbu. - Lei complementar nº. 93 de 11 de dezembro de 2009")