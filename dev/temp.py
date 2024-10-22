import sys
import tempfile
import threading
from sys import flags

import scipy.io.wavfile as wave
import sounddevice as sd
import soundfile as sf
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QPushButton,
)

from dev.dict_hz import guitat_position_to_hz
from play_sound.hz_to_guitar_sound import GuitarString


# import playsound  # Установите пакет playsound: pip install playsound


class TableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Таблица с звуком")
        self.playing = False

        # Создаем сетку для таблицы
        grid = QGridLayout()
        self.setLayout(grid)

        # Создаем кнопки для каждой ячейки
        for row in range(6):
            for col in range(12):
                button = QPushButton(f"{row + 1},{col}")
                button.setFont(QFont("Arial", 12))
                button.setStyleSheet("background-color: transparent; border: none;")  # Делаем кнопку прозрачной
                button.clicked.connect(lambda checked, r=row + 1, c=col: self.play_sound(r, c))
                grid.addWidget(button, row, col)
            # Рисуем сетку
        self.draw_grid()

    def draw_grid(self):
        # Рисуем линии для ладов
        for i in range(1, 13):
            x = i * 20  # Расстояние между ладами
            line = QWidget(self)
            line.setStyleSheet("background-color: gray;")
            line.setFixedWidth(1)
            line.setFixedHeight(120)
            self.layout().addWidget(line, 0, i, 6, 1)  # Занимает 6 строк, 1 столбец

        # Рисуем линии для струн
        for i in range(1, 7):
            y = i * 20  # Расстояние между струнами
            line = QWidget(self)
            line.setStyleSheet("background-color: gray;")
            line.setFixedWidth(260)
            line.setFixedHeight(1)
            self.layout().addWidget(line, i, 0, 1, 12)  # Занимает 1 строку, 12 столбцов

    def play_sound(self, row, col):
        if not self.playing:
            self.playing = True

            def sound_thread():
                frequency = float(guitat_position_to_hz(row, col))
                sound = GuitarString(frequency, duration=4, toType=True)
                with tempfile.NamedTemporaryFile(suffix=".wav", dir=tempfile.gettempdir()) as temp_file:
                    print(temp_file.name)
                    wave.write(temp_file.name, 44100, sound)
                    array, smp_rt = sf.read(temp_file.name, dtype='float32')
                    sd.play(array, smp_rt)
                    sd.wait()
                    sd.stop()
                self.playing = False

            threading.Thread(target=sound_thread).start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TableWidget()
    widget.show()
    sys.exit(app.exec())
