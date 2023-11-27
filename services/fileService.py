import os

class FileService:
    
    def __init__(self, direct, path):
        self.direct = direct
        self.path = path

    def check_files_exist(self):
        return os.path.exists(self.path)

    def create_file(self):
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
