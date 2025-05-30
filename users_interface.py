# Form implementation generated from reading ui file 'interface/users_interface.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Users_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(629, 397)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget_add_user = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget_add_user.setGeometry(QtCore.QRect(0, 0, 611, 341))
        self.tabWidget_add_user.setObjectName("tabWidget_add_user")
        self.tab_reception = QtWidgets.QWidget()
        self.tab_reception.setObjectName("tab_reception")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout(self.tab_reception)
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.labelReception = QtWidgets.QLabel(parent=self.tab_reception)
        self.labelReception.setObjectName("labelReception")
        self.verticalLayout_1.addWidget(self.labelReception)
        self.checkBox_podpis = QtWidgets.QCheckBox(parent=self.tab_reception)
        self.checkBox_podpis.setObjectName("checkBox_podpis")
        self.verticalLayout_1.addWidget(self.checkBox_podpis)
        self.checkBox_opis = QtWidgets.QCheckBox(parent=self.tab_reception)
        self.checkBox_opis.setObjectName("checkBox_opis")
        self.verticalLayout_1.addWidget(self.checkBox_opis)
        self.checkBox_file = QtWidgets.QCheckBox(parent=self.tab_reception)
        self.checkBox_file.setObjectName("checkBox_file")
        self.verticalLayout_1.addWidget(self.checkBox_file)
        self.tableReception = QtWidgets.QTableWidget(parent=self.tab_reception)
        self.tableReception.setObjectName("tableReception")
        self.tableReception.setColumnCount(0)
        self.tableReception.setRowCount(0)
        self.verticalLayout_1.addWidget(self.tableReception)
        self.btnCheckCompleteness = QtWidgets.QPushButton(parent=self.tab_reception)
        self.btnCheckCompleteness.setObjectName("btnCheckCompleteness")
        self.verticalLayout_1.addWidget(self.btnCheckCompleteness)
        self.labelResultReception = QtWidgets.QLabel(parent=self.tab_reception)
        self.labelResultReception.setObjectName("labelResultReception")
        self.verticalLayout_1.addWidget(self.labelResultReception)
        self.tabWidget_add_user.addTab(self.tab_reception, "")
        self.tab_signatures = QtWidgets.QWidget()
        self.tab_signatures.setObjectName("tab_signatures")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_signatures)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listSignatures = QtWidgets.QListWidget(parent=self.tab_signatures)
        self.listSignatures.setObjectName("listSignatures")
        self.verticalLayout_2.addWidget(self.listSignatures)
        self.textSignatureDetail = QtWidgets.QTextBrowser(parent=self.tab_signatures)
        self.textSignatureDetail.setObjectName("textSignatureDetail")
        self.verticalLayout_2.addWidget(self.textSignatureDetail)
        self.btnRefreshSignatures = QtWidgets.QPushButton(parent=self.tab_signatures)
        self.btnRefreshSignatures.setObjectName("btnRefreshSignatures")
        self.verticalLayout_2.addWidget(self.btnRefreshSignatures)
        self.tabWidget_add_user.addTab(self.tab_signatures, "")
        self.tab_history = QtWidgets.QWidget()
        self.tab_history.setObjectName("tab_history")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_history)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboDepartments = QtWidgets.QComboBox(parent=self.tab_history)
        self.comboDepartments.setObjectName("comboDepartments")
        self.verticalLayout_3.addWidget(self.comboDepartments)
        self.tableHistory = QtWidgets.QTableWidget(parent=self.tab_history)
        self.tableHistory.setObjectName("tableHistory")
        self.tableHistory.setColumnCount(0)
        self.tableHistory.setRowCount(0)
        self.verticalLayout_3.addWidget(self.tableHistory)
        self.textHistory = QtWidgets.QTextEdit(parent=self.tab_history)
        self.textHistory.setObjectName("textHistory")
        self.verticalLayout_3.addWidget(self.textHistory)
        self.tabWidget_add_user.addTab(self.tab_history, "")
        self.tab_files = QtWidgets.QWidget()
        self.tab_files.setObjectName("tab_files")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_files)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comboRequests = QtWidgets.QComboBox(parent=self.tab_files)
        self.comboRequests.setObjectName("comboRequests")
        self.verticalLayout_4.addWidget(self.comboRequests)
        self.listFiles = QtWidgets.QListWidget(parent=self.tab_files)
        self.listFiles.setObjectName("listFiles")
        self.verticalLayout_4.addWidget(self.listFiles)
        self.btnAddFile = QtWidgets.QPushButton(parent=self.tab_files)
        self.btnAddFile.setObjectName("btnAddFile")
        self.verticalLayout_4.addWidget(self.btnAddFile)
        self.btnRemoveFile = QtWidgets.QPushButton(parent=self.tab_files)
        self.btnRemoveFile.setObjectName("btnRemoveFile")
        self.verticalLayout_4.addWidget(self.btnRemoveFile)
        self.tabWidget_add_user.addTab(self.tab_files, "")
        self.tab_reproducibility = QtWidgets.QWidget()
        self.tab_reproducibility.setObjectName("tab_reproducibility")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_reproducibility)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btnLoadDoc = QtWidgets.QPushButton(parent=self.tab_reproducibility)
        self.btnLoadDoc.setObjectName("btnLoadDoc")
        self.verticalLayout_5.addWidget(self.btnLoadDoc)
        self.textReproducibilityResult = QtWidgets.QTextBrowser(parent=self.tab_reproducibility)
        self.textReproducibilityResult.setObjectName("textReproducibilityResult")
        self.verticalLayout_5.addWidget(self.textReproducibilityResult)
        self.tabWidget_add_user.addTab(self.tab_reproducibility, "")
        self.tab_response = QtWidgets.QWidget()
        self.tab_response.setObjectName("tab_response")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_response)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.listResponses = QtWidgets.QListWidget(parent=self.tab_response)
        self.listResponses.setObjectName("listResponses")
        self.verticalLayout_6.addWidget(self.listResponses)
        self.radioApprove = QtWidgets.QRadioButton(parent=self.tab_response)
        self.radioApprove.setObjectName("radioApprove")
        self.verticalLayout_6.addWidget(self.radioApprove)
        self.radioReject = QtWidgets.QRadioButton(parent=self.tab_response)
        self.radioReject.setObjectName("radioReject")
        self.verticalLayout_6.addWidget(self.radioReject)
        self.textResponseComment = QtWidgets.QTextEdit(parent=self.tab_response)
        self.textResponseComment.setObjectName("textResponseComment")
        self.verticalLayout_6.addWidget(self.textResponseComment)
        self.btnSendResponse = QtWidgets.QPushButton(parent=self.tab_response)
        self.btnSendResponse.setObjectName("btnSendResponse")
        self.verticalLayout_6.addWidget(self.btnSendResponse)
        self.tabWidget_add_user.addTab(self.tab_response, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget_add_user = QtWidgets.QTableWidget(parent=self.tab)
        self.tableWidget_add_user.setGeometry(QtCore.QRect(10, 20, 581, 231))
        self.tableWidget_add_user.setObjectName("tableWidget_add_user")
        self.tableWidget_add_user.setColumnCount(0)
        self.tableWidget_add_user.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton.setGeometry(QtCore.QRect(270, 270, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget_add_user.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget_add_user.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Электронные документы"))
        self.labelReception.setText(_translate("MainWindow", "Список дел"))
        self.checkBox_podpis.setText(_translate("MainWindow", "Подписи есть"))
        self.checkBox_opis.setText(_translate("MainWindow", "Опись есть"))
        self.checkBox_file.setText(_translate("MainWindow", "Файл приложен"))
        self.btnCheckCompleteness.setText(_translate("MainWindow", "Проверить комплектность"))
        self.labelResultReception.setText(_translate("MainWindow", "Результат:"))
        self.tabWidget_add_user.setTabText(self.tabWidget_add_user.indexOf(self.tab_reception), _translate("MainWindow", "Прием дел"))
        self.btnRefreshSignatures.setText(_translate("MainWindow", "Обновить список"))
        self.tabWidget_add_user.setTabText(self.tabWidget_add_user.indexOf(self.tab_signatures), _translate("MainWindow", "Проверка подписей"))
        self.tabWidget_add_user.setTabText(self.tabWidget_add_user.indexOf(self.tab_history), _translate("MainWindow", "История взаимодействий"))
        self.btnAddFile.setText(_translate("MainWindow", "Добавить файл"))
        self.btnRemoveFile.setText(_translate("MainWindow", "Удалить выбранный"))
        self.tabWidget_add_user.setTabText(self.tabWidget_add_user.indexOf(self.tab_files), _translate("MainWindow", "Файлы к заявкам"))
        self.btnLoadDoc.setText(_translate("MainWindow", "Загрузить документ"))
        self.tabWidget_add_user.setTabText(self.tabWidget_add_user.indexOf(self.tab_reproducibility), _translate("MainWindow", "Воспроизводимость"))
        self.radioApprove.setText(_translate("MainWindow", "Подтвердить"))
        self.radioReject.setText(_translate("MainWindow", "Отказать"))
        self.btnSendResponse.setText(_translate("MainWindow", "Отправить ответ"))
        self.tabWidget_add_user.setTabText(self.tabWidget_add_user.indexOf(self.tab_response), _translate("MainWindow", "Ответные сообщения"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.tabWidget_add_user.setTabText(self.tabWidget_add_user.indexOf(self.tab), _translate("MainWindow", "Пользователи"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
