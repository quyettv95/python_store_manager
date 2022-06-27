from Exceptions.CredentialsNotCorrect import CredentialsNotCorrect
from business.OrderManagement import OrderManagement
from business.ProductManagement import ProductManagement
from business.SaleManagement import SaleManagement
from business.StatisticManagement import StatisticManagement
from libs.Helpers import *
from services.AccountService import AccountService
from services.ProductService import ProductService
import os


clear = lambda: os.system('clear')

class Main:
    currentUser = None

    def __init__(self):
        self.accountService = AccountService()

    def process(self):
        print("Welcome to NIIT Store")
        if self.currentUser is None:
            return self.login()
        self.showMenu()

    def message(self, message):
        lengthStr = len(message)
        print("#"*lengthStr)
        print(message)
        print("#"*lengthStr)

    def login(self):
        # username = input("Enter your username:")
        # password = input("Enter your password:")
        username = "admin"
        password = "admin"
        try:
            self.currentUser = self.accountService.getAccountByCredentials(username, password)
        except CredentialsNotCorrect:
            clear()
            self.message("Username or password is not valid, please try again")
        self.process()

    def showMenu(self):
        clear()
        print("Welcome back, " + self.currentUser.name)
        if self.currentUser.isAdministrator():
            return self.performAdminMenu()
        return self.performStaffMenu()

    def performAdminMenu(self):
        menus = {
            1: "Quản lý người dùng",
            2: "Bán hàng",
            3: "Quản lý sản phẩm",
            4: "Quản lý doanh thu",
            5: "Thống kê",
            6: "Đăng xuất",
        }

        menuOption = self.processMenu(menus)
        self.processMenuOpion(menuOption)

    def processMenuOpion(self, option):
        if option == 2:
            self.sale()
        if option == 3:
            self.productManagement()
        if option == 4:
            self.orderManagement()
        if option == 5:
            self.statistic()

    def sale(self):
        saleManagement = SaleManagement()
        saleManagement.sale(self.currentUser)
        self.process()

    def statistic(self):
        clear()

        while True:
            menus = {
                1: "Thống kê doanh thu theo tháng",
                2: "Thống kê doanh thu theo nhân viên",
                3: "Thống kê doanh thu theo sản phẩm",
                4: "Thoát",
            }

            menuOption = self.processMenu(menus)
            if menuOption == 1:
                statisticManagement = StatisticManagement()
                statisticManagement.byMonth()
            if menuOption == 2:
                statisticManagement = StatisticManagement()
                statisticManagement.byStaff()
            if menuOption == 3:
                statisticManagement = StatisticManagement()
                statisticManagement.byProduct()

            if menuOption == 4:
                return self.process()

    def orderManagement(self):
        clear()

        while True:
            menus = {
                1: "Danh sách đơn hàng",
                2: "Tra cứu đơn hàng",
                3: "Thoát",
            }

            menuOption = self.processMenu(menus)
            if menuOption == 1:
                orderManagement = OrderManagement()
                orderManagement.index()

            if menuOption == 2:
                orderManagement = OrderManagement()
                orderManagement.show()

            if menuOption == 3:
                return self.process()

    def productManagement(self):
        while True:
            menus = {
                1: "Danh sách sản phẩm",
                2: "Thêm sản phẩm",
                3: "Sửa sản phẩm",
                4: "Xóa sản phẩm",
                5: "Thoát"
            }

            menuOption = self.processMenu(menus)
            productManagement = ProductManagement()
            if menuOption == 1:
                productManagement.index()
            if menuOption == 2:
                productManagement.store()
            if menuOption == 3:
                productManagement.update()
            if menuOption == 4:
                productManagement.delete()
            if menuOption == 5:
                return self.process()

    def performStaffMenu(self):
        menus = {
            2: "Bán hàng",
            6: "Đăng xuất"
        }

        menuOption = self.processMenu(menus)
        self.processMenuOpion(menuOption)

    def processMenu(self, menus):
        while True:
            print("Choose your option")
            for key in menus.keys():
                print(str(key) + ": " + menus[key])
            menu = int(input(""))
            if menu in list(menus.keys()):
                return menu
            self.message("Please enter valid option")


Main().process()
# productService = ProductService()
# print(productService.count())
# print(productService.query())
# user = accountService.getAccountByCredentials('admin', 'admin')
# print(user.getRoleName())
# print(user)
# accountService.store({
#     "username": "admin",
#     "password": md5("admin"),
#     "name": "Quyet Tran",
#     "address": "Ha Noi",
#     "role": 1,
# })

# accountService.update(6, {
#     "address": "Vinh"
# })
# print(productService.store({
#     "name": "Iphone 14 Pro Max",
#     "price": "40000000",
#     "code": "SP-007"
# }))

# productService.update(2, {
#     "price": "20000000",
#     "name": "Iphone 13 Pro Max Max",

# })
# productService.delete(1)
# accountService.delete(4)
# accountService.store('admin', md5('admin123'), "Quyet", 1)

