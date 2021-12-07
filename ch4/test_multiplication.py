import unittest
from multiplication import Dollar

class TestMultiplication(unittest.TestCase):
    
    def test_multiplication(self):
        five = Dollar(5)
        product_two = five.times(2)
        product_three = five.times(3)
        self.assertEqual(10, product_two.amount)
        self.assertEqual(15, product_three.amount)

    def test_equality(self):
        five_first = Dollar(5)
        five_second = Dollar(5)
        five_third = Dollar(5)
        six = Dollar(6)
        self.assertTrue(five_first == five_second)
        self.assertFalse(five_third == six)