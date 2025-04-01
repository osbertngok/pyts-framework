"""
This module contains the dependency injection for the minitodo application.
"""

import os
from typing import Annotated, NewType

from fastapi import Depends
from minitodo.services.todoeservice import TodoService
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def get_db_path() -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_dir_path = os.path.join(current_dir, "data", "dynamic")
    if not os.path.exists(db_dir_path):
        os.makedirs(db_dir_path)
    return os.path.join(db_dir_path, "minitodo.db")


DBPathStr = NewType("DBPathStr", str)
AnnotatedDBPathStr = Annotated[DBPathStr, Depends(get_db_path)]


def get_engine(path: AnnotatedDBPathStr) -> Engine:
    return create_engine(path)


AnnotatedEngine = Annotated[Engine, Depends(get_engine)]


def get_todo_service(engine: AnnotatedEngine) -> TodoService:
    return TodoService(engine)


AnnotatedTodoService = Annotated[TodoService, Depends(get_todo_service)]
