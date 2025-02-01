class BankAccount:
    def __init__(self, account_id, balance=0):
        self.acc = account_id
        self.bal = balance
        print(f"Account details \nAccount ID: {self.acc} \nBalance: {self.bal}")

    def deposit(self, money):
        if money > 0:
            self.bal += money
            print(f"Deposited {money}. New balance: {self.bal}")
        else:
            print("Deposit amount must be more than 0")

    def withdraw(self, money):
        if  money <= self.bal:
            self.bal -= money
            print(f"Withdrawn {money}. New balance: {self.bal}")
        elif money > self.bal:
            print("Insufficient funds!")
        else:
            print("Invalid withdrawal amount!")

    def get_bank_details(self):
        print(f"Current Balance: {self.bal}")


account = BankAccount("6455956", 1000)
account.deposit(600)
account.withdraw(500)
account.withdraw(1500)  
