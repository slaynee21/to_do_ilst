# Form implementation generated from reading ui file 'ui_imagedialog.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ImageDialog(object):
    def setupUi(self, ImageDialog):
        ImageDialog.setObjectName("ImageDialog")
        ImageDialog.resize(580, 450)

        self.tabWidget = QtWidgets.QTabWidget(ImageDialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 580, 450))
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.tabWidget.addTab(self.tab, "")

        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(290, 10, 111, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(380, 10, 111, 16))
        self.label_3.setObjectName("label_3")

        self.task_list = QtWidgets.QListWidget(self.tab)
        self.task_list.setGeometry(QtCore.QRect(10, 60, 310, 341))
        self.task_list.setObjectName("task_list")

        self.change_but = QtWidgets.QPushButton(self.tab)
        self.change_but.setGeometry(QtCore.QRect(330, 90, 241, 28))
        self.change_but.setObjectName("change_but")

        self.complite_but = QtWidgets.QPushButton(self.tab)
        self.complite_but.setGeometry(QtCore.QRect(330, 150, 241, 31))
        self.complite_but.setObjectName("complite_but")

        self.complite_mark_but = QtWidgets.QPushButton(self.tab)
        self.complite_mark_but.setGeometry(QtCore.QRect(330, 215, 241, 31))
        self.complite_mark_but.setObjectName("complite_mark_but")

        self.show_comlited_button = QtWidgets.QPushButton(self.tab)
        self.show_comlited_button.setGeometry(QtCore.QRect(330, 280, 241, 31))
        self.show_comlited_button.setObjectName("show_comlited_button")

        self.save_to_file = QtWidgets.QPushButton(self.tab)
        self.save_to_file.setGeometry(QtCore.QRect(330, 345, 241, 31))
        self.save_to_file.setObjectName("save_to_file")

        self.dateEdit = QtWidgets.QDateEdit(self.tab)
        self.dateEdit.setGeometry(QtCore.QRect(290, 30, 90, 22))
        self.dateEdit.setSpecialValueText("")
        self.dateEdit.setObjectName("dateEdit")

        self.dateEdit_2 = QtWidgets.QDateEdit(self.tab)
        self.dateEdit_2.setGeometry(QtCore.QRect(380, 30, 90, 22))
        self.dateEdit_2.setObjectName("dateEdit_2")

        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.dateEdit_2.setDate(QtCore.QDate.currentDate())

        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 281, 22))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(470, 27, 90, 28))
        self.pushButton.setObjectName("pushButton")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.complited_task_list = QtWidgets.QListWidget(self.tab_2)
        self.complited_task_list.setGeometry(QtCore.QRect(10, 50, 301, 371))
        self.complited_task_list.setObjectName("task_list")

        self.back_but = QtWidgets.QPushButton(self.tab_2)
        self.back_but.setGeometry(QtCore.QRect(10, 10, 41, 28))
        self.back_but.setObjectName("back_but")

        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(ImageDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ImageDialog)

        self.addf()

    def addf(self):
        self.pushButton.clicked.connect(lambda: self.add_button())
        self.change_but.clicked.connect(lambda: self.change_button())
        self.complite_but.clicked.connect(lambda: self.complited_button())
        self.complite_mark_but.clicked.connect(lambda: self.mark_selected_button())
        self.back_but.clicked.connect(lambda : self.tabWidget.setCurrentIndex(0))
        self.save_to_file.clicked.connect(lambda : self.save_tasks_to_file())
        self.show_comlited_button.clicked.connect(lambda : self.tabWidget.setCurrentIndex(1))
        self.task_list.itemChanged.connect(lambda: self.task_list.closePersistentEditor(self.task_list.currentItem()))
        self.task_list.itemSelectionChanged.connect(lambda: self.task_list.closePersistentEditor(self.task_list.currentItem()))

    def add_button(self):
        if(self.lineEdit.text()!=""):
            if(self.dateEdit.date()==QtCore.QDate.currentDate()):
                item = QtWidgets.QListWidgetItem()
                item.setCheckState(QtCore.Qt.CheckState.Unchecked)
                item.setText(self.lineEdit.text())
                self.task_list.addItem(item)
                self.lineEdit.setText("")
                self.dateEdit.setDate(QtCore.QDate.currentDate())
                self.dateEdit_2.setDate(QtCore.QDate.currentDate())
            elif(self.dateEdit_2.date()==QtCore.QDate.currentDate()):
                item = QtWidgets.QListWidgetItem()
                item.setCheckState(QtCore.Qt.CheckState.Unchecked)
                item.setText(self.lineEdit.text()+ " (" + self.dateEdit.text()+ ")")
                self.task_list.addItem(item)
                self.lineEdit.setText("")
                self.dateEdit.setDate(QtCore.QDate.currentDate())
                self.dateEdit_2.setDate(QtCore.QDate.currentDate())
            else:
                item = QtWidgets.QListWidgetItem()
                item.setCheckState(QtCore.Qt.CheckState.Unchecked)
                item.setText(self.lineEdit.text() +" (" +self.dateEdit.text()+" - " +self.dateEdit_2.text()+")")
                self.task_list.addItem(item)
                self.lineEdit.setText("")
                self.dateEdit.setDate(QtCore.QDate.currentDate())
                self.dateEdit_2.setDate(QtCore.QDate.currentDate())


    def complited_button(self):
        self.complited_task_list.addItem(self.task_list.currentItem().text())
        self.task_list.takeItem(self.task_list.currentRow())

    def change_button(self):
        self.task_list.openPersistentEditor(self.task_list.currentItem())

    def mark_selected_button(self):
        items_to_remove = []
        item=self.task_list.item
        for row in range(self.task_list.count()):
            if item(row).checkState()==QtCore.Qt.CheckState.Checked:
                items_to_remove.append(row)
        items_to_remove.sort(reverse=True)
        for i in items_to_remove:
            self.complited_task_list.addItem(self.task_list.item(i).text())
            self.task_list.takeItem(i)


    def save_tasks_to_file(self):
        my_file = open("To Do List.txt", "w")
        my_file.write('Task List:\n')
        for i in range(self.task_list.count()):
            my_file.write(self.task_list.item(i).text()+"\n")
        my_file.write('Completed Tasks:\n')
        for k in range(self.complited_task_list.count()):
            my_file.write(self.complited_task_list.item(k).text()+'\n')
        my_file.close()


    def retranslateUi(self, ImageDialog):
        _translate = QtCore.QCoreApplication.translate
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Tasks"))
        self.change_but.setText(_translate("Dialog", "Change"))
        self.label.setText(_translate("Dialog", "Task name"))
        self.label_2.setText(_translate("Dialog", "Start date"))
        self.label_3.setText(_translate("Dialog", "End date"))
        self.complite_but.setText(_translate("Dialog", "Mark as completed"))
        self.complite_mark_but.setText(_translate("Dialog", "Mark selected as completed"))
        self.show_comlited_button.setText(_translate("Dialog", "Show complited"))
        self.save_to_file.setText(_translate("Dialog", "Save tasks to file"))
        self.pushButton.setText(_translate("Dialog", "Add"))
        self.back_but.setText(_translate("Dialog", "Back"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Complited"))
