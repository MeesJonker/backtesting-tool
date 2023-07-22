import datetime;

class Engine:
    """The engine is the main object that runs a backtest"""
    def __init__(self, balance=1e5, time=datetime.now()):
        self.time = time
        self.balance = balance
        self.orders = []
        self.trades = []

class Order:
    """The order object represents a buy/sell order"""
    def __init__(self, ticker, side, size):
        self.ticker = ticker
        self.side = side
        self.size = size
        self.type = 'market'

class Trade:
    """The trade object is created when an order is filled"""
    def __init__(self, ticker, side, size, price):
        self.ticker = ticker
        self.side = side
        self.size = size
        self.price = price