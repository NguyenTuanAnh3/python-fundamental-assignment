import datetime
from handlers.dateHandler import DateHandler
from validator.customer import CustomerValidator
class Customer:

    def __init__(self, car_identity, frequent_parking_number, available_creadit = 0.0, leave_day = None):
        self.customer_validator = CustomerValidator()
        self._car_identity = self.customer_validator.check_car_identity_valid(car_identity)
        self._frequent_parking_number = self.customer_validator.check_frequent_parking_number_valid(frequent_parking_number)
        self._available_creadit = available_creadit
        self._arrival_time = None
        self._leave_day = leave_day
        self.dateHandler = DateHandler()

    @property
    def car_identity(self):
        return self._car_identity
    
    @car_identity.setter
    def car_identity(self, car_identity):
        self._car_identity = car_identity

    @property
    def frequent_parking_number(self):
        return self._frequent_parking_number

    @frequent_parking_number.setter
    def frequent_parking_number(self, frequent_parking_number):
        self._frequent_parking_number = frequent_parking_number

    @property
    def available_creadit(self):
        return self._available_creadit
    
    @available_creadit.setter
    def available_creadit(self, available_creadit):
        self._available_creadit = available_creadit
    
    @property
    def arrival_time(self):
        self._arrival_time = self.dateHandler.convert_date_to_string(datetime.datetime.now())
        return self._arrival_time
    
    @property
    def leave_day(self):
        return self._leave_day

    @leave_day.setter
    def leave_day(self, leave_day):
        self._leave_day = leave_day