import datetime
from models.customer import Customer
from handlers.fileHandler import FileHandler
from config.constants import CUSTOMER_DIR, ARRIVAL_TIME_TEXT

class CustomerService(Customer):
    
    def __init__(self, car_identity, frequent_parking_number = None, available_creadit = 0.0, leave_day = None):
        super().__init__(car_identity, frequent_parking_number, available_creadit, leave_day)
        self.file_handler = FileHandler(CUSTOMER_DIR, self.car_identity)
        self.stored_info = {}

    def check_car_identity_exists(self):
        if self.file_handler.check_files_exist():
            raise Exception('Your car identity already exists')

    def save_customer_information(self):
        try:
            self.check_car_identity_exists()
            save = self.file_handler.handle_file(car_identity = self.car_identity, arrival_time = self.arrival_time, frequent_parking_number = self.frequent_parking_number)
        except Exception as e:
            print(e)
    
    def get_stored_customer_information(self):
        datas = self.file_handler.read_file()
        for data in datas:
            separate = data.split(':',1)
            self.stored_info[separate[0]] = separate[1].rstrip()
        return self.stored_info


    def get_arrival_time(self):
        try:
            get_arrival_time = self.get_stored_customer_information()[ARRIVAL_TIME_TEXT].strip()
            arrival_time = datetime.datetime.strptime(get_arrival_time, "%Y-%m-%d %H:%M")
            if(0 <= arrival_time.hour < 8):
                raise Exception("OOPs, arrival time went wrong")
        except Exception as e:
            print(e)
            exit()
        else:
            return arrival_time
    
    def check_customer_pickup(self):
        if not self.file_handler.check_files_exist():
            raise Exception('Your car identity not found')

    