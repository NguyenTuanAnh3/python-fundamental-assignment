import os
import json
from config.constants import STORE_DIR

class FileHandler:
    
    def __init__(self, direct='', car_identity=''):
        self.direct = direct
        self.path = f'{direct}{car_identity}.txt'

    def check_files_exist(self):
        return os.path.exists(self.path)

    def create_file(self):
        if not os.path.isdir(STORE_DIR):
            os.mkdir(STORE_DIR)

        if not os.path.isdir(self.direct):
            os.mkdir(self.direct)
            
        f = open(self.path, 'x')
        f.close()

    def read_file(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            data = f.readlines()
        return data

    def write_file(self, **kwargs):
        with open(self.path, 'w', encoding='utf-8') as f:
            for key, value in kwargs.items():
                f.write(f'{key.replace("_", " ").title()}: {value}\n')

    def handle_file(self, **kwargs):
        if not self.check_files_exist():
            self.create_file()
        self.write_file(**kwargs)

    def get_information_json(self):
        with open('parkingAreaPrice.json') as f:
            data = json.load(f)
        return data

    def remove_file(self):
        os.remove(self.path)
