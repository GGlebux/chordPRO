import os
import sys

from PyQt6.QtWidgets import QApplication

from python_files.app.app import MainApp
from python_files.database import Database

if __name__ == "__main__":
    # Проверка на наличие базы данных
    if os.path.exists('../resources/chords.db'):
        db = Database()
    else:
        db = Database()
        db.insert_chords_from_csv()

    app = QApplication(sys.argv)
    window = MainApp(db)
    window.show()
    sys.exit(app.exec())
