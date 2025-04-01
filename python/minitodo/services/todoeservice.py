from datetime import datetime
from typing import List, Optional

from minitodo.dtos.todo_dto import TodoDTO
from minitodo.interfaces.services.todoserviceinterface import TodoServiceInterface
from minitodo.models.todo import Todo
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session


class TodoService(TodoServiceInterface):
    def __init__(self, engine: Engine):
        self.engine = engine

    def create_todo(self, title: str, description: str) -> TodoDTO:
        with Session(self.engine) as session:
            todo = Todo(
                title=title,
                description=description,
                completed=False,
                created_at=datetime.now().timestamp(),
                updated_at=datetime.now().timestamp(),
            )
            session.add(todo)
            session.commit()
            return todo.to_dto()

    def get_todo(self, id: int) -> TodoDTO:
        with Session(self.engine) as session:
            todo = session.query(Todo).filter(Todo.id == id).first()
            if todo is None:
                raise ValueError(f"Todo with id {id} not found")
            return todo.to_dto()

    def get_todos(self) -> List[TodoDTO]:
        with Session(self.engine) as session:
            todos = session.query(Todo).all()
            return [todo.to_dto() for todo in todos]

    def update_todo(
        self,
        id: int,
        title: Optional[str],
        description: Optional[str],
        completed: Optional[bool],
    ) -> TodoDTO:
        with Session(self.engine) as session:
            todo = session.query(Todo).filter(Todo.id == id).first()
            if todo is None:
                raise ValueError(f"Todo with id {id} not found")
            if title is not None:
                todo.title = title
            if description is not None:
                todo.description = description
            if completed is not None:
                todo.completed = completed
            todo.updated_at = int(datetime.now().timestamp())
            session.commit()
            return todo.to_dto()

    def delete_todo(self, id: int) -> bool:
        with Session(self.engine) as session:
            todo = session.query(Todo).filter(Todo.id == id).first()
            if todo is None:
                return False
            session.delete(todo)
            session.commit()
            return True
