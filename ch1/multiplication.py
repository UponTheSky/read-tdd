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

    def times(self, multiplier):
        """
        Parameters
        ----------
        multiplier: int

        Returns
        -------
        None
        """   
        self.amount *= multiplier