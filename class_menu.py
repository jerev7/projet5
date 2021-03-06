from PySide2.QtWidgets import (QApplication, QPushButton, QDialog, QLineEdit,
                               QVBoxLayout, QMessageBox)
from PySide2 import QtWidgets, QtCore, QtGui
import mysql.connector
from class_result import *
from class_saved_products import *


class Menu(QDialog):
    """
    This class is used to create the main program window.
    """
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)
        self.setWindowTitle("Project 5 : Openfoodfacts")
        self.mydb = mysql.connector.connect(
                                            host="localhost",
                                            user="jerev7",
                                            passwd="Sally_95540",
                                            database="openfoodfacts"
        )
        self.createMenu()
        # Create widgets
        self.button1 = QPushButton("Which product would you like to replace ?")
        self.button2 = QPushButton("Saved products")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.menuBar)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal
        self.button1.clicked.connect(self.open_resultat)
        self.button2.clicked.connect(self.open_saved_products)

    def open_resultat(self):
        """ Function to open a new search window """
        self.resultat = Resultat(self.mydb, self)
        self.resultat.show()

    def open_saved_products(self):
        """" Function to open the window 'Saved_products'. """
        self.resultat = Saved_products(self.mydb, self)
        self.resultat.show()

    def createMenu(self):
        """ Adds a 'File' menu. """
        self.menuBar = QtWidgets.QMenuBar()

        self.fileMenu = QtWidgets.QMenu("&File", self)
        self.exitAction = self.fileMenu.addAction("&Quit")
        self.menuBar.addMenu(self.fileMenu)

        self.exitAction.triggered.connect(self.accept)
