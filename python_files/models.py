from sqlalchemy import String, Integer
from sqlalchemy.dialects import registry
from sqlalchemy.orm import Mapped, DeclarativeBase, MappedAsDataclass
from sqlalchemy.testing.schema import mapped_column


# reg = registry()

class Base(MappedAsDataclass, DeclarativeBase):
    pass


# @reg.mapped_as_dataclass
class Chord(Base):
    __tablename__ = 'chords'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    root: Mapped[str] = mapped_column(String(10))
    style: Mapped[str] = mapped_column(String(10))
    finger_position: Mapped[str] = mapped_column(String(15), nullable=True)
    structure: Mapped[str] = mapped_column(String(15), nullable=True)

    def __init__(self, root: str, style: str, finger_position: str, structure: str):
        self.root = root
        self.style = style
        self.finger_position = finger_position
        self.structure = structure

    def __str__(self):
        return (f"<Chord(id='{self.id}' root='{self.root}', type='{self.style}', " +
                f"finger_position='{self.finger_position}, structure='{self.structure}'')>")

    def get_id(self):
        return self.id