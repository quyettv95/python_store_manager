from Exceptions.NotFound import NotFound
from database import Database


class BaseService:
    def __init__(self):
        self.conn = Database().getConnection()
        self.table = None
        self.cursor = self.conn.cursor(dictionary=True)

    def count(self, query = {}):
        sql = "SELECT count(*) as total FROM {0}".format(self.table)
        self.cursor.execute(sql)
        return self.cursor.fetchone().get("total")

    def query(self, query = {}):
        sql = "SELECT * FROM {0}".format(self.table)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def find(self, id):
        sql = "SELECT * FROM {0} where id = %s".format(self.table)
        self.cursor.execute(sql, (id,))
        result = self.cursor.fetchone()

        if result is None:
            raise NotFound
        return result

    def findByField(self, field, value):
        sql = "SELECT * FROM {0} where %s = %s".format(self.table)
        self.cursor.execute(sql, (field, value))
        result = self.cursor.fetchone()
        if result is None:
            raise NotFound
        return result

    def findByCode(self, code):
        sql = "SELECT * FROM {0} where code = %s".format(self.table)
        self.cursor.execute(sql, (code,))
        result = self.cursor.fetchone()
        if result is None:
            raise NotFound
        return result

    def store(self, data):
        columns = ", ".join(list(data.keys()))
        sql = "INSERT INTO {2}({0}) VALUES ({1})".format(columns, ", ".join(["%s"] * len(data.keys())), self.table)
        values = tuple(list(data.values()))
        # print(values)
        self.cursor.execute(sql, values)
        self.conn.commit()
        return self.cursor.lastrowid

    def update(self, id, data):
        values = list(data.values())
        updates = []
        for key in data.keys():
            updates.append("{0} = %s".format(key))
        sql = "UPDATE {0} SET {1} WHERE id = %s".format(self.table, ", ".join(updates))
        values.append(id)
        values = tuple(values)
        # SET price = %s, name = %s
        # print(", ".join(updates))
        # # print(values)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def delete(self, id):
        sql = "DELETE FROM {0} WHERE id = %s".format(self.table)
        # print(values)
        self.cursor.execute(sql, (id,))
        self.conn.commit()
