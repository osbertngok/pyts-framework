from dataclasses import dataclass
from typing import Dict, Any


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
