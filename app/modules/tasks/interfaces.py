from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from .models import Task, TaskStatus

class ITaskRepository(ABC):
    """Define a interface (contrato) para o repositório de tarefas."""

    @abstractmethod
    def add(self, description: str, creation_date: str, status: str, due_date: Optional[str], urgency: str) -> int:
        """Adiciona uma nova tarefa ao banco e retorna seu ID."""
        pass

    @abstractmethod
    def get_all_filtered(self, filters: Dict[str, Any]) -> List[Task]:
        """Busca tarefas com base em um dicionário de filtros dinâmicos."""
        pass

    @abstractmethod
    def update_status(self, task_id: int, status: TaskStatus) -> bool:
        """Atualiza o status de uma tarefa e retorna True em caso de sucesso."""
        pass