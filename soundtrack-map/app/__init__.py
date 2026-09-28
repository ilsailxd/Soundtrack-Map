
import os
from flask import Flask
from app.db import init_db
from app.controllers.auth_controller import auth_bp
from app.middleware import auth_middleware

def create_app():
    views_folder = os.path.join(os.path.dirname(__file__), 'views')
    app = Flask(__name__, template_folder=views_folder)

    app.config['SECRET_KEY'] = 'soundtrack-map-chave-secreta-2026'

    # Inicializa o banco de dados SQLite
    init_db()

    app.before_request(auth_middleware)
    app.register_blueprint(auth_bp)

    return app