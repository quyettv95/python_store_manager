from Exceptions.CredentialsNotCorrect import CredentialsNotCorrect
from libs.Helpers import md5
from models.Account import Account
from services.BaseService import BaseService

class AccountService(BaseService):
    def __init__(self):
        super().__init__()
        self.table = "accounts"

    def getAccountByCredentials(self, username, password):
        password = md5(password)
        sql = "SELECT * FROM {0} WHERE username = %s AND password = %s".format(self.table)
        self.cursor.execute(sql, (username, password))
        result = self.cursor.fetchone()
        if result is None:
            raise CredentialsNotCorrect
        return Account(result)



