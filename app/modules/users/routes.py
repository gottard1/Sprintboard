from flask import render_template, request, redirect, url_for, session
from . import users_bp
from .repository import UserRepository
from .services import UserService

# --- Injeção de Dependência ---
user_repository = UserRepository()
user_service = UserService(repository=user_repository)
# -----------------------------

@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = user_service.authenticate_user(username, password)
        
        if user:
            session['user_id'] = user.id
            return redirect(url_for('tasks.home'))
        else:
            return render_template('login.html', error='Usuário ou senha inválidos.')
    
    return render_template('login.html')

@users_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('users.login'))

@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if not username or not password:
            return render_template('register.html', error='Usuário e senha são obrigatórios.')
        
        if password != confirm_password:
            return render_template('register.html', error='As senhas não coincidem.')

        new_user = user_service.register_user(username, password)

        if new_user:
            # Loga o usuário automaticamente após o registro
            session['user_id'] = new_user.id
            return redirect(url_for('tasks.home'))
        else:
            return render_template('register.html', error='Este nome de usuário já está em uso.')

    return render_template('register.html')