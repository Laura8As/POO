import sqlite3


class BaseDeDatos:
    def __init__(self, db_name="veterinaria.db"):
        self.conn = sqlite3.connect(db_name)
        self.crear_tablas()

    def crear_tablas(self):
        query = '''
        CREATE TABLE IF NOT EXISTS dueños (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            direccion TEXT,
            telefono TEXT,
            correo TEXT
        );
        CREATE TABLE IF NOT EXISTS mascotas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            especie TEXT,
            id_dueño INTEGER,
            edad INTEGER,
            FOREIGN KEY (id_dueño) REFERENCES dueños(id)
        );
        
        CREATE TABLE IF NOT EXISTS servicios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            costo REAL
        );
        CREATE TABLE IF NOT EXISTS citas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            hora TEXT,
            motivo TEXT,
            id_mascota INTEGER,
            id_veterinario INTEGER,
            id_servicio INTEGER,
            FOREIGN KEY (id_mascota) REFERENCES mascotas(id),
            FOREIGN KEY (id_veterinario) REFERENCES veterinarios(id),
            FOREIGN KEY ( id_servicio) REFERENCES servicios(id)
        );
        CREATE TABLE IF NOT EXISTS veterinarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            especializacion TEXT,
            horarios_disponibles TEXT
        );
        CREATE TABLE IF NOT EXISTS usuarios (
            username TEXT PRIMARY KEY,
            password TEXT
        );
        '''
        self.conn.executescript(query)
        self.conn.commit()
    
