from models.history import History
import pytest

class TestHistory:
    @classmethod
    def setup_class(self):
        self.his = History('40A-11111')

    def test_car_identity_getter(self):
        assert self.his.car_identity == '40A-11111'

    def test_car_identity_setter(self):
        self.his.car_identity = '40A-11112'
        assert self.his.car_identity == '40A-11112'

    def test_total_payment_getter(self):
        assert self.his.total_payment == 0.0

    def test_total_payment_setter(self):
        self.his.total_payment = 12
        assert self.his.total_payment == 12