from flask import Flask
from flask_bcrypt import Bcrypt
from instance.config import config

bcrypt = Bcrypt()

def create_app(config_name: str = 'default') -> Flask:
    """
    Cria e configura uma instância da aplicação Flask.

    Args:
        config_name (str): O nome da configuração a ser usada (ex: 'development').

    Returns:
        Flask: A instância da aplicação Flask configurada.
    """
    app = Flask(__name__, instance_relative_config=True)
    
    # Carrega a configuração a partir do objeto
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Inicializa extensões
    bcrypt.init_app(app)

    # Registra os Blueprints (módulos) da aplicação
    from .modules.tasks.routes import tasks_bp
    app.register_blueprint(tasks_bp)
    
    from .modules.users.routes import users_bp
    app.register_blueprint(users_bp)
    
    return app