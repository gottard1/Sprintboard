class User:
    """Representa um usuário no sistema."""
    def __init__(self, id: int, username: str, password_hash: str):
        self.id = id
        self.username = username
        self.password_hash = password_hash

    def __repr__(self) -> str:
        return f"User(id={self.id}, username='{self.username}')"