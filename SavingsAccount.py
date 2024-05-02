from BankAccount import BankAccount

class SavingsAccount(BankAccount):

    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_bal() * self.interest_rate
        self.set_balance(self.get_bal() + interest)
        print(f'${interest} added to account balance!')
        print(f'New Balance: {self.get_bal()}')

#instantiating our SavingsAccount class
travis = SavingsAccount("Travis", 2340000, .05)
print(travis.get_bal())
travis.add_interest()
print(travis.get_bal())
travis.add_interest()
travis.add_interest()
travis.add_interest()
travis.add_interest()
travis.add_interest()
travis.add_interest()
travis.add_interest()
travis.add_interest()
travis.add_interest()