# This Python file uses the following encoding: utf-8

import os
import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import datetime
import pymysql
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
        self.actionDelete_User.triggered.connect(self.editUser)

    def addUserClass(self):
        self.window2 = UserReg()
        self.window2.show()
    def editUser(self):
        self.window =EditUsers()
        self.window.show()



    def gmessage(self):
        self.QMessageBox.about('Info', 'User Updated')

        



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
            pass
            # bug needs fixes QMessageBox.Warning(self, 'Not Recognized User', 'Please see the Chief Admin for more details')



edituses,_ = loadUiType('editdelete_users1.ui')
from PyQt5.QtWidgets import QMessageBox

class EditUsers(QWidget, edituses):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.searchUsers)
        self.pushButton_2.clicked.connect(self.editusers)
        self.pushButton_3.clicked.connect(self.saveusers)

    
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
            self.comboBox.addItem(str(data[0]))
            EditUsers.close(self)


    def searchUsers(self):
        usersearch = self.comboBox.currentText()
        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='Sunlabi001.',
            db='timetable',
        )


        self.cur=self.db.cursor()
        self.cur.execute('SELECT * FROM users WHERE User_name = %s', usersearch )
        DBB = self.cur.fetchone()
        
        self.lineEdit.setText(DBB[1])
        self.lineEdit_2.setText(DBB[2])
        self.lineEdit_4.setText(str(DBB[3]))
        self.lineEdit_3.setText(DBB[4])

        self.db.commit()


    def editusers(self):
        self.TODELET = self.lineEdit.text()
        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='Sunlabi001.',
            db='timetable',
        )

        self.cur = self.db.cursor()
        warning = QMessageBox.warning(self, 'Delete User', 'Are you sure you want to delete this User?', QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes:
            self.cur.execute('DELETE FROM users WHERE User_name = %s ', self.TODELET )
            self.db.commit()
            self.lineEdit.setText(' ')
            self.lineEdit_2.setText(' ')
            self.lineEdit_4.setText(' ')
            self.lineEdit_3.setText(' ')
            self.comboBox.setCurrentText(str(0))

        else:
            pass


    def deleteusers(self):
        return self.editusers()


    def saveusers(self):
        saveId = self.comboBox.currentText()
        username = self.lineEdit.text()
        email = self.lineEdit_2.text()
        phone = self.lineEdit_4.text()
        password = self.lineEdit_3.text()
        password2 = self.lineEdit_5.text()

        if password == password2:
            self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='Sunlabi001.',
            db='timetable',)

            self.cur = self.db.cursor()
            self.cur.execute(''' UPDATE users SET User_name=%s, User_email=%s, User_phone=%s, User_password=%s WHERE User_name=%s '''
            , (username, email, phone, password, saveId))
            self.db.commit()

            time.sleep(5)
            self.close()

        else:
            self.label_7.setText('Please Check details')
















def runall():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    runall()

