from typing import Protocol, List
from minitodo.dtos.todo_dto import TodoDTO


class TodoServiceInterface(Protocol):
    """
    CRUD for todos
    """

    def create_todo(self, title: str, description: str) -> TodoDTO: ...

    def get_todo(self, id: int) -> TodoDTO: ...

    def get_todos(self) -> List[TodoDTO]: ...

    def update_todo(self, id: int, title: str, description: str) -> TodoDTO: ...

    def delete_todo(self, id: int) -> None: ...
