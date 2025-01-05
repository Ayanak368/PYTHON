class BankAccount:
    def __init__(self, account_number, name, account_type, balance=0):
        """
        Constructor to initialize the bank account details.
        """
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        """
        Method to deposit money into the bank account.
        """
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully. New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        """
        Method to withdraw money from the bank account.
        """
        if amount > self.balance:
            print(f"Insufficient balance! Current balance: ₹{self.balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully. Remaining balance: ₹{self.balance}")

    def display_account_details(self):
        """
        Method to display account details.
        """
        print("\nAccount Details:")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: ₹{self.balance}")


# Example Usage
account = BankAccount(account_number=123456789, name="John Doe", account_type="Savings", balance=5000)

account.display_account_details()

# Deposit some amount
account.deposit(2000)

# Withdraw some amount
account.withdraw(3000)

# Try withdrawing more than the balance
account.withdraw(5000)

# Final account details
account.display_account_details()
