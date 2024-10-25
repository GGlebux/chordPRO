from PyQt6.QtWidgets import QDialog

from design.input_dialog import Ui_Dialog


class InputDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None, main_app=None, data=None):
        super().__init__(parent)
        self.setupUi(self)
        self.main_app = main_app
        self.is_edit = False
        self.id = None
        self.save_button.setText('Добавить')

        if data:
            self.save_button.setText('Изменить')
            self.id = data[0]
            self.is_edit = True
            self.input_note_box.setCurrentText(data[1])
            self.input_type_box.setCurrentText(data[2])
            self.input_figner_position.setText(data[3])
            self.input_structure.setText(data[4])
            self.input_diff_box.setCurrentText(data[5])


        self.save_button.clicked.connect(self.save_form)

    def save_form(self):
        """Сохраняет данные из формы (диалогового окна) в таблицу"""
        note = self.input_note_box.currentText()
        style = self.input_type_box.currentText()
        fingering = self.input_figner_position.text()
        structure = self.input_structure.text()
        diff = self.input_diff_box.currentText()
        # ToDo: Подключить автоматическую проверку на сложность аккорда при отсутвии данных из модуля {dev}
        form_data = {'id': self.id,
                     'root': note,
                     'style': style,
                     'finger_position': fingering if fingering else '-',
                     'structure': structure if structure else '-',
                     'difficulty': diff,
                     'user_defined': True}
        if self.is_edit:
            self.main_app.save_edit_chord(form_data)
        else:
            self.main_app.add_chord(form_data)
        self.close()
