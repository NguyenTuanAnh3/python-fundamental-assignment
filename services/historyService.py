import os
from models.history import History
from handlers.fileHandler import FileHandler
from config.constants import HISTORY_DIR

class HistoryService(History):
    
    def __init__(self, car_identity, total_payment = 0.0):
        super().__init__(car_identity, total_payment)
        self.file_handler = FileHandler(HISTORY_DIR, car_identity= self.car_identity)

    def set_total_payment(self, addtional_total):
        if not self.file_handler.check_files_exist():
            self._total_payment = self.total_payment + addtional_total
            return round(self.total_payment)
        data = self.file_handler.read_file()
        self._total_payment = float(data[0].split(":")[1].strip()) + addtional_total
        return round(self.total_payment, 2) 

    def save_customer_history(self, start_day, leave_day, available_creadit, total):
        start_day = start_day.strftime("%Y-%m-%d %H-%M")
        if not self.file_handler.check_files_exist():
            if not os.path.isdir(HISTORY_DIR):
                os.makedirs(HISTORY_DIR)

            with open(f'{HISTORY_DIR}{self.car_identity}.txt', 'w+') as f:
                f.write(f'Total payment: {self.total_payment} \n')
                f.write(f'Available credits: {available_creadit} \n')
                f.write(f'Parked Dates:\n')
                f.write(f'{start_day + " - " + leave_day} ${total}')
        else:
            with open(f'{HISTORY_DIR}{self.car_identity}.txt', 'r') as f:
                data = f.readlines()
            data[0] = f'Total payment: {self.total_payment} \n'
            data[1] = f'Available credits: {available_creadit} \n'

            with open(f'{HISTORY_DIR}{self.car_identity}.txt', 'w', encoding='utf-8') as file: 
                file.writelines(data) 
                file.write(f'\n{start_day + " - " + leave_day} ${total}')
        
    def get_history_customer(self):
        data = self.file_handler.read_file()
        for da in data:
            print(da)