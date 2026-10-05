from flask import Flask, redirect, url_for

def create_app():
    app = Flask(__name__, template_folder='views', static_folder='static')
    app.config['SECRET_KEY'] = 'soundtrack_map_secret_key_123'

    # Registo de Blueprints
    from app.controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    # Rota raiz redireciona para o login
    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))

    return app
