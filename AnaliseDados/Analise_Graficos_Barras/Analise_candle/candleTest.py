import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.backends.backend_tkagg as tkagg
import mplfinance as mpf
import yfinance as yf

def geraGrafico():
    try:
        # Obter os valores inseridos nos campos de entrada
        ticker = ticker_entry.get()
        start = start_entry.get()
        end = end_entry.get()

        # Importar dados da biblioteca
        dados = yf.download(ticker, start=start, end=end)

        # Plota o gráfico usando mplfinance
        mpf.plot(dados.head(30), type='candle', figsize=(16, 8), volume=True, mav=(7, 14), style='yahoo')

    except Exception as e:
        result_label.config(text=f"Ocorreu um erro: {e}")

# Função para encerrar o programa
def encerrarPrograma():
    root.destroy()

# Criar a janela principal
root = tk.Tk()
root.title("Gerador de Gráfico Financeiro")

# Criar os campos de entrada e rótulos para o ticker, data de início e data de fim
ticker_label = ttk.Label(root, text="Ticker:")
ticker_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
ticker_entry = ttk.Entry(root)
ticker_entry.grid(row=0, column=1, padx=5, pady=5)

start_label = ttk.Label(root, text="Data de Início (AAAA-MM-DD):")
start_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
start_entry = ttk.Entry(root)
start_entry.grid(row=1, column=1, padx=5, pady=5)

end_label = ttk.Label(root, text="Data de Fim (AAAA-MM-DD):")
end_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
end_entry = ttk.Entry(root)
end_entry.grid(row=2, column=1, padx=5, pady=5)

# Botão para gerar o gráfico
gerar_button = ttk.Button(root, text="Gerar Gráfico", command=geraGrafico)
gerar_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Rótulo para exibir mensagens de erro
result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Botão para encerrar o programa
encerrar_button = ttk.Button(root, text="Encerrar", command=encerrarPrograma)
encerrar_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Iniciar o loop de eventos
root.mainloop()
