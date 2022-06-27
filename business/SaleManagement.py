from Exceptions.NotFound import NotFound
from libs.Helpers import alert, printTable, processMenu
from models.OrderProduct import OrderProduct
from services.OrderProductService import OrderProductService
from services.OrderService import OrderService
from services.ProductService import ProductService


class SaleManagement:
    def __init__(self) -> None:
        self.productService = ProductService()
        self.orderService = OrderService()
        self.orderProductService = OrderProductService()

    def sale(self, account):
        # self.orderService.store({
        #     "code": "OR-01",
        #     "account_id": accountId
        # })
        totalPrice = 0
        orderProducts = []
        while True:
            try:
                productCode = input("Enter Product Code: ")
                # product = self.productService.find(3)
                product = self.productService.findByCode(productCode)
                quantity = int(input("Quantity for {0}: ".format(product['name'])))
                orderProduct = OrderProduct(product, quantity)
                orderProducts.append(orderProduct)
                totalPrice += orderProduct.getPrice()
            except NotFound:
                alert("Product is not valid")
            menu = processMenu({
                1: "Add more product",
                2: "Process Payment"
            })
            if menu == 2:
                break
        totalProduct = self.orderService.count()
        totalProduct += 1
        code  = "OR-" + str(totalProduct)
        orderId = self.orderService.store({
            "code": code,
            "account_id": account.id,
            "total_price": totalPrice
        })
        for orderProduct in orderProducts:
            self.orderProductService.store({
                "product_id": orderProduct.product.get("id"),
                "order_id": orderId,
                "quantity": orderProduct.quantity,
                "price": orderProduct.getPrice(),
            })



