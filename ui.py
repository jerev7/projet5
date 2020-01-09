# !/usr/bin/env python3
#coding:utf-8

from PySide2.QtWidgets import (QApplication, QPushButton, QDialog, QLineEdit, QVBoxLayout, QMessageBox)
from PySide2 import QtWidgets, QtCore, QtGui
import mysql.connector


class Menu(QDialog):

    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)


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
        self.button1.clicked.connect(self.greetings)
        self.button2.clicked.connect(self.greetings)

    # Greets the user
    def greetings(self):
        #print(f"hey {self.edit.text()}")
        self.resultat = Resultat(self)
        self.resultat.show()
        #QMessageBox.information(self, "salut", "ça va", QMessageBox.Close)

    def createMenu(self):
        self.menuBar = QtWidgets.QMenuBar()

        self.fileMenu = QtWidgets.QMenu("&File", self)
        self.exitAction = self.fileMenu.addAction("E&xit")
        self.menuBar.addMenu(self.fileMenu)

        self.exitAction.triggered.connect(self.accept)

class Resultat(QDialog):

    def __init__(self, parent=None):
        super(Resultat, self).__init__(parent)

        
        # Create widgets
        self.text = QtWidgets.QLabel("Choose a category below")
        # self.text.SetLineEdit("Choose a category below")
        self.mycombo = QtWidgets.QComboBox()
        self.button = QPushButton("recherche")
        # Create layout and add widgets
        
        """le probleme est avec le code qui suit"""
        mydb = mysql.connector.connect(
            host="localhost",
            user="jerev7",
            passwd="Sally_95540",
            database="openfoodfacts"
        )

        mycursor = mydb.cursor()
        sql_id = "SELECT id FROM Category"
        sql_name = "SELECT name FROM Category"
        mycursor.execute(sql_id)
        result = mycursor.fetchall()
        for x in result:
            self.mycombo.addItem(x)


        layout = QVBoxLayout()
        
        layout.addWidget(self.text)
        layout.addWidget(self.mycombo)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        #self.button.clicked.connect(self.greetings)
       


if __name__ == '__main__':

    import sys
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    menu = Menu()
    
    # Run the main Qt loop
    sys.exit(menu.exec_())
