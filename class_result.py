from PySide2.QtWidgets import (QApplication, QPushButton,
                               QDialog, QLineEdit, QVBoxLayout, QMessageBox)
from PySide2 import QtWidgets, QtCore, QtGui
import mysql.connector


class Resultat(QDialog):

    def __init__(self, mydb, parent=None):
        super(Resultat, self).__init__(parent)

        self.setWindowTitle("Project 5 : Openfoodfacts")
        self.mydb = mydb
        # Create widgets
        self.text_cat = QtWidgets.QLabel(
            "Select a category below")
        # self.text.SetLineEdit("Choose a category below")
        self.mycombo_cat = QtWidgets.QComboBox()
        self.text_prod = QtWidgets.QLabel("Then select a product")
        self.mycombo_prod = QtWidgets.QComboBox()
        self.text_select_subs = QtWidgets.QLabel("Choose one of the substitution product")
        self.mytable = QtWidgets.QTableWidget(1, 4)
        self.mytable.setHorizontalHeaderLabels(("Selected product;Nutriscore;Stores;Link to website").split(";"))
        header = self.mytable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        # header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.subs_table = QtWidgets.QTableWidget(1, 4)
        self.subs_table.setHorizontalHeaderLabels(("Substitution product;Nutriscore;Stores;Link to website").split(";"))
        header2 = self.mytable.horizontalHeader()
        header2.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header2.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header2.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header2.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        
        header2.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header2.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header2.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header2.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

        self.search_button = QPushButton("Search a substitution product")
        self.save_button = QPushButton("Save result")
        self.save_button.hide()

        self.mycursor = self.mydb.cursor()
        
        # Getting all product categories
        sql_query_cat = "SELECT * FROM Category"
        self.mycursor.execute(sql_query_cat)
        result = self.mycursor.fetchall()
        for category in result:
            category_id = category[0]
            category_name = category[1]
            self.mycombo_cat.addItem("{} - {}".format(category_id, (category_name)))
        self.first_cat = result[0][0]
        self.layout = QVBoxLayout()
        
        self.layout.addWidget(self.text_cat)
        self.layout.addWidget(self.mycombo_cat)
        self.layout.addWidget(self.text_prod)
        self.layout.addWidget(self.mycombo_prod)

        self.update_combo_prod()  # adding categories to the table
        
        self.update_table()
        # # header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        # # header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        # # header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.layout.addWidget(self.mytable)
        self.layout.addWidget(self.search_button)
        self.layout.addWidget(self.text_select_subs)
        self.setLayout(self.layout)
        self.search_button.clicked.connect(self.update_subs_table)
        self.mycombo_cat.currentIndexChanged.connect(self.update_combo_prod)

        self.mycombo_prod.currentIndexChanged.connect(self.update_table)
        self.save_button.clicked.connect(self.save_results)

        self.layout.addWidget(self.subs_table)
        
        # self.text_select_subs.hide()
        self.subs_table.hide()
        self.layout.addWidget(self.save_button)
        # self.create_table(self.prod_name, self.nutri, self.url)

    def update_combo_prod(self):
        self.mycombo_prod.clear()
        category_selected = (self.mycombo_cat.currentIndex()) + self.first_cat
        # print(category_selected)        
        sql_query_test = """SELECT product_name FROM Product inner join Product_category 
                            WHERE Product.id = Product_category.product_id and 
                            Product_category.category_id = %s"""

        self.mycursor.execute(sql_query_test, (category_selected,))
        result = self.mycursor.fetchall()
        for x in result:
            self.mycombo_prod.addItem(x[0])



    def update_table(self):
        
        self.mytable.setHorizontalHeaderLabels(("Selected product;Nutriscore;Stores;Link to website").split(";"))
        header = self.mytable.horizontalHeader()
        product_selected_name = self.mycombo_prod.currentText()
        sql_query = "SELECT id FROM Product WHERE product_name = %s"
        self.mycursor.execute(sql_query, (product_selected_name,))
        result = self.mycursor.fetchall()
        for product in result:
            self.product_selected_id = product[0]

        sql_query2 = "SELECT product_name, nutriscore, stores, url FROM Product WHERE id = %s"
        self.mycursor.execute(sql_query2, (self.product_selected_id,))
        result2 = self.mycursor.fetchall()
        for product in result2:
            res_prod_name = product[0]
            self.res_nutri = product[1]
            res_stores = product[2]
            res_url = product[3]
        
        url = QtWidgets.QTableWidgetItem(res_url)
        product_name = QtWidgets.QTableWidgetItem(res_prod_name)
        nutriscore = QtWidgets.QTableWidgetItem(self.res_nutri)
        stores = QtWidgets.QTableWidgetItem(res_stores)
        self.mytable.setItem(0, 3, url)
        self.mytable.setItem(0, 0, product_name)
        self.mytable.setItem(0, 1, nutriscore)
        self.mytable.setItem(0, 2, stores)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        # self.layout.addWidget(self.mytable)

    def update_subs_table(self):
        print("linked")
        
        self.delete_rows_subs_table()
        
        self.subs_table.setHorizontalHeaderLabels(("Substitution product;Nutriscore;Stores;Link to website").split(";"))
        header2 = self.subs_table.horizontalHeader()
        header2.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header2.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header2.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        
        header2.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header2.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header2.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        
        category_selected = (self.mycombo_cat.currentIndex()) + self.first_cat
        # print(category_selected)        
        sql_query_subs = "SELECT id, product_name, nutriscore, stores, url FROM Product inner join Product_category WHERE Product.id = Product_category.product_id and Product_category.category_id = %s"

        self.mycursor.execute(sql_query_subs, (category_selected,))
        result = self.mycursor.fetchall()
        row_nbr = 0
        self.substitution_possible = []
        for product in result:             
            if product[2] < self.res_nutri:
                self.subs_table.insertRow(row_nbr)
                self.substitution_possible.append(product[0])
                res_prod_name = product[1]
                res_nutri = product[2]
                res_stores = product[3]
                res_url = product[4]
                url = QtWidgets.QTableWidgetItem(res_url)
                product_name = QtWidgets.QTableWidgetItem(res_prod_name)
                nutriscore = QtWidgets.QTableWidgetItem(res_nutri)
                stores = QtWidgets.QTableWidgetItem(res_stores)
                self.subs_table.setItem(row_nbr, 3, url)
                self.subs_table.setItem(row_nbr, 0, product_name)
                self.subs_table.setItem(row_nbr, 1, nutriscore)
                self.subs_table.setItem(row_nbr, 2, stores)
                row_nbr += 1
                
        if row_nbr == 0:
            message_box = QtWidgets.QMessageBox()
            message_box.setWindowTitle("Project 5 : Openfoodfacts")
            message_box.setText("There is no better product than the one selected ! :=)")
            message_box.exec()
        self.subs_table.show()
        self.save_button.show()
        

        
    def delete_rows_subs_table(self):
        
        self.subs_table.clear()
        self.subs_table.setRowCount(0)

    
    def save_results(self):
        print(self.substitution_possible)
        ligne_selectionnee = self.subs_table.currentRow()
        print(ligne_selectionnee)
        substitut_choisi = self.substitution_possible[ligne_selectionnee]
        print(substitut_choisi)

        print("résultats sauvegardés")
        sql1 = "INSERT INTO Product_saved (product_selected_id, substitution_product_id) VALUES (%s, %s)"
        self.mycursor.execute(sql1, (self.product_selected_id, substitut_choisi))
        self.mydb.commit()