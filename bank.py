from abc import ABC

class Bank:

    def __init__(self, name: str):

        self._name: str = name.strip().lower()

    def get_name(self) -> str:

        return self._name.capitalize()

class Account(ABC):

    def __init__(self, account_number: str, holder: Bank):

        self._account_number: str = account_number.strip().lower()
        self._holder: Bank = holder
        self._balance: float = 0

    def get_account_number(self) -> str:

        return self._account_number
    
    def get_holder(self) -> Bank:

        return self._holder
    
    def get_balance(self) -> float:

        return self._balance

class CheckingAccount(Account):

    def __init__(self, account_number: str, bank: Bank, overdraft_limit: float):

        super().__init__(account_number, bank)
        self._overdraft_limit: float = overdraft_limit

    def get_overdraft_limit(self) -> float:

        return self._overdraft_limit
    
    def set_overdraft_limit(self, limit: float) -> None:
        
        if limit > 0: # ensure that the overdraft limit is positive

            self._overdraft_limit = limit

class SavingsAccount(Account):

    def __init__(self, account_number: str, bank: Bank, interest_rate: float):

        super().__init__(account_number, bank)
        self._interest_rate: float = interest_rate

    def get_interest_rate(self) -> float:

        return self._interest_rate
    
    def set_interest_rate(self, rate: float) -> None:

        if rate > 0 and rate < 1: # ensure that the interest rate is between 0 and 1

            self._interest_rate = rate

class Person:

    def __init__(self, name: str, address: str):
        
        self._name: str = name.strip().lower()
        self._address: str = address.strip().lower()
        self._accounts: list[Account] = []

    def add_account(self, account: Account) -> None:

        if account not in self._accounts: # ensure that the account is not already added

            self._accounts.append(account)

    def remove_account(self, account: Account) -> None:

        if account in self._accounts: # ensure that the account is in the list

            self._accounts.remove(account)

    def get_name(self) -> str:

        return self._name.capitalize()
    
    def get_address(self) -> str:

        return self._address.capitalize()
    
    def get_accounts(self) -> list[Account]:

        return self._accounts
    
    def set_address(self, address: str) -> None:

        address = address.strip()

        if len(address) > 1: # ensure that the address is valid

            self._address = address.lower()

