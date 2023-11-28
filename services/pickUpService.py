import datetime
from validator.customer import CustomerValidator
from services.billService import BillService
from services.customerService import CustomerService
from handlers.excelHandler import ExcelHandler
class PickUpService:

    def __init__(self):
        self.customer_validator = CustomerValidator()
        self.car_identity = self.customer_validator.check_car_identity_valid(input("Please enter your car identity: "))
        self.customer_service = CustomerService(self.car_identity)
        self.customer_service.check_customer_pickup()
        self.leave_day = datetime.datetime.now().replace(day=12, hour=19, minute=30).strftime("%Y-%m-%d %H:%M")
        self.billService = BillService(self.car_identity, self.leave_day)
        self.bills = []
        self.total = 0
    
    def handle_pickup(self):
        [self.bills, self.total] = self.billService.get_bills_and_total_fee_parking()
        excel_handler = ExcelHandler(self.car_identity, self.leave_day, self.bills)
        excel_handler.create_excel()

