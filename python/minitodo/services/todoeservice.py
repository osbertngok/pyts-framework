from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from minitodo.interfaces.services.todoserviceinterface import TodoServiceInterface
from minitodo.dtos.todo_dto import TodoDTO
from minitodo.models.todo import Todo
from typing import List


class TodoService(TodoServiceInterface):
    def __init__(self, engine: Engine):
        self.engine = engine

    def create_todo(self, title: str, description: str) -> TodoDTO:
        with Session(self.engine) as session:
            todo = Todo(title=title, description=description)
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

    def update_todo(self, id: int, title: str, description: str) -> TodoDTO:
        with Session(self.engine) as session:
            todo = session.query(Todo).filter(Todo.id == id).first()
            if todo is None:
                raise ValueError(f"Todo with id {id} not found")
            todo.title = title
            todo.description = description
            session.commit()
            return todo.to_dto()

    def delete_todo(self, id: int) -> None:
        with Session(self.engine) as session:
            todo = session.query(Todo).filter(Todo.id == id).first()
            if todo is None:
                raise ValueError(f"Todo with id {id} not found")
            session.delete(todo)
            session.commit()
