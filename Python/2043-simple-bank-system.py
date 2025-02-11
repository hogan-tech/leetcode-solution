from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 - 1 > self.n or account2 - 1 > self.n:
            return False
        if self.balance[account1 - 1] < money:
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account - 1 > self.n:
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account - 1 > self.n:
            return False
        if self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True


bank = Bank([10, 100, 20, 50, 30])
print(bank.withdraw(3, 10))
print(bank.transfer(5, 1, 20))
print(bank.deposit(5, 20))
print(bank.transfer(3, 4, 15))
print(bank.withdraw(10, 50))
