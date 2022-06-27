from services.BaseService import BaseService


class ProductService(BaseService):
    def __init__(self):
        super().__init__()
        self.table = "products"


