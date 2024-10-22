from PyQt6.QtWidgets import QDialog

from design.input_dialog import Ui_Dialog
from python_files.models import Chord


class InputDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None, main_app=None):
        super().__init__(parent)
        self.setupUi(self)
        self.main_app = main_app

        self.save_button.clicked.connect(self.save_form)

    def save_form(self):
        """Сохраняет данные из формы (диалогового окна) в таблицу"""
        note = self.input_note_box.currentText()
        style = self.input_type_box.currentText()
        fingering = self.input_figner_position.text()
        structure = self.input_structure.text()
        diff = self.input_diff_box.currentText()
        # ToDo: Подключить автоматическую проверку на сложность аккорда при отсутвии данных из модуля {dev}
        form_data = [note, style,
                     fingering if fingering else '-',
                     structure if structure else '-', diff, 'True']

        self.main_app.add_chord(form_data)
        self.close()
