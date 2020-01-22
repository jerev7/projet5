# !/usr/bin/env python3
#coding:utf-8

from PySide2.QtWidgets import (QApplication, QPushButton, QDialog, QLineEdit, QVBoxLayout, QMessageBox)
from PySide2 import QtWidgets, QtCore, QtGui
import mysql.connector
# from PySide2.QtSql import QSqlDatabase, QSqlQuery


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
        self.button1.clicked.connect(self.open_resultat)
        self.button2.clicked.connect(self.open_resultat)

    # Greets the user
    def open_resultat(self):
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
        
        self.mytable = QtWidgets.QTableWidget(1, 3)
        self.mytable.setHorizontalHeaderLabels(("Produit sélectionné;Nutriscore;Lien vers le site web").split(";"))
        header = self.mytable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        
        # header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

        self.subs_table = QtWidgets.QTableWidget(1, 3)
        self.subs_table.setHorizontalHeaderLabels(("Produit de substitution;Nutriscore;Lien vers le site web").split(";"))
        header2 = self.mytable.horizontalHeader()
        header2.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header2.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header2.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        
        header2.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header2.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header2.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)


        self.search_button = QPushButton("Rechercher produit de substitution")

        self.mydb = mysql.connector.connect(
        host="localhost",
        user="jerev7",
        passwd="Sally_95540",
        database="openfoodfacts"
        )

        self.mycursor = self.mydb.cursor()
        sql_query_cat = "SELECT * FROM Category"
        self.mycursor.execute(sql_query_cat)
        result = self.mycursor.fetchall()
        for x in result:
            category_id = x[0]
            category_name = x[1]
            self.mycombo_cat.addItem("{} - {}".format(category_id, (category_name)))
        self.first_cat = result[0][0]
        # print(self.first_cat)
        self.layout = QVBoxLayout()
        
        self.layout.addWidget(self.text_cat)
        self.layout.addWidget(self.mycombo_cat)
        self.layout.addWidget(self.text_prod)
        self.layout.addWidget(self.mycombo_prod)
        category_selected = (self.mycombo_cat.currentIndex()) + self.first_cat
        # print(category_selected)        
        sql_query_combo2 = "SELECT product_name FROM Product inner join Product_category WHERE Product.id = Product_category.product_id and Product_category.category_id = %s"

        self.mycursor.execute(sql_query_combo2, (category_selected,))
        result = self.mycursor.fetchall()
        for x in result:
            self.mycombo_prod.addItem(x[0])


        product_selected_name = self.mycombo_prod.currentText()
        
        sql_query = "SELECT id FROM Product WHERE product_name = %s"
        self.mycursor.execute(sql_query, (product_selected_name,))
        result = self.mycursor.fetchall()
        for x in result:
            self.product_selected_id = x[0]

        sql_query2 = "SELECT product_name, nutriscore, url FROM Product WHERE id = %s"
        self.mycursor.execute(sql_query2, (self.product_selected_id,))
        result2 = self.mycursor.fetchall()
        for x in result2:
            res_prod_name = x[0]
            res_nutri = x[1]
            res_url = x[2]
        url = QtWidgets.QLineEdit(res_url)
        product_name = QtWidgets.QTableWidgetItem(res_prod_name)
        nutriscore = QtWidgets.QTableWidgetItem(res_nutri)
        self.mytable.setCellWidget(0, 2, url)
        self.mytable.setItem(0, 0, product_name)
        self.mytable.setItem(0, 1, nutriscore)
        # header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.layout.addWidget(self.mytable)
        self.layout.addWidget(self.search_button)
        self.setLayout(self.layout)
        
        self.search_button.clicked.connect(self.update_subs_table)

        self.mycombo_cat.currentIndexChanged.connect(self.update_combo_prod)

        self.mycombo_prod.currentIndexChanged.connect(self.update_table)
        print(self.mycombo_prod.currentIndex())
            # self.create_table(self.prod_name, self.nutri, self.url)

        
        


    def update_combo_prod(self):
        self.mycombo_prod.clear()
        category_selected = (self.mycombo_cat.currentIndex()) + self.first_cat
        # print(category_selected)        
        sql_query_test = "SELECT product_name FROM Product inner join Product_category WHERE Product.id = Product_category.product_id and Product_category.category_id = %s"

        self.mycursor.execute(sql_query_test, (category_selected,))
        result = self.mycursor.fetchall()
        for x in result:
            self.mycombo_prod.addItem(x[0])



    def update_table(self):
        
        # self.mytable.removeRow(0)
        self.mytable.setHorizontalHeaderLabels(("Produit sélectionné;Nutriscore;Lien vers le site web").split(";"))
        header = self.mytable.horizontalHeader()
        product_selected_name = self.mycombo_prod.currentText()
        sql_query = "SELECT id FROM Product WHERE product_name = %s"
        self.mycursor.execute(sql_query, (product_selected_name,))
        result = self.mycursor.fetchall()
        for x in result:
            self.product_selected_id = x[0]

        sql_query2 = "SELECT product_name, nutriscore, url FROM Product WHERE id = %s"
        self.mycursor.execute(sql_query2, (self.product_selected_id,))
        result2 = self.mycursor.fetchall()
        for x in result2:
            res_prod_name = x[0]
            res_nutri = x[1]
            res_url = x[2]
        url = QtWidgets.QLineEdit(res_url)
        product_name = QtWidgets.QTableWidgetItem(res_prod_name)
        nutriscore = QtWidgets.QTableWidgetItem(res_nutri)
        self.mytable.setCellWidget(0, 2, url)
        self.mytable.setItem(0, 0, product_name)
        self.mytable.setItem(0, 1, nutriscore)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)


        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        # self.layout.addWidget(self.mytable)

    def update_subs_table(self):
        print("linked")

        self.subs_table.setHorizontalHeaderLabels(("Produit de substitution;Nutriscore;Lien vers le site web").split(";"))
        header2 = self.subs_table.horizontalHeader()
        header2.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header2.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header2.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        
        header2.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header2.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header2.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.layout.addWidget(self.subs_table)


if __name__ == '__main__':


    import sys
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    menu = Menu()
    # Run the main Qt loop
    sys.exit(menu.exec_())
