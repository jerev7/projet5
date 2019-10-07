#! /usr/bin/env python3
#coding:utf-8

from PySide2.QtWidgets import (QApplication, QPushButton, QDialog, QLineEdit, QVBoxLayout, QMessageBox)



class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        
        # Create widgets
        self.edit = QLineEdit()
        self.edit.setPlaceholderText("Write your name here...")
        self.button = QPushButton("Show Greetings")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)

    # Greets the user
    def greetings(self):
        #print(f"hey {self.edit.text()}")
        self.resultat = Resultat(self)
        self.resultat.show()
        #QMessageBox.information(self, "salut", "ça va", QMessageBox.Close)

class Resultat(QDialog):

    def __init__(self, parent=None):
        super(Resultat, self).__init__(parent)
        
        # Create widgets
        self.edit = QLineEdit()
        self.edit.setPlaceholderText("deuxieme fenetre...")
        self.button = QPushButton("recherche")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        #self.button.clicked.connect(self.greetings)

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication()
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    app.exec_()
