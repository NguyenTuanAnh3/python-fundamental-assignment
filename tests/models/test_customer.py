from models.customer import Customer
import datetime
import pytest

class TestCustomer:
    @classmethod
    def setup_class(self):
        self.cust = Customer("49A-10071", '12324', 1000)

    def test_car_identity_getter(self):
        assert self.cust.car_identity == "49A-10071"

    def test_frequent_parking_number_getter(self):
        assert self.cust.frequent_parking_number == '12324'
    
    def test_available_credit_getter(self):
        assert self.cust.available_creadit == 1000

    def test_car_identity_setter(self):
        self.cust.car_identity = "43A-10000"
        assert self.cust.car_identity == "43A-10000"

    def test_frequent_parking_number_setter(self):
        self.cust.frequent_parking_number = '12355'
        assert self.cust.frequent_parking_number == '12355'

    def test_available_credit_setter(self):
        self.cust.available_creadit = 1
        assert self.cust.available_creadit == 1

    def test_constructor_wrong_1(self):
        with pytest.raises(Exception) as ex:
            self.cust = Customer("491-10071", '12324', 1000)

    def test_constructor_wrong_2(self):
        with pytest.raises(Exception) as ex:
            self.cust = Customer("49A-10071", '1232324', 1000)

    
    def test_leave_day_getter(self):
        assert self.cust.leave_day == None

    def test_leave_day_setter(self):
        self.cust.leave_day = datetime.datetime.strptime("2023-11-30", "%Y-%m-%d").replace(hour=0, second=0, minute=0)
        assert str(self.cust.leave_day) == '2023-11-30 00:00:00'

    def test_arrival_time_getter(self):
        today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        assert self.cust.arrival_time == today

