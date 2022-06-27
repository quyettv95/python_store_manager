from Exceptions.NotFound import NotFound
from libs.Helpers import alert, printTable
from services.OrderService import OrderService


class OrderManagement:
    def __init__(self):
        self.orderService = OrderService()

    def index(self):
        orders = self.orderService.getAllOrders()
        printTable(['id', 'Mã đơn hàng', 'Tổng tiền', 'Nhân viên bán hàng'], orders)

    def show(self):
        while True:
            try:
                orderCode = input("Nhập mã đơn hàng: ")
                order = self.orderService.findByCode(orderCode)
                orderProducts = self.orderService.getProductsFromOrderId(order.get('id'))
                alert("Thông tin đơn hàng #{0}".format(orderCode))
                formatedOrderProducts = []
                for orderProduct in orderProducts:
                    formatedOrderProducts.append([
                        orderProduct.get('code'),
                        orderProduct.get('name'),
                        orderProduct.get('quantity'),
                        int(orderProduct.get('price')) / int(orderProduct.get('quantity')),
                        orderProduct.get('price'),
                    ])
                printTable(['Mã sản phẩm', 'Tên sản phẩm', 'Số lượng', 'Đơn giá', "Thành tiền"], formatedOrderProducts)
                alert("Tổng giá trị đơn hàng là {0}".format(order.get("total_price")))

                break
            except NotFound:
                alert("Mã đơn hàng không tồn tại trên hệ thống")
