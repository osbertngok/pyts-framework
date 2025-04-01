from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status

from ..di import AnnotatedTodoService
from ..dtos.todo_dto import TodoCreateDTO, TodoDTO, TodoUpdateDTO

router = APIRouter(prefix="/api/v1/todos", tags=["todos"])


@router.get("/", response_model=List[TodoDTO])
async def get_todos(
    todo_service: AnnotatedTodoService,
) -> List[TodoDTO]:
    """Get all todos with optional filtering by completion status."""
    return todo_service.get_todos()


@router.get("/{todo_id}", response_model=TodoDTO)
async def get_todo(todo_id: int, todo_service: AnnotatedTodoService) -> TodoDTO:
    """Get a specific todo by ID."""
    todo = todo_service.get_todo(todo_id)
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with ID {todo_id} not found",
        )
    return todo


@router.post("/", response_model=TodoDTO, status_code=status.HTTP_201_CREATED)
async def create_todo(
    todo_create: TodoCreateDTO, todo_service: AnnotatedTodoService
) -> TodoDTO:
    """Create a new todo."""
    return todo_service.create_todo(
        title=todo_create.title, description=todo_create.description
    )


@router.put("/{todo_id}", response_model=TodoDTO)
async def update_todo(
    todo_id: int, todo_update: TodoUpdateDTO, todo_service: AnnotatedTodoService
) -> TodoDTO:
    """Update an existing todo."""
    updated_todo = todo_service.update_todo(
        todo_id,
        title=todo_update.title,
        description=todo_update.description,
        completed=todo_update.completed,
    )
    if not updated_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with ID {todo_id} not found",
        )
    return updated_todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int, todo_service: AnnotatedTodoService) -> None:
    """Delete a todo by ID."""
    success = todo_service.delete_todo(todo_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with ID {todo_id} not found",
        )
    return None
