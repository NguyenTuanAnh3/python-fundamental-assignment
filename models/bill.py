class Bill:

    def __init__(self):
        self._bill = {}
        self._bills = []

    @property
    def bill(self):
        return self._bill

    @bill.setter
    def bill(self, bill):
        self._bill = bill

    @property
    def bills(self):
        return self._bills
    
    @bills.setter
    def bills(self, bills):
        self._bills = self._bills
    
    
    