import pandas as pd
import plotly.express as px
import streamlit as st

import matplotlib.pyplot as plt

df = pd.read_csv('vehicles_us.csv', sep=",")

st.header('Projeto sprint4')


st.write("Visão dos dados")
hist_button = st.button('Cria histograma')
if hist_button:
     st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
     criahist = px.histogram(df, x="odometer")
     st.plotly_chart(criahist, use_container_width=True)
else:
 st.write(df)

 

fig = px.bar(df, x='type', color='model', title='Contagem de Modelos de Veículos por Ano de Fabricação',
             labels={'type': 'Ano de Fabricação', 'model': 'Modelo de Veículo'},
             height=500)
             
# Personaliza a legenda
fig.update_layout(legend_title_text='Modelo de Veículo')

# Exibe o gráfico
fig.show()

st.plotly_chart(fig, use_container_width=True)


histo = px.histogram(df, x='model_year', color='condition', title='Histograma de Condições por Ano de Fabricação',
                   labels={'model_year': 'Ano de Fabricação', 'condition': 'Condição'},
                   category_orders={'condition': ['fair', 'good', 'excellent', 'like new']},
                   height=500)
             
# Personaliza a legenda
histo.update_layout(legend_title_text='Condição')

# Exibe o gráfico
histo.show()

st.plotly_chart(histo, use_container_width=True)




st.title('Comparativo de Distribuição de Preço entre Dois Anos de Fabricação')
selected_year_1 = st.selectbox('Selecione o Ano de Fabricação 1:', df['model'].unique())
selected_year_2 = st.selectbox('Selecione o Ano de Fabricação 2:', df['model'].unique())
normalize_hist = st.checkbox('Normalizar Histograma', value=True)


filtered_df = df[(df['model'] == selected_year_1) | (df['model'] == selected_year_2)]


fig = px.histogram(filtered_df, x='price', color='model', barmode='overlay', 
                   labels={'price': 'Preço'},
                   category_orders={'model': [selected_year_1, selected_year_2]},
                   nbins=50, histnorm='probability' if normalize_hist else '')
fig.update_layout(title=f'Comparativo de Distribuição de Preço entre {selected_year_1} e {selected_year_2}')

# Exibe o gráfico
st.plotly_chart(fig)