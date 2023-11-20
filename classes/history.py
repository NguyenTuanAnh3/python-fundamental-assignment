import os
from classes.customer import Customer
import datetime

class History(Customer):
    
    def __init__(self, car_identity, available_creadit = 0.0, total_payement = 0.0):
        super().__init__(car_identity, available_creadit)
        self.total_payement = total_payement
        self.path = './history/'
        self.full_path = f'{self.path + self.car_identity}.txt'

    def set_total_payment(self, addtional_total):
        if not self.check_files_exist(self.path, self.full_path):
            return self.total_payement
        with open(self.full_path, 'r') as f:
            self.total_payement = float(f.readlines()[0].split(":")[1].strip())
        return self.total_payement + addtional_total
     
    def save_history_customer(self, start_day, leave_day, total_date):
        if not self.check_files_exist(self.path, self.full_path):
            with open(self.full_path, 'w+') as f:
                f.write(f'Total payment: {self.total_payement} \n')
                f.write(f'Available credits: {self.available_creadit} \n')
                f.write(f'Parked Dates:\n')
                f.write(f'{start_day + " - " + leave_day} ${total_date}')
        else:
            with open(self.full_path, 'r') as f:
                data = f.readlines()
            data[0] = f'Total payment: {self.total_payement} \n'
            data[1] = f'Available credits: {self.available_creadit} \n'

            with open('example.txt', 'w', encoding='utf-8') as file: 
                file.writelines(data) 
                f.write(f'{start_day + " - " + leave_day} ${total_date}')
        
    def get_history_customer(self):
        if not self.check_files_exist(self.path, self.full_path):
            print("Your car identity history not found")
            exit()
        with open(self.full_path, 'r') as f:
            for rf in f.readlines():
                print(rf + '\n')

    