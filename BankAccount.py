class BankAccount():

    def __init__(self, account_holder, balance=0):
        self.__balance = balance
        self.account_holder = account_holder

    def get_bal(self):
        return self.__balance
    
    def set_balance(self, new_balance):
        self.__balance = new_balance

    def set_holder(self, new_holder):
        self.account_holder = new_holder

    def get_holder(self):
        return self.account_holder
    
    #deposit method
    def deposit(self, money):
        if money > 0:
            self.set_balance(self.get_bal() + money)
            print(f"Deposited: ${money}")
            print(f'New Balance: {self.get_bal()}')
        else:
            print('Invalid Deposit!')

    #Withdraw method
    def withdraw(self, amount):
        if 0 < amount <= self.get_bal():
            self.set_balance(self.get_bal() - amount)
            print(f"Withdrew: ${amount}")
            print(f'New Balance: {self.get_bal()}')
        elif amount > self.get_bal():
            print('You dont have that amount in the bank!')
        else:
            print('Invalid')


dylan = BankAccount('Dylan M Katina', 12)
#testing the gettas
print(dylan.get_bal())
print(dylan.get_holder())
#depositing some chedda
dylan.deposit(1000000)

#withdraw money
dylan.withdraw(100)

