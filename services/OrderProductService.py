from services.BaseService import BaseService


class OrderProductService(BaseService):
    def __init__(self):
        super().__init__()
        self.table = "order_product"


