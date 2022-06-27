import hashlib
from prettytable import PrettyTable



def md5(inputStr):
    result = hashlib.md5(inputStr.encode())
    return result.hexdigest()

def printTable(headers, rows):
    table = PrettyTable()
    table.field_names = headers
    for row in rows:
        if isinstance(row, dict):
            table.add_row(list(row.values()))
        else:
            table.add_row(row)
    print(table)

def alert(message):
    lengthStr = len(message)
    print("#"*lengthStr)
    print(message)
    print("#"*lengthStr)

def processMenu(menus):
        while True:
            print("Choose your option")
            for key in menus.keys():
                print(str(key) + ": " + menus[key])
            menu = int(input(""))
            if menu in list(menus.keys()):
                return menu
            alert("Please enter valid option")