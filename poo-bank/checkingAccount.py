from account import Account

class CheckingAccount(Account):
    def __init__(self, client, number) -> None:
        super().newAccount(client, number)
        self._limit = float(1000)
        self._withdraw_limit = int(3)
