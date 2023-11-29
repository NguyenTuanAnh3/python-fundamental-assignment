from models.bill import Bill
import pytest

class TestBill:
    
    @classmethod
    def setup_class(self):
        self.bill = Bill()
    

    def test_bill_getter(self):
        assert len(self.bill.bill) == 0

    def test_bill_setter(self):
        self.bill.bill = {
            'test': 1
        }
        assert self.bill.bill['test'] == 1

    def test_bills_getter(self):
        assert len(self.bill.bills) == 0

    def test_bills_setter(self):
        self.bill.bills.append({
            'test': 1
        })
        assert self.bill.bills[0]['test'] == 1


    def test_constructor_except(self):
        with pytest.raises(TypeError) as e:
            self.bill = Bill({'test': 1})

    def test_bill_setter_wrong(self):
        self.bill = Bill()
        self.bill.bill = {'test': 1}
        assert self.bill.bill['test'] != 0

    def test_bills_setter_wrong(self):
        self.bill = Bill()
        self.bill.bills.append({'test': 1})
        assert self.bill.bills[0]['test'] != 0