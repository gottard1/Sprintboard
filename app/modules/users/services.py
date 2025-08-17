from typing import Optional
from app import bcrypt  # Importa a instância do Bcrypt inicializada na factory
from .models import User
from .interfaces import IUserRepository

class UserService:
    """
    Implementa a lógica de negócio para registro e autenticação de usuários.
    """
    def __init__(self, repository: IUserRepository):
        self.repo = repository

    def register_user(self, username: str, password: str) -> Optional[User]:
        """
        Registra um novo usuário.

        Verifica se o usuário já existe e criptografa a senha antes de salvar.

        Returns:
            User: O objeto do usuário criado ou None se o usuário já existir.
        """
        # 1. Verifica se o usuário já existe
        if self.repo.get_by_username(username):
            return None  # Usuário já existe

        # 2. Criptografa a senha
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

        # 3. Adiciona o novo usuário ao repositório
        return self.repo.add(username, password_hash)

    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        """
        Autentica um usuário.

        Verifica se o usuário existe e se a senha fornecida corresponde à senha
        armazenada (hash).

        Returns:
            User: O objeto do usuário se a autenticação for bem-sucedida, senão None.
        """
        # 1. Busca o usuário pelo username
        user = self.repo.get_by_username(username)
        if not user:
            return None  # Usuário não encontrado

        # 2. Compara a senha fornecida com o hash armazenado
        if bcrypt.check_password_hash(user.password_hash, password):
            return user  # Senha correta
        
        return None  # Senha incorreta