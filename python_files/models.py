from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, DeclarativeBase, MappedAsDataclass
from sqlalchemy.testing.schema import mapped_column


class Base(MappedAsDataclass, DeclarativeBase):
    pass


class Chord(Base):
    __tablename__ = 'chords'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    root: Mapped[str] = mapped_column(String(10))
    style: Mapped[str] = mapped_column(String(10))
    finger_position: Mapped[str] = mapped_column(String(15), nullable=True)
    structure: Mapped[str] = mapped_column(String(15), nullable=True)
    difficulty: Mapped[str] = mapped_column(String(15), nullable=True)
    user_defined: Mapped[bool] = mapped_column(Boolean)

    def __init__(self, root: str, style: str, finger_position: str, structure: str, difficulty: str,
                 user_defined: bool):
        self.root = root
        self.style = style
        self.finger_position = finger_position
        self.structure = structure
        self.difficulty = difficulty
        self.user_defined = user_defined

    def __str__(self):
        return (f"<Chord(id='{self.id}' root='{self.root}', type='{self.style}', " +
                f"finger_position='{self.finger_position}, structure='{self.structure}'')>")

    def super_getter(self):
        return [
            str(self.id),
            self.root,
            self.style,
            self.finger_position,
            self.structure,
            self.difficulty,
            str(self.user_defined)
        ]
