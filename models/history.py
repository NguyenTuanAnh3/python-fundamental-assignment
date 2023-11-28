from validator.customer import CustomerValidator
class History:
    def __init__(self, car_identity, total_payment = 0.0):
        self.customer_validator = CustomerValidator()
        self._car_identity = self.customer_validator.check_car_identity_valid(car_identity)
        self._total_payment = total_payment
        
    @property
    def car_identity(self):
        return self._car_identity

    @car_identity.setter
    def car_identity(self, car_identity):
        self._car_identity = car_identity

    @property
    def total_payment(self):
        return self._total_payment

    @total_payment.setter
    def total_payment(self, total_payment):
        self._total_payment = total_payment