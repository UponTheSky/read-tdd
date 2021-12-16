import unittest
from multiplication import Dollar

class TestMultiplication(unittest.TestCase):
    
    def test_multiplication(self):
        five = Dollar(5)
        product_two = five.times(2)
        product_three = five.times(3)
        self.assertEqual(10, product_two.amount)
        self.assertEqual(15, product_three.amount)
