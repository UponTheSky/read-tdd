import unittest
from multiplication import Dollar

class TestMultiplication(unittest.TestCase):
    
    def test_multiplication(self):
        five = Dollar(5)
        self.assertEqual(Dollar(10), five.times(2))
        self.assertEqual(Dollar(15), five.times(3))

    def test_equality(self):
        five_first = Dollar(5)
        five_second = Dollar(5)
        five_third = Dollar(5)
        six = Dollar(6)
        self.assertTrue(five_first == five_second)
        self.assertFalse(five_third == six)