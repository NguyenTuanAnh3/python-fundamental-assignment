from models.customer import Customer
from services.customerService import CustomerService
from validator.customer import CustomerValidator
from config.constants import CUSTOMER_DIR 
class ParkService:

    def __init__(self):
        self.customer_validator = CustomerValidator()
        self.car_identity = self.customer_validator.check_car_identity_valid(input('Enter your car identity: ').strip())
        self.frequent_parking_number = self.customer_validator.check_frequent_parking_number_valid(input('Enter your frequent parking number (if so): ').strip())
        self.customer_service = CustomerService(car_identity=self.car_identity, frequent_parking_number=self.frequent_parking_number)
        
    def handle_park(self):
        self.customer_service.save_customer_information()
        