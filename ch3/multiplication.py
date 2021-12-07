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
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

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
