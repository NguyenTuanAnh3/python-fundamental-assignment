from validator.customer import CustomerValidator
import pytest

class TestCustomerValidator:

    @classmethod
    def setup_class(self):
        self.customer_valid = CustomerValidator()

    def test_check_car_identity_valid_right(self):
        car_identity = '49A-11111'
        assert self.customer_valid.check_car_identity_valid(car_identity=car_identity) == '49A-11111'
    
    def test_check_car_identity_valid_except(self):
        car_identity = '491-1111'
        with pytest.raises(Exception) as e:
            self.customer_valid.check_car_identity_valid(car_identity=car_identity) 

    def test_check_frequent_parking_number_valid_right(self):
        frequent_parking_number = 11111
        assert self.customer_valid.check_frequent_parking_number_valid(frequent_parking_number=frequent_parking_number) == 11111

    def test_check_frequent_parking_number_valid_right(self):
        frequent_parking_number = 111111 
        with pytest.raises(Exception) as e:
            assert self.customer_valid.check_frequent_parking_number_valid(frequent_parking_number=frequent_parking_number) == 11111
    
    def test_check_frequent_parking_number_is_None(self):
        frequent_parking_number = None
        assert self.customer_valid.check_frequent_parking_number_valid(frequent_parking_number=frequent_parking_number) == None
