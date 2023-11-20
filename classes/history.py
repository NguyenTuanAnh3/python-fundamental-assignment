import os
from classes.customer import Customer
import datetime

class History(Customer):
    
    def __init__(self, car_identity, available_creadit = 0.0, total_payment = 0.0):
        super().__init__(car_identity, available_creadit)
        self.total_payment = total_payment
        self.path = './history/'
        self.full_path = f'{self.path + self.car_identity}.txt'

    def set_total_payment(self, addtional_total):
        if not self.check_files_exist(self.path, self.full_path):
            self.total_payment = self.total_payment + addtional_total
            return self.total_payment
        else:
            with open(self.full_path, 'r') as f:
                self.total_payment = float(f.readlines()[0].split(":")[1].strip()) + addtional_total
            return self.total_payment 
     
    def save_history_customer(self, start_day, leave_day, total_date):
        if not self.check_files_exist(self.path, self.full_path):
            with open(self.full_path, 'w+') as f:
                f.write(f'Total payment: {self.total_payment} \n')
                f.write(f'Available credits: {self.available_creadit} \n')
                f.write(f'Parked Dates:\n')
                f.write(f'{start_day + " - " + leave_day} ${total_date}')
        else:
            with open(self.full_path, 'r') as f:
                data = f.readlines()
            data[0] = f'Total payment: {self.total_payment} \n'
            data[1] = f'Available credits: {self.available_creadit} \n'

            with open(self.full_path, 'w', encoding='utf-8') as file: 
                file.writelines(data) 
                file.write(f'\n{start_day + " - " + leave_day} ${total_date}')
        
    def get_history_customer(self):
        if not self.check_files_exist(self.path, self.full_path):
            print("Your car identity history not found")
            exit()
        with open(self.full_path, 'r') as f:
            for rf in f.readlines():
                print(rf)

    