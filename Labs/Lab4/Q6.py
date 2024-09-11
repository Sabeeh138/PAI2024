from datetime import datetime

class BankAccount:
    def __init__(self, account_number, customer_name, balance=0.0, date_of_opening=None):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.date_of_opening = date_of_opening if date_of_opening else datetime.now().strftime("%Y-%m-%d")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    
    def check_balance(self):
        print(f"Account balance: ${self.balance:.2f}")
    
    def __str__(self):
        return (f"Account Number: {self.account_number}\n"
                f"Customer Name: {self.customer_name}\n"
                f"Balance: ${self.balance:.2f}\n"
                f"Date of Opening: {self.date_of_opening}")

if __name__ == "__main__":
    account = BankAccount(account_number="123456789", customer_name="John Doe")
    print(account)
    account.deposit(500)
    account.withdraw(200)
    account.check_balance()
    print(account)
