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
        #self.tabWidget.tabBar().setVisible(False)
        self.showgenerateTimetable()
        self.pushButton.clicked.connect(self.searchClass)

    def Handled_Button(self):
        self.actionCreate_New_Users.triggered.connect(self.addUserClass)
        self.actionEdit_New_User.triggered.connect(self.editUser)
        self.actionDelete_User.triggered.connect(self.editUser)
        self.actionAdde_New_Teacher.triggered.connect(self.addteacherclass)
        self.actionEdit_Techer.triggered.connect(self.editTeachers)
        self.actionDelete_Teacher.triggered.connect(self.editTeachers)
        self.actionAdd_Subject.triggered.connect(self.SubjectShow)
        self.actionDelete_Subject.triggered.connect(self.showeditsubject)
        self.actionEdit_Subject.triggered.connect(self.showeditsubject)
        #self.actionAdd_Class_2.triggered.connect(self.showaddclass)

    # def showaddclass(self):
    #     self.window= AddClass()
    #     self.window.show

    def addUserClass(self):
        self.window2 = UserReg()
        self.window2.show()
    def editUser(self):
        self.window =EditUsers()
        self.window.show()

    def addteacherclass(self):
        self.window=AddNewTeacher()
        self.window.show()
        
    def editTeachers(self):
        self.window = EditTeachersMain()
        self.window.show()

    def SubjectShow(self):
        self.window = SubjectMain()
        self.window.show()
    def showeditsubject(self):
        self.window = EditDeleteSubject()
        self.window.show()


    
######################################################
###### TABLE WIDEGT ##############################

    def showgenerateTimetable(self):
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(10)
        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='Sunlabi001.',
            db='timetable',
        )

        self.cur=self.db.cursor()
        self.cur.execute('SELECT classname FROM class' )
        
        self.cur.execute(' SELECT classname FROM class')
        DBB =self.cur.fetchall()
        
        for i in DBB:
            self.comboBox.addItem(str(i[0]))
    
        # self.tableWidget.setItem(0,0, QTableWidgetItem('colume'))
        # self.tableWidget.setItem(0,1, QTableWidgetItem('row'))

    def searchClass(self):
        searchId = self.comboBox.currentText()
        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='Sunlabi001.',
            db='timetable',
        )

        self.cur=self.db.cursor()

        self.cur.execute('SELECT * FROM subject WHERE class_taken_subject=%s',  searchId)
        DBB = self.cur.fetchall()
        print(DBB)
        print(DBB[0][1])
        for i in DBB:
            self.tableWidget.setRowCount(5)
            self.tableWidget.setColumnCount(10)
            self.tableWidget.setItem(0,0, QTableWidgetItem("MONDAY"))
            self.tableWidget.setItem(1,0, QTableWidgetItem("TUESDAY"))
            self.tableWidget.setItem(2,0, QTableWidgetItem("WEDNESDAY"))
            self.tableWidget.setItem(3,0, QTableWidgetItem("THURSDAY"))
            self.tableWidget.setItem(4,0, QTableWidgetItem("FRIDAY"))
            if i[4] == "5th":
                print('yes')

            else:
                print('no')
            self.tableWidget.move(0,0)
# self.tableWidget.setItem(0,1, QTableWidgetItem(DBB[0][4]))
# self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
# self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
# self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))

# addclass ,_ =loadUiType('addClass.ui')
# class AddClass(QWidget, addclass):
#     def __init__(self):
#         QWidget.__init__(self)
#         self.setupUi(self)
#         self.show()

#     def createClass(self):
#         self.db = pymysql.connect(
#             host='localhost',
#             user='root',
#             password='Sunlabi001.',
#             db='timetable',)

#         self.cur = self.db.cursor()

#         #self.cur.execute('INSERT INTO class WHERE classname=%s, classnumberofstudent=%s')



####################################################
### Subject Class to Add Subject to class ##########
####################################################



subjectclass ,_ =loadUiType('addSubject.ui')

class SubjectMain(QWidget, subjectclass):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.add_subject)

        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='Sunlabi001.',
            db='timetable',)
        self.cur = self.db.cursor()

        self.cur.execute(' SELECT teachername FROM teachers')
        DBB =self.cur.fetchall()
        
        for i in DBB:
            self.comboBox_2.addItem(str(i[0]))

    def add_subject(self):
        names = self.comboBox.currentText()
        teacher = self.comboBox_2.currentText()
        classsub = self.comboBox_3.currentText()
        days = self.comboBox_4.currentText()
        period = self.comboBox_5.currentText()

        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='Sunlabi001.',
            db='timetable',)
        self.cur = self.db.cursor()

        self.cur = self.db.cursor()
        self.cur.execute(''' INSERT INTO subject (subjectname, teacher_taken_subject, class_taken_subject, period_of_subject, days_for_subject)
        VALUES (%s, %s, %s, %s, %s)''', (names, teacher, classsub, period, days))

        self.db.commit()
        self.db.close()
        self.close()


editsubject ,_ = loadUiType('editDeleteSubject.ui')

class EditDeleteSubject(QWidget, editsubject):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.searchSubject)
        self.pushButton.clicked.connect(self.deletesubject)
        self.pushButton_2.clicked.connect(self.editsubject)

        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='Sunlabi001.',
            db='timetable',)
        self.cur = self.db.cursor()

        self.cur.execute(' SELECT subjectname FROM subject')
        DBB =self.cur.fetchall()        
        for i in DBB:
            self.comboBox.addItem(str(i[0]))

    

    def searchSubject(self):
        subjectSearch = self.comboBox.currentText()
        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='Sunlabi001.',
            db='timetable',
        )

        self.cur=self.db.cursor()
        self.cur.execute('SELECT * FROM subject WHERE subjectname = %s', subjectSearch )
        DBB = self.cur.fetchall()


        for dat in DBB:
            self.comboBox_7.setCurrentText(dat[1])
            self.comboBox_9.setCurrentText(dat[2])
            self.comboBox_10.setCurrentText(dat[3])
            self.comboBox_6.setCurrentText(dat[5])
            self.comboBox_8.setCurrentText(dat[4])
            


    def deletesubject(self):
        deletesub = self.comboBox_7.currentText() 
        self.cur = self.db.cursor()
        warning = QMessageBox.warning(self, 'Delete subject', 'Are you sure you want to delete this User?', QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes:
            self.cur.execute('DELETE FROM subject WHERE subjectname = %s ', deletesub )
            self.db.commit()
            self.comboBox_7.setCurrentText(str(0))
            self.comboBox_9.setCurrentText(str(0))
            self.comboBox_10.setCurrentText(str(0))
            self.comboBox_6.setCurrentText(str(0))
            self.comboBox_8.setCurrentText(str(0))
            self.close()

    def editsubject(self):
        saveId = self.comboBox.currentText()

        subjectname = self.comboBox_7.currentText()
        teachersname = self.comboBox_9.currentText()
        classsubject = self.comboBox_10.currentText()
        daysofweek = self.comboBox_6.currentText()
        period = self.comboBox_8.currentText()

        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='Sunlabi001.',
            db='timetable',)

        self.cur = self.db.cursor()
        warning = QMessageBox.warning(self, 'Edit subject', 'Are you sure you want to Edit this Subject?', QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes:
            self.cur.execute('''
                UPDATE subject SET subjectname=%s, teacher_taken_subject=%s, class_taken_subject=%s, period_of_subject=%s, days_for_subject=%s WHERE subjectname=%s ''',
                (subjectname, teachersname, classsubject, period, daysofweek, saveId))
            self.db.commit()
            self.db.close()
            
            self.comboBox_7.setCurrentText(str(0))
            self.comboBox_9.setCurrentText(str(0))
            self.comboBox_10.setCurrentText(str(0))
            self.comboBox_6.setCurrentText(str(0))
            self.comboBox_8.setCurrentText(str(0))
            self.close()
        else:
            pass




#######################################################
########## Teachers Class #############################
#######################################################

addteacher ,_ = loadUiType('newteacher.ui')


class AddNewTeacher(QWidget, addteacher):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.registerTeacher)


    def registerTeacher(self):
        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='Sunlabi001.',
            db='timetable',
        )
        Name = self.lineEdit.text()
        subject = self.lineEdit_2.text()
        address = self.lineEdit_3.text()
        phone = self.lineEdit_4.text()

        
    
        self.cur = self.db.cursor()
        self.cur.execute('''INSERT INTO teachers (teachername, teacherphone, teachersubject, teachersaddress)
        VALUES (%s, %s, %s, %s)''', (Name, phone, subject, address))
        self.db.commit()
        self.close()


editTeachersUi ,_ = loadUiType('editdelete_teachers.ui')

class EditTeachersMain(QWidget, editTeachersUi):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.searchTeachers)
        self.pushButton_3.clicked.connect(self.SaveTeachers)
        self.pushButton_2.clicked.connect(self.removeteacher)

        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='Sunlabi001.',
            db='timetable',
        )
        self.cur = self.db.cursor()


        self.cur.execute('SELECT teachername FROM teachers')
        DBB = self.cur.fetchall()
        
        for names in DBB:
            self.comboBox.addItem(names[0])
            EditTeachersMain.close(self)
        

    def SaveTeachers(self):
        saveId = self.comboBox.currentText()

        username = self.lineEdit.text()
        subject = self.lineEdit_2.text()
        phone = self.lineEdit_3.text()
        address = self.lineEdit_4.text()


        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='Sunlabi001.',
            db='timetable',)

        self.cur = self.db.cursor()
        self.cur.execute('''
            UPDATE teachers SET teachername=%s, teacherphone=%s, teachersubject=%s, teachersaddress=%s WHERE teachername=%s ''',
            (username, phone, subject, address, saveId))
        self.db.commit()
        self.db.close()
        self.comboBox.setCurrentText(str(0))
        self.lineEdit.setText(' ')
        self.lineEdit_2.setText(' ')
        self.lineEdit_4.setText(' ')
        self.lineEdit_3.setText(' ')
        self.close()
        

    def searchTeachers(self):
        teachersearch = self.comboBox.currentText()
        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='Sunlabi001.',
            db='timetable',
        )
        self.cur = self.db.cursor()

        self.cur.execute('SELECT * FROM teachers WHERE teachername=%s ', teachersearch)
        DBB =self.cur.fetchone()
        

        self.lineEdit.setText(DBB[1])
        self.lineEdit_2.setText(DBB[3])
        self.lineEdit_3.setText(str(DBB[2]))
        self.lineEdit_4.setText(DBB[4])


    def removeteacher(self):
        self.TODELET = self.lineEdit.text()
        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='Sunlabi001.',
            db='timetable',
        )

        self.cur = self.db.cursor()
        warning = QMessageBox.warning(self, 'Delete Teacher', 'Are you sure you want to delete this User?', QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes:
            self.cur.execute('DELETE FROM teachers WHERE teachername = %s ', self.TODELET )
            self.db.commit()
            self.lineEdit.setText(' ')
            self.lineEdit_2.setText(' ')
            self.lineEdit_4.setText(' ')
            self.lineEdit_3.setText(' ')
            self.comboBox.setCurrentText(str(0))

            ### keep crashing if search is NOne, need to fix this


    

########################################################
### User Createtion Class
#########################################################

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
                        
        else:
            pass
            # bug needs fixes QMessageBox.Warning(self, 'Not Recognized User', 'Please see the Chief Admin for more details')



################################################
####              Edit Users Class      ########
################################################


edituses,_ = loadUiType('editdelete_users1.ui')
from PyQt5.QtWidgets import QMessageBox

class EditUsers(QWidget, edituses):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.searchUsers)
        self.pushButton_2.clicked.connect(self.removeUsers)
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


    def removeUsers(self):
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

