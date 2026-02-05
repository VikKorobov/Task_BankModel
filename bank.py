from abc import ABC

class Bank:

    def __init__(self, name: str):

        self._name: str = name

    def get_name(self) -> str:

        return self._name

class Account(ABC):

    def __init__(self, account_number: str, holder: Bank):

        self._account_number: str = account_number
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

        self._overdraft_limit = limit

class SavingsAccount(Account):

    def __init__(self, account_number: str, bank: Bank, interest_rate: float):

        super().__init__(account_number, bank)
        self._interest_rate: float = interest_rate

    def get_interest_rate(self) -> float:

        return self._interest_rate
    
    def set_interest_rate(self, rate: float) -> None:

        self._interest_rate = rate

class Person:

    def __init__(self, name: str, address: str):

        self._name: str = name
        self._address: str = address
        self._accounts: list[Account] = []

    def get_name(self) -> str:

        return self._name
    
    def get_address(self) -> str:

        return self._address
    
    def get_accounts(self) -> list[Account]:

        return self._accounts
    
    def set_address(self, address: str) -> None:

        self._address = address

