class BankAccount:
    def __init__(self, account_number, account_holder, contact_info, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.contact_info = contact_info
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.account_holder} deposited {amount}. New balance is {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{self.account_holder} withdrew {amount}. New balance is {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.balance

    def get_account_info(self):
        return f"Account Holder: {self.account_holder}, Contact: {self.contact_info}, Balance: {self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, contact_info, balance=0.0, interest_rate=0.02):
        super().__init__(account_number, account_holder, contact_info, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied at rate {self.interest_rate}. New balance is {self.balance}")


class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, contact_info, balance=0.0, overdraft_limit=500):
        super().__init__(account_number, account_holder, contact_info, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"{self.account_holder} withdrew {amount}. New balance is {self.balance}")
        else:
            print("Withdrawal denied. Overdraft limit exceeded or invalid amount.")


# Creating objects for Savings and Checking Accounts with account holder info
savings = SavingsAccount("SA123", "Abel Obare", "abelobare7@gmail.com", 10000)
checking = CheckingAccount("CA456", "Erick Were", "erick@gmail.com", 500)

# Deposit example
savings.deposit(200)
savings.apply_interest()

# Withdraw with user input
try:
    amount = float(input("Enter amount to withdraw from savings account: "))
    savings.withdraw(amount)
except ValueError:
    print("Invalid input. Please enter a valid number.")

try:
    amount = float(input("Enter amount to withdraw from checking account: "))
    checking.withdraw(amount)
except ValueError:
    print("Invalid input. Please enter a valid number.")

# Print account information
print("\nAccount Information:")
print(savings.get_account_info())
print(checking.get_account_info())
