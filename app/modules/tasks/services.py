from typing import List, Optional, Dict, Any
from .models import Task, TaskStatus
from .interfaces import ITaskRepository

class TaskService:
    """
    Implementa a lógica de negócio para o gerenciamento de tarefas.
    """
    def __init__(self, repository: ITaskRepository):
        self.repo = repository

    def create_new_task(self, task_data: Dict[str, Any]) -> Optional[int]:
        """
        Cria uma nova tarefa a partir de um dicionário de dados.

        Args:
            task_data (Dict[str, Any]): Dicionário com os dados da tarefa.

        Returns:
            Optional[int]: O ID da tarefa criada ou None em caso de falha.
        """
        description = task_data.get('description')
        creation_date = task_data.get('creation_date')
        if not description or not creation_date:
            return None
        
        return self.repo.add(
            description=description,
            creation_date=creation_date,
            status=task_data.get('status', 'PENDING'),
            due_date=task_data.get('due_date'),
            urgency=task_data.get('urgency', 'NORMAL')
        )

    def get_filtered_tasks(self, filters: Dict[str, Any]) -> List[Task]:
        """Prepara os filtros e busca as tarefas."""
        status_str = filters.get('status')
        if status_str and status_str != 'All':
            try:
                filters['status'] = TaskStatus(status_str.upper())
            except ValueError:
                return []
        else:
            filters.pop('status', None)
        
        return self.repo.get_all_filtered(filters)

    def update_task_status(self, task_id: int, status_str: str) -> bool:
        """Valida e atualiza o status de uma tarefa."""
        try:
            status_enum = TaskStatus(status_str.upper())
            return self.repo.update_status(task_id, status_enum)
        except ValueError:
            return False