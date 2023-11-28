import datetime
from validator.customer import CustomerValidator
from services.billService import BillService
from services.customerService import CustomerService
from services.historyService import HistoryService
from handlers.excelHandler import ExcelHandler
class PickUpService:

    def __init__(self):
        self.customer_validator = CustomerValidator()
        self.car_identity = self.customer_validator.check_car_identity_valid(input("Please enter your car identity: "))
        self.customer_service = CustomerService(self.car_identity)
        self.customer_service.check_customer_pickup()
        self.leave_day = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.billService = BillService(self.car_identity, self.leave_day)
        self.bills = []
        self.total = 0
        self.history_service = HistoryService(self.car_identity)
    
    def payment_pickup(self, start_day):
        while(self.customer_service.available_creadit < self.total):
            print("Your a payment amount not enough")
            enter_credit = float(input("Please enter a payment amount:"))
            self.customer_service.set_available_credit(enter_credit)
            self.customer_service.save_customer_credit()
        self.customer_service.payment(self.total)
        self.history_service.set_total_payment(self.total)
        self.history_service.save_customer_history(start_day=start_day, leave_day=self.leave_day, available_creadit= self.customer_service.available_creadit, total=self.total)
        self.customer_service.remove_customer()

    def handle_pickup(self):
        [self.bills, self.total] = self.billService.get_bills_and_total_fee_parking()
        excel_handler = ExcelHandler(self.car_identity, self.leave_day, self.bills)
        excel_handler.create_excel()
        start_day = self.customer_service.get_arrival_time()
        self.customer_service.get_customer_available_credit()
        print(f'Total payment: {self.total}')
        print(f'Available Credits: {self.customer_service.available_creadit}')
        self.payment_pickup(start_day=start_day)
