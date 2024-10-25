import csv
from pprint import pprint

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from python_files.models import Base, Chord


class Database:
    def __init__(self, db_file='sqlite+pysqlite:///../resources/chords.db'):
        """Создает базу данных SQLite и таблицу Chords"""

        self.engine = create_engine(db_file,
                                    echo=True)  # sqlite+pysqlite:///:memory:
        Base.metadata.create_all(self.engine)

        self.Session = sessionmaker(bind=self.engine)
        self.sex = self.Session()

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
                    self.sex.add(chord)
                csvfile.close()
            self.sex.commit()

    def check_db_empty(self):
        """Проверяет, пуста ли таблица 'chords' в базе данных."""
        with self.Session() as session:
            count = session.query(Chord).count()
            return count == 0

    def insert_chord(self, chord):
        """Добавляет новый аккорд в базу данных."""
        self.sex.add(chord)
        self.sex.commit()

    def get_chords(self):
        """Возвращает список всех аккордов."""
        return self.sex.query(Chord).all()

    def get_chord(self, chord_id=None, data=None):
        """Возвращает аккорд(ы) по указанным параметрам."""
        res = None
        if chord_id:
            res =  [self.sex.query(Chord).filter_by(id=chord_id).one()]
        if data:
            res = self.sex.query(Chord).filter_by(**data).all()
        return res

    def update_chord(self, chord_id, data):
        """Обновляет данные аккорда."""
        self.sex.query(Chord).filter_by(id=chord_id).update(data)
        self.sex.commit()

    def delete_chord(self, chord_id):
        """Удаляет аккорд из базы данных."""
        self.sex.query(Chord).filter_by(id=chord_id).delete()
        self.sex.commit()
