import yfinance as yf
import plotly.graph_objs as graph
import os
if not os.path.exists("images"):
    os.mkdir("images")

ticker = input("Provide a ticker:")
ticker = ticker.upper()
StockData = yf.download(tickers=ticker, period = '90d', interval = '1d' ,rounding= True)

Sgraph = graph.Figure()
Sgraph.add_trace(graph.Candlestick(x=StockData.index,open = StockData['Open'], high=StockData['High'], low=StockData['Low'], close=StockData['Close'], name = 'market data'))
Sgraph.update_layout(title = ticker + '\'s share price', xaxis_title = 'Date', yaxis_title = 'Price')

Sgraph.write_image("static/fig1.png")