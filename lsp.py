class SavingsAccount():
    def __init__(self, balance) -> None:
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Insufficient funds in your account!")

class CheckingAccount(SavingsAccount):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            super().withdraw(amount)  # Using the parent's withdraw method
        else:
            print("Exceeds overdraft limit or insufficient funds in you account!")

def perform_bank_actions(account):
    account.withdraw(500)
    account.withdraw(600)
    account.withdraw(700)

if __name__ == "__main__":
    savings_account = SavingsAccount(500)
    checking_account = CheckingAccount(2000, overdraft_limit=500)
    perform_bank_actions(savings_account)
    perform_bank_actions(checking_account)
