# !/usr/bin/env python3
#coding:utf-8

from PySide2.QtWidgets import (QApplication, QPushButton, QDialog, QLineEdit, QVBoxLayout, QMessageBox)
from PySide2 import QtWidgets, QtCore, QtGui
import mysql.connector
from PySide2.QtSql import QSqlDatabase, QSqlQuery


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
        self.text_cat = QtWidgets.QLabel("Sélectionnez une catégorie ci-dessous")
        # self.text.SetLineEdit("Choose a category below")
        self.mycombo_cat = QtWidgets.QComboBox()
        self.text_prod = QtWidgets.QLabel("Sélectionnez ensuite un produit ci-dessous")
        self.mycombo_prod = QtWidgets.QComboBox()
        

        self.mydb = mysql.connector.connect(
        host="localhost",
        user="jerev7",
        passwd="Sally_95540",
        database="openfoodfacts"
        )

        self.mycursor = self.mydb.cursor()
        sql_query = "SELECT * FROM Category"
        self.mycursor.execute(sql_query)
        result = self.mycursor.fetchall()
        for x in result:
            category_id = x[0]
            category_name = x[1]
            self.mycombo_cat.addItem("{} - {}".format(category_id, (category_name)))


        layout = QVBoxLayout()
        
        layout.addWidget(self.text_cat)
        layout.addWidget(self.mycombo_cat)
        layout.addWidget(self.text_prod)
        layout.addWidget(self.mycombo_prod)

        category_selected = (self.mycombo_cat.currentIndex()) + 311
        print(category_selected)        
        sql_query_test = "SELECT product_id FROM Product_category WHERE category_id = (%s)"

        self.mycursor.execute(sql_query_test, (category_selected,))
        result2 = self.mycursor.fetchall()
        
        sql_query_test2 = "SELECT product_name FROM Product WHERE id = %s"
        for x in result2:
            self.mycursor.execute(sql_query_test2, (x))
            result3 = self.mycursor.fetchall()
            for x in result3:
                self.mycombo_prod.addItem(x[0])

        # Set dialog layout
        self.setLayout(layout)
        self.mycombo_cat.currentIndexChanged.connect(self.update_combo)


    def update_combo(self):
        self.mycombo_prod.clear()
        category_selected = (self.mycombo_cat.currentIndex()) + 311
        # print(category_selected)        
        sql_query_test = "SELECT product_id FROM Product_category WHERE category_id = (%s)"

        self.mycursor.execute(sql_query_test, (category_selected,))
        result2 = self.mycursor.fetchall()
        
        sql_query_test2 = "SELECT product_name FROM Product WHERE id = %s"
        for x in result2:
            self.mycursor.execute(sql_query_test2, (x))
            result3 = self.mycursor.fetchall()
            for x in result3:
                self.mycombo_prod.addItem(x[0])    
        # Add button signal to greetings slot
        #self.button.clicked.connect(self.greetings)
    # def update_combo(self):


if __name__ == '__main__':


    import sys
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    menu = Menu()
    # db = QSqlDatabase.addDatabase("QSQLITE")
    # db.setHostName("localhost")
    # db.setDatabaseName("openfoodfacts")
    # db.setUserName("jerev7")
    # db.setPassword("Sally_95540")
    # if db.open():
    #     query = QSqlQuery(db)
    #     while query.next():
    #         print(query.value(0))

    # Run the main Qt loop
    sys.exit(menu.exec_())
