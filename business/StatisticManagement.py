
from cProfile import label
from services.OrderService import OrderService
import matplotlib.pyplot as plt

class StatisticManagement:
    def __init__(self) -> None:
        self.orderService = OrderService()

    def byMonth(self):
        statisByMonths = self.orderService.getStatisticByMonth()
        x = []
        y = []
        z = []
        for statisByMonth in statisByMonths:
            x.append(statisByMonth.get('yearmonth'))
            y.append(statisByMonth.get('revenue'))
        plt.bar(x,y, color='r')
        plt.show()
        pass

    def byStaff(self):
        statisByStaffs = self.orderService.getStatisticByStaff()
        labels = []
        y = []
        for statisByStaff in statisByStaffs:
            labels.append(statisByStaff.get('name'))
            y.append(statisByStaff.get('revenue'))
        plt.pie(y, labels=labels)
        plt.show()
        pass

    def byProduct(self):
        statisByProducts = self.orderService.getStatisticByProduct()
        labels = []
        y = []
        for statisByProduct in statisByProducts:
            labels.append(statisByProduct.get('name'))
            y.append(statisByProduct.get('revenue'))
        plt.pie(y, labels=labels)
        plt.show()

        pass
