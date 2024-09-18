from abc import ABC, abstractmethod
from account import Account
from datetime import date, time, datetime, timedelta

class Transaction(ABC):
    
    @abstractmethod
    def register(account: Account):
        pass