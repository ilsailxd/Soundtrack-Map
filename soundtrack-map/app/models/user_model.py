from app.db import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel:

    @staticmethod
    def create_user(username, email, password):
        """CREATE: Cadastra um novo utilizador no banco SQLite."""
        hashed_password = generate_password_hash(password)
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = "INSERT INTO Users (username, email, password_hash) VALUES (?, ?, ?)"
        cursor.execute(query, (username, email, hashed_password))
        conn.commit()
        conn.close()

    @staticmethod
    def find_by_username(username):
        """READ: Busca um utilizador pelo nome de utilizador."""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = "SELECT id, username, email, password_hash FROM Users WHERE username = ?"
        cursor.execute(query, (username,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return dict(row)
        return None

    @staticmethod
    def find_by_email(email):
        """READ: Busca um utilizador pelo e-mail."""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = "SELECT id, username, email, password_hash FROM Users WHERE email = ?"
        cursor.execute(query, (email,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return dict(row)
        return None

    @staticmethod
    def find_by_id(user_id):
        """READ: Busca um utilizador pelo ID."""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = "SELECT id, username, email, password_hash FROM Users WHERE id = ?"
        cursor.execute(query, (user_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return dict(row)
        return None

    @staticmethod
    def update_password(user_id, new_password):
        """UPDATE: Atualiza a senha de um utilizador pelo ID."""
        hashed_password = generate_password_hash(new_password)
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = "UPDATE Users SET password_hash = ? WHERE id = ?"
        cursor.execute(query, (hashed_password, user_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_user(user_id):
        """DELETE: Remove um utilizador do banco de dados pelo ID."""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = "DELETE FROM Users WHERE id = ?"
        cursor.execute(query, (user_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def verify_password(stored_password_hash, password_input):
        """Verifica se a senha digitada coincide com a hash armazenada."""
        return check_password_hash(stored_password_hash, password_input)