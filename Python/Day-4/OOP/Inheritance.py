from bank_account import BankAccount

class SavingsAccount(BankAccount):
    
    def __init__(self,initial_balance,interest_rate):
        super().__init__(initial_balance)
        self.interest_rate=interest_rate
        
    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        print(f"Interest Applied: {interest}")
        self.deposit(interest)

saving=SavingsAccount(2000,0.05)
saving.apply_interest()
saving.withdraw(300)
print("Savings Account Balance:",saving.get_balance())