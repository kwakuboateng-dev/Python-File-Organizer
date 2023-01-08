import os
import shutil


class FileOrganizer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.files = os.listdir(file_path)
