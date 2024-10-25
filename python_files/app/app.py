import os
import sqlite3

import sqlalchemy
from PyQt6.QtGui import QPixmap, QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

from design.main_desing import Ui_MainWindow
from dev.static_methods import data_to_chord, validate_and_convert
from python_files.app.input import InputDialog


class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db

        self.setupUi(self)

        # Добавляем изображение грифа
        img_path = os.path.abspath('../resources/neck.png')
        self.pixmap = QPixmap(img_path)
        self.image.setPixmap(self.pixmap)

        # Обработчики событий для кнопок
        self.add_button.clicked.connect(self.open_input_dialog)
        self.remove_button.clicked.connect(self.delete_chord)
        self.edit_button.clicked.connect(self.edit_chord)
        self.update_button.clicked.connect(lambda: self.update_table(is_all=True))
        self.search_button.clicked.connect(self.search_chords)
        self.view_button.clicked.connect(self.display_chord)

    def update_table(self, is_all=True, data=None):
        """Отображает в таблице всё аккорды из БД или только полученые."""
        if is_all:
            self.empty_interface()
            chords = self.db.get_chords()
        elif data:
            chords = data
        else:
            chords = []
        self.empty_interface(full=False)
        for chord in chords:
            row_count = self.table.rowCount()
            self.table.setRowCount(row_count + 1)
            row_data = chord.super_getter()
            for i, value in enumerate(row_data):
                item = QTableWidgetItem(value)
                self.table.setItem(row_count, i, item)

        new_row = self.table.rowCount()
        self.table.setCurrentCell(new_row - 1, 0)
        self.display_size_of_table()

    def add_chord(self, row_data):
        """Добавляет пользовательский аккорд в таблицу и бд."""
        chord = data_to_chord(row_data)
        try:
            self.db.insert_chord(chord)
            self.update_table()
        except (sqlalchemy.exc.OperationalError,
                sqlalchemy.exc.IntegrityError,
                sqlalchemy.exc.InvalidRequestError,
                sqlalchemy.exc.StatementError,
                sqlite3.OperationalError) as e:
            QMessageBox.warning(self, 'Ошибка', f"Ошибка при работе с базой данных:\n{e}")

    def delete_chord(self):
        """Удаляет пользовательский аккорд из таблицы"""
        cur_row = self.table.currentRow()
        if cur_row != -1:
            chord_id = int(self.table.item(cur_row, 0).text())
            user_defined = True if self.table.item(cur_row, 6).text() == 'True' else False
            if user_defined:
                try:
                    self.db.delete_chord(chord_id)
                    self.update_table()
                except (sqlalchemy.exc.OperationalError,
                        sqlalchemy.exc.IntegrityError,
                        sqlalchemy.exc.InvalidRequestError,
                        sqlalchemy.exc.StatementError,
                        sqlite3.OperationalError) as e:
                    QMessageBox.warning(self, 'Ошибка', f"Ошибка при работе с базой данных:\n{e}")
            else:
                QMessageBox.warning(self, 'Ошибка', 'Вы можете удалить только пользовательские аккорды!')

    def edit_chord(self):
        """Изменяет пользовательский аккорд в таблице"""
        cur_row = self.table.currentRow()
        if cur_row != -1:
            user_defined = True if self.table.item(cur_row, 6).text() == 'True' else False
            if user_defined:
                data = [self.table.item(cur_row, i).text() for i in range(0, 6)]
                self.open_input_dialog(data=data)
                self.update_table()
            else:
                QMessageBox.warning(self, 'Ошибка', 'Вы можете изменить только пользовательские аккорды!')

    def save_edit_chord(self, row_data):
        """Сохраняет измененный аккорд из таблицы в бд"""
        chord_id = row_data['id']
        del row_data['id']
        try:
            self.db.update_chord(chord_id, row_data)
            self.update_table()
        except (sqlalchemy.exc.OperationalError,
                sqlalchemy.exc.IntegrityError,
                sqlalchemy.exc.InvalidRequestError,
                sqlalchemy.exc.StatementError,
                sqlite3.OperationalError) as e:
            QMessageBox.warning(self, 'Ошибка', f"Ошибка при работе с базой данных:\n{e}")

    def search_chords(self):
        """Ищет аккорды в бд по введенным параметрам"""
        chord_id = self.id_box.value() if self.id_box.value() != 0 else None
        if chord_id:
            input_data = None
        else:
            # Поля пустые -> не передаем их, иначе передаем текст полей
            root = None if not self.note_box.currentText() else self.note_box.currentText()
            chord_style = None if not self.type_box.currentText() else self.type_box.currentText()
            diff = None if not self.diff_box.currentText() else self.diff_box.currentText()
            user_defined = None if not self.user_defined_box.currentText() else self.user_defined_box.currentText()
            input_data = {}
            if root:
                input_data['root'] = root
            if chord_style:
                input_data['style'] = chord_style
            if diff:
                input_data['difficulty'] = diff
            if user_defined:
                input_data['user_defined'] = True if user_defined == 'True' else False
            print('first === ', root, chord_style, diff, user_defined)
        try:
            chords = self.db.get_chord(chord_id=chord_id, data=input_data)
            self.update_table(is_all=False, data=chords)
        except (sqlalchemy.exc.OperationalError,
                sqlalchemy.exc.IntegrityError,
                sqlalchemy.exc.InvalidRequestError,
                sqlalchemy.exc.StatementError,
                sqlite3.OperationalError) as e:
            QMessageBox.warning(self, 'Ошибка', f"Ошибка при работе с базой данных:\n{e}")

    def display_chord(self):
        cur_row = self.table.currentRow()
        if cur_row != -1:
            fingering = self.table.item(cur_row, 3).text()
            finger = validate_and_convert(fingering)
            print('Я АППЛИКАТУРА ===', finger)
            if finger:
                print("Я ТУТА")
                qp = QPainter()
                img_path = os.path.abspath('../resources/neck.png')
                self.pixmap = QPixmap(img_path)
                qp.begin(self.pixmap)

                coords = [[(lad, string) for lad in [95, 170, 240, 303, 363, 423, 477, 528, 575, 620, 663]] for
                          string in
                          [40, 62, 86, 110, 132, 157]]

                for i in range(len(finger)):
                    if finger[i] >= 0:
                        qp.setBrush(QColor(173, 255, 47))
                        x = coords[i][finger[i]][0]
                        y = coords[i][finger[i]][1]
                        qp.drawEllipse(x, y, 20, 20)
                    elif finger[i] == -2:
                        qp.setBrush(QColor(255, 0, 0))
                        y = coords[i][0][1]
                        x = 50
                        qp.drawEllipse(x, y, 20, 20)
                qp.end()
                self.image.setPixmap(self.pixmap)
            else:
                QMessageBox.warning(self, 'Ошибка', 'Неверный формат аппликатуры!\nКорректный формат: <4,x,3,2,1,1>')

    def empty_interface(self, full=True):
        self.table.clearContents()
        self.table.setRowCount(0)
        if full:
            self.id_box.setValue(0)
            self.note_box.setCurrentText('')
            self.type_box.setCurrentText('')
            self.diff_box.setCurrentText('')
            self.user_defined_box.setCurrentText('')

    def display_size_of_table(self):
        size = self.table.rowCount()
        self.len_table.setText(f'Найдено элементов: {size}')

    def open_input_dialog(self, data=None):
        dialog = InputDialog(self, self, data=data)
        dialog.exec()
