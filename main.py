# !/usr/bin/env python3
# coding:utf-8

"""This module is the one you have to launch to start the program. """

import sys
from PySide2.QtWidgets import (QApplication, QPushButton, QDialog,
                               QLineEdit, QVBoxLayout, QMessageBox)
from PySide2 import QtWidgets, QtCore, QtGui
import mysql.connector
from class_menu import *


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    menu = Menu()
    # Run the main Qt loop
    sys.exit(menu.exec_())
