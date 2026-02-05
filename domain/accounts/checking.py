from domain.account import Account
from domain.bank import Bank

class CheckingAccount(Account):

    def __init__(self, account_number: str, bank: Bank, overdraft_limit: float):

        super().__init__(account_number, bank)
        self._overdraft_limit: float = overdraft_limit

    def deposit(self, amount: float) -> None:
        
        if amount > 0: # ensure that the deposit amount is positive

            self._balance += amount

    def withdraw(self, amount: float) -> None:

        # ensure that the withdrawal amount is positive and does not exceed the overdraft limit
        if amount > 0 and amount < self._balance + self._overdraft_limit: 

            self._balance -= amount

    def get_overdraft_limit(self) -> float:

        return self._overdraft_limit
    
    def set_overdraft_limit(self, limit: float) -> None:
        
        if limit > 0: # ensure that the overdraft limit is positive

            self._overdraft_limit = limit