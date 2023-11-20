import os

class Customer():

    def __init__(self, car_identity, available_creadit = 0.0):
        self._car_identity = car_identity
        self._available_creadit = available_creadit
        self.path = './customers/'
        self.path_credit = './credits/'
        self.full_path = f'{self.path + self.car_identity}.txt'
        self.full_path_credit = f'{self.path_credit + self.car_identity}_credit.txt'

    @property
    def car_identity(self):
        return self._car_identity

    @property
    def available_creadit(self):
        return self._available_creadit
    
    def check_files_exist(self, path, full_path):
        if not os.path.isdir(path):
            os.makedirs(path)        
        return os.path.exists(full_path)
        
    def get_customer_information(self):
        with open(self.full_path, 'r') as f:
            for line in f.readlines():
                line_split = line.split(':', 1)
                self.info[line_split[0]] = line_split[1]
        return self.info

    def get_available_credit(self):
        if not self.check_files_exist(self.path_credit, self.full_path_credit):
            return self.available_creadit
            
        with open(self.full_path_credit, 'r') as f:
            self._available_creadit = float(f.read().split(':')[1].strip())

        return self.available_creadit

    def set_available_credit(self, credit):
        self._available_creadit = round(self._available_creadit + credit, 2)
        return self.available_creadit
    
    def save_customer_credit(self):
        if not self.check_files_exist(self.path_credit, self.full_path_credit):
            create_file = open(self.full_path_credit, 'x')
            create_file.close()
        
        with open(self.full_path_credit, 'w') as f:
            f.write(f"Your available credit: {self.available_creadit}")

    def delete_customer_parking(self):
        if not self.check_files_exist(self.path, self.full_path):
            return
        os.remove(self.full_path)
    
    def __str__(self):
        return f'Your Car Identity is {self._car_identity}'