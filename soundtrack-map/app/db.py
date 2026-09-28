import sqlite3
import os

# Define o caminho do banco de dados na raiz do projeto
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'soundtrack_map.db')

def get_db_connection():
    """Abre e retorna uma conexão com o arquivo do banco SQLite."""
    conn = sqlite3.connect(DB_PATH)
    # Permite acessar colunas pelo nome (ex: row['username'])
    conn.row_factory = sqlite3.Row
    # Ativa o suporte a chaves estrangeiras (Foreign Keys)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    """Cria as tabelas no banco de dados SQLite caso ainda não existam."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 1. Tabela de Utilizadores
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    # 2. Tabela de Pins / Marcadores Musicais (Para os próximos passos do mapa)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Pins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            music_url TEXT,
            photo_url TEXT,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
        );
    """)
    
    conn.commit()
    conn.close()