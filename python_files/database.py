import csv
import os

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session

from python_files.models import Base, Chord


class Database:
    def __init__(self):
        self.create_db()
        self.insert_chords_from_csv()
        self.Session = sessionmaker(bind=self.engine)

    def __enter__(self):
        self.session = self.Session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.session.commit()
        else:
            self.session.rollback()
        self.session.close()

    def create_db(self):
        """Создает базу данных SQLite и таблицу Chords"""
        if not os.path.exists('../resources/chords.db'):
            self.engine = create_engine("sqlite+pysqlite:///../resources/chords.db",
                                        echo=True)  # sqlite+pysqlite:///:memory:
            Base.metadata.create_all(self.engine)

    def insert_chords_from_csv(self, csv_name='../resources/chords.csv'):
        """Вставляет данные из CSV файла в базу данных SQLite."""

        with open(csv_name, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            next(reader)
            for row in reader:
                chord = Chord(
                    root=row[0],
                    style=row[1],
                    finger_position=row[3],
                    structure=row[2])
                self.session.add(chord)
            csvfile.close()
        self.session.commit()

    def insert_chord(self, chord):
        """Добавляет новый аккорд в базу данных."""

        pass

    def get_chords(self):
        """Возвращает список всех аккордов."""

        return self.session.query(Chord).all()

    def get_chord(self, id, root=None, style=None, structure=None, finger_position=None):
        """Возвращает аккорд по указанным параметрам."""

        pass

    def update_chord(self, chord):
        """Обновляет данные аккорда."""

        pass

    def delete_chord(self, id):
        """Удаляет аккорд из базы данных."""

        pass
