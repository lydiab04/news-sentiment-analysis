import talib

def compute_sma(close_prices, window=20):
    return talib.SMA(close_prices, timeperiod=window)

def compute_rsi(close_prices, window=14):
    return talib.RSI(close_prices, timeperiod=window)

def compute_macd(close_prices):
    macd, signal, hist = talib.MACD(close_prices)
    return macd, signal, hist