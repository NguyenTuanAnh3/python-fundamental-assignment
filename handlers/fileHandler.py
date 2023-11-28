import os
from config.constants import store_dir

class FileHandler:
    
    def __init__(self, direct, car_identity):
        self.direct = direct
        self.path = f'{direct}{car_identity}.txt'

    def check_files_exist(self):
        return os.path.exists(self.path)

    def create_file(self):
        if not os.path.isdir(store_dir):
            os.mkdir(store_dir)

        if not os.path.isdir(self.direct):
            os.mkdir(self.direct)
            
        f = open(self.path, 'x')
        f.close()

    def write_file(self, **kwargs):
        with open(self.path, 'w', encoding='utf-8') as f:
            for key, value in kwargs.items():
                f.write(f'{key.replace("_", " ").title()}: {value}\n')

    def handle_file(self, **kwargs):
        if not self.check_files_exist():
            self.create_file()
        self.write_file(**kwargs)
