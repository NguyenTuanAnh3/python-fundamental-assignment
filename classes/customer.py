import os

class Customer():

    def __init__(self, car_identity):
        self._car_identity = car_identity
        self.path = './customers/'

    @property
    def car_identity(self):
        return self._car_identity

    def is_customer_information_exist(self):
        if not os.path.isdir(self.path):
            os.makedirs(self.path)        
        return os.path.exists(f'{self.path + self.car_identity}.txt')
        
    def get_customer_information(self):
        with open(f'{self.path + self.car_identity}.txt', 'r') as f:
            for line in f.readlines():
                line_split = line.split(':', 1)
                self.info[line_split[0]] = line_split[1]
        return self.info
        
    def __str__(self):
        return f'Your Car Identity is {self._car_identity}'