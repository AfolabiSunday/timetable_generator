# This Python file uses the following encoding: utf-8

import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import datetime
import pymysql
from PyQt5.QtWidgets import 

from PyQt5.uic import loadUiType

page ,_ = loadUiType('timetable.ui')
createuser ,_ = loadUiType('registerUser.ui')

class MainApp(QMainWindow, page):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handled_Button()

    def Handled_Button(self):
        self.actionCreate_New_Users.triggered.connect(self.addUserClass)
        self.actionEdit_New_User.triggered.connect(self.editUser)

    def addUserClass(self):
        self.window2 = UserReg()
        self.window2.show()
    def editUser(self):
        self.window =EditUsers()
        self.window.show()

        



class UserReg(QWidget, createuser):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Registration)

    
    def Registration(self):
        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='Sunlabi001.',
            db='timetable',
        )
        username = self.lineEdit.text()
        email = self.lineEdit_2.text()
        phone = self.lineEdit_4.text()
        password= self.lineEdit_3.text()
        password2 = self.lineEdit_5.text()

        
        if password == password2:
            self.cur = self.db.cursor()
            self.cur.execute('''INSERT INTO users (User_name, User_email, User_phone, User_password)
             VALUES (%s, %s, %s, %s)''',
            (username, email, phone, password))
            self.db.commit()
            print(email + username +password2 +password + phone)
            
        else:
            



edituses ,_ = loadUiType('editdelete_users1.ui')


class EditUsers(QWidget, edituses):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

    
        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='Sunlabi001.',
            db='timetable',
        )

        self.cur=self.db.cursor()
        self.cur.execute('SELECT User_name FROM users')
        DBB = self.cur.fetchall()
        

        for data in DBB:
            self.comboBox.addItem(str(DBB))
















def runall():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    runall()

