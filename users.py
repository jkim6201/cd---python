from users_with_bank_accounts import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {
            "checking": BankAccount(int_rate=0.02, balance=0),
            "savings": BankAccount(int_rate=0.5, balance=1000)
        }

    def make_deposit(self, amount, account_name):
        self.account[account_name].deposit(account)
        return self

    def make_withdrawal(self, amount, account_name):
        self.account[account_name].withdrawal(account)
        return self

    def display_user_balance(self, account_name):
        print(f"Welcome {self.name} Your current Balance is: {self.account[account_name].balance}")

    def transfer_money(self, amount, other_user):
        self.account[account_name].balance -= amount
        other_user.account[account_name].balance += amount
        print(f"The amount you are about to transfer is:{amount} to {other_user.name}")
        return self


# account_holder1 = User("Jenny", "python@python.com")
# account_holder2 = User("Cola", "pycharm@pycharm.com")

# account_holder1.transfer_money(100, account_holder2, "checking")
# account_holder2.display_user_balance("checking")