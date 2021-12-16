from abc import abstractmethod, ABC

class Expression(ABC):
    @abstractmethod
    def reduce(self, bank, to):
        pass

class Sum(Expression):
    def __init__(self, augend=0, addend=0):
        self.augend = augend
        self.addend = addend    

    def reduce(self, bank, to):
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

    def reduce(self, bank, to):
        rate = bank.rate(self._currency, to)
        return Money(self._amount // rate, to)

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
    def __init__(self):
        self._rates = {}

    def add_rate(self, _from, _to, rate):
        self._rates[Pair(_from, _to)] = int(rate)

    def reduce(self, source, to):
        return source.reduce(self, to)

    def rate(self, _from, _to):
        if _from == _to: 
            return 1
        return int(self._rates.get(Pair(_from, _to)))

class Pair:
    def __init__(self, _from, _to):
        self._from = _from
        self._to = _to

    def __eq__(self, other):
        if other.__class__.__name__ != "Pair":
            return ValueError("Not a comparison of two pairs")
        
        return (self._from == other._from) and (self._to == other._to)

    def __hash__(self):
        return 0
