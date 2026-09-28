from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.user_model import UserModel

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Validação simples de campos obrigatórios
        if not username or not email or not password:
            flash('Preencha todos os campos!', 'danger')
            return render_template('register.html')

        # Verifica se o utilizador ou e-mail já existem no banco
        if UserModel.find_by_username(username):
            flash('Nome de utilizador já cadastrado!', 'danger')
            return render_template('register.html')

        if UserModel.find_by_email(email):
            flash('E-mail já cadastrado!', 'danger')
            return render_template('register.html')

        # Cadastra o utilizador no banco SQLite
        UserModel.create_user(username, email, password)
        flash('Registo efetuado com sucesso! Faça login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = UserModel.find_by_username(username)

        # Repara que agora acedemos como dicionário: user['password_hash'] e user['id']
        if user and UserModel.verify_password(user['password_hash'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('auth.dashboard'))

        flash('Utilizador ou senha incorretos!', 'danger')

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Sessão encerrada.', 'info')
    return redirect(url_for('auth.login'))


@auth_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', username=session.get('username'))

@auth_bp.route('/')
def index():
    # Se o utilizador já tem sessão ativa, vai direto para o mapa (dashboard)
    if 'user_id' in session:
        return redirect(url_for('auth.dashboard'))
    
    # Se não estiver logado, vai para a página de login
    return redirect(url_for('auth.login'))

