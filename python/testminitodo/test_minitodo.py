import os

from minitodo.interfaces.services.todoserviceinterface import TodoServiceInterface
from minitodo.models.todo import Todo
from minitodo.services.todoeservice import TodoService
from pytest import fixture
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session


class TestMinitodo:

    @fixture
    def db(self) -> Engine:
        db_path = os.path.join(os.path.dirname(__file__), "data", "test_minitodo.db")
        if os.path.exists(db_path):
            os.remove(db_path)
        engine = create_engine(f"sqlite:///{db_path}")
        with Session(engine) as session:
            Todo.__table__.create(bind=engine)
            session.commit()
        return engine

    @fixture
    def todo_service(self, db: Engine) -> TodoServiceInterface:
        return TodoService(db)

    def test_create_todo(self, todo_service: TodoServiceInterface):
        todo = todo_service.create_todo("Test Todo", "Test Description")
        assert todo.title == "Test Todo"
        assert todo.description == "Test Description"
        assert todo.completed == False
