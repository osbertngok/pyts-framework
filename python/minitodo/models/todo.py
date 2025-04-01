from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from ..dtos.todo_dto import TodoDTO


class Todo(Base):
    __tablename__ = "todos"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    completed: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)

    def to_dto(self) -> TodoDTO:
        return TodoDTO(
            id=self.id,
            title=self.title,
            description=self.description,
            completed=self.completed,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
