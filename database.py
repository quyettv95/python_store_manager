from matplotlib.pyplot import connect
import mysql.connector

class Database:
    __host = 'localhost'
    __username = 'root'
    __password = 'root'
    __dbName = 'store'
    __port = '3306'

    def getConnection(self):
        connection = mysql.connector.connect(user=self.__username, password=self.__password,
                              host=self.__host,
                              database=self.__dbName, port=self.__port)
        return connection
