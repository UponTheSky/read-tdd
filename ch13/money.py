from abc import abstractmethod, ABC

class Expression(ABC):
    @abstractmethod
    def reduce(self):
        pass

class Sum(Expression):
    def __init__(self, augend=0, addend=0):
        self.augend = augend
        self.addend = addend    

    def reduce(self, to):
        amount = self.augend._amount + self.addend._amount
        return Money(amount, to)

class Money(Expression):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        return (self._amount == other._amount) and (self._currency == other._currency)

    def __str__(self):
        return self._amount + " " + self._currency

    def __add__(self, other):
        return Sum(self, other)

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    def currency(self):
        return self._currency

    def reduce(self, _):
        return self

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")


# it seems like super().__class__ is not available in Python
class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

class Bank:
    def reduce(self, source, to):
        return source.reduce(to)
