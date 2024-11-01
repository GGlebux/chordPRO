import os
import sqlite3
import tempfile
import threading

import scipy.io.wavfile as wave
import sounddevice as sd
import soundfile as sf
import sqlalchemy
import numpy as np

from PyQt6.QtGui import QPixmap, QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

from design.main_desing import Ui_MainWindow
from dev.static_methods import data_to_chord, validate_and_convert
from play_sound.hz_to_guitar_sound import GuitarString
from python_files.app.input import InputDialog
from dev.dict_hz import guitat_position_to_hz


class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.playing = False

        self.setupUi(self)
        self.setWindowTitle('акк0рды')

        # Добавляем изображение грифа
        self.img_path = os.path.abspath('../resources/neck.png')
        self.pixmap = QPixmap(self.img_path)
        self.image.setPixmap(self.pixmap)

        # Расположение точек для рисования аппликатуры
        self.coords = [[(lad, string) for lad in [95, 170, 240, 303, 363, 423, 477, 528, 575, 620, 663]] for
                          string in
                          [40, 62, 86, 110, 132, 157]]

        # Обработчики событий для кнопок
        self.add_button.clicked.connect(self.open_input_dialog)
        self.remove_button.clicked.connect(self.delete_chord)
        self.edit_button.clicked.connect(self.edit_chord)
        self.update_button.clicked.connect(lambda: self.update_table(is_all=True))
        self.search_button.clicked.connect(self.search_chords)
        self.view_button.clicked.connect(self.display_chord)
        self.sound_button.clicked.connect(self.sound)

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
        """Рисует аккорд на label с грифом"""
        cur_row = self.table.currentRow()
        if cur_row != -1:
            fingering = self.table.item(cur_row, 3).text()
            finger = validate_and_convert(fingering)
            if finger:
                qp = QPainter()

                self.pixmap = QPixmap(self.img_path)
                qp.begin(self.pixmap)



                for i in range(len(finger)):
                    if finger[i] >= 0:
                        qp.setBrush(QColor(173, 255, 47))
                        x = self.coords[i][finger[i]][0]
                        y = self.coords[i][finger[i]][1]
                        qp.drawEllipse(x, y, 20, 20)
                    elif finger[i] == -2:
                        qp.setBrush(QColor(255, 0, 0))
                        y = self.coords[i][0][1]
                        x = 50
                        qp.drawEllipse(x, y, 20, 20)
                qp.end()
                self.image.setPixmap(self.pixmap)
            else:
                QMessageBox.warning(self, 'Ошибка', 'Неверный формат аппликатуры!\nКорректный формат: <4,x,3,0,1,1>')

    def empty_interface(self, full=True):
        self.table.clearContents()
        self.table.setRowCount(0)
        self.image.setPixmap(self.pixmap)
        if full:
            self.id_box.setValue(0)
            self.note_box.setCurrentText('')
            self.type_box.setCurrentText('')
            self.diff_box.setCurrentText('')
            self.user_defined_box.setCurrentText('')

    def sound(self):
        """Воспроизводит аккорд"""
        cur_row = self.table.currentRow()
        if cur_row != -1:
            fingering = self.table.item(cur_row, 3).text()
            finger = validate_and_convert(fingering)

            if finger:
                # Список звуков аппликатуры
                sounds = []
                for string, fret in enumerate(finger, start=1):
                    if fret == -2:
                        continue
                    else:
                        frequency = guitat_position_to_hz(string, fret + 1)
                        sound = GuitarString(frequency, duration=3)
                        sounds.append(sound)

                # Добавим паузы между звуками
                offset = 0.2  # Смещение в секундах между звуками
                sample_offset = int(offset * 44100)  # Смещение в сэмплах
                result = []
                for i, sound in enumerate(sounds):
                    padded_sound = np.pad(sound, (sample_offset * i, 0), 'constant')
                    result.append(padded_sound)

                result.reverse()

                # Записываем, открываем, играем
                if not self.playing:
                    self.playing = True

                    def sound_thread():
                        # Создаем отдельные звуковые дорожки
                        sound_tracks = []
                        for u, s in enumerate(result):
                            track = np.zeros_like(result[0])
                            track[:len(s)] = s
                            sound_tracks.append(track)

                        # Объединяем дорожки
                        final_sound = np.sum(sound_tracks, axis=0)

                        with tempfile.NamedTemporaryFile(suffix=".wav", dir=tempfile.gettempdir()) as temp_file:
                            wave.write(temp_file.name, 44100, final_sound)
                            array, smp_rt = sf.read(temp_file.name, dtype='float32')
                            sd.play(array, smp_rt)
                            sd.wait()
                            sd.stop()
                        self.playing = False

                    threading.Thread(target=sound_thread).start()
            else:
                QMessageBox.warning(self, 'Ошибка', 'Невозможно воспроизвести аккорд\n(неверный формат аппликатуры)')

    def display_size_of_table(self):
        size = self.table.rowCount()
        self.len_table.setText(f'Найдено элементов: {size}')

    def open_input_dialog(self, data=None):
        dialog = InputDialog(self, self, data=data)
        dialog.exec()

