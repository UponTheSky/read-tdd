from abc import abstractmethod

class Money(object):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        return (self._amount == other._amount) and (self._currency == other._currency)

    def __str__(self):
        return self._amount + " " + self._currency

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    def currency(self):
        return self._currency

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")

# it seems like super().__class__ is not available in Python
class Franc(Money, object):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
