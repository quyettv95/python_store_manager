from email import header
from Exceptions.NotFound import NotFound
from libs.Helpers import printTable
from services.ProductService import ProductService


class ProductManagement:
    def __init__(self) -> None:
        self.productService = ProductService()

    def index(self):
        products = self.productService.query()
        headers = ["id", "name", "price", "code"]
        printTable(headers, products)

    def store(self):
        name = input("Enter name: ")
        price = input("Enter price: ")
        code = input("Enter code: ")
        self.productService.store({
            "name": name,
            "price": price,
            "code": code
        })

    def update(self):
        id = input("Enter id to update: ")
        try:
            self.productService.find(id)
            name = input("Enter name: ")
            price = input("Enter price: ")
            code = input("Enter code: ")
            self.productService.update(id, {
                "name": name,
                "price": price,
                "code": code
            })
        except NotFound:
            print("Product Is Not Valid")

    def delete(self):
        id = input("Enter id to delete: ")
        try:
            self.productService.find(id)
            self.productService.delete(id)
        except NotFound:
            print("Product Is Not Valid")


