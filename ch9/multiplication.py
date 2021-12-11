from abc import abstractmethod

class Money(object):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        return (self._amount == other._amount) and (self.__class__.__name__ == other.__class__.__name__)

    @abstractmethod
    def times(self, amount):
        pass

    @abstractmethod
    def currency(self):
        self._currency

    @staticmethod
    def dollar(amount):
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount):
        return Franc(amount, "CHF")

# it seems like super().__class__ is not available in Python
class Dollar(Money, object):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def times(self, multiplier):
        return Money.dollar(self._amount * multiplier)
    
    def currency(self):
        return self._currency

class Franc(Money, object):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def times(self, multiplier):
        return Money.franc(self._amount * multiplier)

    def currency(self):
        return self._currency