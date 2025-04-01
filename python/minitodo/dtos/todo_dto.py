from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class TodoDTO:
    id: int
    title: str
    description: str
    completed: bool
    created_at: int
    updated_at: int

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
        }


@dataclass
class TodoCreateDTO:
    title: str
    description: str


@dataclass
class TodoUpdateDTO:
    title: Optional[str]
    description: Optional[str]
    completed: Optional[bool]
