import psycopg
from typing import Optional
from app.common.database import create_connection
from .models import User
from .interfaces import IUserRepository

class UserRepository(IUserRepository):
    """
    Implementação do repositório de usuários para PostgreSQL.
    """
    def __init__(self):
        pass

    def add(self, username: str, password_hash: str) -> Optional[User]:
        try:
            with create_connection() as conn:
                with conn.cursor(row_factory=psycopg.rows.dict_row) as cursor:
                    query = "INSERT INTO users (username, password_hash) VALUES (%s, %s) RETURNING *;"
                    cursor.execute(query, (username, password_hash))
                    user_data = cursor.fetchone()
                    conn.commit()
                    return User(**user_data) if user_data else None
        except psycopg.errors.UniqueViolation:
            return None

    def get_by_username(self, username: str) -> Optional[User]:
        with create_connection() as conn:
            with conn.cursor(row_factory=psycopg.rows.dict_row) as cursor:
                query = "SELECT * FROM users WHERE username = %s;"
                cursor.execute(query, (username,))
                user_data = cursor.fetchone()
                return User(**user_data) if user_data else None