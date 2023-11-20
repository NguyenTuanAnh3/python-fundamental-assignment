import os
from classes.customer import Customer

class Park(Customer):
    
    def __init__(self, car_identity, arrival_time, frequent_parking_number):
        super().__init__(car_identity)
        self._arrival_time = arrival_time
        self._frequent_parking_number = frequent_parking_number
        self.path = './customers/'

    @property
    def arrival_time(self):
        return self._arrival_time

    @property
    def frequent_parking_number(self):
        return self._frequent_parking_number

    def save_customer_information(self):
        path_file = f'{self.path + self.car_identity}.txt'
        try:
            if not self.check_files_exist(self.path, self.full_path):
                create_file = open( path_file, 'x')
                try:
                    with open(path_file, 'w') as f:
                        f.write(f'Car Identity: {self.car_identity}\n')
                        f.write(f'Arrival Time: {self.arrival_time}\n')
                        f.write(f'Frequent Parking Number: {self.frequent_parking_number}\n')
                except FileNotFoundError as e:
                    return e
            else:
                raise Exception("Your car identity already exists")
        except Exception as e:
            print(e)            



        