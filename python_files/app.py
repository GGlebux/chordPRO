from pprint import pprint

from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem

from design.desing import Ui_MainWindow


class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setupUi(self)
        # self.update_ui()
        self.pushButton.clicked.connect(self.ggwp)

    def update_ui(self):
        self.model = QStandardItemModel()
        self.tableWidget.setItemMo(self.model)

    def add_row(self):
        chords = self.db.get_chords()
        for chord in chords:
            row_data = [
                str(chord.id),
                chord.root,
                chord.style,
                chord.finger_position,
                chord.structure,
            ]
            # Создаем список элементов модели
            items = [QStandardItem(str(value)) for value in row_data]
            # Добавляем строку в модель
            self.model.appendRow(items)

    def ggwp(self):
        chords =  self.db.get_chords()
        pprint(chords)