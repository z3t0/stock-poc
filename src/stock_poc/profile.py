import random
from uuid import uuid4


class Profile():
    def __init__(self):
        self.uuid = uuid4()
        self.cash = random.randint(1, 100000)
        self.stocks = {}

    def buy(self, symbol, shares):
        pass

    def sell(self, symbol, shares):
        pass
