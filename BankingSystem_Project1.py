"""""""""Write a python program to replicate a Banking system. The following features are mandatory:
1.Account login
2. Amount Depositing
3. Amount Withdrawal
Other than the above features you can add any other also."""

class Bankmanager:
    def __init__(self):
        self.accounts = {"1100456":{'pin':'456','balance':'100'},"1100789":{'pin':'789','balance':'0'}}

    def create_account(self,account_num, pin):
        if account_num not in self.accounts:
            self.accounts[account_num]={'pin':pin,'balance':0}
            print("Account created successfully")
        else:
            print("Account number already exists. Please choose a different account number.")

    def login(self, account_num, pin):
        if account_num in self.accounts and self.accounts[account_num]['pin']==pin:
            print("Login successfully")
            return True
        else:
         print("Incorrect account number or PIN. Login failed.")
         return False

    def balance(self, account_num):
        if account_num in self.accounts:
         print(f"Current balance: {self.accounts[account_num]['balance']}")

        else:
            print("Invalid account number")

    def deposit(self, account_num, amount):
        if account_num in self.accounts and amount>0:
            self.accounts[account_num]['balance']+=amount
            print(f"Deposited {amount},Current balance {self.accounts[account_num]['balance']}")
        else:
            print("Invalid account number or amount for deposit")

    def withdraw(self,account_num,amount):
        if account_num in self.accounts and amount > 0 and amount <= self.accounts[account_num]['balance']:
            self.accounts[account_num]['balance']-=amount
            print(f"Withdraw: {amount},Current balance: {self.accounts[account_num]['balance']}")
        else:
            print("Invalid account number, amount for withdrawl, or sufficient funds")



    def change_password(self, account_num, current_pin, new_pin):
        if account_num in self.accounts and self.accounts[account_num]['pin'] == current_pin:
            self.accounts[account_num]['pin'] = new_pin
            print("Password changed successfully!")
        else:
            print("Incorrect account number or current PIN. Unable to change password.")


bank_system = Bankmanager()
bank_system.create_account("1100123", "123")
bank_system.create_account("1100456", "456")
account_num=input("Enter your account number:")
pin=input("Enter your PIN:")
if bank_system.login(account_num,pin):
        while True:
            print("Select your option\n 1.Deposit\n 2.Withdraw\n 3.Balance\n 4.Change Password\n 5.Exit Program")
            choice = input("Enter your choice: ")
            if choice == '1':
                amount = float(input("Enter the deposit amount: "))
                bank_system.deposit(account_num, amount)
            elif choice == '2':
                amount = float(input("Enter the withdrawal amount: "))
                bank_system.withdraw(account_num, amount)
            elif choice == '3':
                bank_system.balance(account_num)
            elif choice == '4':
                new_pin = input("Enter your new PIN: ")
                bank_system.change_password(account_num, pin, new_pin)
            elif choice == '5':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")