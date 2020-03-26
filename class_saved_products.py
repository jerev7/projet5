from PySide2.QtWidgets import (QApplication, QPushButton, QDialog, QLineEdit, QVBoxLayout, QMessageBox)
from PySide2 import QtWidgets, QtCore, QtGui
import mysql.connector





class Saved_products(QDialog):
    
    def __init__(self, mydb, parent=None):
        super(Saved_products, self).__init__(parent)

        self.mydb = mydb

        self.mytable3 = QtWidgets.QTableWidget(0, 4)
        self.mytable3.setHorizontalHeaderLabels(("Produit sélectionné;Substitution choisi;Magasins;Lien vers le site web").split(";"))
        header = self.mytable3.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        # header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.update_data()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.mytable3)
        self.setLayout(self.layout)


    def update_data(self):

        sql1 = "SELECT product_name FROM Product WHERE id = %s"
        sql2 = "SELECT product_name, stores, url FROM Product WHERE id = %s"
        sql3 = "SELECT product_selected_id FROM Product_saved"
        sql4 = "SELECT substitution_product_id FROM Product_saved"

        self.mycursor = self.mydb.cursor()

        self.mycursor.execute(sql3)
        result3 = self.mycursor.fetchall()
        self.mycursor.execute(sql4)
        result4 = self.mycursor.fetchall()

        row_nbr = 0
        for product_selected_id in result3:
            self.mycursor.execute(sql1, product_selected_id)
            self.mytable3.insertRow(row_nbr)
            result1 = self.mycursor.fetchall()
            for product in result1:
                prod_name = QtWidgets.QTableWidgetItem(product[0])
                self.mytable3.setItem(row_nbr, 0, prod_name)
            row_nbr += 1
        row_nbr = 0
        for substitution_id in result4:
            self.mycursor.execute(sql2, substitution_id)
            result2 = self.mycursor.fetchall()
            for substitution_product in result2:
                subs_name = QtWidgets.QTableWidgetItem(substitution_product[0])
                subs_stores = QtWidgets.QTableWidgetItem(substitution_product[1])
                subs_url = QtWidgets.QTableWidgetItem(substitution_product[2])
                self.mytable3.setItem(row_nbr, 1, subs_name)
                self.mytable3.setItem(row_nbr, 2, subs_stores)
                self.mytable3.setItem(row_nbr, 3, subs_url)
            row_nbr += 1