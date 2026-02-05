from abc import ABC

class Bank:

    def __init__(self, name: str):

        self._name: str = name


class Account(ABC):

    def __init__(self, account_number: str, holder: Bank):

        self._account_number: str = account_number
        self._holder: Bank = holder
        self._balance: float = 0


class CheckingAccount(Account):

    def __init__(self, account_number: str, bank: Bank, overdraft_limit: float):

        super().__init__(account_number, bank)
        self._overdraft_limit: float = overdraft_limit


class SavingsAccount(Account):

    def __init__(self, account_number: str, bank: Bank, interest_rate: float):

        super().__init__(account_number, bank)
        self._interest_rate: float = interest_rate


class Person:

    def __init__(self, name: str, address: str):

        self._name: str = name
        self._address: str = address
        self._accounts: list[Account] = []

