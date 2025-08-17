import psycopg
from flask import current_app

def create_connection():
    """
    Cria uma nova conexão com o banco de dados usando a URL de configuração
    armazenada no contexto da aplicação Flask.

    Returns:
        psycopg.Connection: Uma instância de conexão com o banco de dados.
    
    Raises:
        ConnectionError: Se a conexão com o banco de dados falhar.
    """
    try:
        # Pega a URL do banco do arquivo de configuração carregado pelo app
        conn = psycopg.connect(current_app.config['DATABASE_URL'])
        return conn
    except psycopg.OperationalError as e:
        # Lança uma exceção mais clara para a aplicação lidar
        raise ConnectionError(f"Erro ao conectar ao banco de dados: {e}") from e