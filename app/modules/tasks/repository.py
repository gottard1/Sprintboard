import psycopg
from typing import List, Dict, Any
from app.common.database import create_connection
from .models import Task, TaskStatus
from .interfaces import ITaskRepository

class TaskRepository(ITaskRepository):
    """
    Implementação do repositório de tarefas que interage com um banco de dados PostgreSQL.
    """
    def __init__(self):
        pass

    def add(self, description: str, creation_date: str, status: str, due_date: str, urgency: str) -> int:
        # A conexão é criada e fechada para esta operação específica.
        with create_connection() as conn:
            with conn.cursor() as cursor:
                query = """
                    INSERT INTO tasks (description, creation_date, status, due_date, urgency) 
                    VALUES (%s, %s, %s, %s, %s) RETURNING id;
                """
                cursor.execute(query, (description, creation_date, status, due_date, urgency))
                task_id = cursor.fetchone()[0]
                conn.commit()
                return task_id

    def get_all_filtered(self, filters: Dict[str, Any]) -> List[Task]:
        with create_connection() as conn:
            with conn.cursor(row_factory=psycopg.rows.dict_row) as cursor:
                query = "SELECT * FROM tasks WHERE 1=1"
                params = []
                
                if filters.get('status'):
                    query += " AND status = %s"
                    params.append(filters['status'].value)
                
                if filters.get('urgency'):
                    query += " AND urgency = %s"
                    params.append(filters['urgency'])
                
                query += " ORDER BY id;"
                cursor.execute(query, tuple(params))
                return [Task(**row) for row in cursor.fetchall()]

    def update_status(self, task_id: int, status: TaskStatus) -> bool:
        try:
            with create_connection() as conn:
                with conn.cursor() as cursor:
                    query = "UPDATE tasks SET status = %s WHERE id = %s;"
                    cursor.execute(query, (status.value, task_id))
                    conn.commit()
                    return cursor.rowcount > 0
        except Exception as e:
            # O rollback é implícito ao sair do 'with' em caso de erro,
            # mas o importante é capturar e logar o erro.
            print(f"Repository Error on update_status: {e}")
            return False