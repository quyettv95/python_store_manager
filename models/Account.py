class Account():
    def __init__(self, data):
        self.name = data.get('name')
        self.id = data.get('id')
        self.role = data.get('role')
        self.address = data.get('address')
        self.username = data.get('username')

    def getRoleName(self):
        if self.role == 1 :
            return "Admin"
        return "Staff"

    def isAdministrator(self):
        return self.role == 1