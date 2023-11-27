import datetime

class Customer:

    def __init__(self, car_identity, available_creadit = 0.0, leave_day = None):
        self._car_identity = car_identity
        self._available_creadit = available_creadit
        self._arrival_time = None
        self._leave_day = leave_day

    @property
    def car_identity(self):
        return self._car_identity
    
    @car_identity.setter
    def car_identity(self, car_identity):
        self._car_identity = car_identity

    @property
    def available_creadit(self):
        return _available_creadit
    
    @available_creadit.setter
    def available_creadit(self, available_creadit):
        self._available_creadit = available_creadit
    
    @property
    def arrival_time(self):
        self._arrival_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        return self._arrival_time
    
    @property
    def leave_day(self):
        return self._leave_day

    @leave_day.setter
    def leave_day(self, leave_day):
        self._leave_day = leave_day