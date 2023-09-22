class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited rs{amount}. New balance: rs{self.__account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew rs{amount}. New balance: rs{self.__account_balance}")
        elif amount > self.__account_balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Amount must be greater than zero.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: rs{self.__account_balance}")



if __name__ == "__main__":
    
    account = BankAccount("12345", "Rani", 1000.0)

    
    account.display_balance()

    
    account.deposit(500.0)

    
    account.withdraw(200.0)

    
    account.withdraw(1500.0)

    
    account.display_balance()
