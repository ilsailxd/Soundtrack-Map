from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models.user_model import UserModel

auth_bp = Blueprint('auth', __name__)

# Rota raiz (/) redirecionando para o login
@auth_bp.route('/')
def index():
    return redirect(url_for('auth.login'))

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('auth.dashboard'))

    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')

        user = UserModel.authenticate(email, password)

        if user:
            session['user'] = {
                'id': user['id'],
                'name': user['name'],
                'email': user['email']
            }
            return redirect(url_for('auth.dashboard'))
        else:
            flash('E-mail ou senha incorretos!', 'danger')

    return render_template('login.html')
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if 'user' in session:
        return redirect(url_for('auth.dashboard'))

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')

        # Tenta cadastrar no Model
        success, message = UserModel.create(name, email, password)

        if success:
            flash(message, 'success')
            return redirect(url_for('auth.login'))
        else:
            flash(message, 'danger')

    return render_template('register.html')

@auth_bp.route('/dashboard')
def dashboard():
    user = session.get('user')
    return render_template('dashboard.html', user=user)

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('Você saiu do sistema.', 'info')
    return redirect(url_for('auth.login'))