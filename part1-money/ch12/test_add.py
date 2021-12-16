import unittest
from money import Money, Franc, Bank

class TestAddition(unittest.TestCase):
    def test_simple_addition(self):
        summation = Money.dollar(5) + Money.dollar(5)
        bank = Bank()
        reduced = bank.reduce(summation, "USD")
        self.assertEqual(Money.dollar(10), reduced)