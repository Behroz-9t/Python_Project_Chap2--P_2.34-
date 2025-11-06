import tkinter as tk
from tkinter import filedialog

class DocumentReader:

    def __init__(self):
        root = tk.Tk() # creating a root window
        root.withdraw() # Hides the small, blank main tkinter root window
        print("Opening a file selecting window.Carefully select a text file.")

        self._file_path=filedialog.askopenfilename() # Open the file selection dialog.This will return the full path to the selected file
        

    def reader(self):
                           
        self._content=[]
        if self._file_path:  # Check if the user selected a file 
            print(f"\nYou have selected the file path: {self._file_path}\n")

            try:

                with open(self._file_path) as document_file: # with ensures that the file is opened and automatically closes the file so we dont have to write file.close()

                    self._content=list(document_file.read()) #reads the doc text file and stores it in content of type list

            except Exception as e:
                    print(f"An error occurred while reading the file: {e}")

        else:
             print("No document is selected.Program ended succesfully!")
                

