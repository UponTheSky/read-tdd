class Dollar:
    def __init__(self, amount):
        """
        Parameters
        ----------
        amount: int

        Returns
        -------
        None
        """    
        self._amount = amount

    def __eq__(self, other):
        return self._amount == other._amount

    def times(self, multiplier):
        """
        Parameters
        ----------
        multiplier: int

        Returns
        -------
        Dollar
        """   
        return __class__(self.amount * multiplier)
