from models.customer import Customer
from services.fileService import FileService
from config.constants import customer_dir

class CustomerService(Customer):
    
    def __init__(self, car_identity, frequent_parking_number, available_creadit = 0.0, leave_day = 0.0):
        super().__init__(car_identity, frequent_parking_number, available_creadit, leave_day)
        self.path = f'{customer_dir}{self.car_identity}.txt'
        self.file_service = FileService(customer_dir, self.path)

    def check_car_identity_exists(self):
        if self.file_service.check_files_exist():
            raise Exception('Your car identity already exists')

    def save_customer_information(self):
        try:
            self.check_car_identity_exists()
            save = self.file_service.handle_file(car_identity = self.car_identity, arrival_time = self.arrival_time, frequent_parking_number = self.frequent_parking_number)
        except Exception as e:
            print(e)
    