from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.user_model import UserModel

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if not username or not email or not password:
            flash('Preencha todos os campos!', 'danger')
            return render_template('register.html')

        if UserModel.find_by_email(email):
            flash('E-mail já cadastrado!', 'danger')
            return render_template('register.html')

        if UserModel.find_by_username(username):
            flash('Nome de utilizador já cadastrado!', 'danger')
            return render_template('register.html')

        UserModel.create_user(username, email, password)
        flash('Cadastro realizado com sucesso! Faça seu login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_input = request.form.get('email')
        password = request.form.get('password')

        user = UserModel.find_by_email(login_input)
        if not user:
            user = UserModel.find_by_username(login_input)

        if user and UserModel.verify_password(user['password_hash'], password):
            session['user_id'] = user['id']
            session['user_name'] = user['username']
            return redirect(url_for('auth.dashboard'))

        flash('E-mail/Usuário ou senha incorretos.', 'danger')

    return render_template('login.html')

@auth_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    return render_template('dashboard.html', user={'name': session.get('user_name')})

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
