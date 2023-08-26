import sqlite3
import hashlib


class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()

    def guardar_en_db(self):
        query = "INSERT INTO usuarios (username, password) VALUES (?, ?);"
        conn = sqlite3.connect("veterinaria.db")
        cursor = conn.cursor()
        cursor.execute(query, (self.username, self.password_hash))
        conn.commit()
        conn.close()
    
    @staticmethod
    def verificar_credenciales(username, password):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        query = "SELECT COUNT(*) FROM usuarios WHERE username = ? AND password = ?;"
        conn = sqlite3.connect("veterinaria.db")
        cursor = conn.cursor()
        cursor.execute(query, (username, password_hash))
        result = cursor.fetchone()[0]
        conn.close()
        return result == 1