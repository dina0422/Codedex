import unittest

class BankAccount:
  def __init__(self, initial_balance=0):
    self.balance = initial_balance

  def deposit(self, amount):
    if amount <= 0:
      raise ValueError('Deposit amount must be positive')
    self.balance += amount

  def withdraw(self, amount):
    if amount <= 0:
      raise ValueError('Withdrawal amount must be positive')
    if amount > self.balance:
      raise ValueError('Insufficient funds')
    self.balance -= amount
    
class TestBankAccount(unittest.TestCase):
    
    def setUp(self):
      self.bankaccount = BankAccount(100)
      
    def tearDown(self):
      self.bankaccount = None
      
    def test_deposit_positive_amount():
        self.bankaccount.deposit(50)
        self.assertEqual(self.bankaccount.balance, 150)
        
    