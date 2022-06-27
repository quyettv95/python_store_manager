
class OrderProduct():
    def __init__(self, product, quantity) -> None:
        self.product = product
        self.quantity = quantity

    def getPrice(self):
        return int(self.product.get('price')) * self.quantity