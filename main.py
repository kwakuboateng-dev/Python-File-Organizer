import os
import shutil


class FileOrganizer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.files = os.listdir(file_path)

    def organize(self):
        for file in self.files:
            filename, extension = os.path.splitext(file)
            extension = extension[1:]
            if os.path.exists(f'{self.file_path}/{extension}'):
                shutil.move(f'{self.file_path}/{file}',
                            f'{self.file_path}/{extension}/{file}')
            else:
                os.makedirs(f'{self.file_path}/{extension}')
                shutil.move(f'{self.file_path}/{file}',
                            f'{self.file_path}/{extension}/{file}')
