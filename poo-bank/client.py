from account import Account
from transaction import Transaction

class Client:
    def __init__(self, address) -> None:
        self._address = str(address)
        self._accounts = []

    #create transaction
    def perform_transaction(account: Account, transaction: Transaction):
        pass

    def add_account(account: Account):
        pass