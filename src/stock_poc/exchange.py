from stock import Stock


class Exchange():
    def __init__(self, n=100):
        self.stocks = {}
        self.profiles = {}

        self.populate_stocks(n)

    def populate_stocks(self, n):
        for i in range(n):
            stock = Stock()
            self.stocks[stock.uuid] = stock

    def tick(self):
        for key, val in self.stocks.items():
            val.tick()
