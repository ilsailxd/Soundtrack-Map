from app.db import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel:

    @staticmethod
    def create_user(username, email, password):
        hashed_password = generate_password_hash(password)
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = "INSERT INTO Users (username, email, password_hash) VALUES (?, ?, ?)"
        cursor.execute(query, (username, email, hashed_password))
        
        conn.commit()
        conn.close()

    @staticmethod
    def find_by_username(username):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = "SELECT id, username, email, password_hash FROM Users WHERE username = ?"
        cursor.execute(query, (username,))
        row = cursor.fetchone()
        conn.close()
        
        return dict(row) if row else None

    @staticmethod
    def find_by_email(email):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = "SELECT id, username, email, password_hash FROM Users WHERE email = ?"
        cursor.execute(query, (email,))
        row = cursor.fetchone()
        conn.close()
        
        return dict(row) if row else None

    @staticmethod
    def verify_password(stored_password_hash, password_input):
        return check_password_hash(stored_password_hash, password_input)
