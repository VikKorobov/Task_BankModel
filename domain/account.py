from abc import ABC, abstractmethod
from domain.bank import Bank

class Account(ABC):

    def __init__(self, account_number: str, holder: Bank):

        self._account_number: str = account_number.strip().lower()
        self._holder: Bank = holder
        self._balance: float = 0

    @abstractmethod
    def deposit(self, amount: float) -> None: pass

    @abstractmethod
    def withdraw(self, amount: float) -> None: pass

    def transfer(self, amount: float, target_account: Account) -> None:
 
        self.withdraw(amount)
        target_account.deposit(amount)

    def get_account_number(self) -> str:

        return self._account_number
    
    def get_holder(self) -> Bank:

        return self._holder
    
    def get_balance(self) -> float:

        return self._balance