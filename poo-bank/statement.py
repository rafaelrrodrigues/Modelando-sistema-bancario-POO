from transaction import Transaction

class Statement:
    def __init__(self) -> None:
        self._statement = [] # to save the statement

    def add_transaction(self, transaction: Transaction):
        pass
    
    @property
    def statement(self):
        return self._statement
    