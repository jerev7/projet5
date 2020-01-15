# !/usr/bin/env python3
#coding:utf-8

from PySide2.QtWidgets import (QApplication, QPushButton, QDialog, QLineEdit, QVBoxLayout, QMessageBox)
from PySide2 import QtWidgets, QtCore, QtGui
import mysql.connector
from PySide2.QtSql import QSqlDatabase, QSqlQuery
# from sqlalchemy import create_engine
# engine = create_engine("mysql://jerev7:Sally_95540@localhost/openfoodfacts",
#                             encoding='latin1', echo=True)

# db = QSqlDatabase.addDatabase("QMSQL")
# db.setHostName("127.0.0.1")
# db.setDatabaseName("openfoodfacts")
# db.setUserName("jerev7")
# db.setPassword("Sally_95540")
# db.open()
#     query = QSqlQuery(db)
#     query.exec_("SELECT * FROM Category")
#     while query.next():
#         print(query.value)
# else:
#     print("probleme database")

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
        self.text = QtWidgets.QLabel("Sélectionnez une catégorie ci-dessous")
        # self.text.SetLineEdit("Choose a category below")
        self.mycombo = QtWidgets.QComboBox()
        self.button = QPushButton("recherche")
        # Create layout and add widgets
        
        
        """le probleme est avec le code qui suit"""
        # self.db = QSqlDatabase.addDatabase("QSQLITE")
        # self.db.setHostName("localhost")
        # self.db.setDatabaseName("openfoodfacts")
        # self.db.setUserName("jerev7")
        # self.db.setPassword("Sally_95540")
        # # self.db.open()
        # self.addstuff()
        # query = QSqlQuery(db)
        # query.exec_("SELECT id FROM Category")
        
        # while query.next():
        #     self.mycombo.addItems(query.value(0))


        mydb = mysql.connector.connect(
        host="localhost",
        user="jerev7",
        passwd="Sally_95540",
        database="openfoodfacts"
        )

        mycursor = mydb.cursor()
        sql_query = "SELECT * FROM Category"
        mycursor.execute(sql_query)
        result = mycursor.fetchall()
        for x in result:
            category_id = x[0]
            category_name = x[1]
            self.mycombo.addItem("{} - {}".format(category_id, (category_name)))

        layout = QVBoxLayout()
        
        layout.addWidget(self.text)
        layout.addWidget(self.mycombo)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        #self.button.clicked.connect(self.greetings)


    # def addstuff(self):
    #     print("aaaaaa")
    #     if self.db.open():
    #         print("ébbbbbb")
    #         query = QSqlQuery("SELECT * FROM Category")
    #         # query.exec_("SELECT * FROM Category")
        
    #         while query.next():
    #             categ = query.value(0)
    #             self.mycombo.addItem(categ)
    #             print("item added")
    #     else:
    #         print("database probleme encore!")
       


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
