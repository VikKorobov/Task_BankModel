from domain.account import Account
from domain.bank import Bank


class SavingsAccount(Account):

    def __init__(self, account_number: str, bank: Bank, interest_rate: float):

        super().__init__(account_number, bank)
        self._interest_rate: float = interest_rate

    def deposit(self, amount: float) -> None:
        if amount > 0: # ensure that the deposit amount is positive

            self._balance += amount

    def withdraw(self, amount: float) -> None:

        # ensure that the withdrawal amount is positive and does not exceed the balance
        if amount > 0 and amount < self._balance: 

            self._balance -= amount

    def apply_monthly_interest(self) -> None:

        self._balance += self._balance * self._interest_rate

    def get_interest_rate(self) -> float:

        return self._interest_rate
    
    def set_interest_rate(self, rate: float) -> None:

        if rate > 0 and rate < 1: # ensure that the interest rate is between 0 and 1

            self._interest_rate = rate