from pprint import pprint

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView, QSizePolicy
from sqlalchemy.orm.sync import clear

from design.desing import Ui_MainWindow


class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db

        self.setupUi(self)
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.pixmap = QPixmap('../resources/guitar_neck.png')
        self.image.setPixmap(self.pixmap)
        self.image.setFixedSize()

        self.uptadeButton.clicked.connect(self.add_rows)

    def add_rows(self):
        self.empty_table()
        chords = self.db.get_chords()
        for chord in chords:
            row_count = self.table.rowCount()
            self.table.setRowCount(row_count + 1)
            row_data = [
                chord.root,
                chord.style,
                chord.finger_position,
                chord.structure,
                chord.difficulty,
                str(chord.user_defined)
            ]
            for i, value in enumerate(row_data):
                item = QTableWidgetItem(value)
                self.table.setItem(row_count, i, item)
        self.ggwp()

    def empty_table(self):
        self.table.clearContents()
        self.table.setRowCount(0)

    def ggwp(self):
        chords = self.db.get_chords()
        pprint('Элементов в бд ===' + str(len(chords)))
