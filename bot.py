import alpaca_trade_api as tradeapi
import talib
import time

# Alpaca API credentials
API_KEY = 'YOUR_API_KEY'
API_SECRET = 'YOUR_API_SECRET'
BASE_URL = 'https://paper-api.alpaca.markets'  # Use 'https://api.alpaca.markets' for live trading

# Initialize Alpaca API
api = tradeapi.REST(API_KEY, API_SECRET, base_url=BASE_URL, api_version='v2')

# EMA lengths
ema9_length = 9
ema22_length = 22
ema15_length = 15

# Symbol to trade
symbol = 'AAPL'  # Change to the desired stock symbol

def ema_crossover_1h(symbol):
    # Get 1-hour historical data
    bars_1h = api.get_barset(symbol, '1H', limit=100).df[symbol]

    # Calculate EMA values
    ema9_1h = talib.EMA(bars_1h['close'], timeperiod=ema9_length)
    ema22_1h = talib.EMA(bars_1h['close'], timeperiod=ema22_length)

    # Check for EMA crossover
    if ema9_1h.iloc[-1] > ema22_1h.iloc[-1] and ema9_1h.iloc[-2] <= ema22_1h.iloc[-2]:
        return True
    else:
        return False

def close_below_ema15_15m(symbol):
    # Get 15-minute historical data
    bars_15m = api.get_barset(symbol, '15Min', limit=100).df[symbol]

    # Calculate EMA values
    ema15_15m = talib.EMA(bars_15m['close'], timeperiod=ema15_length)

    # Check if the last closed candle's close is below EMA15
    if bars_15m['close'].iloc[-1] < ema15_15m.iloc[-1]:
        return True
    else:
        return False

while True:
    if ema_crossover_1h(symbol):
        # Place a buy order
        api.submit_order(
            symbol=symbol,
            qty=1,
            side='buy',
            type='limit',
            time_in_force='gtc',
            limit_price=api.get_latest_trade(symbol).price
        )
        print("Buy order placed")

    if close_below_ema15_15m(symbol):
        # Place a sell order
        api.submit_order(
            symbol=symbol,
            qty=1,
            side='sell',
            type='limit',
            time_in_force='gtc',
            limit_price=api.get_latest_trade(symbol).price
        )
        print("Sell order placed")

    time.sleep(900)  # Sleep for 15 minutes (900 seconds)