#pip install mplfinance

import pandas as pd
import mplfinance as mpf
import yfinance as yf

dados = yf.download('AAPL', start='2023-01-01', end='2023-12-31')
mpf.plot(dados.head(30), type='candle', figsize = (16,8), volume=True, mav=(7,14), style='yahoo')