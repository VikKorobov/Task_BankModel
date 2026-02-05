from domain.accounts.checking import CheckingAccount
from domain.accounts.savings import SavingsAccount
from domain.bank import Bank
from domain.person import Person

if __name__ == "__main__":

    bank = Bank("My Bank")
    person = Person("John Doe", "123 Main St")
    checking_account = CheckingAccount("123456", bank, 500)
    savings_account = SavingsAccount("654321", bank, 0.02)

    person.add_account(checking_account)
    person.add_account(savings_account)

    checking_account.deposit(1000)
    checking_account.withdraw(200)
    print(f"Checking Account Balance: {checking_account.get_balance()}")
    
    savings_account.deposit(2000)
    savings_account.withdraw(500)
    print(f"Savings Account Balance: {savings_account.get_balance()}")

    savings_account.apply_monthly_interest()

    for months in range(12):

        savings_account.apply_monthly_interest()
        print(f"Balance after {months + 1} month(s): {savings_account.get_balance()}")

    checking_account.set_overdraft_limit(3000)
    checking_account.transfer(2500, savings_account)
    print(f"Checking Account Balance after transfer: {checking_account.get_balance()}")
    print(f"Savings Account Balance after transfer: {savings_account.get_balance()}")


    

