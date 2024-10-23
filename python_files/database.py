import csv


from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session

from python_files.models import Base, Chord


class Database:
    def __init__(self):
        """Создает базу данных SQLite и таблицу Chords"""

        self.engine = create_engine("sqlite+pysqlite:///../resources/chords.db",
                                    echo=True)  # sqlite+pysqlite:///:memory:
        Base.metadata.create_all(self.engine)
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

    def insert_chords_from_csv(self, csv_name='../resources/chords.csv', delimiter=',', has_header=True):
        """Вставляет данные из CSV файла в базу данных SQLite."""

        if self.check_db_empty():
            with open(csv_name, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=delimiter)
                if has_header:
                    next(reader)
                for row in reader:
                    chord = Chord(
                        root=row[0],
                        style=row[1],
                        finger_position=row[2],
                        structure=row[3],
                        difficulty=row[4],
                        user_defined=False
                    )
                    self.session.add(chord)
                csvfile.close()
            self.session.commit()

    def check_db_empty(self):
        """Проверяет, пуста ли таблица 'chords' в базе данных."""
        with self.Session() as session:
            count = session.query(Chord).count()
            return count == 0

    def insert_chord(self, chord):
        """Добавляет новый аккорд в базу данных."""

        self.session.add(chord)

    def get_chords(self):
        """Возвращает список всех аккордов."""

        return self.session.query(Chord).all()

    def get_chord(self, id, root=None, style=None, structure=None, finger_position=None):
        """Возвращает аккорд по указанным параметрам."""

        return self.session.query(id)

    def update_chord(self, chord):
        """Обновляет данные аккорда."""

        pass

    def delete_chord(self, id):
        """Удаляет аккорд из базы данных."""
        # ToDo: Тут нельзя использовать номер строки в таблцие для удаления по id из бд
        self.session.query(Chord).filter_by(id=id).delete()
