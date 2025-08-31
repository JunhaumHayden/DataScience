#pip install mplfinance

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def geraGrafico(ticker, start, end):

    try:
        #importar dados da biblioteca
        dados = yf.download(ticker, start=start, end = end)

        # Se não houver erro, continua com o código
        #dados
        dados.columns
        #renomear as colunas
        dados.columns = ['Abertura', 'Maximo', 'Minimo', 'Fechamento', 'Fech_Ajust', 'Volume']
        #remonear apenas 1 coluna, necessario atribuir o novo nome
        dados = dados.rename_axis('Data')

        #cria um dataframe com as primeiras 60 linhas .copy() para copiar os dados para o df
        df = dados.head(60).copy()

        # Convertendo o índice em uma coluna de data
        df['Data'] = df.index

        # Convertendo as datas para o formato numérico de matplotlib
        # Isso é necessário para que o Matplotlib possa plotar as datas corretamente no gráfico
        df['Data'] = df['Data'].apply(mdates.date2num)

        #criando media movel no dataframe
        df['MA7'] = df['Fechamento'].rolling(window=7).mean()
        df['MA14'] = df['Fechamento'].rolling(window=14).mean()

        # Criando subplots
        '''
        "Primeiro, criamos uma figura que conterá nossos gráficos usando make_subplots.
        Isso nos permite ter múltiplos gráficos em uma única visualização.
        Aqui, teremos dois subplots: um para o gráfico de candlestick e outro para o volume de transações."

        '''
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                            vertical_spacing=0.1,
                            subplot_titles=('Candlesticks', 'Volume Transacionado'),
                            row_width=[0.2, 0.7])

        '''
        "No gráfico de candlestick, cada candle representa um dia de negociação,
        mostrando o preço de abertura, fechamento, máximo e mínimo. Vamos adicionar este gráfico à nossa figura."
        '''
        # Adicionando o gráfico de candlestick
        fig.add_trace(go.Candlestick(x=df.index,
                                    open=df['Abertura'],
                                    high=df['Maximo'],
                                    low=df['Minimo'],
                                    close=df['Fechamento'],
                                    name='Candlestick'),
                                    row=1, col=1)

        # Adicionando as médias móveis
        # Adicionamos também médias móveis ao mesmo subplot para análise de tendências
        fig.add_trace(go.Scatter(x=df.index,
                                y=df['MA7'],
                                mode='lines',
                                name='MA7 - Média Móvel 7 Dias'),
                                row=1, col=1)

        fig.add_trace(go.Scatter(x=df.index,
                                y=df['MA14'],
                                mode='lines',
                                name='MA14 - Média Móvel 14 Dias'),
                                row=1, col=1)

        # Adicionando o gráfico de barras para o volume
        # Em seguida, criamos um gráfico de barras para o volume de transações, que nos dá uma ideia da atividade de negociação naquele dia
        fig.add_trace(go.Bar(x=df.index,
                            y=df['Volume'],
                            name='Volume'),
                            row=2, col=1)

        # Atualizando layout
        #Finalmente, configuramos o layout da figura, ajustando títulos, formatos de eixo e outras configurações para tornar o gráfico claro e legível.
        fig.update_layout(yaxis_title='Preço',
                        xaxis_rangeslider_visible=False,  # Desativa o range slider
                        width=1100, height=600)

        # Mostrando o gráfico
        fig.show()
        return True

    except Exception as e:
        # Se ocorrer um erro, imprime a mensagem de erro
        return "Ocorreu um erro:", e

# Loop infinito para o menu interativo
while True:
    # Exibir opções para o usuário
    print("MENU INTERATIVO")
    print("1. Gerar gráfico")
    print("0. Encerrar")

    # Solicitar a entrada do usuário
    opcao = input("Digite a opção desejada: ")

    # Verificar a opção escolhida
    if opcao == "1":
        ticker = input("Digite o ticker: ")
        start = input("Digite a data de início (AAAA-MM-DD): ")
        end = input("Digite a data de fim (AAAA-MM-DD): ")
        resultado = geraGrafico(ticker, start, end) 
        #if isinstance(resultado, pd.DataFrame):  # Verifica se o resultado é um DataFrame
        if resultado: 
            print(resultado)
        else:
            print(resultado)  # Imprime a mensagem de erro
            
    elif opcao == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")