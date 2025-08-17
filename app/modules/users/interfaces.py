from abc import ABC, abstractmethod
from typing import Optional
from .models import User

class IUserRepository(ABC):
    """Define a interface (contrato) para o repositório de usuários."""

    @abstractmethod
    def add(self, username: str, password_hash: str) -> Optional[User]:
        """
        Adiciona um novo usuário ao banco de dados.

        Returns:
            User: O objeto do usuário criado ou None em caso de falha.
        """
        pass

    @abstractmethod
    def get_by_username(self, username: str) -> Optional[User]:
        """
        Busca um usuário pelo seu nome de usuário.

        Returns:
            User: O objeto do usuário encontrado ou None se não existir.
        """
        pass