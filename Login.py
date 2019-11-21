import mysql.connector
import webbrowser
import subprocess
import sys
import connect_to_db
import svn.remote
import pprint
import svn.local
import os, glob
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import *
from GUI_PyQt5_Designer.Log_On_CIS import *
from GUI_PyQt5_Designer.Login_user import *
from GUI_PyQt5_Designer.Main_window_tabs import *
from Log_On_CIS import *
from time import gmtime, strftime
import json

global data
with open('config.json') as json_data_file:
    data = json.load(json_data_file)

class MyWin(QtWidgets.QMainWindow):  # Авторизация юзера
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)  # сделать пароль невидемым
        self.ui.pushButton.clicked.connect(self.getresult)
        self.ui.lineEdit_2.returnPressed.connect(self.getresult)
        self.ui.pushButton_2.clicked.connect(self.loginuser)
        self.ui.lineEdit_1.setPlaceholderText('Enter username')
        self.ui.lineEdit_2.setPlaceholderText('Enter password')

    def loginuser(self):
        MyApp2.show()

    def getresult(self):
        global log
        self.aboutshow1 = Second()
        log = self.ui.lineEdit_1.text()
        pas = self.ui.lineEdit_2.text()
        self.logpas = (log, pas)

        # MySQL connect to DB
        mydb = mysql.connector.connect(
            host=data['mysql']['host'],
            user="dpe",
            passwd="dpe",
            database="dpe",
            charset='utf8',
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM login_db")
        myresult = mycursor.fetchall()
        for i in myresult:
            if self.logpas == i:
                self.ui.label_3.setText("Authorization OK")
                myapp.close()  # Закрывает текущее окно

                a = strftime("%Y%m%d", gmtime())
                global update_log
                update_log = a + '(' + log + ')'
            else:
                self.ui.label_3.setText("Incorrect login or pass")
        MyApp3.show()
        MyApp3.ui2.label_14.setText(update_log)

        sch_part = []
        dir_name = glob.glob('C:\Cadence\Company\EKTOS_CIS\SCH_Libraries/**/*.OLB')
        for some in dir_name:
            x = some.replace("C:\\Cadence\\Company\\EKTOS_CIS\\SCH_Libraries\\", "")
            y = x.split('\\')[1]
            sch_part.append(y)

        dir_name2 = glob.glob('C:\Cadence\Company\EKTOS_CIS\_NEW_PARTS_/**/*.OLB')
        for some in dir_name2:
            x = some.replace("C:\\Cadence\\Company\\EKTOS_CIS\\_NEW_PARTS_\\", "")
            # print(x)
            y = x.split('\\')[1]
            sch_part.append(y)
        MyApp3.ui2.comboBox_67.addItem('')
        MyApp3.ui2.comboBox_68.addItem('')
        MyApp3.ui2.comboBox_69.addItem('')
        for peremennaya in sch_part:
            MyApp3.ui2.comboBox_67.addItem(str(peremennaya))
            MyApp3.ui2.comboBox_68.addItem(str(peremennaya))
            MyApp3.ui2.comboBox_69.addItem(str(peremennaya))

        pcb_foot = []
        dir_name3 = glob.glob('C:\Cadence\Company\EKTOS_CIS\PCB_Footprints/**/*.dra')
        for some in dir_name3:
            x = some.replace("C:\\Cadence\\Company\\EKTOS_CIS\\PCB_Footprints\\", "")
            y = x.split('\\')[1]
            pcb_foot.append(y)
        dir_name4 = glob.glob('C:\Cadence\Company\EKTOS_CIS\PCB_Footprints/*.dra')
        for some in dir_name4:
            x = some.replace("C:\\Cadence\\Company\\EKTOS_CIS\\PCB_Footprints\\", "")
            pcb_foot.append(x)
        dir_name5 = glob.glob('C:\Cadence\Company\EKTOS_CIS\_NEW_PARTS_/**/*.dra')
        for some in dir_name5:
            x = some.replace("C:\\Cadence\\Company\\EKTOS_CIS\\_NEW_PARTS_\\", "")
            y = x.split('\\')[1]
            pcb_foot.append(y)
        MyApp3.ui2.comboBox_70.addItem('')
        MyApp3.ui2.comboBox_71.addItem('')
        MyApp3.ui2.comboBox_72.addItem('')
        MyApp3.ui2.comboBox_73.addItem('')
        MyApp3.ui2.comboBox_74.addItem('')
        for peremennaya in pcb_foot:
            MyApp3.ui2.comboBox_70.addItem(str(peremennaya))
            MyApp3.ui2.comboBox_71.addItem(str(peremennaya))
            MyApp3.ui2.comboBox_72.addItem(str(peremennaya))
            MyApp3.ui2.comboBox_73.addItem(str(peremennaya))
            MyApp3.ui2.comboBox_74.addItem(str(peremennaya))

        datasheets = []
        dir_name6 = glob.glob('C:\Cadence\Company\EKTOS_CIS\data\Datasheets/*.pdf')
        for some in dir_name6:
            x = some.replace("C:\\Cadence\\Company\\EKTOS_CIS\\data\\Datasheets\\", "")
            datasheets.append(x)
        dir_name7 = glob.glob('C:\Cadence\Company\EKTOS_CIS\_NEW_PARTS_/**/*.pdf')
        for some in dir_name7:
            x = some.replace("C:\\Cadence\\Company\\EKTOS_CIS\\_NEW_PARTS_\\", "")
            y = x.split('\\')[1]
            datasheets.append(y)
        MyApp3.ui2.comboBox_75.addItem('')
        for peremennaya in datasheets:
            MyApp3.ui2.comboBox_75.addItem(str(peremennaya))

        # r = svn.remote.RemoteClient('http://scm.ektos.net/scm/svn/cis-components')
        # entries = r.list()
        # for filename in entries:
        #     print(filename)
        #     fixed1 = ''.join(filename.split("/"))
        #     if len(fixed1) == 3:
        #         r = svn.remote.RemoteClient('http://scm.ektos.net/scm/svn/cis-components/{}'.format(fixed1))
        #         r1 = r.list()
        #         for peremennaya in r1:
        #             if '.dra' in peremennaya:
        #                 MyApp3.ui2.comboBox_70.addItem(str(peremennaya))
        #                 MyApp3.ui2.comboBox_71.addItem(str(peremennaya))
        #                 MyApp3.ui2.comboBox_72.addItem(str(peremennaya))
        #                 MyApp3.ui2.comboBox_73.addItem(str(peremennaya))
        #                 MyApp3.ui2.comboBox_74.addItem(str(peremennaya))
        #             elif '.OLB' in peremennaya:
        #                 MyApp3.ui2.comboBox_67.addItem(str(peremennaya))
        #                 MyApp3.ui2.comboBox_68.addItem(str(peremennaya))
        #                 MyApp3.ui2.comboBox_69.addItem(str(peremennaya))
        #             elif '.pdf' in peremennaya:
        #                 MyApp3.ui2.comboBox_75.addItem(str(peremennaya))


class Second(QtWidgets.QMainWindow, Ui_Form):  # Логин нового юзера
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui1 = Ui_Form()
        self.ui1.setupUi(self)
        self.ui1.pushButton_2.clicked.connect(self.loginUser)

    def loginUser(self):
        log_newuser = self.ui1.Edit_user_name.text()
        pas_newuser = self.ui1.Edit_password.text()
        pas2_newuser = self.ui1.Edit_repeat_password.text()
        if pas_newuser == pas2_newuser:
            mydb = mysql.connector.connect(
                host=data['mysql']['host'],
                user="dpe",
                passwd="dpe",
                database="dpe",
                charset='utf8',
            )
            mycursor = mydb.cursor()
            sql = "INSERT INTO login_db (Login, Pass) VALUES (%s, %s)"
            val = (log_newuser, pas_newuser)
            mycursor.execute(sql, val)
            mydb.commit()
            self.ui1.label_4.setText("New user added successfully")
        else:
            self.ui1.label_4.setText("Error: Different passes")


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow2):  # Главное меню
    global counter1
    counter1 = 0

    global masiv
    masiv = [0]

    global masiv_new
    masiv_new = [[], [], [], []]

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        # a = strftime("%Y%m%d", gmtime())
        # global update_log
        # update_log = a + '(' + log + ')'




        self.ui2 = Ui_MainWindow2()
        self.ui2.setupUi(self)
        # self.ui2.pushButton_9.clicked.connect(self.first_serch)
        # self.ui2.pushButton.clicked.connect(self.relayadd)
        self.ui2.pushButton_2.clicked.connect(self.resistor)
        self.ui2.pushButton_3.clicked.connect(self.transistor)
        self.ui2.pushButton_4.clicked.connect(self.connector)
        self.ui2.pushButton_5.clicked.connect(self.diode)
        self.ui2.pushButton_6.clicked.connect(self.inductor)
        self.ui2.pushButton_7.clicked.connect(self.capasitor)
        self.ui2.pushButton_11.clicked.connect(self.integrated_circuit)
        self.ui2.pushButton_8.clicked.connect(self.mecanical)
        self.ui2.pushButton_10.clicked.connect(self.other)
        # self.ui2.label_14.setText(update_log)

        # self.ui2.lineEdit_13.setPlaceholderText('Automatically added ')
        self.ui2.lineEdit_29.setPlaceholderText('Automatically added ')
        self.ui2.lineEdit_70.setPlaceholderText('Automatically added ')
        self.ui2.lineEdit_97.setPlaceholderText('Automatically added ')
        self.ui2.lineEdit_126.setPlaceholderText('Automatically added ')
        self.ui2.lineEdit_151.setPlaceholderText('Automatically added ')
        self.ui2.lineEdit_175.setPlaceholderText('Automatically added ')
        self.ui2.lineEdit_299.setPlaceholderText('Automatically added ')
        self.ui2.lineEdit_207.setPlaceholderText('Automatically added ')
        self.ui2.lineEdit_271.setPlaceholderText('Automatically added ')
        self.ui2.editSearch3.setPlaceholderText('                          Component search')

        self.ui2.pushButton_28.clicked.connect(self.datasheet_view)
        self.ui2.pushButton_27.clicked.connect(self.refresh)
        self.ui2.pushButton_26.clicked.connect(self.clear)
        self.ui2.listFound.itemClicked.connect(self.lict)
        self.ui2.pushButton.clicked.connect(self.add_to_db)

        self.ui2.pushButton_17.clicked.connect(self.add_vendor_to_table)



        # self.ui2.boxSearch1.activated.connect(self.prinprintprint)

        mydb = mysql.connector.connect(
            host=data['mysql']['host'],
            user="dpe",
            passwd="dpe",
            database="dpe",
            charset='utf8',
        )
        mycursor = mydb.cursor()
        mycursor.execute(
            "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'dpe' AND TABLE_NAME = 'test_relay' order by ordinal_position;")
        self.ui2.boxSearch1.addItem('')
        self.ui2.boxSearch2.addItem('')
        self.ui2.boxSearch3.addItem('')
        for variable in mycursor:
            b = str(variable)
            fixed1 = ''.join(b.split(")"))
            fixed2 = ''.join(fixed1.split("("))
            fixed3 = ''.join(fixed2.split("'"))
            fixed4 = ''.join(fixed3.split(","))
            global columns_name
            self.ui2.boxSearch1.addItem(str(fixed4))
            self.ui2.boxSearch2.addItem(str(fixed4))
            self.ui2.boxSearch3.addItem(str(fixed4))

            if fixed4 == 'vcoil':
                break

        self.ui2.editSearch1.returnPressed.connect(self.search_1)
        self.ui2.editSearch2.returnPressed.connect(self.search_2)
        self.ui2.editSearch3.returnPressed.connect(self.search_3)

    def connect_to_db(self):
        mydb = mysql.connector.connect(
            host=data['mysql']['host'],
            user=data['mysql']['user'],
            passwd=data['mysql']['passwd'],
            database=data['mysql']['db'],
            charset='utf8',
        )
        mycursor = mydb.cursor()
        return mycursor

    def search_1(self):
        global all_component_arrey
        all_component_arrey = ['test_relay', 'test_resistor']  #ДОБАВИТЬ НОВЫЕ ТАБЛИЦИ СЮДА
        print(all_component_arrey)
        global d
        self.ui2.listFound.clear()

## Connection to DB __________________________________________________________________________________

        connection = connect_to_db.getConnectiot()
        mycursor = connection.cursor()


        c = self.ui2.editSearch1.text()
        parametr = self.ui2.boxSearch1.currentText()
        d = []

        for peremennaya in all_component_arrey:
            mycursor.execute("SELECT ektospn FROM {} WHERE {} LIKE '%{}%'".format(peremennaya, parametr, c))
            for variable in mycursor:
                b = str(variable)
                fixed1 = ''.join(b.split(")"))
                fixed2 = ''.join(fixed1.split("("))
                fixed3 = ''.join(fixed2.split("'"))
                fixed4 = ''.join(fixed3.split(","))
                d.append(fixed4)

        for variable in d:
            self.ui2.listFound.addItem(variable)

            # mycursor.execute("SELECT Part_Number FROM {} WHERE {} LIKE '%{}%'".format(table2, search2, c))
        # for somedata in mycursor:
        #
        #     x = str(somedata)
        #     if somedata == 'Manufacturer' or somedata == 'Man_Part_Number' or somedata == 'Man_Part_Number' or somedata == 'Vendor' or somedata == 'Vendor_Code':
        #         self.ui2.listFound.addItem(str(x))

    def search_2(self):
        self.ui2.listFound.clear()
        e = self.ui2.editSearch2.text()
        d2 = []
        parametr2 = self.ui2.boxSearch2.currentText()
        connection = connect_to_db.getConnectiot()
        mycursor = connection.cursor()
        for some in d:
            mycursor.execute(
                "SELECT ektospn FROM test_relay WHERE {} LIKE '%{}%' AND ektospn = '{}'".format(parametr2, e, some))
            for variable2 in mycursor:
                b = str(variable2)
                fixed1 = ''.join(b.split(")"))
                fixed2 = ''.join(fixed1.split("("))
                fixed3 = ''.join(fixed2.split("'"))
                fixed4 = ''.join(fixed3.split(","))
                d2.append(fixed4)
        for variable in d2:
            self.ui2.listFound.addItem(variable)

    def search_3(self):

        self.ui2.listFound.clear()
        f = self.ui2.editSearch3.text()
        d3 = []
        parametr3 = self.ui2.boxSearch3.currentText()
        mydb = mysql.connector.connect(
            host="mysql.ektos.net",
            user="dpe",
            passwd="dpe",
            database="dpe",
            charset='utf8',
        )
        mycursor = mydb.cursor()
        print(d)
        for some in d:
            mycursor.execute(
                "SELECT ektospn FROM test_relay WHERE {} LIKE '%{}%' AND ektospn = '{}'".format(parametr3, f, some))
            for variable3 in mycursor:
                b = str(variable3)
                fixed1 = ''.join(b.split(")"))
                fixed2 = ''.join(fixed1.split("("))
                fixed3 = ''.join(fixed2.split("'"))
                fixed4 = ''.join(fixed3.split(","))
                d3.append(fixed4)
        for variable in d3:
            print(variable)
            self.ui2.listFound.addItem(variable)

    def lict(self, item):
        global peremennaya
        masiv = []
        connection = connect_to_db.getConnectiot()
        mycursor = connection.cursor()
        found_item = item.text()
        for perem in all_component_arrey:
            mycursor.execute("SELECT EXISTS(SELECT ektospn FROM {} WHERE ektospn = '{}')".format(perem, found_item))
            for some_data in mycursor:
                if str(some_data) == '(1,)':
                    peremennaya = perem
        mycursor.execute(
            "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'dpe' AND TABLE_NAME = '{}' order by ordinal_position;".format(peremennaya))
        for variable in mycursor:
            b = str(variable)
            fixed1 = ''.join(b.split(")"))
            fixed2 = ''.join(fixed1.split("("))
            fixed3 = ''.join(fixed2.split("'"))
            fixed4 = ''.join(fixed3.split(","))
            masiv.append(fixed4)
        self.ui2.tableViewPatameters.setRowCount(len(masiv))
        global k
        k = 0
        print(masiv)
        for i in masiv:
            k += 1
            self.ui2.tableViewPatameters.setItem(k-1, 0, QTableWidgetItem(i))
        connection = connect_to_db.getConnectiot()
        mycursor = connection.cursor()
        global masiv_for_edit_data
        masiv_for_edit_data = []
        mycursor.execute("SELECT * FROM {} WHERE ektospn = '{}'".format(peremennaya, found_item))
        for data12 in mycursor:
            global coount
            print(data12)
            coount = -1
            for i in data12:
                i2 = str(i)
                print(i2)
                coount += 1
                masiv_for_edit_data.append(i2)
                self.ui2.tableViewPatameters.setItem(coount, 1, QTableWidgetItem(i2))
        self.ui2.pushButton_14.clicked.connect(self.edit_value)

        # global found_item
        # found_item = item.text()
        #
        # mydb = mysql.connector.connect(
        #     host="mysql.ektos.net",
        #     user="dpe",
        #     passwd="dpe",
        #     database="dpe",
        #     charset='utf8',
        # )
        # mycursor = mydb.cursor()
        # a = 'Part_Number'
        # b = table1
        #
        # c = found_item
        # fixed1 = ''.join(c.split(")"))
        # fixed2 = ''.join(fixed1.split("("))
        # fixed3 = ''.join(fixed2.split("'"))
        # fixed3 = ''.join(fixed3.split(","))
        #
        # mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
        # for data12 in mycursor:
        #     global coount
        #     coount = -1
        #     for i in data12:
        #         coount +=1
        #         self.ui2.tableViewPatameters.setItem(coount, 1, QTableWidgetItem(i))
        # b = table2
        # mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
        # for data12 in mycursor:
        #     coount1 = -1
        #     for i in data12:
        #         coount1 += 1
        #         if coount1 == 2 or coount1 == 3 or coount1 == 5 or coount1 == 6:
        #             coount += 1
        #             self.ui2.tableViewPatameters.setItem(coount, 1, QTableWidgetItem(i))
        #
        # self.ui2.pushButton_14.clicked.connect(self.edit_component)
        # self.ui2.pushButton_15.clicked.connect(self.review_component)


    def add_vendor_to_table(self):
        if masiv[-1]  == 9:
            self.ui2.groupBox_25.setEnabled(False)
            print("asadssssssssssssssssssssss")
        manuf = self.ui2.lineEdit_5.text()
        manuf_pn = self.ui2.lineEdit_6.text()
        vendor = self.ui2.boxVendor.currentText()
        vendor_code = self.ui2.lineEdit_248.text()
        self.ui2.tableWidget.setRowCount(10)

        self.ui2.tableWidget.setItem(masiv[-1], 0, QTableWidgetItem(manuf))
        self.ui2.tableWidget.setItem(masiv[-1], 1, QTableWidgetItem(manuf_pn))
        self.ui2.tableWidget.setItem(masiv[-1], 2, QTableWidgetItem(vendor))
        self.ui2.tableWidget.setItem(masiv[-1], 3, QTableWidgetItem(vendor_code))

        self.ui2.lineEdit_5.clear()
        self.ui2.lineEdit_6.clear()
        self.ui2.boxVendor.clearEditText()
        self.ui2.lineEdit_248.clear()
        masiv.append(int(masiv[-1]) + 1)


        masiv_new[0].append(manuf)
        masiv_new[1].append(manuf_pn)
        masiv_new[2].append(vendor)
        masiv_new[3].append(vendor_code)

    def add_to_db(self):

        part_num = self.ui2.lineEdit_250.text()
        part_type = self.ui2.boxStatus_50.currentText()
        value = self.ui2.lineEdit_251.text()
        description = self.ui2.lineEdit_252.text()
        schematic_part = self.ui2.comboBox_67.currentText()
        pcb_footprint = self.ui2.comboBox_70.currentText()
        rohs = self.ui2.boxStatus_53.currentText()
        status = self.ui2.boxStatus_49.currentText()
        datasheet = self.ui2.comboBox_75.currentText()
        notes = self.ui2.lineEdit_258.text()
        create_date = self.ui2.label_14.text()
        rewiew_date = self.ui2.label_19.text()
        updaye_date = self.ui2.label_17.text()
        m_type = self.ui2.boxStatus_35.currentText()
        t_min = self.ui2.lineEdit_218.text()
        t_max = self.ui2.lineEdit_232.text()
        project_num = self.ui2.lineEdit_259.text()
        height = self.ui2.lineEdit_236.text()
        automative_st = self.ui2.boxStatus_54.currentText()
        manufacure = self.ui2.lineEdit_5.text()
        man_pn = self.ui2.lineEdit_6.text()
        vendor = self.ui2.boxVendor.currentText()
        vendor_code = self.ui2.lineEdit_248.text()

        vcoil = self.ui2.lineEdit_254.text()
        icoil = self.ui2.lineEdit_255.text()
        vsw_dc = self.ui2.lineEdit_256.text()
        vsw_ac = self.ui2.lineEdit_257.text()
        isw_dc = self.ui2.lineEdit_274.text()
        isw_ac = self.ui2.lineEdit_285.text()
        cont_form = self.ui2.lineEdit_287.text()
        lxw = self.ui2.lineEdit_239.text()
        connection = connect_to_db.getConnectiot()
        mycursor = connection.cursor()
        sql = "INSERT INTO test_relay (ektospn, part_type, value, description, schematic_part1, pcb_footprint1, rohs," \
              "status, datasheet, notes, create1, reviewed, update1, m_type, tmin, tmax, project_number, height, " \
              "automotivest, vcoil, icoil, vsw_dc, vsw_ac, isw_dc, isw_ac, contact_form, lxw) VALUES " \
              "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s)"
        val = (part_num, part_type, value, description, schematic_part, pcb_footprint,
               rohs, status, datasheet, notes, create_date, rewiew_date, updaye_date, m_type, t_min,
               t_max, project_num, height, automative_st, vcoil, icoil, vsw_dc, vsw_ac, isw_dc, isw_ac, cont_form, lxw)
        mycursor.execute(sql, val)



        todell = [0,1,2,3,4,5,6,7,8,9]
        for i in todell:
            print(i)
            sql1 = "INSERT INTO test_vendor (ektospn, manufacture, manufacture_pn, datasheet, vendor, vendor_code, " \
                   "create1, revie, update1, notes) VALUES " \
                  "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val1 = (part_num, masiv_new[0][i], masiv_new[1][i], datasheet, masiv_new[2][i], masiv_new[3][i], create_date, rewiew_date, updaye_date, notes)
            mycursor.execute(sql1, val1)
            if i == len(masiv_new[0])-1:
                break
        print(masiv_new)





        # __________________________________________________________________
        #
        # sql = "INSERT INTO ektos_2019_inductor (Part_Number, Part_Type, Value1, Description, Schematic_Part, " \
        #       "PCB_Footprint, ROHS, Status1, Datasheet, Image, Notes, Part_Class, Create_Date, Review_Date, Update_Date," \
        #       "M_Type, Tmin, Tmax, Height, AutomotiveStandard, RmsCurrent, SaturationCurrent, DcresistanceMax, Size) VALUES " \
        #       "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
        #       "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
        #       "%s, %s, %s, %s)"
        # val = (part_num, part_type, value, description, schematic_part, pcb_footprint,
        #        rohs, status, datasheet, image, notes, part_class, create_date, rewiew_date, updaye_date, m_type, t_min,
        #        t_max, height, automativ_standart, rms_current, saturation_current, dcresistance_max, siz





    def edit_value(self):
        if peremennaya == 'test_relay':
            self.ui2.tabWidget.setCurrentIndex(0)
            self.ui2.lineEdit_250.setText(masiv_for_edit_data[0])
            self.ui2.boxStatus_50.setCurrentText(masiv_for_edit_data[1])
            self.ui2.lineEdit_251.setText(masiv_for_edit_data[2])
            self.ui2.lineEdit_252.setText(masiv_for_edit_data[3])
            self.ui2.comboBox_67.setItemText(0, masiv_for_edit_data[4])
            self.ui2.comboBox_70.setItemText(0, masiv_for_edit_data[5])
            self.ui2.boxStatus_53.setCurrentText(masiv_for_edit_data[6])
            self.ui2.boxStatus_49.setCurrentText(masiv_for_edit_data[7])
            self.ui2.comboBox_75.setItemText(0, masiv_for_edit_data[8])
            self.ui2.lineEdit_258.setText(masiv_for_edit_data[9])
            self.ui2.label_14.setText(masiv_for_edit_data[10])
            self.ui2.label_19.setText(masiv_for_edit_data[11])
            self.ui2.label_17.setText(masiv_for_edit_data[12])
            self.ui2.boxStatus_35.setCurrentText(masiv_for_edit_data[13])
            self.ui2.lineEdit_218.setText(masiv_for_edit_data[14])
            self.ui2.lineEdit_232.setText(masiv_for_edit_data[15])
            self.ui2.lineEdit_259.setText(masiv_for_edit_data[16])
            self.ui2.lineEdit_236.setText(masiv_for_edit_data[17])
            self.ui2.boxStatus_54.setCurrentText(masiv_for_edit_data[18])

            self.ui2.lineEdit_254.setText(masiv_for_edit_data[19])
            self.ui2.lineEdit_255.setText(masiv_for_edit_data[20])
            self.ui2.lineEdit_256.setText(masiv_for_edit_data[21])
            self.ui2.lineEdit_257.setText(masiv_for_edit_data[22])
            self.ui2.lineEdit_274.setText(masiv_for_edit_data[23])
            self.ui2.lineEdit_285.setText(masiv_for_edit_data[24])
            self.ui2.lineEdit_287.setText(masiv_for_edit_data[25])
            self.ui2.lineEdit_239.setText(masiv_for_edit_data[26])

        # self.ui2.tabWidget.setCurrentIndex(0)
        # a = strftime("%Y%m%d", gmtime())  # дата и время
        # update_log = a+'('+log+')'
        # self.ui2.label_22.setText(str(update_log))
        # self.ui2.label_18.setEnabled(False)
        # mydb = mysql.connector.connect(
        #     host="mysql.ektos.net",
        #     user="dpe",
        #     passwd="dpe",
        #     database="dpe",
        #     charset='utf8',
        # )
        # mycursor = mydb.cursor()
        # a = 'Part_Number'
        # b = table1
        # c = found_item
        # fixed1 = ''.join(c.split(")"))
        # fixed2 = ''.join(fixed1.split("("))
        # fixed3 = ''.join(fixed2.split("'"))
        # fixed3 = ''.join(fixed3.split(","))
        # mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
        # counter = -1
        # for data12 in mycursor:
        #     b = data12
        #     for i in data12:
        #         counter += 1
        # self.ui2.lineEdit_1.setText(b[0])
        # self.ui2.lineEdit_2.setText(b[1])
        # self.ui2.lineEdit_3.setText(b[2])
        # self.ui2.lineEdit_4.setText(b[3])
        # self.ui2.lineEdit_5.setText(b[4])
        # self.ui2.lineEdit_6.setText(b[5])
        # self.ui2.boxStatus_31.setCurrentText(b[6])
        # self.ui2.boxStatus.setCurrentText(b[7])
        # self.ui2.lineEdit_9.setText(b[8])
        # self.ui2.lineEdit_10.setText(b[9])
        # self.ui2.lineEdit_11.setText(b[10])
        # self.ui2.lineEdit_12.setText(b[11])
        # self.ui2.lineEdit_13.setText(b[12])
        # self.ui2.lineEdit_14.setText(b[13])
        # self.ui2.lineEdit_15.setText(str(update_log))
        # self.ui2.lineEdit_15.setEnabled(False)
        # self.ui2.boxStatus_32.setCurrentText(b[15])
        # self.ui2.lineEdit_33.setText(b[16])
        # self.ui2.lineEdit_34.setText(b[17])
        # self.ui2.lineEdit_35.setText(b[18])
        # self.ui2.lineEdit_36.setText(b[19])
        # self.ui2.lineEdit_37.setText(b[20])
        # self.ui2.lineEdit_38.setText(b[21])
        # self.ui2.lineEdit_39.setText(b[22])
        # self.ui2.lineEdit_40.setText(b[23])
        # self.ui2.lineEdit_41.setText(b[24])
        # self.ui2.lineEdit_42.setText(b[25])
        # self.ui2.lineEdit_43.setText(b[26])
        # self.ui2.lineEdit_44.setText(b[27])
        # self.ui2.boxStatus_28.setCurrentText(b[28])
        # self.ui2.boxStatus_29.setCurrentText(b[29])
        # self.ui2.lineEdit_47.setText(b[30])
        # self.ui2.lineEdit_48.setText(b[31])
        # b = table2
        # mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
        # counter = -1
        # for data12 in mycursor:
        #     b = data12
        #     for i in data12:
        #         counter += 1
        # self.ui2.lineEdit_58.setText(b[4])  # vendor
        # self.ui2.lineEdit_64.setText(b[5])  # vendor code
        # self.ui2.lineEdit_45.setText(b[3])  # man part number
        # self.ui2.lineEdit_46.setText(b[2])  # manufacture
        #
        # self.ui2.lineEdit_13.setEnabled(False)
        # self.ui2.pushButton.clicked.connect(self.relayadd)

    def clear(self):
        self.ui2.label_2.clear()
        self.ui2.lineEdit_250.clear()
        self.ui2.lineEdit_251.clear()
        self.ui2.lineEdit_5.clear()
        self.ui2.lineEdit_6.clear()
        self.ui2.lineEdit_252.clear()
        self.ui2.comboBox_75.clear()
        self.ui2.label_17.clear()
        self.ui2.label_19.clear()
        self.ui2.lineEdit_254.clear()
        self.ui2.lineEdit_255.clear()
        self.ui2.lineEdit_256.clear()
        self.ui2.lineEdit_257.clear()
        self.ui2.lineEdit_274.clear()
        self.ui2.lineEdit_285.clear()
        self.ui2.lineEdit_287.clear()
        self.ui2.lineEdit_218.clear()
        self.ui2.lineEdit_232.clear()
        self.ui2.lineEdit_236.clear()
        self.ui2.lineEdit_259.clear()
        self.ui2.lineEdit_239.clear()
        self.ui2.lineEdit_265.clear()
        self.ui2.lineEdit_258.clear()
        self.ui2.boxVendor.clearEditText()
        self.ui2.lineEdit_248.clear()
        self.ui2.boxVendor_2.clearEditText()
        self.ui2.lineEdit_259.clear()
        self.ui2.tableWidget.clearContents()

    def datasheet_view(self):
        v = self.ui2.comboBox_75.currentText()
        # open("C:\\Cadence\\Company\\EKTOS_CIS\\", v)

        dir_name01 = glob.glob('C:\Cadence\Company\EKTOS_CIS\data\Datasheets/*.pdf')
        for some_number in dir_name01:
            if v in some_number:
                os.startfile(some_number)
        dir_name02 = glob.glob('C:\Cadence\Company\EKTOS_CIS\_NEW_PARTS_/**/*.pdf')
        for some_number2 in dir_name02:
            if v in some_number2:
                os.startfile(some_number2)

    def add_date(self):
        self.ui2.label_14.setText(update_log)

    def refresh(self):
        pcb_foot = []
        dir_name3 = glob.glob('C:\Cadence\Company\EKTOS_CIS\PCB_Footprints/**/*.dra')
        for some in dir_name3:
            x = some.replace("C:\\Cadence\\Company\\EKTOS_CIS\\PCB_Footprints\\", "")
            y = x.split('\\')[1]
            pcb_foot.append(y)
        dir_name4 = glob.glob('C:\Cadence\Company\EKTOS_CIS\PCB_Footprints/*.dra')
        for some in dir_name4:
            x = some.replace("C:\\Cadence\\Company\\EKTOS_CIS\\PCB_Footprints\\", "")
            pcb_foot.append(x)
        dir_name5 = glob.glob('C:\Cadence\Company\EKTOS_CIS\_NEW_PARTS_/**/*.dra')
        for some in dir_name5:
            x = some.replace("C:\\Cadence\\Company\\EKTOS_CIS\\_NEW_PARTS_\\", "")
            y = x.split('\\')[1]
            pcb_foot.append(y)
        for peremennaya in pcb_foot:
            MyApp3.ui2.comboBox_70.addItem(str(peremennaya))
            MyApp3.ui2.comboBox_71.addItem(str(peremennaya))
            MyApp3.ui2.comboBox_72.addItem(str(peremennaya))
            MyApp3.ui2.comboBox_73.addItem(str(peremennaya))
            MyApp3.ui2.comboBox_74.addItem(str(peremennaya))

        datasheets = []
        dir_name6 = glob.glob('C:\Cadence\Company\EKTOS_CIS\data\Datasheets/*.pdf')
        for some in dir_name6:
            x = some.replace("C:\\Cadence\\Company\\EKTOS_CIS\\data\\Datasheets\\", "")
            datasheets.append(x)
        dir_name7 = glob.glob('C:\Cadence\Company\EKTOS_CIS\_NEW_PARTS_/**/*.pdf')
        for some in dir_name7:
            x = some.replace("C:\\Cadence\\Company\\EKTOS_CIS\\_NEW_PARTS_\\", "")
            y = x.split('\\')[1]
            datasheets.append(y)
        for peremennaya in datasheets:
            MyApp3.ui2.comboBox_75.addItem(str(peremennaya))

    def other(self):
        a = strftime("%Y%m%d", gmtime())
        global update_log
        update_log = a + '(' + log + ')'
        self.ui2.lineEdit_271.setText(update_log)
        part_num = self.ui2.lineEdit_266.text()
        part_type = self.ui2.lineEdit_260.text()
        value = self.ui2.lineEdit_261.text()
        description = self.ui2.lineEdit_262.text()
        schematic_part = self.ui2.lineEdit_263.text()
        pcb_footprint = self.ui2.lineEdit_264.text()
        status = self.ui2.boxStatus_10.currentText()
        rohs = self.ui2.boxStatus_27.currentText()
        datasheet = self.ui2.lineEdit_267.text()
        image = self.ui2.lineEdit_268.text()
        notes = self.ui2.lineEdit_269.text()
        part_class = self.ui2.lineEdit_270.text()
        create_date = self.ui2.lineEdit_271.text()
        rewiew_date = self.ui2.lineEdit_272.text()
        updaye_date = self.ui2.lineEdit_273.text()
        m_type = self.ui2.boxStatus_30.currentText()
        t_min = self.ui2.lineEdit_275.text()
        t_max = self.ui2.lineEdit_276.text()
        height = self.ui2.lineEdit_277.text()
        automativ_standart = self.ui2.lineEdit_278.text()
        v_min = self.ui2.lineEdit_279.text()
        v_max = self.ui2.lineEdit_280.text()
        power = self.ui2.lineEdit_281.text()
        current = self.ui2.lineEdit_282.text()
        t_coeff = self.ui2.lineEdit_283.text()
        tol = self.ui2.lineEdit_284.text()
        vendor = self.ui2.lineEdit_216.text()
        vendor_code = self.ui2.lineEdit_217.text()
        manufacturer = self.ui2.lineEdit_230.text()
        man_part_number = self.ui2.lineEdit_231.text()

        create_user = myapp.logpas[0]
        if self.ui2.label_352.setEnabled == True:
            self.ui2.label_352.setText(create_user)

        mydb = mysql.connector.connect(
            host="mysql.ektos.net",
            user="dpe",
            passwd="dpe",
            database="dpe",
            charset='utf8',
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO ektos_2019_other (Part_Number, Part_Type, Value1, Description, Schematic_Part, " \
              "PCB_Footprint, ROHS, Status1, Datasheet, Image, Notes, Part_Class, Create_Date, Review_Date, Update_Date," \
              "M_Type, Tmin, Tmax, Height, AutomotiveStandard, Vmin, Vmax, Power1, Current, T_Coeff, Tol) VALUES " \
              "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s)"
        val = (part_num, part_type, value, description, schematic_part, pcb_footprint,
               rohs, status, datasheet, image, notes, part_class, create_date, rewiew_date, updaye_date, m_type, t_min,
               t_max, height, automativ_standart, v_min, v_max, power, current, t_coeff, tol)
        sql_vendor = "INSERT INTO 2019_ektos_cis_vendors (Part_Number, Manufacturer, Man_Part_Number, Datasheet, Vendor, " \
                     "Vendor_Code, Create_Date, Update_Date, Notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val_vendor = (part_num, manufacturer, man_part_number, datasheet, vendor, vendor_code, create_date, updaye_date, notes)

        if self.ui2.lineEdit_271.isEnabled() == False:
            try:
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_268.setText("Data recorded succssfully")
            except Exception:
                x = str(self.ui2.lineEdit_266.text())
                mycursor.execute("DELETE FROM ektos_2019_other WHERE Part_Number = '{}'".format(x))
                mycursor.execute("DELETE FROM 2019_ektos_cis_vendors WHERE Part_Number = '{}'".format(x))

                # self.ui2.label_265.setText("Duplicate entry for Part Number unique value")
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_268.setText("Data recorded succssfully")
            mydb.commit()
            self.clear_lines()

        if self.ui2.lineEdit_271.isEnabled() == True:
            try:

                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_268.setText("Data recorded succssfully")
                self.clear_lines()

            except Exception:
                self.ui2.label_268.setText("Duplicate entry for Part Number unique value")
            mydb.commit()
        self.ui2.groupBox_28.setEnabled(True)
        self.ui2.groupBox_29.setEnabled(True)

    def mecanical(self):
        a = strftime("%Y%m%d", gmtime())
        global update_log
        update_log = a + '(' + log + ')'
        self.ui2.lineEdit_207.setText(update_log)
        part_num = self.ui2.lineEdit_202.text()
        part_type = self.ui2.lineEdit_196.text()
        value = self.ui2.lineEdit_197.text()
        description = self.ui2.lineEdit_198.text()
        schematic_part = self.ui2.lineEdit_199.text()
        pcb_footprint = self.ui2.lineEdit_200.text()
        status = self.ui2.boxStatus_9.currentText()
        rohs = self.ui2.boxStatus_25.currentText()
        datasheet = self.ui2.lineEdit_203.text()
        image = self.ui2.lineEdit_204.text()
        notes = self.ui2.lineEdit_205.text()
        part_class = self.ui2.lineEdit_206.text()
        create_date = self.ui2.lineEdit_207.text()
        rewiew_date = self.ui2.lineEdit_208.text()
        updaye_date = self.ui2.lineEdit_209.text()
        m_type = self.ui2.boxStatus_26.currentText()
        t_min = self.ui2.lineEdit_211.text()
        t_max = self.ui2.lineEdit_212.text()
        height = self.ui2.lineEdit_213.text()
        automativ_standart = self.ui2.lineEdit_214.text()
        size = self.ui2.lineEdit_215.text()
        vendor = self.ui2.lineEdit_216.text()
        vendor_code = self.ui2.lineEdit_217.text()
        manufacturer = self.ui2.lineEdit_228.text()
        man_part_number = self.ui2.lineEdit_229.text()

        create_user = myapp.logpas[0]
        if self.ui2.label_276.setEnabled == True:
            self.ui2.label_276.setText(create_user)

        mydb = mysql.connector.connect(
            host="mysql.ektos.net",
            user="dpe",
            passwd="dpe",
            database="dpe",
            charset='utf8',
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO ektos_2019_mechanical (Part_Number, Part_Type, Value1, Description, Schematic_Part, " \
              "PCB_Footprint, ROHS, Status1, Datasheet, Image, Notes, Part_Class, Create_Date, Review_Date, Update_Date," \
              "M_Type, Tmin, Tmax, Height, AutomotiveStandard, Size) VALUES " \
              "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s)"
        val = (part_num, part_type, value, description, schematic_part, pcb_footprint,
               rohs, status, datasheet, image, notes, part_class, create_date, rewiew_date, updaye_date, m_type, t_min,
               t_max, height, automativ_standart, size)
        sql_vendor = "INSERT INTO 2019_ektos_cis_vendors (Part_Number, Manufacturer, Man_Part_Number, Datasheet, Vendor, " \
                     "Vendor_Code, Create_Date, Update_Date, Notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val_vendor = (part_num, manufacturer, man_part_number, datasheet, vendor, vendor_code, create_date, updaye_date, notes)

        if self.ui2.lineEdit_207.isEnabled() == False:
            try:
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_267.setText("Data recorded succssfully")
            except Exception:
                x = str(self.ui2.lineEdit_202.text())
                mycursor.execute("DELETE FROM ektos_2019_mechanical WHERE Part_Number = '{}'".format(x))
                mycursor.execute("DELETE FROM 2019_ektos_cis_vendors WHERE Part_Number = '{}'".format(x))
                # self.ui2.label_265.setText("Duplicate entry for Part Number unique value")
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_267.setText("Data recorded succssfully")
            mydb.commit()
            self.clear_lines()

        if self.ui2.lineEdit_207.isEnabled() == True:
            try:
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_267.setText("Data recorded succssfully")
                self.clear_lines()
            except Exception:
                self.ui2.label_267.setText("Duplicate entry for Part Number unique value")
            mydb.commit()
        self.ui2.groupBox_22.setEnabled(True)
        self.ui2.groupBox_23.setEnabled(True)

    def integrated_circuit(self):
        a = strftime("%Y%m%d", gmtime())
        global update_log
        update_log = a + '(' + log + ')'
        self.ui2.lineEdit_299.setText(update_log)
        part_num = self.ui2.lineEdit_294.text()
        part_type = self.ui2.lineEdit_192.text()
        value = self.ui2.lineEdit_193.text()
        description = self.ui2.lineEdit_194.text()
        schematic_part = self.ui2.lineEdit_291.text()
        pcb_footprint = self.ui2.lineEdit_292.text()
        status = self.ui2.boxStatus_8.currentText()
        rohs = self.ui2.boxStatus_23.currentText()
        datasheet = self.ui2.lineEdit_295.text()
        image = self.ui2.lineEdit_296.text()
        notes = self.ui2.lineEdit_297.text()
        part_class = self.ui2.lineEdit_298.text()
        create_date = self.ui2.lineEdit_299.text()
        rewiew_date = self.ui2.lineEdit_300.text()
        updaye_date = self.ui2.lineEdit_301.text()
        m_type = self.ui2.boxStatus_24.currentText()
        t_min = self.ui2.lineEdit_303.text()
        t_max = self.ui2.lineEdit_304.text()
        height = self.ui2.lineEdit_305.text()
        automativ_standart = self.ui2.lineEdit_306.text()
        v_min = self.ui2.lineEdit_307.text()
        v_max = self.ui2.lineEdit_308.text()
        power = self.ui2.lineEdit_309.text()
        current = self.ui2.lineEdit_310.text()
        vendor = self.ui2.lineEdit_191.text()
        vendor_code = self.ui2.lineEdit_195.text()
        manufacturer = self.ui2.lineEdit_226.text()
        man_part_number = self.ui2.lineEdit_227.text()

        create_user = myapp.logpas[0]
        if self.ui2.label_386.setEnabled == True:
            self.ui2.label_386.setText(create_user)

        mydb = mysql.connector.connect(
            host="mysql.ektos.net",
            user="dpe",
            passwd="dpe",
            database="dpe",
            charset='utf8',
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO ektos_2019_integratedcircuit (Part_Number, Part_Type, Value1, Description, Schematic_Part, " \
              "PCB_Footprint, ROHS, Status1, Datasheet, Image, Notes, Part_Class, Create_Date, Review_Date, Update_Date," \
              "M_Type, Tmin, Tmax, Height, AutomotiveStandard, Vmin, Vmax, Power, Current) VALUES " \
              "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s)"
        val = (part_num, part_type, value, description, schematic_part, pcb_footprint,
               rohs, status, datasheet, image, notes, part_class, create_date, rewiew_date, updaye_date, m_type, t_min,
               t_max, height, automativ_standart, v_min, v_max, power, current)
        sql_vendor = "INSERT INTO 2019_ektos_cis_vendors (Part_Number, Manufacturer, Man_Part_Number, Datasheet, Vendor, " \
                     "Vendor_Code, Create_Date, Update_Date, Notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val_vendor = (part_num, manufacturer, man_part_number, datasheet, vendor, vendor_code, create_date, updaye_date, notes)

        if self.ui2.lineEdit_299.isEnabled() == False:
            try:
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_266.setText("Data recorded succssfully")
            except Exception:
                x = str(self.ui2.lineEdit_294.text())
                mycursor.execute("DELETE FROM ektos_2019_integratedcircuit WHERE Part_Number = '{}'".format(x))
                mycursor.execute("DELETE FROM 2019_ektos_cis_vendors WHERE Part_Number = '{}'".format(x))
                # self.ui2.label_265.setText("Duplicate entry for Part Number unique value")
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_266.setText("Data recorded succssfully")
            mydb.commit()
            self.clear_lines()

        if self.ui2.lineEdit_299.isEnabled() == True:
            try:
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_266.setText("Data recorded succssfully")
                self.clear_lines()
            except Exception:
                self.ui2.label_266.setText("Duplicate entry for Part Number unique value")
            mydb.commit()
        self.ui2.groupBox_31.setEnabled(True)
        self.ui2.groupBox_32.setEnabled(True)

    def capasitor(self):
        a = strftime("%Y%m%d", gmtime())
        global update_log
        update_log = a + '(' + log + ')'
        self.ui2.lineEdit_175.setText(update_log)
        part_num = self.ui2.lineEdit_170.text()
        part_type = self.ui2.lineEdit_164.text()
        value = self.ui2.lineEdit_165.text()
        description = self.ui2.lineEdit_166.text()
        schematic_part = self.ui2.lineEdit_167.text()
        pcb_footprint = self.ui2.lineEdit_168.text()
        status = self.ui2.boxStatus_7.currentText()
        rohs = self.ui2.boxStatus_21.currentText()
        datasheet = self.ui2.lineEdit_171.text()
        image = self.ui2.lineEdit_172.text()
        notes = self.ui2.lineEdit_173.text()
        part_class = self.ui2.lineEdit_174.text()
        create_date = self.ui2.lineEdit_175.text()
        rewiew_date = self.ui2.lineEdit_176.text()
        updaye_date = self.ui2.lineEdit_177.text()
        m_type = self.ui2.boxStatus_22.currentText()
        t_min = self.ui2.lineEdit_179.text()
        t_max = self.ui2.lineEdit_180.text()
        height = self.ui2.lineEdit_181.text()
        automativ_standart = self.ui2.lineEdit_182.text()
        rated_voltage = self.ui2.lineEdit_183.text()
        dielectric = self.ui2.lineEdit_184.text()
        leakage_current = self.ui2.lineEdit_185.text()
        endurance = self.ui2.lineEdit_186.text()
        ripple_current_100kHz = self.ui2.lineEdit_187.text()
        impedance_100kHz = self.ui2.lineEdit_188.text()
        size_code = self.ui2.lineEdit_189.text()
        size = self.ui2.lineEdit_190.text()
        vendor = self.ui2.lineEdit_191.text()
        vendor_code = self.ui2.lineEdit_195.text()
        manufacturer = self.ui2.lineEdit_224.text()
        man_part_number = self.ui2.lineEdit_225.text()

        create_user = myapp.logpas[0]
        if self.ui2.label_238.setEnabled == True:
            self.ui2.label_238.setText(create_user)

        mydb = mysql.connector.connect(
            host="mysql.ektos.net",
            user="dpe",
            passwd="dpe",
            database="dpe",
            charset='utf8',
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO ektos_2019_capacitor (Part_Number, Part_Type, Value1, Description, Schematic_Part, " \
              "PCB_Footprint, ROHS, Status1, Datasheet, Image, Notes, Part_Class, Create_Date, Review_Date, Update_Date," \
              "M_Type, Tmin, Tmax, Height, AutomotiveStandard, RatedVoltage, Dielectric, LeakageCurrent, Endurance," \
              "RippleCurrent100kHz, Impedance100kHz, SizeCode, Size) VALUES " \
              "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (part_num, part_type, value, description, schematic_part, pcb_footprint,
               rohs, status, datasheet, image, notes, part_class, create_date, rewiew_date, updaye_date, m_type, t_min,
               t_max, height, automativ_standart, rated_voltage, dielectric, leakage_current, endurance, ripple_current_100kHz,
               impedance_100kHz, size_code, size)
        sql_vendor = "INSERT INTO 2019_ektos_cis_vendors (Part_Number, Manufacturer, Man_Part_Number, Datasheet, Vendor, " \
                     "Vendor_Code, Create_Date, Update_Date, Notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val_vendor = (part_num, manufacturer, man_part_number, datasheet, vendor, vendor_code, create_date, updaye_date, notes)

        if self.ui2.lineEdit_175.isEnabled() == False:
            try:
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_265.setText("Data recorded succssfully")
            except Exception:
                x = str(self.ui2.lineEdit_170.text())
                mycursor.execute("DELETE FROM ektos_2019_capacitor WHERE Part_Number = '{}'".format(x))
                mycursor.execute("DELETE FROM 2019_ektos_cis_vendors WHERE Part_Number = '{}'".format(x))

                # self.ui2.label_265.setText("Duplicate entry for Part Number unique value")
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_265.setText("Data recorded succssfully")

            mydb.commit()
            self.clear_lines()

        if self.ui2.lineEdit_175.isEnabled() == True:
            try:
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_265.setText("Data recorded succssfully")
                self.clear_lines()
            except Exception:
                self.ui2.label_265.setText("Duplicate entry for Part Number unique value")
            mydb.commit()
        self.ui2.groupBox_19.setEnabled(True)
        self.ui2.groupBox_20.setEnabled(True)



    def clear_lines(self):
        edit_masiv = [self.ui2.lineEdit_1, self.ui2.lineEdit_2, self.ui2.lineEdit_3, self.ui2.lineEdit_4,
                      self.ui2.lineEdit_5, self.ui2.lineEdit_6, self.ui2.lineEdit_9, self.ui2.lineEdit_10,
                      self.ui2.lineEdit_11, self.ui2.lineEdit_12, self.ui2.lineEdit_13, self.ui2.lineEdit_14,
                      self.ui2.lineEdit_15,self.ui2.lineEdit_18, self.ui2.lineEdit_19, self.ui2.lineEdit_20,
                      self.ui2.lineEdit_21, self.ui2.lineEdit_22,self.ui2.lineEdit_24, self.ui2.lineEdit_25,
                      self.ui2.lineEdit_26, self.ui2.lineEdit_27, self.ui2.lineEdit_28, self.ui2.lineEdit_29,
                      self.ui2.lineEdit_30, self.ui2.lineEdit_31,self.ui2.lineEdit_33, self.ui2.lineEdit_34,
                      self.ui2.lineEdit_35, self.ui2.lineEdit_36, self.ui2.lineEdit_37, self.ui2.lineEdit_38,
                      self.ui2.lineEdit_39, self.ui2.lineEdit_40, self.ui2.lineEdit_41, self.ui2.lineEdit_42,
                      self.ui2.lineEdit_43, self.ui2.lineEdit_44,self.ui2.lineEdit_47, self.ui2.lineEdit_48,
                      self.ui2.lineEdit_49, self.ui2.lineEdit_50, self.ui2.lineEdit_51, self.ui2.lineEdit_52,
                      self.ui2.lineEdit_53, self.ui2.lineEdit_54, self.ui2.lineEdit_55, self.ui2.lineEdit_56,
                      self.ui2.lineEdit_57, self.ui2.lineEdit_58, self.ui2.lineEdit_59, self.ui2.lineEdit_60,
                      self.ui2.lineEdit_61, self.ui2.lineEdit_62, self.ui2.lineEdit_63, self.ui2.lineEdit_64,
                      self.ui2.lineEdit_65, self.ui2.lineEdit_66, self.ui2.lineEdit_67, self.ui2.lineEdit_68,
                      self.ui2.lineEdit_69, self.ui2.lineEdit_70, self.ui2.lineEdit_71, self.ui2.lineEdit_72,
                      self.ui2.lineEdit_73, self.ui2.lineEdit_74, self.ui2.lineEdit_75, self.ui2.lineEdit_76,
                      self.ui2.lineEdit_77, self.ui2.lineEdit_78, self.ui2.lineEdit_79, self.ui2.lineEdit_80,
                      self.ui2.lineEdit_81, self.ui2.lineEdit_82, self.ui2.lineEdit_83, self.ui2.lineEdit_84,
                      self.ui2.lineEdit_85, self.ui2.lineEdit_86, self.ui2.lineEdit_87, self.ui2.lineEdit_88,
                      self.ui2.lineEdit_89, self.ui2.lineEdit_90, self.ui2.lineEdit_91, self.ui2.lineEdit_92,
                      self.ui2.lineEdit_93, self.ui2.lineEdit_94, self.ui2.lineEdit_95, self.ui2.lineEdit_96,
                      self.ui2.lineEdit_97, self.ui2.lineEdit_98, self.ui2.lineEdit_99, self.ui2.lineEdit_100,
                      self.ui2.lineEdit_101, self.ui2.lineEdit_102, self.ui2.lineEdit_103, self.ui2.lineEdit_104,
                      self.ui2.lineEdit_105, self.ui2.lineEdit_106, self.ui2.lineEdit_107, self.ui2.lineEdit_108,
                      self.ui2.lineEdit_109, self.ui2.lineEdit_110, self.ui2.lineEdit_111, self.ui2.lineEdit_112,
                      self.ui2.lineEdit_113, self.ui2.lineEdit_114, self.ui2.lineEdit_115, self.ui2.lineEdit_116,
                      self.ui2.lineEdit_117, self.ui2.lineEdit_118, self.ui2.lineEdit_119, self.ui2.lineEdit_120,
                      self.ui2.lineEdit_121, self.ui2.lineEdit_122, self.ui2.lineEdit_123, self.ui2.lineEdit_124,
                      self.ui2.lineEdit_125, self.ui2.lineEdit_126, self.ui2.lineEdit_127, self.ui2.lineEdit_128,
                      self.ui2.lineEdit_130, self.ui2.lineEdit_131, self.ui2.lineEdit_132, self.ui2.lineEdit_133,
                      self.ui2.lineEdit_134, self.ui2.lineEdit_135, self.ui2.lineEdit_136, self.ui2.lineEdit_137,
                      self.ui2.lineEdit_138, self.ui2.lineEdit_139, self.ui2.lineEdit_140, self.ui2.lineEdit_141,
                      self.ui2.lineEdit_142, self.ui2.lineEdit_143, self.ui2.lineEdit_144, self.ui2.lineEdit_145,
                      self.ui2.lineEdit_146, self.ui2.lineEdit_147, self.ui2.lineEdit_148, self.ui2.lineEdit_149,
                      self.ui2.lineEdit_150, self.ui2.lineEdit_151, self.ui2.lineEdit_152, self.ui2.lineEdit_153,
                      self.ui2.lineEdit_155, self.ui2.lineEdit_156, self.ui2.lineEdit_157, self.ui2.lineEdit_158,
                      self.ui2.lineEdit_159, self.ui2.lineEdit_160, self.ui2.lineEdit_161, self.ui2.lineEdit_162,
                      self.ui2.lineEdit_163, self.ui2.lineEdit_164, self.ui2.lineEdit_165, self.ui2.lineEdit_166,
                      self.ui2.lineEdit_167, self.ui2.lineEdit_168, self.ui2.lineEdit_169, self.ui2.lineEdit_170,
                      self.ui2.lineEdit_171, self.ui2.lineEdit_172, self.ui2.lineEdit_173, self.ui2.lineEdit_174,
                      self.ui2.lineEdit_175, self.ui2.lineEdit_176, self.ui2.lineEdit_177, self.ui2.lineEdit_179,
                      self.ui2.lineEdit_180, self.ui2.lineEdit_181, self.ui2.lineEdit_182, self.ui2.lineEdit_183,
                      self.ui2.lineEdit_184, self.ui2.lineEdit_185, self.ui2.lineEdit_186, self.ui2.lineEdit_187,
                      self.ui2.lineEdit_188, self.ui2.lineEdit_189, self.ui2.lineEdit_190, self.ui2.lineEdit_191,
                      self.ui2.lineEdit_192, self.ui2.lineEdit_193, self.ui2.lineEdit_194, self.ui2.lineEdit_195,
                      self.ui2.lineEdit_196, self.ui2.lineEdit_197, self.ui2.lineEdit_198, self.ui2.lineEdit_199,
                      self.ui2.lineEdit_200, self.ui2.lineEdit_202, self.ui2.lineEdit_203, self.ui2.lineEdit_204,
                      self.ui2.lineEdit_205, self.ui2.lineEdit_206, self.ui2.lineEdit_207, self.ui2.lineEdit_208,
                      self.ui2.lineEdit_209, self.ui2.lineEdit_211, self.ui2.lineEdit_212, self.ui2.lineEdit_213,
                      self.ui2.lineEdit_214, self.ui2.lineEdit_215, self.ui2.lineEdit_216, self.ui2.lineEdit_217,
                      self.ui2.lineEdit_260, self.ui2.lineEdit_261, self.ui2.lineEdit_262, self.ui2.lineEdit_263,
                      self.ui2.lineEdit_264, self.ui2.lineEdit_266, self.ui2.lineEdit_267, self.ui2.lineEdit_268,
                      self.ui2.lineEdit_269, self.ui2.lineEdit_270, self.ui2.lineEdit_271, self.ui2.lineEdit_272,
                      self.ui2.lineEdit_273, self.ui2.lineEdit_275, self.ui2.lineEdit_276, self.ui2.lineEdit_45,
                      self.ui2.lineEdit_277, self.ui2.lineEdit_278, self.ui2.lineEdit_279, self.ui2.lineEdit_280,
                      self.ui2.lineEdit_281, self.ui2.lineEdit_282, self.ui2.lineEdit_283, self.ui2.lineEdit_284,
                      self.ui2.lineEdit_291, self.ui2.lineEdit_292, self.ui2.lineEdit_294, self.ui2.lineEdit_295,
                      self.ui2.lineEdit_296, self.ui2.lineEdit_297, self.ui2.lineEdit_298, self.ui2.lineEdit_299,
                      self.ui2.lineEdit_300, self.ui2.lineEdit_301, self.ui2.lineEdit_303, self.ui2.lineEdit_46,
                      self.ui2.lineEdit_304, self.ui2.lineEdit_305, self.ui2.lineEdit_306, self.ui2.lineEdit_307,
                      self.ui2.lineEdit_308, self.ui2.lineEdit_309, self.ui2.lineEdit_310, self.ui2.lineEdit_314,
                      self.ui2.lineEdit_315, self.ui2.lineEdit_316, self.ui2.lineEdit_317, self.ui2.lineEdit_178,
                      self.ui2.lineEdit_201, self.ui2.lineEdit_129, self.ui2.lineEdit_154, self.ui2.lineEdit_219,
                      self.ui2.lineEdit_210, self.ui2.lineEdit_221, self.ui2.lineEdit_220, self.ui2.lineEdit_223,
                      self.ui2.lineEdit_222, self.ui2.lineEdit_227, self.ui2.lineEdit_226, self.ui2.lineEdit_229,
                      self.ui2.lineEdit_228, self.ui2.lineEdit_231, self.ui2.lineEdit_230, self.ui2.lineEdit_225,
                      self.ui2.lineEdit_224]
        for i in range(0, 269):
            edit_masiv[i].clear()

    def inductor(self):
        a = strftime("%Y%m%d", gmtime())
        global update_log
        update_log = a + '(' + log + ')'
        self.ui2.lineEdit_151.setText(update_log)
        part_num = self.ui2.lineEdit_146.text()
        part_type = self.ui2.lineEdit_140.text()
        value = self.ui2.lineEdit_141.text()
        description = self.ui2.lineEdit_142.text()
        schematic_part = self.ui2.lineEdit_143.text()
        pcb_footprint = self.ui2.lineEdit_144.text()
        status = self.ui2.boxStatus_6.currentText()
        rohs = self.ui2.boxStatus_19.currentText()
        datasheet = self.ui2.lineEdit_147.text()
        image = self.ui2.lineEdit_148.text()
        notes = self.ui2.lineEdit_149.text()
        part_class = self.ui2.lineEdit_150.text()
        create_date = self.ui2.lineEdit_151.text()
        rewiew_date = self.ui2.lineEdit_152.text()
        updaye_date = self.ui2.lineEdit_153.text()
        m_type = self.ui2.boxStatus_20.currentText()
        t_min = self.ui2.lineEdit_155.text()
        t_max = self.ui2.lineEdit_156.text()
        height = self.ui2.lineEdit_157.text()
        automativ_standart = self.ui2.lineEdit_158.text()
        rms_current = self.ui2.lineEdit_159.text()
        saturation_current = self.ui2.lineEdit_160.text()
        dcresistance_max = self.ui2.lineEdit_161.text()
        size = self.ui2.lineEdit_162.text()
        vendor = self.ui2.lineEdit_163.text()
        vendor_code = self.ui2.lineEdit_169.text()
        manufacturer = self.ui2.lineEdit_222.text()
        man_part_number = self.ui2.lineEdit_223.text()

        create_user = myapp.logpas[0]
        if self.ui2.label_208.setEnabled == True:
            self.ui2.label_208.setText(create_user)

        mydb = mysql.connector.connect(
            host="mysql.ektos.net",
            user="dpe",
            passwd="dpe",
            database="dpe",
            charset='utf8',
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO ektos_2019_inductor (Part_Number, Part_Type, Value1, Description, Schematic_Part, " \
              "PCB_Footprint, ROHS, Status1, Datasheet, Image, Notes, Part_Class, Create_Date, Review_Date, Update_Date," \
              "M_Type, Tmin, Tmax, Height, AutomotiveStandard, RmsCurrent, SaturationCurrent, DcresistanceMax, Size) VALUES " \
              "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s)"
        val = (part_num, part_type, value, description, schematic_part, pcb_footprint,
               rohs, status, datasheet, image, notes, part_class, create_date, rewiew_date, updaye_date, m_type, t_min,
               t_max, height, automativ_standart, rms_current, saturation_current, dcresistance_max, size)
        sql_vendor = "INSERT INTO 2019_ektos_cis_vendors (Part_Number, Manufacturer, Man_Part_Number, Datasheet, Vendor, " \
                     "Vendor_Code, Create_Date, Update_Date, Notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val_vendor = (part_num, manufacturer, man_part_number, datasheet, vendor, vendor_code, create_date, updaye_date, notes)

        if self.ui2.lineEdit_151.isEnabled() == False:
            try:
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_264.setText("Data recorded succssfully")
            except Exception:
                x = str(self.ui2.lineEdit_146.text())
                mycursor.execute("DELETE FROM ektos_2019_diode WHERE Part_Number = '{}'".format(x))
                mycursor.execute("DELETE FROM 2019_ektos_cis_vendors WHERE Part_Number = '{}'".format(x))
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_264.setText("Data recorded succssfully")
            mydb.commit()
            self.clear_lines()

        if self.ui2.lineEdit_151.isEnabled() == True:
            try:
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_264.setText("Data recorded succssfully")
                self.clear_lines()
            except Exception:
                self.ui2.label_264.setText("Duplicate entry for Part Number unique value")
            mydb.commit()
        self.ui2.groupBox_16.setEnabled(True)
        self.ui2.groupBox_17.setEnabled(True)

    def diode(self):
        a = strftime("%Y%m%d", gmtime())
        global update_log
        update_log = a + '(' + log + ')'
        self.ui2.lineEdit_126.setText(update_log)
        part_num = self.ui2.lineEdit_121.text()
        part_type = self.ui2.lineEdit_115.text()
        value = self.ui2.lineEdit_116.text()
        description = self.ui2.lineEdit_117.text()
        schematic_part = self.ui2.lineEdit_118.text()
        pcb_footprint = self.ui2.lineEdit_119.text()
        status = self.ui2.boxStatus_4.currentText()
        rohs = self.ui2.boxStatus_11.currentText()
        datasheet = self.ui2.lineEdit_122.text()
        image = self.ui2.lineEdit_123.text()
        notes = self.ui2.lineEdit_124.text()
        part_class = self.ui2.lineEdit_125.text()
        create_date = self.ui2.lineEdit_126.text()
        rewiew_date = self.ui2.lineEdit_127.text()
        updaye_date = self.ui2.lineEdit_128.text()
        m_type = self.ui2.boxStatus_12.currentText()
        t_min = self.ui2.lineEdit_130.text()
        t_max = self.ui2.lineEdit_131.text()
        height = self.ui2.lineEdit_132.text()
        automativ_standart = self.ui2.lineEdit_133.text()
        reverse_vrrm_max = self.ui2.lineEdit_134.text()
        forward_current = self.ui2.lineEdit_135.text()
        forward_voltage_vf = self.ui2.lineEdit_136.text()
        reverse_recovery_time_max = self.ui2.lineEdit_137.text()
        forward_surge_current_max = self.ui2.lineEdit_138.text()
        vendor = self.ui2.lineEdit_139.text()
        vendor_code = self.ui2.lineEdit_145.text()
        manufacturer = self.ui2.lineEdit_220.text()
        man_part_number = self.ui2.lineEdit_221.text()

        create_user = myapp.logpas[0]
        if self.ui2.label_171.setEnabled == True:
            self.ui2.label_171.setText(create_user)

        mydb = mysql.connector.connect(
            host="mysql.ektos.net",
            user="dpe",
            passwd="dpe",
            database="dpe",
            charset='utf8',
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO ektos_2019_diode (Part_Number, Part_Type, Value1, Description, Schematic_Part, " \
              "PCB_Footprint, ROHS, Status1, Datasheet, Image, Notes, Part_Class, Create_Date, Review_Date, Update_Date," \
              "M_Type, Tmin, Tmax, Height, AutomotiveStandard, ReverseVrrmMax, ForwardCurrent, " \
              "ForwardVoltageVf, ReverseRecoveryTimeMax, ForwardSurgeCurrentMax) VALUES " \
              "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s)"
        val = (part_num, part_type, value, description, schematic_part, pcb_footprint,
               rohs, status, datasheet, image, notes, part_class, create_date, rewiew_date, updaye_date, m_type, t_min,
               t_max, height, automativ_standart, reverse_vrrm_max, forward_current, forward_voltage_vf,
               reverse_recovery_time_max, forward_surge_current_max)
        sql_vendor = "INSERT INTO 2019_ektos_cis_vendors (Part_Number, Manufacturer, Man_Part_Number, Datasheet, Vendor, " \
                     "Vendor_Code, Create_Date, Update_Date, Notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val_vendor = (part_num, manufacturer, man_part_number, datasheet, vendor, vendor_code, create_date, updaye_date, notes)

        if self.ui2.lineEdit_126.isEnabled() == False:
            try:
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_181.setText("Data recorded succssfully")
            except Exception:
                x = str(self.ui2.lineEdit_121.text())
                mycursor.execute("DELETE FROM ektos_2019_diode WHERE Part_Number = '{}'".format(x))
                mycursor.execute("DELETE FROM 2019_ektos_cis_vendors WHERE Part_Number = '{}'".format(x))
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_181.setText("Data recorded succssfully")
            mydb.commit()
            self.clear_lines()

        if self.ui2.lineEdit_126.isEnabled() == True:
            try:
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_181.setText("Data recorded succssfully")
                self.clear_lines()
            except Exception:
                self.ui2.label_181.setText("Duplicate entry for Part Number unique value")
            mydb.commit()
        self.ui2.groupBox_13.setEnabled(True)
        self.ui2.groupBox_14.setEnabled(True)


    def connector(self):
        a = strftime("%Y%m%d", gmtime())
        global update_log
        update_log = a + '(' + log + ')'
        self.ui2.lineEdit_97.setText(update_log)
        part_num = self.ui2.lineEdit_92.text()
        part_type = self.ui2.lineEdit_86.text()
        value = self.ui2.lineEdit_87.text()
        description = self.ui2.lineEdit_88.text()
        schematic_part = self.ui2.lineEdit_89.text()
        pcb_footprint = self.ui2.lineEdit_90.text()
        status = self.ui2.boxStatus_4.currentText()
        rohs = self.ui2.boxStatus_11.currentText()
        datasheet = self.ui2.lineEdit_93.text()
        image = self.ui2.lineEdit_94.text()
        notes = self.ui2.lineEdit_95.text()
        part_class = self.ui2.lineEdit_96.text()
        create_date = self.ui2.lineEdit_97.text()
        rewiew_date = self.ui2.lineEdit_98.text()
        updaye_date = self.ui2.lineEdit_99.text()
        m_type = self.ui2.boxStatus_12.currentText()
        t_min = self.ui2.lineEdit_101.text()
        t_max = self.ui2.lineEdit_102.text()
        height = self.ui2.lineEdit_103.text()
        automativ_standart = self.ui2.lineEdit_104.text()
        pitch_spacing = self.ui2.lineEdit_105.text()
        contacts_qty = self.ui2.lineEdit_106.text()
        gender = self.ui2.lineEdit_107.text()
        rows_qty = self.ui2.lineEdit_108.text()
        max_voltage_dc = self.ui2.lineEdit_109.text()
        max_voltage_ac = self.ui2.lineEdit_110.text()
        max_current_dc = self.ui2.lineEdit_111.text()
        max_current_ac = self.ui2.lineEdit_112.text()
        frequency_max = self.ui2.lineEdit_113.text()
        vendor = self.ui2.lineEdit_114.text()
        vendor_code = self.ui2.lineEdit_120.text()
        manufacturer = self.ui2.lineEdit_219.text()
        man_part_number = self.ui2.lineEdit_210.text()

        create_user = myapp.logpas[0]
        if self.ui2.label_136.setEnabled == True:
            self.ui2.label_136.setText(create_user)

        mydb = mysql.connector.connect(
            host="mysql.ektos.net",
            user="dpe",
            passwd="dpe",
            database="dpe",
            charset='utf8',
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO ektos_2019_connector (Part_Number, Part_Type, Value1, Description, Schematic_Part, " \
              "PCB_Footprint, ROHS, Status1, Datasheet, Image, Notes, Part_Class, Create_Date, Review_Date, Update_Date," \
              "M_Type, Tmin, Tmax, Height, AutomotiveStandard, PitchSpacing, ContactsQty, Gender, RowsQty, " \
              "MaxVoltageDC, MaxVoltageAC, MaxCurrentDC, MaxCurrentAC, FrequencyMax) VALUES " \
              "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (part_num, part_type, value, description, schematic_part, pcb_footprint,
               rohs, status, datasheet, image, notes, part_class, create_date, rewiew_date, updaye_date, m_type, t_min,
               t_max, height, automativ_standart, pitch_spacing, contacts_qty, gender, rows_qty, max_voltage_dc,
               max_voltage_ac, max_current_dc, max_current_ac, frequency_max)
        sql_vendor = "INSERT INTO 2019_ektos_cis_vendors (Part_Number, Manufacturer, Man_Part_Number, Datasheet, Vendor, " \
                     "Vendor_Code, Create_Date, Update_Date, Notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val_vendor = (part_num, manufacturer, man_part_number, datasheet, vendor, vendor_code, create_date, updaye_date, notes)

        if self.ui2.lineEdit_97.isEnabled() == False:
            try:
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_180.setText("Data recorded succssfully")
            except Exception:
                x = str(self.ui2.lineEdit_92.text())
                mycursor.execute("DELETE FROM ektos_2019_connector WHERE Part_Number = '{}'".format(x))
                mycursor.execute("DELETE FROM 2019_ektos_cis_vendors WHERE Part_Number = '{}'".format(x))
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_180.setText("Data recorded succssfully")
            mydb.commit()
            self.clear_lines()

        if self.ui2.lineEdit_97.isEnabled() == True:
            try:
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_180.setText("Data recorded succssfully")
                self.clear_lines()
            except Exception:
                self.ui2.label_180.setText("Duplicate entry for Part Number unique value")
            mydb.commit()
        self.ui2.groupBox_11.setEnabled(True)
        self.ui2.groupBox_10.setEnabled(True)
        self.ui2.groupBox_26.setEnabled(True)


    def transistor(self):
        a = strftime("%Y%m%d", gmtime())
        global update_log
        update_log = a + '(' + log + ')'
        self.ui2.lineEdit_70.setText(update_log)
        part_num = self.ui2.lineEdit_65.text()
        part_type = self.ui2.lineEdit_59.text()
        value = self.ui2.lineEdit_60.text()
        description = self.ui2.lineEdit_61.text()
        schematic_part = self.ui2.lineEdit_62.text()
        pcb_footprint = self.ui2.lineEdit_63.text()
        status = self.ui2.boxStatus_3.currentText()
        rohs = self.ui2.boxStatus_14.currentText()
        datasheet = self.ui2.lineEdit_66.text()
        image = self.ui2.lineEdit_67.text()
        notes = self.ui2.lineEdit_68.text()
        part_class = self.ui2.lineEdit_69.text()
        create_date = self.ui2.lineEdit_70.text()
        rewiew_date = self.ui2.lineEdit_71.text()
        updaye_date = self.ui2.lineEdit_72.text()
        m_type = self.ui2.boxStatus_13.currentText()
        t_min = self.ui2.lineEdit_74.text()
        t_max = self.ui2.lineEdit_75.text()
        height = self.ui2.lineEdit_76.text()
        automativ_standart = self.ui2.lineEdit_77.text()
        power = self.ui2.lineEdit_78.text()
        collector_drain_current = self.ui2.lineEdit_79.text()
        vceo_vgs = self.ui2.lineEdit_80.text()
        fmax = self.ui2.lineEdit_81.text()
        rdson = self.ui2.lineEdit_82.text()
        thresholdvgs = self.ui2.lineEdit_83.text()
        polarity = self.ui2.lineEdit_91.text()
        vendor = self.ui2.lineEdit_84.text()
        vendor_code = self.ui2.lineEdit_100.text()
        manufacturer = self.ui2.lineEdit_154.text()
        man_part_number = self.ui2.lineEdit_129.text()

        create_user = myapp.logpas[0]
        if self.ui2.label_103.setEnabled == True:
            self.ui2.label_103.setText(create_user)

        mydb = mysql.connector.connect(
            host="mysql.ektos.net",
            user="dpe",
            passwd="dpe",
            database="dpe",
            charset='utf8',
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO ektos_2019_transistor (Part_Number, Part_Type, Value1, Description, Schematic_Part, " \
              "PCB_Footprint, ROHS, Status1, Datasheet, Image, Notes, Part_Class, Create_Date, Review_Date, Update_Date," \
              "M_Type, Tmin, Tmax, Height, AutomotiveStandard, Power1, CollectorDrainCurrent, VceoVgs, " \
              "Fmax, Rdson, ThresholdVgs, Polarity) VALUES " \
              "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s)"
        val = (part_num, part_type, value, description, schematic_part, pcb_footprint,
               rohs, status, datasheet, image, notes, part_class, create_date, rewiew_date, updaye_date, m_type, t_min,
               t_max, height, automativ_standart, power, collector_drain_current, vceo_vgs, fmax,
               rdson, thresholdvgs, polarity)
        sql_vendor = "INSERT INTO 2019_ektos_cis_vendors (Part_Number, Manufacturer, Man_Part_Number, Datasheet, Vendor, " \
                     "Vendor_Code, Create_Date, Update_Date, Notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val_vendor = (part_num, manufacturer, man_part_number, datasheet, vendor, vendor_code, create_date, updaye_date, notes)

        self.ui2.label_179.setText("Data recorded succssfully")
        if self.ui2.lineEdit_70.isEnabled() == False:
            try:
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_179.setText("Data recorded succssfully")
            except Exception:
                x = str(self.ui2.lineEdit_65.text())
                mycursor.execute("DELETE FROM ektos_2019_transistor WHERE Part_Number = '{}'".format(x))
                mycursor.execute("DELETE FROM 2019_ektos_cis_vendors WHERE Part_Number = '{}'".format(x))
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_179.setText("Data recorded succssfully")
            mydb.commit()
            self.clear_lines()

        if self.ui2.lineEdit_70.isEnabled() == True:
            try:
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_179.setText("Data recorded succssfully")
                self.clear_lines()
            except Exception:
                self.ui2.label_179.setText("Duplicate entry for Part Number unique value")
            mydb.commit()
        self.ui2.groupBox_7.setEnabled(True)
        self.ui2.groupBox_8.setEnabled(True)

    def resistor(self):
        a = strftime("%Y%m%d", gmtime())
        global update_log
        update_log = a + '(' + log + ')'
        self.ui2.lineEdit_29.setText(update_log)
        part_num = self.ui2.lineEdit_24.text()
        part_type = self.ui2.lineEdit_18.text()
        value = self.ui2.lineEdit_19.text()
        description = self.ui2.lineEdit_20.text()
        schematic_part = self.ui2.lineEdit_21.text()
        pcb_footprint = self.ui2.lineEdit_22.text()
        status = self.ui2.boxStatus_2.currentText()
        rohs = self.ui2.boxStatus_15.currentText()
        datasheet = self.ui2.lineEdit_25.text()
        image = self.ui2.lineEdit_26.text()
        notes = self.ui2.lineEdit_27.text()
        part_class = self.ui2.lineEdit_28.text()
        create_date = self.ui2.lineEdit_29.text()
        rewiew_date = self.ui2.lineEdit_30.text()
        updaye_date = self.ui2.lineEdit_31.text()
        m_type = self.ui2.boxStatus_16.currentText()
        t_min = self.ui2.lineEdit_33.text()
        t_max = self.ui2.lineEdit_34.text()
        height = self.ui2.lineEdit_35.text()
        automativ_standart = self.ui2.lineEdit_52.text()
        imax = self.ui2.lineEdit_53.text()
        vmax = self.ui2.lineEdit_54.text()
        power = self.ui2.lineEdit_55.text()
        t_coeff = self.ui2.lineEdit_56.text()
        tol = self.ui2.lineEdit_57.text()
        vendor = self.ui2.lineEdit_73.text()
        vendor_code = self.ui2.lineEdit_85.text()
        man_part_number = self.ui2.lineEdit_178.text()
        manufacturer = self.ui2.lineEdit_201.text()

        create_user = myapp.logpas[0]
        if self.ui2.label_65.setEnabled == True:
            self.ui2.label_65.setText(create_user)

        mydb = mysql.connector.connect(
            host="mysql.ektos.net",
            user="dpe",
            passwd="dpe",
            database="dpe",
            charset='utf8',
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO ektos_2019_resistor (Part_Number, Part_Type, Value1, Description, Schematic_Part, " \
              "PCB_Footprint, ROHS, Status1, Datasheet, Image, Notes, Part_Class, Create_Date, Review_Date, Update_Date," \
              "M_Type, Tmin, Tmax, Height, AutomotiveStandard, Imax, Vmax, Power1, T_Coeff, " \
              "Tol) VALUES " \
              "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s)"
        val = (part_num, part_type, value, description, schematic_part, pcb_footprint,
               rohs, status, datasheet, image, notes, part_class, create_date, rewiew_date, updaye_date, m_type, t_min,
               t_max, height, automativ_standart, imax, vmax, power, t_coeff, tol)
        sql_vendor = "INSERT INTO 2019_ektos_cis_vendors (Part_Number, Manufacturer, Man_Part_Number, Datasheet, Vendor, " \
                     "Vendor_Code, Create_Date, Update_Date, Notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val_vendor = (part_num, manufacturer, man_part_number, datasheet, vendor, vendor_code, create_date, updaye_date, notes)


        if self.ui2.lineEdit_29.isEnabled() == False:
            try:
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_178.setText("Data recorded succssfully")
            except Exception:
                x = str(self.ui2.lineEdit_24.text())
                mycursor.execute("DELETE FROM ektos_2019_resistor WHERE Part_Number = '{}'".format(x))
                mycursor.execute("DELETE FROM 2019_ektos_cis_vendors WHERE Part_Number = '{}'".format(x))

                # self.ui2.label_265.setText("Duplicate entry for Part Number unique value")
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_178.setText("Data recorded succssfully")
            mydb.commit()
            self.clear_lines()

        if self.ui2.lineEdit_29.isEnabled() == True:
            try:
                mycursor.execute(sql, val)
                mycursor.execute(sql_vendor, val_vendor)
                self.ui2.label_178.setText("Data recorded succssfully")
                self.clear_lines()
            except Exception:
                self.ui2.label_178.setText("Duplicate entry for Part Number unique value")
            mydb.commit()
        self.ui2.groupBox_2.setEnabled(True)
        self.ui2.groupBox_4.setEnabled(True)

    # def first_serch(self):
    #     global search1
    #     search1 = self.ui2.boxSearch1.currentText()
    #     self.ui2.boxSearch1.activated(self.prinprintprint)
    #     self.ui2.editSearch1.setText(search1)
    #     self.ui2.boxSearch2.setEnabled(True)
    #     self.ui2.editSearch2.setEnabled(False)
    #     self.ui2.pushButton_12.setEnabled(True)
    #
    #     mydb = mysql.connector.connect(
    #         host="mysql.ektos.net",
    #         user="dpe",
    #         passwd="dpe",
    #         database="dpe",
    #         charset='utf8',
    #     )
    #     mycursor = mydb.cursor()
    #     global table1
    #     global table2
    #     table = search1
    #
    #     if table == 'Relay':
    #         table1 = 'ektos_2019_relay'
    #         table2 = '2019_ektos_cis_vendors'
    #     elif table == 'Resistor':
    #         table1 = 'ektos_2019_resistor'
    #         table2 = '2019_ektos_cis_vendors'
    #     elif table == 'Transistor':
    #         table1 = 'ektos_2019_transistor'
    #         table2 = '2019_ektos_cis_vendors'
    #     elif table == 'Connector':
    #         table1 = 'ektos_2019_connector'
    #         table2 = '2019_ektos_cis_vendors'
    #     elif table == 'Diode':
    #         table1 = 'ektos_2019_diode'
    #         table2 = '2019_ektos_cis_vendors'
    #     elif table == 'Inductor':
    #         table1 = 'ektos_2019_inductor'
    #         table2 = '2019_ektos_cis_vendors'
    #     elif table == 'Capacitor':
    #         table1 = 'ektos_2019_capacitor'
    #         table2 = '2019_ektos_cis_vendors'
    #     elif table == 'IntegratedCircuit':
    #         table1 = 'ektos_2019_integratedcircuit'
    #         table2 = '2019_ektos_cis_vendors'
    #     elif table == 'Mechanical':
    #         table1 = 'ektos_2019_mechanical'
    #         table2 = '2019_ektos_cis_vendors'
    #     elif table == 'Other':
    #         table1 = 'ektos_2019_other'
    #         table2 = '2019_ektos_cis_vendors'
    #
    #     mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'dpe' AND TABLE_NAME = '{}' order by ordinal_position;".format(table1))
    #     counter = 0
    #     global masiv
    #     masiv = []
    #     self.ui2.boxSearch2.clear()
    #     for table_name in mycursor:
    #         b = str(table_name)
    #         fixed1 = ''.join(b.split(")"))
    #         fixed2 = ''.join(fixed1.split("("))
    #         fixed3 = ''.join(fixed2.split("'"))
    #         fixed4 = ''.join(fixed3.split(","))
    #         self.ui2.boxSearch2.addItem(str(fixed4))
    #
    #         masiv.append(fixed4)
    #         global counter2
    #         counter+=1
    #         counter2 = counter
    #     mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'dpe' AND TABLE_NAME = '{}' order by ordinal_position;".format(table2))
    #     counter = 0
    #
    #     for table_name in mycursor:
    #         b = str(table_name)
    #         fixed1 = ''.join(b.split(")"))
    #         fixed2 = ''.join(fixed1.split("("))
    #         fixed3 = ''.join(fixed2.split("'"))
    #         fixed4 = ''.join(fixed3.split(","))
    #         if fixed4 == 'Manufacturer' or fixed4 == 'Man_Part_Number' or fixed4 == 'Man_Part_Number' or fixed4 == 'Vendor' or fixed4 == 'Vendor_Code':
    #             self.ui2.boxSearch2.addItem(str(fixed4))
    #             masiv.append(fixed4)
    #     self.ui2.pushButton_12.clicked.connect(self.second_serch)
    #
    # def prinprintprint(self):
    #     table = self.ui2.boxSearch1.currentText()
    #     self.ui2.editSearch1.setText(table)
    #
    #     mydb = mysql.connector.connect(
    #         host="mysql.ektos.net",
    #         user="dpe",
    #         passwd="dpe",
    #         database="dpe",
    #         charset='utf8',
    #     )
    #     mycursor = mydb.cursor()
    #     global table1
    #     global table2
    #
    #     if table == 'Relay':
    #         table1 = 'test_relay'
    #         table2 = 'test_vendor'
    #         self.ui2.boxSearch2.setEnabled(True)
    #     # elif table == 'Resistor':
    #     #     table1 = 'ektos_2019_resistor'
    #     #     table2 = '2019_ektos_cis_vendors'
    #     # elif table == 'Transistor':
    #     #     table1 = 'ektos_2019_transistor'
    #     #     table2 = '2019_ektos_cis_vendors'
    #     # elif table == 'Connector':
    #     #     table1 = 'ektos_2019_connector'
    #     #     table2 = '2019_ektos_cis_vendors'
    #     # elif table == 'Diode':
    #     #     table1 = 'ektos_2019_diode'
    #     #     table2 = '2019_ektos_cis_vendors'
    #     # elif table == 'Inductor':
    #     #     table1 = 'ektos_2019_inductor'
    #     #     table2 = '2019_ektos_cis_vendors'
    #     # elif table == 'Capacitor':
    #     #     table1 = 'ektos_2019_capacitor'
    #     #     table2 = '2019_ektos_cis_vendors'
    #     # elif table == 'IntegratedCircuit':
    #     #     table1 = 'ektos_2019_integratedcircuit'
    #     #     table2 = '2019_ektos_cis_vendors'
    #     # elif table == 'Mechanical':
    #     #     table1 = 'ektos_2019_mechanical'
    #     #     table2 = '2019_ektos_cis_vendors'
    #     # elif table == 'Other':
    #     #     table1 = 'ektos_2019_other'
    #     #     table2 = '2019_ektos_cis_vendors'
    #
    #     mycursor.execute(
    #         "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'dpe' AND TABLE_NAME = '{}' order by ordinal_position;".format(
    #             table1))
    #     counter = 0
    #     global masiv
    #     masiv = []
    #     self.ui2.boxSearch2.clear()
    #     for table_name in mycursor:
    #         b = str(table_name)
    #         fixed1 = ''.join(b.split(")"))
    #         fixed2 = ''.join(fixed1.split("("))
    #         fixed3 = ''.join(fixed2.split("'"))
    #         fixed4 = ''.join(fixed3.split(","))
    #         self.ui2.boxSearch2.addItem(str(fixed4))
    #
    #         masiv.append(fixed4)
    #         global counter2
    #         counter += 1
    #         counter2 = counter
    #     mycursor.execute(
    #         "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'dpe' AND TABLE_NAME = '{}' order by ordinal_position;".format(
    #             table2))
    #     counter = 0
    #
    #     for table_name in mycursor:
    #         b = str(table_name)
    #         fixed1 = ''.join(b.split(")"))
    #         fixed2 = ''.join(fixed1.split("("))
    #         fixed3 = ''.join(fixed2.split("'"))
    #         fixed4 = ''.join(fixed3.split(","))
    #         if fixed4 == 'Manufacturer' or fixed4 == 'Man_Part_Number' or fixed4 == 'Man_Part_Number' or fixed4 == 'Vendor' or fixed4 == 'Vendor_Code':
    #             self.ui2.boxSearch2.addItem(str(fixed4))
    #             masiv.append(fixed4)
    #     self.ui2.pushButton_12.clicked.connect(self.second_serch)
    #
    #
    #
    # def second_serch(self):
    #     global search2
    #     search2 = self.ui2.boxSearch2.currentText()
    #     self.ui2.editSearch2.setText(search2)
    #     self.ui2.editSearch3.setEnabled(True)
    #     self.ui2.pushButton_13.setEnabled(True)
    #     self.ui2.pushButton_13.clicked.connect(self.third_serch)
    #     global edit_search
    #     edit_search = self.ui2.editSearch3.returnPressed.connect(self.onPressed)
    #     v = self.ui2.editSearch3.show()
    #
    # def third_serch(self):
    #     self.ui2.listFound.clear()
    #     global search3
    #
    #
    #     mydb = mysql.connector.connect(
    #         host="mysql.ektos.net",
    #         user="dpe",
    #         passwd="dpe",
    #         database="dpe",
    #         charset='utf8',
    #     )
    #     mycursor = mydb.cursor()
    #     a = search2
    #     b = table1
    #     mycursor.execute("SELECT Part_Number FROM {}".format(b))
    #     for data in mycursor:
    #         b = str(data)
    #         fixed1 = ''.join(b.split(")"))
    #         fixed2 = ''.join(fixed1.split("("))
    #         fixed3 = ''.join(fixed2.split("'"))
    #         fixed3 = ''.join(fixed3.split(","))
    #         self.ui2.listFound.addItem(str(fixed3))
    #
    #     self.ui2.listFound.itemDoubleClicked.connect(self.lict)
    def onPressed(self):
        self.ui2.editSearch3
        mydb = mysql.connector.connect(
            host="mysql.ektos.net",
            user="dpe",
            passwd="dpe",
            database="dpe",
            charset='utf8',
        )
        mycursor = mydb.cursor()


        if search1 == 'Relay':
            table1 = 'ektos_2019_relay'
            table2 = '2019_ektos_cis_vendors'
        elif search1 == 'Resistor':
            table1 = 'ektos_2019_resistor'
            table2 = '2019_ektos_cis_vendors'
        elif search1 == 'Transistor':
            table1 = 'ektos_2019_transistor'
            table2 = '2019_ektos_cis_vendors'
        elif search1 == 'Connector':
            table1 = 'ektos_2019_connector'
            table2 = '2019_ektos_cis_vendors'
        elif search1 == 'Diode':
            table1 = 'ektos_2019_diode'
            table2 = '2019_ektos_cis_vendors'
        elif search1 == 'Inductor':
            table1 = 'ektos_2019_inductor'
            table2 = '2019_ektos_cis_vendors'
        elif search1 == 'Capacitor':
            table1 = 'ektos_2019_capacitor'
            table2 = '2019_ektos_cis_vendors'
        elif search1 == 'IntegratedCircuit':
            table1 = 'ektos_2019_integratedcircuit'
            table2 = '2019_ektos_cis_vendors'
        elif search1 == 'Mechanical':
            table1 = 'ektos_2019_mechanical'
            table2 = '2019_ektos_cis_vendors'
        elif search1 == 'Other':
            table1 = 'ektos_2019_other'
            table2 = '2019_ektos_cis_vendors'

        # self.ui2.label_176.setText(self.ui2.editSearch3.text())
        c = self.ui2.editSearch3.text()


        mycursor.execute("SELECT Part_Number FROM {} WHERE {} LIKE '%{}%'".format(table1, search2, c))
        # mycursor.execute("SELECT Part_Number FROM ektos_2019_relay WHERE Part_Type LIKE 'RELAY\SOLID'")
        self.ui2.listFound.clear()
        for somedata in mycursor:

            x = str(somedata)
            self.ui2.listFound.addItem(str(x))
        mycursor.execute("SELECT Part_Number FROM {} WHERE {} LIKE '%{}%'".format(table2, search2, c))
        for somedata in mycursor:

            x = str(somedata)
            if somedata == 'Manufacturer' or somedata == 'Man_Part_Number' or somedata == 'Man_Part_Number' or somedata == 'Vendor' or somedata == 'Vendor_Code':
                self.ui2.listFound.addItem(str(x))



    def review_component(self):
        type_of_component = self.ui2.boxSearch1.currentText()

        mydb = mysql.connector.connect(
            host="mysql.ektos.net",
            user="dpe",
            passwd="dpe",
            database="dpe",
            charset='utf8',
        )
        mycursor = mydb.cursor()
        a = 'Part_Number'
        b = table1
        c = found_item
        fixed1 = ''.join(c.split(")"))
        fixed2 = ''.join(fixed1.split("("))
        fixed3 = ''.join(fixed2.split("'"))
        fixed3 = ''.join(fixed3.split(","))
        mycursor.execute("SELECT Review_Date FROM {}  WHERE {} = '{}'".format(b, a, fixed3))
        for some_data in mycursor:
            global fixedd3
            fixedd1 = ''.join(str(some_data).split(")"))
            fixedd2 = ''.join(fixedd1.split("("))
            fixedd3 = ''.join(fixedd2.split("'"))
            fixedd3 = ''.join(fixedd3.split(","))

        if str(fixedd3) != '':
            self.ui2.label_176.setText("This component has been reviewed")
        else:
            if type_of_component == 'Capacitor':
                self.ui2.tabWidget.setCurrentIndex(6)
                self.ui2.groupBox_19.setEnabled(False)
                self.ui2.groupBox_20.setEnabled(False)

                mydb = mysql.connector.connect(
                    host="mysql.ektos.net",
                    user="dpe",
                    passwd="dpe",
                    database="dpe",
                    charset='utf8',
                )
                mycursor = mydb.cursor()
                a = 'Part_Number'
                b = table1
                c = found_item
                fixed1 = ''.join(c.split(")"))
                fixed2 = ''.join(fixed1.split("("))
                fixed3 = ''.join(fixed2.split("'"))
                fixed3 = ''.join(fixed3.split(","))
                mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
                counter = -1
                for data12 in mycursor:
                    b = data12
                    for i in data12:
                        counter += 1
                if b[13] != '':
                    self.ui2.label_265.setText("This component has been reviewed")
                    self.ui2.lineEdit_176.setEnabled(False)
                else:
                    self.ui2.lineEdit_170.setText(b[0]),
                    self.ui2.lineEdit_164.setText(b[1]),
                    self.ui2.lineEdit_165.setText(b[2]),
                    self.ui2.lineEdit_166.setText(b[3]),
                    self.ui2.lineEdit_167.setText(b[4]),
                    self.ui2.lineEdit_168.setText(b[5]),
                    self.ui2.boxStatus_21.setCurrentText(b[6]),
                    self.ui2.boxStatus_7.setCurrentText(b[7]),
                    self.ui2.lineEdit_171.setText(b[8]),
                    self.ui2.lineEdit_172.setText(b[9]),
                    self.ui2.lineEdit_173.setText(b[10]),
                    self.ui2.lineEdit_174.setText(b[11]),
                    self.ui2.lineEdit_175.setText(b[12]),
                    self.ui2.lineEdit_176.setText(b[13]),
                    self.ui2.lineEdit_177.setText(b[14]),
                    self.ui2.boxStatus_22.setCurrentText(b[15]),
                    self.ui2.lineEdit_179.setText(b[16]),
                    self.ui2.lineEdit_180.setText(b[17]),
                    self.ui2.lineEdit_181.setText(b[18]),
                    self.ui2.lineEdit_182.setText(b[19]),
                    self.ui2.lineEdit_183.setText(b[20]),
                    self.ui2.lineEdit_184.setText(b[21]),
                    self.ui2.lineEdit_185.setText(b[22]),
                    self.ui2.lineEdit_186.setText(b[23]),
                    self.ui2.lineEdit_187.setText(b[24]),
                    self.ui2.lineEdit_188.setText(b[25]),
                    self.ui2.lineEdit_189.setText(b[26]),
                    self.ui2.lineEdit_190.setText(b[27]),
                    b = table2
                    mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
                    for data12 in mycursor:
                        b = data12
                    self.ui2.lineEdit_195.setText(b[5])
                    self.ui2.lineEdit_191.setText(b[4])
                    self.ui2.lineEdit_225.setText(b[3])
                    self.ui2.lineEdit_224.setText(b[2])


            elif type_of_component == 'Connector':
                self.ui2.tabWidget.setCurrentIndex(3)
                self.ui2.groupBox_10.setEnabled(False)
                self.ui2.groupBox_11.setEnabled(False)
                self.ui2.groupBox_26.setEnabled(False)

                mydb = mysql.connector.connect(
                    host="mysql.ektos.net",
                    user="dpe",
                    passwd="dpe",
                    database="dpe",
                    charset='utf8',
                )
                mycursor = mydb.cursor()
                a = 'Part_Number'
                b = table1
                c = found_item
                fixed1 = ''.join(c.split(")"))
                fixed2 = ''.join(fixed1.split("("))
                fixed3 = ''.join(fixed2.split("'"))
                fixed3 = ''.join(fixed3.split(","))
                mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
                counter = -1
                for data12 in mycursor:
                    b = data12
                    for i in data12:
                        counter += 1
                if b[13] != '':
                    self.ui2.label_265.setText("This component has been reviewed")
                    self.ui2.lineEdit_176.setEnabled(False)
                else:
                    self.ui2.lineEdit_92.setText(b[0])
                    self.ui2.lineEdit_86.setText(b[1])
                    self.ui2.lineEdit_87.setText(b[2])
                    self.ui2.lineEdit_88.setText(b[3])
                    self.ui2.lineEdit_89.setText(b[4])
                    self.ui2.lineEdit_90.setText(b[5])
                    self.ui2.boxStatus_11.setCurrentText(b[6])
                    self.ui2.boxStatus_4.setCurrentText(b[7])
                    self.ui2.lineEdit_93.setText(b[8])
                    self.ui2.lineEdit_94.setText(b[9])
                    self.ui2.lineEdit_95.setText(b[10])
                    self.ui2.lineEdit_96.setText(b[11])
                    self.ui2.lineEdit_97.setText(b[12])
                    self.ui2.lineEdit_98.setText(b[13])
                    self.ui2.boxStatus_12.setCurrentText(b[15])
                    self.ui2.lineEdit_101.setText(b[16])
                    self.ui2.lineEdit_102.setText(b[17])
                    self.ui2.lineEdit_103.setText(b[18])
                    self.ui2.lineEdit_104.setText(b[19])
                    self.ui2.lineEdit_105.setText(b[20])
                    self.ui2.lineEdit_106.setText(b[21])
                    self.ui2.lineEdit_107.setText(b[22])
                    self.ui2.lineEdit_108.setText(b[23])
                    self.ui2.lineEdit_109.setText(b[24])
                    self.ui2.lineEdit_110.setText(b[25])
                    self.ui2.lineEdit_111.setText(b[26])
                    self.ui2.lineEdit_112.setText(b[27])
                    self.ui2.lineEdit_113.setText(b[28])
                    b = table2
                    mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
                    for data12 in mycursor:
                        b = data12
                    self.ui2.lineEdit_114.setText(b[4])
                    self.ui2.lineEdit_120.setText(b[5])
                    self.ui2.lineEdit_210.setText(b[3])
                    self.ui2.lineEdit_219.setText(b[2])


            elif type_of_component == 'Diode':
                self.ui2.tabWidget.setCurrentIndex(4)
                self.ui2.groupBox_13.setEnabled(False)
                self.ui2.groupBox_14.setEnabled(False)

                mydb = mysql.connector.connect(
                    host="mysql.ektos.net",
                    user="dpe",
                    passwd="dpe",
                    database="dpe",
                    charset='utf8',
                )
                mycursor = mydb.cursor()
                a = 'Part_Number'
                b = table1
                c = found_item
                fixed1 = ''.join(c.split(")"))
                fixed2 = ''.join(fixed1.split("("))
                fixed3 = ''.join(fixed2.split("'"))
                fixed3 = ''.join(fixed3.split(","))
                mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
                counter = -1
                for data12 in mycursor:
                    b = data12
                    for i in data12:
                        counter += 1
                if b[13] != '':
                    self.ui2.label_265.setText("This component has been reviewed")
                    self.ui2.lineEdit_176.setEnabled(False)
                else:
                    self.ui2.lineEdit_121.setText(b[0])
                    self.ui2.lineEdit_115.setText(b[1])
                    self.ui2.lineEdit_116.setText(b[2])
                    self.ui2.lineEdit_117.setText(b[3])
                    self.ui2.lineEdit_118.setText(b[4])
                    self.ui2.lineEdit_119.setText(b[5])
                    self.ui2.boxStatus_17.setCurrentText(b[6])
                    self.ui2.boxStatus_5.setCurrentText(b[7])
                    self.ui2.lineEdit_122.setText(b[8])
                    self.ui2.lineEdit_123.setText(b[9])
                    self.ui2.lineEdit_124.setText(b[10])
                    self.ui2.lineEdit_125.setText(b[11])
                    self.ui2.lineEdit_126.setText(b[12])
                    self.ui2.lineEdit_127.setText(b[13])
                    self.ui2.boxStatus_18.setCurrentText(b[15])
                    self.ui2.lineEdit_130.setText(b[16])
                    self.ui2.lineEdit_131.setText(b[17])
                    self.ui2.lineEdit_132.setText(b[18])
                    self.ui2.lineEdit_133.setText(b[19])
                    self.ui2.lineEdit_134.setText(b[20])
                    self.ui2.lineEdit_135.setText(b[21])
                    self.ui2.lineEdit_136.setText(b[22])
                    self.ui2.lineEdit_137.setText(b[23])
                    self.ui2.lineEdit_138.setText(b[24])
                    b = table2
                    mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
                    for data12 in mycursor:
                        b = data12
                    self.ui2.lineEdit_139.setText(b[4])
                    self.ui2.lineEdit_145.setText(b[5])
                    self.ui2.lineEdit_221.setText(b[3])
                    self.ui2.lineEdit_220.setText(b[2])

            elif type_of_component == 'Inductor':
                self.ui2.tabWidget.setCurrentIndex(5)
                self.ui2.groupBox_16.setEnabled(False)
                self.ui2.groupBox_17.setEnabled(False)

                mydb = mysql.connector.connect(
                    host="mysql.ektos.net",
                    user="dpe",
                    passwd="dpe",
                    database="dpe",
                    charset='utf8',
                )
                mycursor = mydb.cursor()
                a = 'Part_Number'
                b = table1
                c = found_item
                fixed1 = ''.join(c.split(")"))
                fixed2 = ''.join(fixed1.split("("))
                fixed3 = ''.join(fixed2.split("'"))
                fixed3 = ''.join(fixed3.split(","))
                mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
                counter = -1
                for data12 in mycursor:
                    b = data12
                    for i in data12:
                        counter += 1
                if b[13] != '':
                    self.ui2.label_265.setText("This component has been reviewed")
                    self.ui2.lineEdit_176.setEnabled(False)
                else:
                    self.ui2.lineEdit_146.setText(b[0])
                    self.ui2.lineEdit_140.setText(b[1])
                    self.ui2.lineEdit_141.setText(b[2])
                    self.ui2.lineEdit_142.setText(b[3])
                    self.ui2.lineEdit_143.setText(b[4])
                    self.ui2.lineEdit_144.setText(b[5])
                    self.ui2.boxStatus_19.setCurrentText(b[6])
                    self.ui2.boxStatus_6.setCurrentText(b[7])
                    self.ui2.lineEdit_147.setText(b[8])
                    self.ui2.lineEdit_148.setText(b[9])
                    self.ui2.lineEdit_149.setText(b[10])
                    self.ui2.lineEdit_150.setText(b[11])
                    self.ui2.lineEdit_151.setText(b[12])
                    self.ui2.lineEdit_152.setText(b[13])
                    self.ui2.boxStatus_20.setCurrentText(b[15])
                    self.ui2.lineEdit_155.setText(b[16])
                    self.ui2.lineEdit_156.setText(b[17])
                    self.ui2.lineEdit_157.setText(b[18])
                    self.ui2.lineEdit_158.setText(b[19])
                    self.ui2.lineEdit_159.setText(b[20])
                    self.ui2.lineEdit_160.setText(b[21])
                    self.ui2.lineEdit_161.setText(b[22])
                    self.ui2.lineEdit_162.setText(b[23])
                    b = table2
                    mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
                    for data12 in mycursor:
                        b = data12
                    self.ui2.lineEdit_163.setText(b[4])
                    self.ui2.lineEdit_169.setText(b[5])
                    self.ui2.lineEdit_223.setText(b[3])
                    self.ui2.lineEdit_222.setText(b[2])

            elif type_of_component == 'IntegratedCircuit':
                self.ui2.tabWidget.setCurrentIndex(7)
                self.ui2.groupBox_31.setEnabled(False)
                self.ui2.groupBox_32.setEnabled(False)

                mydb = mysql.connector.connect(
                    host="mysql.ektos.net",
                    user="dpe",
                    passwd="dpe",
                    database="dpe",
                    charset='utf8',
                )
                mycursor = mydb.cursor()
                a = 'Part_Number'
                b = table1
                c = found_item
                fixed1 = ''.join(c.split(")"))
                fixed2 = ''.join(fixed1.split("("))
                fixed3 = ''.join(fixed2.split("'"))
                fixed3 = ''.join(fixed3.split(","))
                mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
                counter = -1
                for data12 in mycursor:
                    b = data12
                    for i in data12:
                        counter += 1
                if b[13] != '':
                    self.ui2.label_265.setText("This component has been reviewed")
                    self.ui2.lineEdit_176.setEnabled(False)
                else:
                    self.ui2.lineEdit_294.setText(b[0])
                    self.ui2.lineEdit_192.setText(b[1])
                    self.ui2.lineEdit_193.setText(b[2])
                    self.ui2.lineEdit_194.setText(b[3])
                    self.ui2.lineEdit_291.setText(b[4])
                    self.ui2.lineEdit_292.setText(b[5])
                    self.ui2.boxStatus_23.setCurrentText(b[6])
                    self.ui2.boxStatus_8.setCurrentText(b[7])
                    self.ui2.lineEdit_295.setText(b[8])
                    self.ui2.lineEdit_296.setText(b[9])
                    self.ui2.lineEdit_297.setText(b[10])
                    self.ui2.lineEdit_298.setText(b[11])
                    self.ui2.lineEdit_299.setText(b[12])
                    self.ui2.lineEdit_300.setText(b[13])
                    self.ui2.boxStatus_24.setCurrentText(b[15])
                    self.ui2.lineEdit_303.setText(b[16])
                    self.ui2.lineEdit_304.setText(b[17])
                    self.ui2.lineEdit_305.setText(b[18])
                    self.ui2.lineEdit_306.setText(b[19])
                    self.ui2.lineEdit_307.setText(b[20])
                    self.ui2.lineEdit_308.setText(b[21])
                    self.ui2.lineEdit_309.setText(b[22])
                    self.ui2.lineEdit_310.setText(b[23])
                    self.ui2.lineEdit_314.setText(b[24])
                    self.ui2.lineEdit_315.setText(b[25])

            elif type_of_component == 'Mechanical':
                self.ui2.tabWidget.setCurrentIndex(8)
                self.ui2.groupBox_22.setEnabled(False)
                self.ui2.groupBox_23.setEnabled(False)

                mydb = mysql.connector.connect(
                    host="mysql.ektos.net",
                    user="dpe",
                    passwd="dpe",
                    database="dpe",
                    charset='utf8',
                )
                mycursor = mydb.cursor()
                a = 'Part_Number'
                b = table1
                c = found_item
                fixed1 = ''.join(c.split(")"))
                fixed2 = ''.join(fixed1.split("("))
                fixed3 = ''.join(fixed2.split("'"))
                fixed3 = ''.join(fixed3.split(","))
                mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
                counter = -1
                for data12 in mycursor:
                    b = data12
                    for i in data12:
                        counter += 1
                if b[13] != '':
                    self.ui2.label_265.setText("This component has been reviewed")
                    self.ui2.lineEdit_176.setEnabled(False)
                else:
                    self.ui2.lineEdit_202.setText(b[0])
                    self.ui2.lineEdit_196.setText(b[1])
                    self.ui2.lineEdit_197.setText(b[2])
                    self.ui2.lineEdit_198.setText(b[3])
                    self.ui2.lineEdit_199.setText(b[4])
                    self.ui2.lineEdit_200.setText(b[5])
                    self.ui2.boxStatus_25.setCurrentText(b[6])
                    self.ui2.boxStatus_9.setCurrentText(b[7])
                    self.ui2.lineEdit_203.setText(b[8])
                    self.ui2.lineEdit_204.setText(b[9])
                    self.ui2.lineEdit_205.setText(b[10])
                    self.ui2.lineEdit_206.setText(b[11])
                    self.ui2.lineEdit_207.setText(b[12])
                    self.ui2.lineEdit_208.setText(b[13])
                    self.ui2.boxStatus_26.setCurrentText(b[15])
                    self.ui2.lineEdit_211.setText(b[16])
                    self.ui2.lineEdit_212.setText(b[17])
                    self.ui2.lineEdit_213.setText(b[18])
                    self.ui2.lineEdit_214.setText(b[19])
                    self.ui2.lineEdit_215.setText(b[20])
                    b = table2
                    mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
                    for data12 in mycursor:
                        b = data12
                    self.ui2.lineEdit_216.setText(b[4])
                    self.ui2.lineEdit_217.setText(b[5])
                    self.ui2.lineEdit_229.setText(b[3])
                    self.ui2.lineEdit_228.setText(b[2])

            elif type_of_component == 'Other':
                self.ui2.tabWidget.setCurrentIndex(9)
                self.ui2.groupBox_28.setEnabled(False)
                self.ui2.groupBox_29.setEnabled(False)

                mydb = mysql.connector.connect(
                    host="mysql.ektos.net",
                    user="dpe",
                    passwd="dpe",
                    database="dpe",
                    charset='utf8',
                )
                mycursor = mydb.cursor()
                a = 'Part_Number'
                b = table1
                c = found_item
                fixed1 = ''.join(c.split(")"))
                fixed2 = ''.join(fixed1.split("("))
                fixed3 = ''.join(fixed2.split("'"))
                fixed3 = ''.join(fixed3.split(","))
                mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
                counter = -1
                for data12 in mycursor:
                    b = data12
                    for i in data12:
                        counter += 1
                if b[13] != '':
                    self.ui2.label_265.setText("This component has been reviewed")
                    self.ui2.lineEdit_176.setEnabled(False)
                else:
                    self.ui2.lineEdit_266.setText(b[0])
                    self.ui2.lineEdit_260.setText(b[1])
                    self.ui2.lineEdit_261.setText(b[2])
                    self.ui2.lineEdit_262.setText(b[3])
                    self.ui2.lineEdit_263.setText(b[4])
                    self.ui2.lineEdit_264.setText(b[5])
                    self.ui2.boxStatus_27.setCurrentText(b[6])
                    self.ui2.boxStatus_10.setCurrentText(b[7])
                    self.ui2.lineEdit_267.setText(b[8])
                    self.ui2.lineEdit_268.setText(b[9])
                    self.ui2.lineEdit_269.setText(b[10])
                    self.ui2.lineEdit_270.setText(b[11])
                    self.ui2.lineEdit_271.setText(b[12])
                    self.ui2.lineEdit_272.setText(b[13])
                    self.ui2.boxStatus_30.setCurrentText(b[15])
                    self.ui2.lineEdit_275.setText(b[16])
                    self.ui2.lineEdit_276.setText(b[17])
                    self.ui2.lineEdit_277.setText(b[18])
                    self.ui2.lineEdit_278.setText(b[19])
                    self.ui2.lineEdit_279.setText(b[20])
                    self.ui2.lineEdit_280.setText(b[21])
                    self.ui2.lineEdit_281.setText(b[22])
                    self.ui2.lineEdit_282.setText(b[23])
                    self.ui2.lineEdit_283.setText(b[24])
                    self.ui2.lineEdit_284.setText(b[25])
                    b = table2
                    mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
                    for data12 in mycursor:
                        b = data12
                    self.ui2.lineEdit_316.setText(b[4])
                    self.ui2.lineEdit_317.setText(b[5])
                    self.ui2.lineEdit_231.setText(b[3])
                    self.ui2.lineEdit_230.setText(b[2])


            elif type_of_component == 'Relay':
                self.ui2.tabWidget.setCurrentIndex(0)
                self.ui2.groupBox.setEnabled(False)
                self.ui2.groupBox_3.setEnabled(False)
                self.ui2.groupBox_25.setEnabled(False)

                mydb = mysql.connector.connect(
                    host="mysql.ektos.net",
                    user="dpe",
                    passwd="dpe",
                    database="dpe",
                    charset='utf8',
                )
                mycursor = mydb.cursor()
                a = 'Part_Number'
                b = table1
                c = found_item
                fixed1 = ''.join(c.split(")"))
                fixed2 = ''.join(fixed1.split("("))
                fixed3 = ''.join(fixed2.split("'"))
                fixed3 = ''.join(fixed3.split(","))
                mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
                counter = -1
                for data12 in mycursor:
                    b = data12
                    for i in data12:
                        counter += 1
                if b[13] != '':
                    self.ui2.label_265.setText("This component has been reviewed")
                    self.ui2.lineEdit_176.setEnabled(False)
                else:
                    self.ui2.lineEdit_1.setText(b[0])
                    self.ui2.lineEdit_2.setText(b[1])
                    self.ui2.lineEdit_3.setText(b[2])
                    self.ui2.lineEdit_4.setText(b[3])
                    self.ui2.lineEdit_5.setText(b[4])
                    self.ui2.lineEdit_6.setText(b[5])
                    self.ui2.boxStatus_31.setCurrentText(b[6])
                    self.ui2.boxStatus.setCurrentText(b[7])
                    self.ui2.lineEdit_9.setText(b[8])
                    self.ui2.lineEdit_10.setText(b[9])
                    self.ui2.lineEdit_11.setText(b[10])
                    self.ui2.lineEdit_12.setText(b[11])
                    self.ui2.lineEdit_13.setText(b[12])
                    self.ui2.lineEdit_14.setText(b[13])
                    self.ui2.boxStatus_32.setCurrentText(b[15])
                    self.ui2.lineEdit_33.setText(b[16])
                    self.ui2.lineEdit_34.setText(b[17])
                    self.ui2.lineEdit_35.setText(b[18])
                    self.ui2.lineEdit_36.setText(b[19])
                    self.ui2.lineEdit_37.setText(b[20])
                    self.ui2.lineEdit_38.setText(b[21])
                    self.ui2.lineEdit_39.setText(b[22])
                    self.ui2.lineEdit_40.setText(b[23])
                    self.ui2.lineEdit_41.setText(b[24])
                    self.ui2.lineEdit_42.setText(b[25])
                    self.ui2.lineEdit_43.setText(b[26])
                    self.ui2.lineEdit_44.setText(b[27])
                    self.ui2.boxStatus_28.setCurrentText(b[28])
                    self.ui2.boxStatus_29.setCurrentText(b[29])
                    self.ui2.lineEdit_47.setText(b[30])
                    self.ui2.lineEdit_48.setText(b[31])
                    b = table2
                    mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
                    for data12 in mycursor:
                        b = data12
                    self.ui2.lineEdit_58.setText(b[4])
                    self.ui2.lineEdit_64.setText(b[5])
                    self.ui2.lineEdit_45.setText(b[3])
                    self.ui2.lineEdit_46.setText(b[2])

            elif type_of_component == 'Resistor':
                self.ui2.tabWidget.setCurrentIndex(1)
                self.ui2.groupBox_2.setEnabled(False)
                self.ui2.groupBox_4.setEnabled(False)

                mydb = mysql.connector.connect(
                    host="mysql.ektos.net",
                    user="dpe",
                    passwd="dpe",
                    database="dpe",
                    charset='utf8',
                )
                mycursor = mydb.cursor()
                a = 'Part_Number'
                b = table1
                c = found_item
                fixed1 = ''.join(c.split(")"))
                fixed2 = ''.join(fixed1.split("("))
                fixed3 = ''.join(fixed2.split("'"))
                fixed3 = ''.join(fixed3.split(","))
                mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
                counter = -1
                for data12 in mycursor:
                    b = data12
                    for i in data12:
                        counter += 1
                if b[13] != '':
                    self.ui2.label_265.setText("This component has been reviewed")
                    self.ui2.lineEdit_176.setEnabled(False)
                else:
                    self.ui2.lineEdit_24.setText(b[0])
                    self.ui2.lineEdit_18.setText(b[1])
                    self.ui2.lineEdit_19.setText(b[2])
                    self.ui2.lineEdit_20.setText(b[3])
                    self.ui2.lineEdit_21.setText(b[4])
                    self.ui2.lineEdit_22.setText(b[5])
                    self.ui2.boxStatus_15.setCurrentText(b[6])
                    self.ui2.boxStatus_2.setCurrentText(b[7])
                    self.ui2.lineEdit_25.setText(b[8])
                    self.ui2.lineEdit_26.setText(b[9])
                    self.ui2.lineEdit_27.setText(b[10])
                    self.ui2.lineEdit_28.setText(b[11])
                    self.ui2.lineEdit_29.setText(b[12])
                    self.ui2.lineEdit_30.setText(b[13])
                    self.ui2.boxStatus_16.setCurrentText(b[15])
                    self.ui2.lineEdit_49.setText(b[16])
                    self.ui2.lineEdit_50.setText(b[17])
                    self.ui2.lineEdit_51.setText(b[18])
                    self.ui2.lineEdit_52.setText(b[19])
                    self.ui2.lineEdit_53.setText(b[20])
                    self.ui2.lineEdit_54.setText(b[21])
                    self.ui2.lineEdit_55.setText(b[22])
                    self.ui2.lineEdit_56.setText(b[23])
                    self.ui2.lineEdit_57.setText(b[24])
                    b = table2
                    mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
                    for data12 in mycursor:
                        b = data12
                    self.ui2.lineEdit_73.setText(b[4])
                    self.ui2.lineEdit_85.setText(b[5])
                    self.ui2.lineEdit_178.setText(b[3])
                    self.ui2.lineEdit_201.setText(b[2])

            elif type_of_component == 'Transistor':
                self.ui2.tabWidget.setCurrentIndex(2)
                self.ui2.groupBox_7.setEnabled(False)
                self.ui2.groupBox_8.setEnabled(False)

                mydb = mysql.connector.connect(
                    host="mysql.ektos.net",
                    user="dpe",
                    passwd="dpe",
                    database="dpe",
                    charset='utf8',
                )
                mycursor = mydb.cursor()
                a = 'Part_Number'
                b = table1
                c = found_item
                fixed1 = ''.join(c.split(")"))
                fixed2 = ''.join(fixed1.split("("))
                fixed3 = ''.join(fixed2.split("'"))
                fixed3 = ''.join(fixed3.split(","))
                mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
                counter = -1
                for data12 in mycursor:
                    b = data12
                    for i in data12:
                        counter += 1
                if b[13] != '':
                    self.ui2.label_265.setText("This component has been reviewed")
                    self.ui2.lineEdit_176.setEnabled(False)
                else:
                    self.ui2.lineEdit_65.setText(b[0])
                    self.ui2.lineEdit_59.setText(b[1])
                    self.ui2.lineEdit_60.setText(b[2])
                    self.ui2.lineEdit_61.setText(b[3])
                    self.ui2.lineEdit_62.setText(b[4])
                    self.ui2.lineEdit_63.setText(b[5])
                    self.ui2.boxStatus_14.setCurrentText(b[6])
                    self.ui2.boxStatus_3.setCurrentText(b[7])
                    self.ui2.lineEdit_66.setText(b[8])
                    self.ui2.lineEdit_67.setText(b[9])
                    self.ui2.lineEdit_68.setText(b[10])
                    self.ui2.lineEdit_69.setText(b[11])
                    self.ui2.lineEdit_70.setText(b[12])
                    self.ui2.lineEdit_71.setText(b[13])
                    self.ui2.boxStatus_13.setCurrentText(b[15])
                    self.ui2.lineEdit_74.setText(b[16])
                    self.ui2.lineEdit_75.setText(b[17])
                    self.ui2.lineEdit_76.setText(b[18])
                    self.ui2.lineEdit_77.setText(b[19])
                    self.ui2.lineEdit_78.setText(b[20])
                    self.ui2.lineEdit_79.setText(b[21])
                    self.ui2.lineEdit_80.setText(b[22])
                    self.ui2.lineEdit_81.setText(b[23])
                    self.ui2.lineEdit_82.setText(b[24])
                    self.ui2.lineEdit_83.setText(b[25])
                    self.ui2.lineEdit_84.setText(b[26])
                    b = table2
                    mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
                    for data12 in mycursor:
                        b = data12
                    self.ui2.lineEdit_91.setText(b[4])
                    self.ui2.lineEdit_100.setText(b[5])
                    self.ui2.lineEdit_129.setText(b[3])
                    self.ui2.lineEdit_154.setText(b[2])

    def edit_component(self):
        type_of_component = self.ui2.boxSearch1.currentText()
        if type_of_component == 'Capacitor':
            self.ui2.tabWidget.setCurrentIndex(6)
            a = strftime("%Y%m%d", gmtime())  # дата и время
            update_log = a + '(' + log + ')'
            self.ui2.label_242.setText(str(update_log))
            self.ui2.label_238.setEnabled(False)
            mydb = mysql.connector.connect(
                host="mysql.ektos.net",
                user="dpe",
                passwd="dpe",
                database="dpe",
                charset='utf8',
            )
            mycursor = mydb.cursor()
            a = 'Part_Number'
            b = table1
            c = found_item
            fixed1 = ''.join(c.split(")"))
            fixed2 = ''.join(fixed1.split("("))
            fixed3 = ''.join(fixed2.split("'"))
            fixed3 = ''.join(fixed3.split(","))
            # mycursor.execute("DELETE * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
            mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
            counter = -1
            for data12 in mycursor:
                b = data12
                for i in data12:
                    counter += 1

            self.ui2.lineEdit_170.setText(b[0])
            self.ui2.lineEdit_164.setText(b[1])
            self.ui2.lineEdit_165.setText(b[2])
            self.ui2.lineEdit_166.setText(b[3])
            self.ui2.lineEdit_167.setText(b[4])
            self.ui2.lineEdit_168.setText(b[5])
            self.ui2.boxStatus_21.setCurrentText(b[6])
            self.ui2.boxStatus_7.setCurrentText(b[7])
            self.ui2.lineEdit_171.setText(b[8])
            self.ui2.lineEdit_172.setText(b[9])
            self.ui2.lineEdit_173.setText(b[10])
            self.ui2.lineEdit_174.setText(b[11])
            self.ui2.lineEdit_175.setText(b[12])
            self.ui2.lineEdit_176.setText(b[13])
            self.ui2.lineEdit_177.setText(b[14])
            self.ui2.boxStatus_22.setCurrentText(b[15])
            self.ui2.lineEdit_179.setText(b[16])
            self.ui2.lineEdit_180.setText(b[17])
            self.ui2.lineEdit_181.setText(b[18])
            self.ui2.lineEdit_182.setText(b[19])
            self.ui2.lineEdit_183.setText(b[20])
            self.ui2.lineEdit_184.setText(b[21])
            self.ui2.lineEdit_185.setText(b[22])
            self.ui2.lineEdit_186.setText(b[23])
            self.ui2.lineEdit_187.setText(b[24])
            self.ui2.lineEdit_188.setText(b[25])
            self.ui2.lineEdit_189.setText(b[26])
            self.ui2.lineEdit_190.setText(b[27])
            b = table2
            mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
            counter = -1
            for data12 in mycursor:
                b = data12
                for i in data12:
                    counter += 1
            self.ui2.lineEdit_191.setText(b[4])
            self.ui2.lineEdit_195.setText(b[5])
            self.ui2.lineEdit_225.setText(b[3])
            self.ui2.lineEdit_224.setText(b[2])

            self.ui2.lineEdit_175.setEnabled(False)
            self.ui2.pushButton_7.clicked.connect(self.capasitor)


        elif type_of_component == 'Connector':
            self.ui2.tabWidget.setCurrentIndex(3)
            a = strftime("%Y%m%d", gmtime())  # дата и время
            update_log = a + '(' + log + ')'
            self.ui2.label_140.setText(str(update_log))
            self.ui2.label_136.setEnabled(False)
            mydb = mysql.connector.connect(
                host="mysql.ektos.net",
                user="dpe",
                passwd="dpe",
                database="dpe",
                charset='utf8',
            )
            mycursor = mydb.cursor()
            a = 'Part_Number'
            b = table1
            c = found_item
            fixed1 = ''.join(c.split(")"))
            fixed2 = ''.join(fixed1.split("("))
            fixed3 = ''.join(fixed2.split("'"))
            fixed3 = ''.join(fixed3.split(","))
            mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
            counter = -1
            for data12 in mycursor:
                b = data12
                for i in data12:
                    counter += 1

            self.ui2.lineEdit_92.setText(b[0])
            self.ui2.lineEdit_86.setText(b[1])
            self.ui2.lineEdit_87.setText(b[2])
            self.ui2.lineEdit_88.setText(b[3])
            self.ui2.lineEdit_89.setText(b[4])
            self.ui2.lineEdit_90.setText(b[5])
            self.ui2.boxStatus_11.setCurrentText(b[6])
            self.ui2.boxStatus_4.setCurrentText(b[7])
            self.ui2.lineEdit_93.setText(b[8])
            self.ui2.lineEdit_94.setText(b[9])
            self.ui2.lineEdit_95.setText(b[10])
            self.ui2.lineEdit_96.setText(b[11])
            self.ui2.lineEdit_97.setText(b[12])
            self.ui2.lineEdit_97.setEnabled(False)
            self.ui2.lineEdit_98.setText(b[13])
            self.ui2.lineEdit_98.setEnabled(False)
            self.ui2.lineEdit_99.setText(str(update_log))
            self.ui2.lineEdit_99.setEnabled(False)
            self.ui2.boxStatus_12.setCurrentText(b[15])
            self.ui2.lineEdit_101.setText(b[16])
            self.ui2.lineEdit_102.setText(b[17])
            self.ui2.lineEdit_103.setText(b[18])
            self.ui2.lineEdit_104.setText(b[19])
            self.ui2.lineEdit_105.setText(b[20])
            self.ui2.lineEdit_106.setText(b[21])
            self.ui2.lineEdit_107.setText(b[22])
            self.ui2.lineEdit_108.setText(b[23])
            self.ui2.lineEdit_109.setText(b[24])
            self.ui2.lineEdit_110.setText(b[25])
            self.ui2.lineEdit_111.setText(b[26])
            self.ui2.lineEdit_112.setText(b[27])
            self.ui2.lineEdit_113.setText(b[28])
            b = table2
            mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
            counter = -1
            for data12 in mycursor:
                b = data12
                for i in data12:
                    counter += 1
            self.ui2.lineEdit_114.setText(b[4])  # vendor
            self.ui2.lineEdit_120.setText(b[5])  # vendor code
            self.ui2.lineEdit_210.setText(b[3])  # man part number
            self.ui2.lineEdit_219.setText(b[2])  # manufacture

            self.ui2.lineEdit_97.setEnabled(False)
            self.ui2.pushButton_4.clicked.connect(self.connector)
        elif type_of_component == 'Diode':
            self.ui2.tabWidget.setCurrentIndex(4)
            a = strftime("%Y%m%d", gmtime())  # дата и время
            update_log = a + '(' + log + ')'
            self.ui2.label_175.setText(str(update_log))
            self.ui2.label_171.setEnabled(False)
            mydb = mysql.connector.connect(
                host="mysql.ektos.net",
                user="dpe",
                passwd="dpe",
                database="dpe",
                charset='utf8',
            )
            mycursor = mydb.cursor()
            a = 'Part_Number'
            b = table1
            c = found_item
            fixed1 = ''.join(c.split(")"))
            fixed2 = ''.join(fixed1.split("("))
            fixed3 = ''.join(fixed2.split("'"))
            fixed3 = ''.join(fixed3.split(","))
            mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
            counter = -1
            for data12 in mycursor:
                b = data12
                for i in data12:
                    counter += 1

            self.ui2.lineEdit_121.setText(b[0])
            self.ui2.lineEdit_115.setText(b[1])
            self.ui2.lineEdit_116.setText(b[2])
            self.ui2.lineEdit_117.setText(b[3])
            self.ui2.lineEdit_118.setText(b[4])
            self.ui2.lineEdit_119.setText(b[5])
            self.ui2.boxStatus_17.setCurrentText(b[6])
            self.ui2.boxStatus_5.setCurrentText(b[7])
            self.ui2.lineEdit_122.setText(b[8])
            self.ui2.lineEdit_123.setText(b[9])
            self.ui2.lineEdit_124.setText(b[10])
            self.ui2.lineEdit_125.setText(b[11])
            self.ui2.lineEdit_126.setText(b[12])
            self.ui2.lineEdit_126.setEnabled(False)
            self.ui2.lineEdit_127.setText(b[13])
            self.ui2.lineEdit_127.setEnabled(False)
            self.ui2.lineEdit_128.setText(str(update_log))
            self.ui2.lineEdit_128.setEnabled(False)
            self.ui2.boxStatus_18.setCurrentText(b[15])
            self.ui2.lineEdit_130.setText(b[16])
            self.ui2.lineEdit_131.setText(b[17])
            self.ui2.lineEdit_132.setText(b[18])
            self.ui2.lineEdit_133.setText(b[19])
            self.ui2.lineEdit_134.setText(b[20])
            self.ui2.lineEdit_135.setText(b[21])
            self.ui2.lineEdit_136.setText(b[22])
            self.ui2.lineEdit_137.setText(b[23])
            self.ui2.lineEdit_138.setText(b[24])
            b = table2
            mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
            counter = -1
            for data12 in mycursor:
                b = data12
                for i in data12:
                    counter += 1
            self.ui2.lineEdit_139.setText(b[4])  # vendor
            self.ui2.lineEdit_145.setText(b[5])  # vendor code
            self.ui2.lineEdit_221.setText(b[3])  # man part number
            self.ui2.lineEdit_220.setText(b[2])  # manufacture

            self.ui2.lineEdit_126.setEnabled(False)
            self.ui2.pushButton_5.clicked.connect(self.diode)
        elif type_of_component == 'Inductor':
            self.ui2.tabWidget.setCurrentIndex(5)
            a = strftime("%Y%m%d", gmtime())  # дата и время
            update_log = a + '(' + log + ')'
            self.ui2.label_212.setText(str(update_log))
            self.ui2.label_208.setEnabled(False)
            mydb = mysql.connector.connect(
                host="mysql.ektos.net",
                user="dpe",
                passwd="dpe",
                database="dpe",
                charset='utf8',
            )
            mycursor = mydb.cursor()
            a = 'Part_Number'
            b = table1
            c = found_item
            fixed1 = ''.join(c.split(")"))
            fixed2 = ''.join(fixed1.split("("))
            fixed3 = ''.join(fixed2.split("'"))
            fixed3 = ''.join(fixed3.split(","))
            mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
            counter = -1
            for data12 in mycursor:
                b = data12
                for i in data12:
                    counter += 1

            self.ui2.lineEdit_146.setText(b[0])
            self.ui2.lineEdit_140.setText(b[1])
            self.ui2.lineEdit_141.setText(b[2])
            self.ui2.lineEdit_142.setText(b[3])
            self.ui2.lineEdit_143.setText(b[4])
            self.ui2.lineEdit_144.setText(b[5])
            self.ui2.boxStatus_19.setCurrentText(b[6])
            self.ui2.boxStatus_6.setCurrentText(b[7])
            self.ui2.lineEdit_147.setText(b[8])
            self.ui2.lineEdit_148.setText(b[9])
            self.ui2.lineEdit_149.setText(b[10])
            self.ui2.lineEdit_150.setText(b[11])
            self.ui2.lineEdit_151.setText(b[12])
            self.ui2.lineEdit_151.setEnabled(False)
            self.ui2.lineEdit_152.setText(b[13])
            self.ui2.lineEdit_152.setEnabled(False)
            self.ui2.lineEdit_153.setText(str(update_log))
            self.ui2.lineEdit_153.setEnabled(False)
            self.ui2.boxStatus_20.setCurrentText(b[15])
            self.ui2.lineEdit_155.setText(b[16])
            self.ui2.lineEdit_156.setText(b[17])
            self.ui2.lineEdit_157.setText(b[18])
            self.ui2.lineEdit_158.setText(b[19])
            self.ui2.lineEdit_159.setText(b[20])
            self.ui2.lineEdit_160.setText(b[21])
            self.ui2.lineEdit_161.setText(b[22])
            self.ui2.lineEdit_162.setText(b[23])
            b = table2
            mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
            counter = -1
            for data12 in mycursor:
                b = data12
                for i in data12:
                    counter += 1
            self.ui2.lineEdit_163.setText(b[4])  # vendor
            self.ui2.lineEdit_169.setText(b[5])  # vendor code
            self.ui2.lineEdit_223.setText(b[3])  # man part number
            self.ui2.lineEdit_222.setText(b[2])  # manufacture

            self.ui2.lineEdit_151.setEnabled(False)
            self.ui2.pushButton_6.clicked.connect(self.inductor)
        elif type_of_component == 'IntegratedCircuit':
            self.ui2.tabWidget.setCurrentIndex(7)
            a = strftime("%Y%m%d", gmtime())  # дата и время
            update_log = a + '(' + log + ')'
            self.ui2.label_390.setText(str(update_log))
            self.ui2.label_386.setEnabled(False)
            mydb = mysql.connector.connect(
                host="mysql.ektos.net",
                user="dpe",
                passwd="dpe",
                database="dpe",
                charset='utf8',
            )
            mycursor = mydb.cursor()
            a = 'Part_Number'
            b = table1
            c = found_item
            fixed1 = ''.join(c.split(")"))
            fixed2 = ''.join(fixed1.split("("))
            fixed3 = ''.join(fixed2.split("'"))
            fixed3 = ''.join(fixed3.split(","))
            mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
            counter = -1
            for data12 in mycursor:
                b = data12
                for i in data12:
                    counter += 1

            self.ui2.lineEdit_294.setText(b[0])
            self.ui2.lineEdit_192.setText(b[1])
            self.ui2.lineEdit_193.setText(b[2])
            self.ui2.lineEdit_194.setText(b[3])
            self.ui2.lineEdit_291.setText(b[4])
            self.ui2.lineEdit_292.setText(b[5])
            self.ui2.boxStatus_23.setCurrentText(b[6])
            self.ui2.boxStatus_8.setCurrentText(b[7])
            self.ui2.lineEdit_295.setText(b[8])
            self.ui2.lineEdit_296.setText(b[9])
            self.ui2.lineEdit_297.setText(b[10])
            self.ui2.lineEdit_298.setText(b[11])
            self.ui2.lineEdit_299.setText(b[12])
            self.ui2.lineEdit_299.setEnabled(False)
            self.ui2.lineEdit_300.setText(b[13])
            self.ui2.lineEdit_300.setEnabled(False)
            self.ui2.lineEdit_301.setText(str(update_log))
            self.ui2.lineEdit_301.setEnabled(False)
            self.ui2.boxStatus_24.setCurrentText(b[15])
            self.ui2.lineEdit_303.setText(b[16])
            self.ui2.lineEdit_304.setText(b[17])
            self.ui2.lineEdit_305.setText(b[18])
            self.ui2.lineEdit_306.setText(b[19])
            self.ui2.lineEdit_307.setText(b[20])
            self.ui2.lineEdit_308.setText(b[21])
            self.ui2.lineEdit_309.setText(b[22])
            self.ui2.lineEdit_310.setText(b[23])
            b = table2
            mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
            counter = -1
            for data12 in mycursor:
                b = data12
                for i in data12:
                    counter += 1
            self.ui2.lineEdit_314.setText(b[4])  # vendor
            self.ui2.lineEdit_315.setText(b[5])  # vendor code
            self.ui2.lineEdit_227.setText(b[3])  # man part number
            self.ui2.lineEdit_226.setText(b[2])  # manufacture

            self.ui2.lineEdit_299.setEnabled(False)
            self.ui2.pushButton_11.clicked.connect(self.integrated_circuit)
        elif type_of_component == 'Mechanical':
            self.ui2.tabWidget.setCurrentIndex(8)
            a = strftime("%Y%m%d", gmtime())  # дата и время
            update_log = a + '(' + log + ')'
            self.ui2.label_280.setText(str(update_log))
            self.ui2.label_276.setEnabled(False)
            mydb = mysql.connector.connect(
                host="mysql.ektos.net",
                user="dpe",
                passwd="dpe",
                database="dpe",
                charset='utf8',
            )
            mycursor = mydb.cursor()
            a = 'Part_Number'
            b = table1
            c = found_item
            fixed1 = ''.join(c.split(")"))
            fixed2 = ''.join(fixed1.split("("))
            fixed3 = ''.join(fixed2.split("'"))
            fixed3 = ''.join(fixed3.split(","))
            mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
            counter = -1
            for data12 in mycursor:
                b = data12
                for i in data12:
                    counter += 1

            self.ui2.lineEdit_202.setText(b[0])
            self.ui2.lineEdit_196.setText(b[1])
            self.ui2.lineEdit_197.setText(b[2])
            self.ui2.lineEdit_198.setText(b[3])
            self.ui2.lineEdit_199.setText(b[4])
            self.ui2.lineEdit_200.setText(b[5])
            self.ui2.boxStatus_25.setCurrentText(b[6])
            self.ui2.boxStatus_9.setCurrentText(b[7])
            self.ui2.lineEdit_203.setText(b[8])
            self.ui2.lineEdit_204.setText(b[9])
            self.ui2.lineEdit_205.setText(b[10])
            self.ui2.lineEdit_206.setText(b[11])
            self.ui2.lineEdit_207.setText(b[12])
            self.ui2.lineEdit_207.setEnabled(False)
            self.ui2.lineEdit_208.setText(b[13])
            self.ui2.lineEdit_208.setEnabled(False)
            self.ui2.lineEdit_209.setText(str(update_log))
            self.ui2.lineEdit_209.setEnabled(False)
            self.ui2.boxStatus_26.setCurrentText(b[15])
            self.ui2.lineEdit_211.setText(b[16])
            self.ui2.lineEdit_212.setText(b[17])
            self.ui2.lineEdit_213.setText(b[18])
            self.ui2.lineEdit_214.setText(b[19])
            self.ui2.lineEdit_215.setText(b[20])
            b = table2
            mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
            counter = -1
            for data12 in mycursor:
                b = data12
                for i in data12:
                    counter += 1
            self.ui2.lineEdit_216.setText(b[4])  # vendor
            self.ui2.lineEdit_217.setText(b[5])  # vendor code
            self.ui2.lineEdit_229.setText(b[3])  # man part number
            self.ui2.lineEdit_228.setText(b[2])  # manufacture

            self.ui2.lineEdit_207.setEnabled(False)
            self.ui2.pushButton_8.clicked.connect(self.mecanical)
        elif type_of_component == 'Other':
            self.ui2.tabWidget.setCurrentIndex(9)
            a = strftime("%Y%m%d", gmtime())  # дата и время
            update_log = a + '(' + log + ')'
            self.ui2.label_356.setText(str(update_log))
            self.ui2.label_352.setEnabled(False)
            mydb = mysql.connector.connect(
                host="mysql.ektos.net",
                user="dpe",
                passwd="dpe",
                database="dpe",
                charset='utf8',
            )
            mycursor = mydb.cursor()
            a = 'Part_Number'
            b = table1
            c = found_item
            fixed1 = ''.join(c.split(")"))
            fixed2 = ''.join(fixed1.split("("))
            fixed3 = ''.join(fixed2.split("'"))
            fixed3 = ''.join(fixed3.split(","))
            mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
            counter = -1
            for data12 in mycursor:
                b = data12
                for i in data12:
                    counter += 1

            self.ui2.lineEdit_266.setText(b[0])
            self.ui2.lineEdit_260.setText(b[1])
            self.ui2.lineEdit_261.setText(b[2])
            self.ui2.lineEdit_262.setText(b[3])
            self.ui2.lineEdit_263.setText(b[4])
            self.ui2.lineEdit_264.setText(b[5])
            self.ui2.boxStatus_27.setCurrentText(b[6])
            self.ui2.boxStatus_10.setCurrentText(b[7])
            self.ui2.lineEdit_267.setText(b[8])
            self.ui2.lineEdit_268.setText(b[9])
            self.ui2.lineEdit_269.setText(b[10])
            self.ui2.lineEdit_270.setText(b[11])
            self.ui2.lineEdit_271.setText(b[12])
            self.ui2.lineEdit_271.setEnabled(False)
            self.ui2.lineEdit_272.setText(b[13])
            self.ui2.lineEdit_272.setEnabled(False)
            self.ui2.lineEdit_273.setText(str(update_log))
            self.ui2.lineEdit_273.setEnabled(False)
            self.ui2.boxStatus_30.setCurrentText(b[15])
            self.ui2.lineEdit_275.setText(b[16])
            self.ui2.lineEdit_276.setText(b[17])
            self.ui2.lineEdit_277.setText(b[18])
            self.ui2.lineEdit_278.setText(b[19])
            self.ui2.lineEdit_279.setText(b[20])
            self.ui2.lineEdit_280.setText(b[21])
            self.ui2.lineEdit_281.setText(b[22])
            self.ui2.lineEdit_282.setText(b[23])
            self.ui2.lineEdit_283.setText(b[24])
            self.ui2.lineEdit_284.setText(b[25])
            b = table2
            mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
            counter = -1
            for data12 in mycursor:
                b = data12
                for i in data12:
                    counter += 1
            self.ui2.lineEdit_316.setText(b[4])  # vendor
            self.ui2.lineEdit_317.setText(b[5])  # vendor code
            self.ui2.lineEdit_231.setText(b[3])  # man part number
            self.ui2.lineEdit_230.setText(b[2])  # manufacture

            self.ui2.lineEdit_271.setEnabled(False)
            self.ui2.pushButton_10.clicked.connect(self.other)
        elif type_of_component == 'Relay':
            self.ui2.tabWidget.setCurrentIndex(0)
            a = strftime("%Y%m%d", gmtime())  # дата и время
            update_log = a+'('+log+')'
            self.ui2.label_22.setText(str(update_log))
            self.ui2.label_18.setEnabled(False)
            mydb = mysql.connector.connect(
                host="mysql.ektos.net",
                user="dpe",
                passwd="dpe",
                database="dpe",
                charset='utf8',
            )
            mycursor = mydb.cursor()
            a = 'Part_Number'
            b = table1
            c = found_item
            fixed1 = ''.join(c.split(")"))
            fixed2 = ''.join(fixed1.split("("))
            fixed3 = ''.join(fixed2.split("'"))
            fixed3 = ''.join(fixed3.split(","))
            mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
            counter = -1
            for data12 in mycursor:
                b = data12
                for i in data12:
                    counter += 1
            self.ui2.lineEdit_1.setText(b[0])
            self.ui2.lineEdit_2.setText(b[1])
            self.ui2.lineEdit_3.setText(b[2])
            self.ui2.lineEdit_4.setText(b[3])
            self.ui2.lineEdit_5.setText(b[4])
            self.ui2.lineEdit_6.setText(b[5])
            self.ui2.boxStatus_31.setCurrentText(b[6])
            self.ui2.boxStatus.setCurrentText(b[7])
            self.ui2.lineEdit_9.setText(b[8])
            self.ui2.lineEdit_10.setText(b[9])
            self.ui2.lineEdit_11.setText(b[10])
            self.ui2.lineEdit_12.setText(b[11])
            self.ui2.lineEdit_13.setText(b[12])
            self.ui2.lineEdit_14.setText(b[13])
            self.ui2.lineEdit_15.setText(str(update_log))
            self.ui2.lineEdit_15.setEnabled(False)
            self.ui2.boxStatus_32.setCurrentText(b[15])
            self.ui2.lineEdit_33.setText(b[16])
            self.ui2.lineEdit_34.setText(b[17])
            self.ui2.lineEdit_35.setText(b[18])
            self.ui2.lineEdit_36.setText(b[19])
            self.ui2.lineEdit_37.setText(b[20])
            self.ui2.lineEdit_38.setText(b[21])
            self.ui2.lineEdit_39.setText(b[22])
            self.ui2.lineEdit_40.setText(b[23])
            self.ui2.lineEdit_41.setText(b[24])
            self.ui2.lineEdit_42.setText(b[25])
            self.ui2.lineEdit_43.setText(b[26])
            self.ui2.lineEdit_44.setText(b[27])
            self.ui2.boxStatus_28.setCurrentText(b[28])
            self.ui2.boxStatus_29.setCurrentText(b[29])
            self.ui2.lineEdit_47.setText(b[30])
            self.ui2.lineEdit_48.setText(b[31])
            b = table2
            mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
            counter = -1
            for data12 in mycursor:
                b = data12
                for i in data12:
                    counter += 1
            self.ui2.lineEdit_58.setText(b[4])  # vendor
            self.ui2.lineEdit_64.setText(b[5])  # vendor code
            self.ui2.lineEdit_45.setText(b[3])  # man part number
            self.ui2.lineEdit_46.setText(b[2])  # manufacture

            self.ui2.lineEdit_13.setEnabled(False)
            self.ui2.pushButton.clicked.connect(self.relayadd)
        elif type_of_component == 'Resistor':
            self.ui2.tabWidget.setCurrentIndex(1)
            a = strftime("%Y%m%d", gmtime())  # дата и время
            update_log = a + '(' + log + ')'
            self.ui2.label_69.setText(str(update_log))
            self.ui2.label_65.setEnabled(False)
            mydb = mysql.connector.connect(
                host="mysql.ektos.net",
                user="dpe",
                passwd="dpe",
                database="dpe",
                charset='utf8',
            )
            mycursor = mydb.cursor()
            a = 'Part_Number'
            b = table1
            c = found_item
            fixed1 = ''.join(c.split(")"))
            fixed2 = ''.join(fixed1.split("("))
            fixed3 = ''.join(fixed2.split("'"))
            fixed3 = ''.join(fixed3.split(","))
            mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
            counter = -1
            for data12 in mycursor:
                b = data12
                for i in data12:
                    counter += 1

            self.ui2.lineEdit_24.setText(b[0])
            self.ui2.lineEdit_18.setText(b[1])
            self.ui2.lineEdit_19.setText(b[2])
            self.ui2.lineEdit_20.setText(b[3])
            self.ui2.lineEdit_21.setText(b[4])
            self.ui2.lineEdit_22.setText(b[5])
            self.ui2.boxStatus_15.setCurrentText(b[6])
            self.ui2.boxStatus_2.setCurrentText(b[7])
            self.ui2.lineEdit_25.setText(b[8])
            self.ui2.lineEdit_26.setText(b[9])
            self.ui2.lineEdit_27.setText(b[10])
            self.ui2.lineEdit_28.setText(b[11])
            self.ui2.lineEdit_29.setText(b[12])
            self.ui2.lineEdit_29.setEnabled(False)
            self.ui2.lineEdit_30.setText(b[13])
            self.ui2.lineEdit_31.setText(str(update_log))
            self.ui2.lineEdit_31.setEnabled(False)
            self.ui2.boxStatus_16.setCurrentText(b[15])
            self.ui2.lineEdit_49.setText(b[16])
            self.ui2.lineEdit_50.setText(b[17])
            self.ui2.lineEdit_51.setText(b[18])
            self.ui2.lineEdit_52.setText(b[19])
            self.ui2.lineEdit_53.setText(b[20])
            self.ui2.lineEdit_54.setText(b[21])
            self.ui2.lineEdit_55.setText(b[22])
            self.ui2.lineEdit_56.setText(b[23])
            self.ui2.lineEdit_57.setText(b[24])
            self.ui2.lineEdit_73.setText(b[25])
            self.ui2.lineEdit_85.setText(b[26])
            b = table2
            mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
            counter = -1
            for data12 in mycursor:
                b = data12
                for i in data12:
                    counter += 1
            self.ui2.lineEdit_73.setText(b[4])  # vendor
            self.ui2.lineEdit_85.setText(b[5])  # vendor code
            self.ui2.lineEdit_178.setText(b[3])  # man part number
            self.ui2.lineEdit_201.setText(b[2])  # manufacture

            self.ui2.label_178.setEnabled(False)
            self.ui2.pushButton_2.clicked.connect(self.resistor)
        elif type_of_component == 'Transistor':
            self.ui2.tabWidget.setCurrentIndex(2)
            a = strftime("%Y%m%d", gmtime())  # дата и время
            update_log = a + '(' + log + ')'
            self.ui2.label_107.setText(str(update_log))
            self.ui2.label_103.setEnabled(False)
            mydb = mysql.connector.connect(
                host="mysql.ektos.net",
                user="dpe",
                passwd="dpe",
                database="dpe",
                charset='utf8',
            )
            mycursor = mydb.cursor()
            a = 'Part_Number'
            b = table1
            c = found_item
            fixed1 = ''.join(c.split(")"))
            fixed2 = ''.join(fixed1.split("("))
            fixed3 = ''.join(fixed2.split("'"))
            fixed3 = ''.join(fixed3.split(","))
            mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
            counter = -1
            for data12 in mycursor:
                b = data12
                for i in data12:
                    counter += 1

            self.ui2.lineEdit_65.setText(b[0])
            self.ui2.lineEdit_59.setText(b[1])
            self.ui2.lineEdit_60.setText(b[2])
            self.ui2.lineEdit_61.setText(b[3])
            self.ui2.lineEdit_62.setText(b[4])
            self.ui2.lineEdit_63.setText(b[5])
            self.ui2.boxStatus_14.setCurrentText(b[6])
            self.ui2.boxStatus_3.setCurrentText(b[7])
            self.ui2.lineEdit_66.setText(b[8])
            self.ui2.lineEdit_67.setText(b[9])
            self.ui2.lineEdit_68.setText(b[10])
            self.ui2.lineEdit_69.setText(b[11])
            self.ui2.lineEdit_70.setText(b[12])
            self.ui2.lineEdit_70.setEnabled(False)
            self.ui2.lineEdit_71.setText(b[13])
            self.ui2.lineEdit_71.setEnabled(False)
            self.ui2.lineEdit_72.setText(str(update_log))
            self.ui2.lineEdit_72.setEnabled(False)
            self.ui2.boxStatus_13.setCurrentText(b[15])
            self.ui2.lineEdit_74.setText(b[16])
            self.ui2.lineEdit_75.setText(b[17])
            self.ui2.lineEdit_76.setText(b[18])
            self.ui2.lineEdit_77.setText(b[19])
            self.ui2.lineEdit_78.setText(b[20])
            self.ui2.lineEdit_79.setText(b[21])
            self.ui2.lineEdit_80.setText(b[22])
            self.ui2.lineEdit_81.setText(b[23])
            self.ui2.lineEdit_82.setText(b[24])
            self.ui2.lineEdit_83.setText(b[25])
            self.ui2.lineEdit_84.setText(b[26])
            self.ui2.lineEdit_91.setText(b[27])
            self.ui2.lineEdit_100.setText(b[28])
            b = table2
            mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(b, a, fixed3))
            counter = -1
            for data12 in mycursor:
                b = data12
                for i in data12:
                    counter += 1
            self.ui2.lineEdit_91.setText(b[4])  # vendor
            self.ui2.lineEdit_100.setText(b[5])  # vendor code
            self.ui2.lineEdit_129.setText(b[3])  # man part number
            self.ui2.lineEdit_154.setText(b[2])  # manufacture

            self.ui2.pushButton_3.clicked.connect(self.transistor())


    # def relayadd(self):
    #     a = strftime("%Y%m%d", gmtime())
    #     global update_log
    #     update_log = a + '(' + log + ')'
    #
    #     relay_id = self.ui2.label_2.text()
    #     relay_status = self.ui2.boxStatus_49.currentText()
    #     relay_ektospn = self.ui2.lineEdit_250.text()
    #     relay_part_type = self.ui2.boxStatus_50.currentText()
    #     relay_value = self.ui2.lineEdit_251.text()
    #     relay_manufacture = self.ui2.lineEdit_5.text()
    #     relay_manufacture_pn = self.ui2.lineEdit_6.text()
    #     relay_description = self.ui2.lineEdit_252.text()
    #     relay_schematic_part1 = self.ui2.comboBox_67.currentText()
    #     relay_schematic_part2 = self.ui2.comboBox_68.currentText()
    #     relay_schematic_part3 = self.ui2.comboBox_69.currentText()
    #     relay_pcb_footprint1 = self.ui2.comboBox_70.currentText()
    #     relay_pcb_footprint2 = self.ui2.comboBox_71.currentText()
    #     relay_pcb_footprint3 = self.ui2.comboBox_72.currentText()
    #     relay_pcb_footprint4 = self.ui2.comboBox_73.currentText()
    #     relay_pcb_footprint5 = self.ui2.comboBox_74.currentText()
    #     relay_datasheet = self.ui2.lineEdit_38.text()
    #     realy_vcoil = self.ui2.lineEdit_254.text()
    #     relay_icoil = self.ui2.lineEdit_255.text()
    #     relay_vsw_dc = self.ui2.lineEdit_256.text()
    #     relay_vsw_ac = self.ui2.lineEdit_257.text()
    #     relay_isw_dc = self.ui2.lineEdit_274.text()
    #     relay_isw_ac = self.ui2.lineEdit_285.text()
    #     relay_contact_form = self.lineEdit_287.text()
    #     relay_tmin = self.ui2.lineEdit_218.text()
    #     relay_tmax = self.ui2.lineEdit_232.text()
    #     relay_height = self.ui2.lineEdit_236.text()
    #     relay_lxw = self.ui2.lineEdit_239.text()
    #     relay_m_type = self.ui2.boxStatus_35.currentText()
    #     relay_rohs = self.ui2.boxStatus_53.currentText()
    #     relay_automotivest = self.ui2.boxStatus_54.currentText()
    #     relay_part_class = self.ui2.boxStatus_55.currentText()
    #     relay_notes = self.ui2.lineEdit_258.text()
    #     relay_vendor = self.ui2.boxVendor.currentText()
    #     relay_vendor_code = self.ui2.lineEdit_248.text()
    #     relay_alternative_vendor = self.ui2.boxVendor_2.currentText()
    #     rekay_alternative_vendor_code = self.ui2.lineEdit_259.text()
    #     relay_create = self.ui2.label_14.text()
    #     relay_update = self.ui2.label_17.text()
    #     relay_reviewed = self.ui2.label_19.text()
    #     self.ui2.label_14.setText(update_log)
    #
    #     # # self.ui2.lineEdit_13.setText(update_log)
    #     # part_num = self.ui2.lineEdit_1.text()
    #     # part_type = self.ui2.lineEdit_2.text()
    #     # value = self.ui2.lineEdit_3.text()
    #     # description = self.ui2.lineEdit_4.text()
    #     # # schematic_part = self.ui2.lineEdit_5.text()
    #     # # pcb_footprint = self.ui2.lineEdit_6.text()
    #     # status = self.ui2.boxStatus.currentText()
    #     # rohs = self.ui2.boxStatus_31.currentText()
    #     # datasheet = self.ui2.lineEdit_9.text()
    #     # # image = self.ui2.lineEdit_10.text()
    #     # notes = self.ui2.lineEdit_11.text()
    #     # part_class = self.ui2.lineEdit_12.text()
    #     # # create_date = self.ui2.lineEdit_13.text()
    #     # # rewiew_date = self.ui2.lineEdit_14.text()
    #     # # updaye_date = self.ui2.lineEdit_15.text()
    #     # m_type = self.ui2.boxStatus_32.currentText()
    #     # t_min = self.ui2.lineEdit_33.text()
    #     # t_max = self.ui2.lineEdit_34.text()
    #     # height = self.ui2.lineEdit_35.text()
    #     # automative = self.ui2.lineEdit_36.text()
    #     # vcoil_min = self.ui2.lineEdit_37.text()
    #     # vcoil_nom = self.ui2.lineEdit_38.text()
    #     # vcoil_max = self.ui2.lineEdit_39.text()
    #     # coil_power = self.ui2.lineEdit_40.text()
    #     # max_switch_voltage_dc = self.ui2.lineEdit_41.text()
    #     # max_switch_voltage_ac =self.ui2.lineEdit_42.text()
    #     # max_switch_current_dc = self.ui2.lineEdit_43.text()
    #     # max_switch_current_ac = self.ui2.lineEdit_44.text()
    #     # # latched = self.ui2.boxStatus_28.currentText()
    #     # # polarized_coil = self.ui2.boxStatus_29.currentText()
    #     # # contact_types = self.ui2.lineEdit_47.text()
    #     # # size = self.ui2.lineEdit_48.text()
    #     # # vendor = self.ui2.lineEdit_58.text()
    #     # # vendor_code = self.ui2.lineEdit_64.text()
    #     # # manufacturer = self.ui2.lineEdit_46.text()
    #     # # man_part_number = self.ui2.lineEdit_45.text()
    #     # # create_user = myapp.logpas[0]
    #     # # if self.ui2.label_18.setEnabled == True:
    #     # #     self.ui2.label_18.setText(create_user)
    #     mydb = mysql.connector.connect(
    #         host="mysql.ektos.net",
    #         user="dpe",
    #         passwd="dpe",
    #         database="dpe",
    #         charset='utf8',
    #     )
    #     # if self.ui2.lineEdit_1.text() != '':
    #     #
    #     mycursor = mydb.cursor()
    #     sql = "INSERT INTO test_relay (relay_id, relay_status, relay_ektospn, relay_part_type, relay_value, " \
    #           "relay_manufacture, relay_manufacture_pn, relay_description, relay_schematic_part1, relay_pcb_footprint1," \
    #           " relay_datasheet,realy_vcoil, relay_icoil, relay_vsw_dc, relay_vsw_ac, relay_isw_dc, relay_isw_ac, " \
    #           "relay_contact_form, relay_tmin, relay_tmax, relay_height, relay_lxw, relay_m_type, relay_rohs, " \
    #           "relay_automotivest, relay_part_class, relay_notes) VALUES " \
    #           "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
    #           " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
    #           " %s, %s, %s, %s, %s, %s, %s)"
    #     val = (relay_id, relay_status, relay_ektospn, relay_part_type, relay_value, relay_manufacture, relay_manufacture_pn,
    #            relay_description, relay_schematic_part1, relay_pcb_footprint1, relay_datasheet,realy_vcoil, relay_icoil,
    #            relay_vsw_dc, relay_vsw_ac, relay_isw_dc, relay_isw_ac, relay_contact_form, relay_tmin, relay_tmax,
    #            relay_height, relay_lxw, relay_m_type, relay_rohs, relay_automotivest, relay_part_class, relay_notes,
    #            relay_create, relay_update, relay_reviewed)
    #     mycursor.execute(sql, val)
    #     sql_vendor = "INSERT INTO test_vendor (ektospn, manufacture, manufacture_pn, datasheet, vendor, " \
    #           "vendor_code, create, update, notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    #     val_vendor = (relay_ektospn, relay_manufacture, relay_manufacture_pn, relay_datasheet, relay_vendor,
    #                   relay_vendor_code, relay_create, relay_update, relay_notes)
    #     mycursor.execute(sql_vendor, val_vendor)

            # if self.ui2.lineEdit_13.isEnabled() == False:
            #     try:
            #         mycursor.execute(sql_vendor, val_vendor)
            #         mycursor.execute(sql, val)
            #         self.ui2.label_177.setText("Data recorded succssfully")
            #     except Exception:
            #         x = str(self.ui2.lineEdit_1.text())
            #         mycursor.execute("DELETE FROM ektos_2019_relay WHERE Part_Number = '{}'".format(x))
            #         mycursor.execute("DELETE FROM 2019_ektos_cis_vendors WHERE Part_Number = '{}'".format(x))
            #
            #         # self.ui2.label_265.setText("Duplicate entry for Part Number unique value")
            #         mycursor.execute(sql, val)
            #         mycursor.execute(sql_vendor, val_vendor)
            #         self.ui2.label_177.setText("Data recorded succssfully")
            #     mydb.commit()
            #     self.clear_lines()
            #
            # if self.ui2.lineEdit_13.isEnabled() == True:
            #     try:
            #         mycursor.execute(sql, val)
            #         mycursor.execute(sql_vendor, val_vendor)
            #         self.ui2.label_177.setText("Data recorded succssfully")
            #         self.clear_lines()
            #     except Exception:
            #         self.ui2.label_177.setText("Duplicate entry for Part Number unique value")
            #     mydb.commit()
            # self.ui2.groupBox.setEnabled(True)
            # self.ui2.groupBox_3.setEnabled(True)
            # self.ui2.groupBox_25.setEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    MyApp3 = MainWindow()
    MyApp2 = Second()
    myapp.show()


    sys.exit(app.exec_())



