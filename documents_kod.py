import os
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
import MySQLdb as mdb
from documents import *
import mimetypes

try:
    connect = mdb.connect('127.0.0.1', 'root', 'root', 'tech_service2')
    cur = connect.cursor()
except mdb.Error as e:
    QMessageBox.critical(None, 'Ошибка', f'Ошибка подключения к бд {e}')

class Documents(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.main_window = main_window

        self.cases = []
        self.documents = []
        self.opici = []

        self.setup_tables()
        self.load_data()
        self.load_cb_departments()
        self.ui.back_pushButton_2.clicked.connect(self.back)
        self.ui.load_doc_btn.clicked.connect(self.upload_doc)


    def setup_tables(self):
        '''установка заголовков для таблиц'''
        try:
            #таблица электронных дел
            self.ui.cases_table.setColumnCount(5)
            self.ui.cases_table.setHorizontalHeaderLabels(['ID', 'Название', 'Подразделение', 'Проверено', 'Архив'])

            #дерево документов
            self.ui.doc_tree.setHeaderLabels(['ID', 'Название', 'Дело', 'Проверки', 'Дата'])

            #таблица описей
            self.ui.opici_table.setColumnCount(4)
            self.ui.opici_table.setHorizontalHeaderLabels(["ID", "Описание", "Дело", "Проверено"])

        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', f'Ошибка таблиц {e}')
            print(e)

    def load_data(self):
        self.load_cases()
        self.load_docs()
        self.load_opici()


    def load_cases(self):
        '''загрузка электронных дел в таблицу'''
        try:
            cur.execute("""select c.id, c.title, d.name, c.completeness_checked, a.name
            from cases c
            left join departments d on c.id_department = d.id 
            left join archive a on c.id_archive = a.id""")

            res = cur.fetchall()

            self.ui.cases_table.setRowCount(0)
            for row_data in res:
                row = self.ui.cases_table.rowCount()
                self.ui.cases_table.insertRow(row)

                for col in range(5):
                    item = QtWidgets.QTableWidgetItem(str(row_data[col]))
                    item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
                    self.ui.cases_table.setItem(row, col, item)

             # Сортировка в PyQt6
            self.ui.cases_table.setSortingEnabled(True)
            self.ui.cases_table.sortByColumn(0, Qt.SortOrder.AscendingOrder)

        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', f'Ошибка запроса дел {e}')
            print(e)
            connect.rollback()

    def load_docs(self):
        """Загрузка документов с названиями дел"""
        try:

            self.ui.doc_tree.clear()
            cur.execute("""SELECT d.id, d.title, c.title,
                CONCAT('Полнота: ', d.completeness_checked,', Подпись: ', d.signature_verified,
                        ', Воспр.: ', d.reproducibility_verified), d.created_at
            FROM documents d
            LEFT JOIN cases c ON d.id_case = c.id
        """)

            res = cur.fetchall()

            for row_data in res:
                item = QtWidgets.QTreeWidgetItem(self.ui.doc_tree)
                for col in range(5):
                    item.setText(col, str(row_data[col]))

        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', f'Ошибка загрузки документов: {e}')


    def load_opici(self):
        """Загрузка описей с цветовой индекацией"""
        try:
            cur.execute("""
            SELECT o.id, o.description, c.title, o.complectness_checked
            FROM opici o
            LEFT JOIN cases c ON o.id_case = c.id
        """)

            res = cur.fetchall()

            self.ui.opici_table.setRowCount(0)
            for row_data in res:
                row = self.ui.opici_table.rowCount()
                self.ui.opici_table.insertRow(row)

                for col in range(4):
                    value = row_data[col]
                    item = QtWidgets.QTableWidgetItem(str(value))

                    self.ui.opici_table.setItem(row, col, item)

        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', f'Ошибка загрузки описей:{e}')
            print(e)
            connect.rollback()

    def load_cb_departments(self):
        '''загрузка подразделений в комбо бокс'''
        try:
            self.ui.status_cb.clear()
            self.ui.status_cb.addItem('Все подразделения', None)
            cur.execute("""select id, name from departments""")
            res = cur.fetchall()

            for i in res:
                self.ui.status_cb.addItem(i[1], i[0])

            connect.commit()

            self.ui.status_cb.currentIndexChanged.connect(self.filter_by_departments)

        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', f'Ошибка подразделений {e}')

    def filter_by_departments(self):
        '''сортировка по подразделениям в Табе электронных дел'''
        try:
            selected_dept_id = self.ui.status_cb.currentData()

            cur.execute("""select c.id, c.title, d.name, c.completeness_checked,
            a.name, c.id_department from cases c 
            left join departments d on c.id_department = d.id
            left join archive a on c.id_archive = a.id""")

            all_cases = cur.fetchall()

            self.ui.cases_table.setRowCount(0)

            for case in all_cases:
                case_id, title, dept_name, checked, archive_name, dept_id = case

                if selected_dept_id is None or dept_id == selected_dept_id:
                    row = self.ui.cases_table.rowCount()
                    self.ui.cases_table.insertRow(row)

                    for col, value in enumerate([case_id, title, dept_name, checked, archive_name]):
                        item = QtWidgets.QTableWidgetItem(str(value))
                        self.ui.cases_table.setItem(row, col, item)

        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', f"Ошибка фильтра {e}")
            print(e)

    def upload_doc(self):
        try:
            selected_case_id = self.get_selected_case_id()
            if not selected_case_id:
                QMessageBox.warning(self, 'Ошибка', 'Сначала выберите дело')
                return

            file_path,_ = QFileDialog.getOpenFileName(self, "Выберите документ", "",
                                                      "Документы (*.pdf *.doc *.docx *.xls *.xlsx *.txt);;"
                                                      "Изображения *.png *.jpg *.jpeg);;Все файлы (*)")

            if not file_path:
                return

            #получаем информацию о файле
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            file_type = mimetypes.guess_type(file_path)[0] or 'application/octet-stream'

            with open(file_path, 'rb') as f:
                file_data = f.read()

            cur.execute("""
                   INSERT INTO documents 
                   (id_case, title, file_name, file_data, file_size, file_type, 
                    completeness_checked, signature_verified, reproducibility_verified, created_at)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
               """, (
                selected_case_id,
                file_name,  # title
                file_name,  # file_name
                file_data,  # file_data
                file_size,  # file_size
                file_type,  # file_type
                0,  # completeness_checked
                0,  # signature_verified
                0  # reproducibility_verified
            ))

            connect.commit()
            QMessageBox.information(self, 'Успех', 'Документ успешно загружен')
            self.load_docs()

        except Exception as e:
            connect.rollback()
            QMessageBox.critical(self, 'Ошибка', f'Ошибка загрузки документа: {e}')
            print(e)

    def get_selected_case_id(self):
        '''получение id выбранного дела'''
        selected_items = self.ui.cases_table.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            id_item = self.ui.cases_table.item(row, 0)
            return int(id_item.text()) if id_item else None
        return None

    def back(self):
        self.close()
        self.main_window.show()













