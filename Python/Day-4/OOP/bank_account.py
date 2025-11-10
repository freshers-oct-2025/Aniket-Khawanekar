
class BankAccount:
    __balance=0  
    def __init__(self,initial_balance):
        self.__balance=initial_balance  
    
    def deposit(self,amount):
        if(amount>0):
            self.__balance += amount
            print(f"Deposited: {amount}")
            
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self,amount):
        if(0<amount<=self.__balance):
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
    
    def get_balance(self):
        return self.__balance
if __name__ == "__main__":
        acc=BankAccount(1000)
        acc.deposit(500)
        acc.withdraw(200)
        print("Current Balance:",acc.get_balance())
        # print(acc.__balance)        
        print(acc._BankAccount__balance)