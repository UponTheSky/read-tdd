from abc import abstractmethod

class Money(object):
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        return (self._amount == other._amount) and (self.__class__.__name__ == other.__class__.__name__)

    @abstractmethod
    def times(self, amount):
        pass

    @staticmethod
    def dollar(amount):
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount)

# it seems like super().__class__ is not available in Python
class Dollar(Money, object):
    def __init__(self, amount):
        super().__init__(amount)

    def times(self, multiplier):
        return self.__class__(self._amount * multiplier)

class Franc(Money, object):
    def __init__(self, amount):
        super().__init__(amount)

    def times(self, multiplier):
        return self.__class__(self._amount * multiplier)
