class History:
    def __init__(self, total_payment = 0.0):
        self._total_payment = total_payment
    
    @property
    def total_payment(self):
        return self._total_payment

    @total_payment.setter
    def total_payment(self, total_payment):
        self._total_payment = total_payment