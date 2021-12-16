import unittest
from money import Money, Sum, Bank

class TestAddition(unittest.TestCase):
    def test_simple_addition(self):
        five = Money.dollar(5)
        summation = five + five
        bank = Bank()
        reduced = bank.reduce(summation, "USD")
        self.assertEqual(Money.dollar(10), reduced)

    def test_plus_returns_sum(self):
        five = Money.dollar(5)
        summation = five + five
        self.assertEqual(five, summation.augend)
        self.assertEqual(five, summation.addend)
    
    def test_reduce_sum(self):
        summation = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(summation, "USD")
        self.assertEqual(Money.dollar(7), result)

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        self.assertEqual(Money.dollar(1), result)

    def test_reduce_money_different_currency(self):
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(Money.franc(2), "USD")
        self.assertEqual(Money.dollar(1), result)

    def test_identity_rate(self):
        self.assertEqual(1, Bank().rate("USD", "USD"))