from domain.account import Account

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