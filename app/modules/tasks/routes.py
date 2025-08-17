from flask import render_template, request, jsonify, redirect, url_for, session
from . import tasks_bp
from .repository import TaskRepository
from .services import TaskService

# --- Injeção de Dependência ---
# Instanciamos as classes concretas aqui e as injetamos onde necessário.
# Em aplicações maiores, um container de injeção de dependência pode ser usado.
task_repository = TaskRepository()
task_service = TaskService(repository=task_repository)
# -----------------------------

@tasks_bp.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('users.login'))
    return redirect(url_for('tasks.home'))

@tasks_bp.route('/home')
def home():
    if 'user_id' not in session:
        return redirect(url_for('users.login'))
    
    filters = {
        'status': request.args.get('status', 'All'),
        'urgency': request.args.get('urgency')
    }
    tasks = task_service.get_filtered_tasks(filters)
    return render_template('home.html', tasks=tasks)

@tasks_bp.route('/add_task', methods=['POST'])
def add_task():
    if 'user_id' not in session:
        return jsonify({'success': False, 'error': 'Unauthorized'}), 401

    data = request.get_json()
    if not data or not data.get('description'):
        return jsonify({'success': False, 'error': 'Descrição é obrigatória'}), 400

    task_id = task_service.create_new_task(data)
    if task_id:
        return jsonify({'success': True, 'task_id': task_id})
    else:
        return jsonify({'success': False, 'error': 'Falha ao criar tarefa'}), 500

@tasks_bp.route('/update_task_status/<int:task_id>', methods=['POST'])
def update_task_status(task_id):
    if 'user_id' not in session:
        return jsonify({'success': False, 'error': 'Unauthorized'}), 401

    data = request.get_json()
    new_status = data.get('status')
    if not new_status:
        return jsonify({'success': False, 'error': 'Status é obrigatório'}), 400

    if task_service.update_task_status(task_id, new_status):
        return jsonify({'success': True})
    
    return jsonify({'success': False, 'error': 'Falha ao atualizar status'}), 400