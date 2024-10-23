from pprint import pprint

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView, QSizePolicy, QMessageBox
from sqlalchemy.orm.sync import clear

from design.main_desing import Ui_MainWindow
from python_files.app.input_dialog import InputDialog
from python_files.models import Chord


class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db

        self.setupUi(self)
        # self.setWindowState(Qt.WindowState.WindowMaximized)
        # self.pixmap = QPixmap('../resources/guitar_neck.png')
        # self.image.setPixmap(self.pixmap)
        # self.image.setFixedSize(1028, 630)

        self.add_button.clicked.connect(self.open_input_dialog)
        self.remove_button.clicked.connect(self.delete_chord)
        self.edit_button.clicked.connect(self.edit_chord)
        self.update_button.clicked.connect(self.update_table)

    def update_table(self):
        """Отображает в таблице всё аккорды из БД"""
        self.empty_interface()
        chords = self.db.get_chords()
        for chord in chords:
            row_count = self.table.rowCount()
            self.table.setRowCount(row_count + 1)
            row_data = chord.super_getter()

            for i, value in enumerate(row_data):
                item = QTableWidgetItem(value)
                self.table.setItem(row_count, i, item)
        new_row = self.table.rowCount()
        self.table.setCurrentCell(new_row, 1)

    def add_chord(self, row_data):
        """Добавляет пользовательский аккорд в таблицу и дб"""
        chord = Chord(
            root=row_data[0],
            style=row_data[1],
            finger_position=row_data[2],
            structure=row_data[3],
            difficulty=row_data[4],
            user_defined=bool(row_data[4])
        )
        self.db.insert_chord(chord)
        self.update_table()

    def delete_chord(self):
        """Удаляет пользовательский аккорд из таблицы"""
        cur_row = self.table.currentRow()
        if cur_row != -1:
            id = int(self.table.item(cur_row, 0).text())
            user_defined = True if self.table.item(cur_row, 6).text() == 'True' else False
            if user_defined:
                self.db.delete_chord(id)
                self.update_table()
            else:
                QMessageBox.warning(self, 'Ошибка', 'Вы можете удалить только пользовательские аккорды!')

    def edit_chord(self):
        """Изменяет пользовательский аккорд в таблице"""
        cur_row = self.table.currentRow()
        if cur_row != -1:
            id = int(self.table.item(cur_row, 0).text())
            user_defined = True if self.table.item(cur_row, 6).text() == 'True' else False
        if user_defined:

            pass

    def empty_interface(self):
        self.table.clearContents()
        self.table.setRowCount(0)
        # self.id_box.selectAll()
        # self.note_box.show()
        # self.type_box.clear()
        # self.diff_box.clear()
        # self.user_defined_box.clear()

    def ggwp(self):
        chords = self.db.get_chords()
        print('Элементов в бд === ' + str(len(chords)))

    def open_input_dialog(self):
        dialog = InputDialog(self, self)
        dialog.exec()
