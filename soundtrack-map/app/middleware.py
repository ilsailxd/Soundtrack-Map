from flask import session, redirect, url_for, request

PUBLIC_ROUTES = ['auth.login', 'auth.register', 'static']

def auth_middleware():
    endpoint = request.endpoint

    if endpoint and endpoint not in PUBLIC_ROUTES:
        if 'user' not in session:
            return redirect(url_for('auth.login'))