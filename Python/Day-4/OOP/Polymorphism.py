from bank_account import BankAccount
from Inheritance import SavingsAccount
class CheckingAccount(BankAccount):
    def __init__(self,initial_balance):
        super().__init__(initial_balance)
        self.__transaction_fee=2

    def withdraw(self, amount):
        print("Applying Transaction fee")
        super.withdraw(amount+self.__transaction_fee)
    

def process_withdrawl(acc,amount):
    print(f"\n Processing a withdrawl from a {acc.__class__.__name__}")
    acc.withdraw(amount)
    
saving_acc=SavingsAccount(1000,0.05)
checking_acc=CheckingAccount(1000)

process_withdrawl(saving_acc,100)
process_withdrawl(checking_acc,100)