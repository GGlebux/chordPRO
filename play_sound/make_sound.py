import sys
import tempfile
import threading

import scipy.io.wavfile as wave
import sounddevice as sd
import soundfile as sf

from PyQt6.QtWidgets import QApplication, QMainWindow

from design import Ui_MainWindow
from hz_to_guitar_sound import GuitarString


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.playing = False
        self.pushButton.clicked.connect(self.sound)

    def sound(self):
        if not self.playing:
            self.playing = True

            def sound_thread():
                frequency = float(self.doubleSpinBox.text())
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
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
