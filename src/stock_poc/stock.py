import random
from uuid import uuid4


class Stock():
    def __init__(self):
        self.value = random.randint(1, 1000)
        self.volatility = random.random() * 1000
        self.counter = 0
        self.uuid = str(uuid4())
        self.shares = 0
        self.total_shares = random.randint(1, 1000)

        self.set_delta()

    def set_delta(self):
        self.delta_range = random.random() * 100
        self.delta = random.uniform(-self.delta_range, self.delta_range)

    def tick(self):
        if self.counter >= self.volatility:
            self.change_parameters()

        self.value += self.delta
        self.counter += 1

    def change_parameters(self):
        self.set_delta()
        self.counter = 0

    def buy(self, shares):
        new_count = shares + self.shares
        if new_count > self.total_shares:
            raise Exception("Cannot buy more shares than available")
        else:
            self.shares = new_count

    def sell(self, shares):
        new_count = self.shares - shares
        if new_count < 0:
            raise Exception("Cannot remove more shares than have been sold")
        else:
            self.shares = new_count
        
