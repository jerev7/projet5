from PySide2.QtWidgets import (QApplication, QPushButton, QDialog, QLineEdit, QVBoxLayout, QMessageBox)
from PySide2 import QtWidgets, QtCore, QtGui
import mysql.connector
from class_result import *
from class_saved_products import *



class Menu(QDialog):

    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)

        self.mydb = mysql.connector.connect(
        host="localhost",
        user="jerev7",
        passwd="Sally_95540",
        database="openfoodfacts"
        )
        self.createMenu()
        
        # Create widgets
        self.button1 = QPushButton("Quel aliment souhaitez-vous remplacer ?")
        self.button2 = QPushButton("Retrouver mes aliments substitués")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.menuBar)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button1.clicked.connect(self.open_resultat)
        self.button2.clicked.connect(self.open_saved_products)

    # Greets the user
    def open_resultat(self):
        #print(f"hey {self.edit.text()}")
        self.resultat = Resultat(self.mydb, self)
        self.resultat.show()
        #QMessageBox.information(self, "salut", "ça va", QMessageBox.Close)

    def open_saved_products(self):
        self.resultat = Saved_products(self.mydb, self)
        self.resultat.show()

    def createMenu(self):
        self.menuBar = QtWidgets.QMenuBar()

        self.fileMenu = QtWidgets.QMenu("&File", self)
        self.exitAction = self.fileMenu.addAction("E&xit")
        self.menuBar.addMenu(self.fileMenu)

        self.exitAction.triggered.connect(self.accept)