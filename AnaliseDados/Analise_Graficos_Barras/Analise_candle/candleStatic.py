#pip install mplfinance

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#importar dados da biblioteca
dados = yf.download('petr4.SA', start='2023-01-01', end = '2023-12-31')
#dados
dados.columns
#renomear as colunas
dados.columns = ['Abertura', 'Maximo', 'Minimo', 'Fechamento', 'Fech_Ajust', 'Volume']
#remonear apenas 1 coluna, necessario atribuir o novo nome
dados = dados.rename_axis('Data')

#criar um grafico com metodo .plot=(altura, largura)
dados['Fechamento'].plot(figsize=(10,6))
#O grafico complementado com matplotlib.pyplot
plt.title('Variação do preço por data', fontsize=16)
plt.legend(['Fechamento'])
#cria um dataframe com as primeiras 60 linhas .copy() para copiar os dados para o df
df = dados.head(60).copy()

#Converter o indice em uma coluna de data
df['Data'] = df.index

#converter as dadas para o formato numerico de matplotlib
#isso é necessario para que o matplotlib possa plotar as data corretamente no grafico
#.apply para aplicar a cada linha
df['Data'] = df['Data'].apply(mdates.date2num)


#cria o fundo
fig, ax = plt.subplots(figsize=(15,8))

#definir a largura dos candles no grafico
width = 0.7

for i in range(len(df)):
  #determina a cor do candle
  #verde para fechamento maior que abertura
  #vermelho para fechamento menor que abertura
  if df['Fechamento'].iloc[i] > df['Abertura'].iloc[i]:
        color = 'green'
  else:
        color = 'red'

  #Desenhando a linha vertical do candle (mecha)
  # mostra os precos minimos e maximos do dia
  #usar 'ax.plot' para desenhar uma linha vertical
  #[df['data'].iloc[i], df['data']iloc[i]] - define o ponto x da linha (data),
  #[df['minimo'].iloc[i], df['maximo'].iloc[i]] - define
  #fazendo primeiro a linha 
  ax.plot([df['Data'].iloc[i], df['Data'].iloc[i]],
            [df['Minimo'].iloc[i], df['Maximo'].iloc[i]],
            color=color,
            linewidth=1)
  #fazendo o retangulo
  #.add_patch metodo para adicionar objetos
  #abs metodo para o numero sempre ser positivo (modulo)
  ax.add_patch(plt.Rectangle((df['Data'].iloc[i] - width/2, min(df['Abertura'].iloc[i], df['Fechamento'].iloc[i])),
                               width,
                               abs(df['Fechamento'].iloc[i] - df['Abertura'].iloc[i]),
                               facecolor=color))
#criando media movel
df['MA7'] = df['Fechamento'].rolling(window=7).mean()
df['MA14'] = df['Fechamento'].rolling(window=14).mean()

# Plotando as médias móveis
ax.plot(df['Data'], df['MA7'], color='orange', label='Média Móvel 7 Dias')  # Média de 7 dias
ax.plot(df['Data'], df['MA14'], color='yellow', label='Média Móvel 14 Dias')  # Média de 14 dias
# Adicionando legendas para as médias móveis
ax.legend()

# Formatando o eixo x para mostrar as datas
# Configuramos o formato da data e a rotação para melhor legibilidade
ax.xaxis_date() #O método xaxis_date() é usado para dizer ao Matplotlib que as datas estão sendo usadas no eixo x
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)

# Adicionando título e rótulos para os eixos x e y
plt.title("Gráfico de Candlestick - PETR4.SA com matplotlib")
plt.xlabel("Data")
plt.ylabel("Preço")

# Adicionando uma grade para facilitar a visualização dos valores
plt.grid(True)

# Exibindo o gráfico
plt.show()
