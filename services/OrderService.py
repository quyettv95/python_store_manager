from services.BaseService import BaseService


class OrderService(BaseService):
    def __init__(self):
        super().__init__()
        self.table = "orders"

    def getAllOrders(self):
        sql = "select {0}.id, code, total_price, accounts.name as account_name from {0} join accounts on accounts.id = {0}.account_id".format(self.table)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def getProductsFromOrderId(self, orderId):
        sql = "select * from products join order_product on order_product.product_id = products.id where order_id = %s"
        self.cursor.execute(sql, (orderId,))
        return self.cursor.fetchall()

    def getStatisticByMonth(self):
        sql = "SELECT sum(total_price) as revenue,DATE_FORMAT(created_at, \"%Y-%m\") as yearmonth FROM orders group by yearmonth;"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def getStatisticByStaff(self):
        sql = "SELECT sum(total_price) as revenue, name FROM orders join accounts on accounts.id = orders.account_id group by account_id;"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def getStatisticByProduct(self):
        sql = "SELECT sum(total_price) as revenue, products.name as name From orders join order_product on order_product.order_id = orders.id join products on products.id = order_product.product_id group by product_id order by revenue desc;"
        self.cursor.execute(sql)
        return self.cursor.fetchall()


