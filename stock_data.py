class StockPos(object):
    def __init__(self, name, amount):
        self.name = name
        self.url = ''
        self.price = 0
        self.amount = amount

def as_StockPos(dct):
    return StockPos(dct['name'], dct['amount'])
