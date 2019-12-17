! /usr/bin/env python3
#coding:utf-8

from PySide2.QtWidgets import (QApplication, QPushButton, QDialog, QLineEdit, QVBoxLayout, QMessageBox)



class Menu(QDialog):

    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)
        
        # Create widgets
        self.button1 = QPushButton("Quel aliment souhaitez-vous remplacer ?")
        self.button2 = QPushButton("Retrouver mes aliments substitués")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button1.clicked.connect(self.greetings)
        self.button2.clicked.connect(self.greetings)

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
    menu = Menu()
    menu.show()
    # Run the main Qt loop
    app.exec_()
