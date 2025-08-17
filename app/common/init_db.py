import os
import psycopg
from dotenv import load_dotenv

def initialize_database():
    """
    Lê a URL do banco do arquivo .env e cria as tabelas necessárias.
    Este script deve ser executado manualmente para configurar o banco.
    """
    print("Iniciando a configuração do banco de dados...")
    
    # Carrega as variáveis do arquivo .env
    load_dotenv()
    db_url = os.environ.get('DATABASE_URL')

    if not db_url:
        print("Erro: A variável DATABASE_URL não foi encontrada no arquivo .env.")
        return

    conn = None
    try:
        # Conecta ao banco de dados
        conn = psycopg.connect(db_url)
        with conn.cursor() as cursor:
            # Cria a tabela de usuários
            print("Criando tabela 'users' (se não existir)...")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(255) UNIQUE NOT NULL,
                    password_hash VARCHAR(255) NOT NULL
                );
            """)
            
            # Cria a tabela de tarefas
            print("Criando tabela 'tasks' (se não existir)...")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id SERIAL PRIMARY KEY,
                    description VARCHAR(255) NOT NULL,
                    creation_date TIMESTAMP WITH TIME ZONE NOT NULL,
                    status VARCHAR(50) NOT NULL CHECK (status IN ('PENDING', 'IN_PROGRESS', 'COMPLETED', 'CANCELED')),
                    due_date TIMESTAMP WITH TIME ZONE,
                    urgency VARCHAR(50) NOT NULL CHECK (urgency IN ('LOW', 'NORMAL', 'HIGH'))
                );
            """)
            
            # Adicione aqui a criação de outras tabelas se necessário

        # Salva as alterações
        conn.commit()
        print("Tabelas criadas com sucesso!")

    except psycopg.OperationalError as e:
        print(f"Erro de conexão com o banco de dados: {e}")
    finally:
        if conn:
            conn.close()
            print("Conexão com o banco de dados fechada.")

if __name__ == '__main__':
    initialize_database()