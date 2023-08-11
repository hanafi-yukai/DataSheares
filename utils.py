from os import system, name
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys
import csv

datasheares_icon = "images/appicon.png"

"""
this function takes in a file name and returns a datalist containing the file contents

:param file_name:   name of the file
:return:            list of rows, each row is a list
"""

def load_csv_data(file_name:str) -> list:
    # Function to load CSV data from the given file name and return it as a li5st of lists.
    openfile = open(file_name)  # Open the file with the given file name.
    csvreader = csv.reader(openfile)  # Create a CSV reader object to read the file.
    datalist = [row for row in csvreader]  # Initialize an empty list to store the data.
    return datalist  # Return the final list of lists containing the CSV data.

# clear() clears the terminal/output
def clear():
    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def get_csv_file(window_title):
    app = QApplication(sys.argv)
    file_dialog = QFileDialog()
    file_dialog.setWindowTitle(window_title)
    file_dialog.setNameFilter("CSV Files (*.csv)")
    file_dialog.setWindowFlags(file_dialog.windowFlags() | Qt.WindowStaysOnTopHint)
    file_dialog.show()
    app.exec_()
    file_path = file_dialog.selectedFiles()[0] if file_dialog.result() else None
    return file_path

def show_message(type, title, message):
    app = QApplication([])
    msg_box = QMessageBox()
    match(type):
        case(1):
            msg_box.setIcon(QIcon(datasheares_icon))
        case(2):
            msg_box.setIcon(QMessageBox.Critical)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec_()

def confirm_exit():
    app = QApplication(sys.argv)
    msg_box = QMessageBox()
    msg_box.setWindowIcon(QIcon(datasheares_icon))
    msg_box.setWindowTitle("Confirm")
    msg_box.setText("Are you sure you want to close DataSheares? :((((")
    msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    choice = msg_box.exec_()
    if choice == QMessageBox.Yes:
        sys.exit()  # Exit the application
    else:
        app.quit()  # Close the message box and continue the application
