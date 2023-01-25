# 8th January, 2022
import tkinter as tk
import os
import shutil
from tkinter import filedialog


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


class App:
    def __init__(self, root):
        self.root = root
        self.button = tk.Button(
            root, text="Select Folder", command=self.select_folder)
        self.button.pack()
        self.listbox = tk.Listbox(root)
        self.listbox.pack()

    def select_folder(self):
        # Open a file dialog to select a folder
        folder = filedialog.askdirectory()
        # Clear the list box
        self.listbox.delete(0, tk.END)
        # Create a FileOrganizer object
        organizer = FileOrganizer(folder)
        # Organize the files in the selected folder
        organizer.organize()
        # Iterate through the subfolders in the selected folder
        for subfolder in os.listdir(folder):
            # Add the subfolder name to the list box
            self.listbox.insert(tk.END, subfolder)


root = tk.Tk()
root.title('File Organizer')
root.geometry('300x300')
app = App(root)
root.mainloop()
