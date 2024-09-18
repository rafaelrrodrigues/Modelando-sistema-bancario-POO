class Account:
    def __init__(self, client, number) -> None:
        self._agency = str(None)
        self._balance = float(0)
        self._client = client
        self._number = int(number)
        self._history = None

    def balance():
        pass

    def deposit():
        pass

    @classmethod
    def newAccount(cls, client, number):
        return cls(client, number)
    
    def withdraw():
        pass
