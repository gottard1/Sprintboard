from enum import Enum
from datetime import datetime
from typing import Optional

class TaskStatus(Enum):
    """Enumeração para os status possíveis de uma tarefa."""
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"

class Task:
    """Representa uma tarefa no sistema."""
    def __init__(self, id: int, description: str, creation_date: datetime, status: str, due_date: Optional[datetime], urgency: str):
        self.id = id
        self.description = description
        self.creation_date = creation_date
        self.status = TaskStatus(status)
        self.due_date = due_date
        self.urgency = urgency

    def __repr__(self) -> str:
        return f"Task(id={self.id}, description='{self.description}', status='{self.status.value}')"