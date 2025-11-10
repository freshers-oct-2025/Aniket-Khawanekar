from abc import ABC,abstractmethod
import uuid
from typing import List,Optional


class Account(ABC):
    
    def __init__(self,account_holder:str,initial_balance:float=0):
        self.__account_number=str(uuid.uuid4())[:8]
        self.__account_holder=account_holder
        self._balance=initial_balance
        self.__transaction_history=[]
        
    @property
    def account_number(self):
        return self.__account_number
    @property
    def account_holder(self):
        return self.__account_holder
    @property
    def balance(self):
        return self._balance

    @abstractmethod
    def withdraw(self,amount:float)->bool:
        pass
    
    @abstractmethod
    def get_account_type(self)->str:
        pass
    
    def deposit(self,amount:float)-> bool:
        if amount>0:
            self._balance+=amount
            self._add_transaction(f"Deposited ${amount:.2f}")
            return True
        return False
    
    def _add_transaction(self,description:str):
        self.__transaction_history.append({
            'description':description,
            'balance':self._balance
        })  
        
    def get_transaction_history(self)->List[dict]:
        return self.__transaction_history.copy()


class SavingAccount(Account):
    def __init__(self,account_holder:str,initial_balance: float=0,interest_rate:float=0.02):
        super().__init__(account_holder,initial_balance)
        self.__interest_rate=interest_rate
        self.__withdrawl_limit=5
        self.__withdrawl_this_month=0

    def withdraw(self, amount: float)->bool:
        if(self.__withdrawl_this_month>=self.__withdrawl_limit):
            print(f"Monthly withdrawl limit ({self.__withdrawl_limit}) reached")
            return False
        if(0<amount<=self._balance):
            self._balance-=amount
            self.__withdrawl_this_month+=1
            self._add_transaction(f"Withdrawl ${amount:.2f}")
            return True
        return False
    
    def calculate_interest(self) -> float:
        interest = self._balance * self.__interest_rate / 12
        return interest
    
    def apply_interest(self):
        interest = self.calculate_interest()
        self._balance += interest
        self._add_transaction(f"Interest applied: ${interest:.2f}")
    
    def get_account_type(self) -> str:
        return "Savings Account"    
    
class CheckingAccount(Account):
    def __init__(self, account_holder: str, initial_balance: float = 0, overdraft_limit: float = 500):
        super().__init__(account_holder, initial_balance)
        self.__overdraft_limit = overdraft_limit
    
    def withdraw(self, amount: float) -> bool:
        if amount <= self._balance + self.__overdraft_limit:
            self._balance -= amount
            self._add_transaction(f"Withdrew ${amount:.2f}")
            return True
        print(f"Insufficient funds! Available: ${self._balance + self._overdraft_limit:.2f}")
        return False
    
    def get_account_type(self) -> str:
        return "Checking Account"
    
    
class Bank:
    def __init__(self, name: str):
        self.name = name
        self.__accounts = {} 
        self._customers = {} 
    
    def create_account(self, account_type: str, customer: 'Customer', initial_balance: float = 0) -> Optional[Account]:
        if account_type.lower() == 'savings':
            account = SavingAccount(customer.name, initial_balance)
        elif account_type.lower() == 'checking':
            account = CheckingAccount(customer.name, initial_balance)
        else:
            return None
        self.__accounts[account.account_number] = account
        customer.add_account(account)

        if customer.customer_id not in self._customers:
            self._customers[customer.customer_id] = customer

        return account
    
    def get_account(self, account_number: str) -> Optional[Account]:
        """Get account by account number"""
        return self.__accounts.get(account_number)
    
    def transfer(self, from_account: str, to_account: str, amount: float) -> bool:
        """Transfer money between accounts"""
        from_acc = self.get_account(from_account)
        to_acc = self.get_account(to_account)
        
        if from_acc and to_acc:
            if from_acc.withdraw(amount):
                to_acc.deposit(amount)
                print(f"Transferred ${amount:.2f} from {from_account} to {to_account}")
                return True
        return False
    
    def get_total_deposits(self) -> float:
        """Get total deposits in bank"""
        return sum(acc.balance for acc in self.__accounts.values() if acc.balance > 0)


class Customer:
    def __init__(self, name: str, email: str):
        self.customer_id = str(uuid.uuid4())[:8]
        self.name = name
        self.email = email
        self._accounts: List[Account] = []  
    
    def add_account(self, account: Account):
        self._accounts.append(account)
    
    def get_total_balance(self) -> float:
        return sum(acc.balance for acc in self._accounts)
    
    def get_accounts_summary(self):
        for acc in self._accounts:
            print(f"{acc.get_account_type()} ({acc.account_number}): ${acc.balance:.2f}")



def process_monthly_maintenance(accounts: List[Account]):
    for account in accounts:
        print(f"\nProcessing {account.get_account_type()} - {account.account_number}")
        if isinstance(account, SavingAccount):
            account.apply_interest()
            print(f"Interest applied to savings account")
        elif isinstance(account, CheckingAccount):
            if account.balance < 0:
                fee = 35
                account._balance -= fee
                account._add_transaction(f"Overdraft fee: ${fee}")
                print(f"Overdraft fee applied")    

if __name__ == "__main__":
    bank = Bank("Python National Bank")
    
    customer1 = Customer("Aniket Kh", "Aniket@email.com")
    customer2 = Customer("Bob Johnson", "bob@email.com")
    
    savings_acc = bank.create_account("savings", customer1, 1000)
    checking_acc = bank.create_account("checking", customer1, 500)
    bob_savings = bank.create_account("savings", customer2, 2000)
    
    print(f"Aniket's Savings Account: {savings_acc.account_number}")
    print(f"Balance: ${savings_acc.balance:.2f}")
    
    savings_acc.withdraw(100)
    checking_acc.withdraw(600) 
    
    print("\nAniket's Account Summary:")
    customer1.get_accounts_summary()
    print(f"Total Balance: ${customer1.get_total_balance():.2f}")
    
    bank.transfer(savings_acc.account_number, bob_savings.account_number, 200)
    
    all_accounts = [savings_acc, checking_acc, bob_savings]
    process_monthly_maintenance(all_accounts)
    
    print("\nTransaction History for Aniket's Savings:")
    for transaction in savings_acc.get_transaction_history():
        print(f"{transaction['description']} - Balance: ${transaction['balance']:.2f}")