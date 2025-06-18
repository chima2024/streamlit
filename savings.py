class SavingsAccount:
    def _init_(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount, deposit_method):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} successful via {deposit_method}.")
            print(f"New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def get_balance(self):
        return self.balance

# Example usage
account = SavingsAccount("1234567890", "John Doe")
print("Initial balance:", account.get_balance())

account.deposit(1000, "Cash")
account.deposit(500, "Electronic Fund Transfer")
