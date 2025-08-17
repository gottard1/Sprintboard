from flask import Blueprint

# O Blueprint aponta para as pastas de templates e static na raiz do app
tasks_bp = Blueprint(
    'tasks',
    __name__,
    template_folder='../../templates',
    static_folder='../../static'
)