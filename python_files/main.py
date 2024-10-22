import sys

from PyQt6.QtWidgets import QApplication

from python_files.app.app import MainApp
from python_files.database import Database

if __name__ == "__main__":
    with Database() as db:
        app = QApplication(sys.argv)
        db.insert_chords_from_csv()
        window = MainApp(db)
        window.show()
        sys.exit(app.exec())

