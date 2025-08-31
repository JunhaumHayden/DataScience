import pandas as pd
import mplfinance as mpf
import yfinance as yf

def geraGrafico(ticker, start, end):
    try:
        # Importar dados da biblioteca
        dados = yf.download(ticker, start=start, end=end)

        # Plota o gráfico usando mplfinance
        mpf.plot(dados.head(30), type='candle', figsize=(16, 8), volume=True, mav=(7, 14), style='yahoo')

    except Exception as e:
        print("Ocorreu um erro:", e)

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
        geraGrafico(ticker, start, end)
    elif opcao == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
