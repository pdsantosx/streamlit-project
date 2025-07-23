#Importar as biblotecas 
import streamlit as st
import plotly as px

#Importar o utils
from ultius import format_number


#Nosso df que criamos
from dataset import df


#Importar o app
from graficos import grafico_map_estado



#Colocar em cima o layout da página
st.set_page_config(layout='wide')

# O titulo do Dashboard
st.title("Dashboard de Vendas 📊")

#Criar as abas
abaUm, abaDois, AbaTres = st.tabs(['Dataset', 'Receita', 'Vendedores'])


#Exibir na abaUm
with abaUm:
    st.dataframe(df)

#Metricas
with abaDois:
    colunaUm, colunaDois = st.columns(2)
    with colunaUm:
        #Coletar o preço total do dataset
        st.metric('Receita Total', format_number(df['Preço'].sum()))
        st.plotly_chart(grafico_map_estado, use_container_width=True)
    with colunaDois:
        st.metric('Quantidade de Vendas', format_number(df.shape[0]))

with AbaTres:
    st.subheader("Top Vendedores por Receita")
    vendas = df.groupby('Vendedor')['Preço'].sum().sort_values(ascending=False)
    st.bar_chart(vendas)