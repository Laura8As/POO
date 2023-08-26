
import sqlite3
from tabulate import tabulate
class Mascota:
    
    def __init__(self, id=None, nombre=None, especie=None, id_dueño=None, edad=None):
        self.id = id                    # Identificador único de la mascota
        self.nombre = nombre            # Nombre de la mascota
        self.especie = especie          # Especie de la mascota (perro, gato, etc.)
        self.id_dueño = id_dueño        # Identificador del dueño al que pertenece la mascota
        self.edad = edad                # Edad de la mascota
        self.conn = sqlite3.connect("veterinaria.db")

    
    def obtener_macotas(self):
        
        cursor = self.conn.cursor()
        mascotas =cursor.execute("SELECT * FROM mascotas").fetchall()
        self.conn.close()
        return mascotas
    
    def mostrar_mascotas(self):
       
        mascotas = self.obtener_macotas()
        headers = ["ID", "nombre", "especie", "id_dueño", "edad"]
        table = tabulate(mascotas, headers=headers, tablefmt="grid")
        print(table)    

    def historial_medico(self, id):
   
        cursor = self.conn.cursor()
        historial =cursor.execute("SELECT c.fecha, c.hora, c.motivo, s.costo FROM mascotas as m inner join citas as c ON m.id = c.id_mascota inner join servicios as s on s.id = c.id_servicio WHERE m.id = ? ", (id,)).fetchall()
        cursor.close()
        headers = ["fecha", "hora", "motivo_consulta", "costo"]
        headers = ["ID", "fecha", "hora", "motivo_consulta", "costo"]
        table = tabulate(historial, headers=headers, tablefmt="grid")
        print(table)   
        
    
    def guardar_en_db(self):
        query = "INSERT INTO mascotas (nombre, especie, id_dueño, edad) VALUES (?, ?, ?,?);"
        conn = sqlite3.connect("veterinaria.db")
        cursor = conn.cursor()
        cursor.execute(query, (self.nombre, self.especie, self.id_dueño, self.edad))
        conn.commit()
        conn.close()
    
    
    def actualizar_info(self, id=None ,nombre=None, especie=None, edad=None):
        
        conn = sqlite3.connect("veterinaria.db")
        
        if nombre is not None:
            query = "UPDATE mascotas SET nombre = ? WHERE id = ?"         # Actualizar el nombre de la mascota si se proporciona
            cursor = conn.cursor()
            cursor.execute(query, (nombre,id ))
            conn.commit()
            conn.close()
        if especie is not None:
            query = "UPDATE mascotas SET especie = ? WHERE id = ?"       # Actualizar la especie de la mascota si se proporciona
            cursor = conn.cursor()
            cursor.execute(query, (especie,id ))
            conn.commit()
            conn.close()
        if edad is not None:
            query = "UPDATE mascotas SET edad = ? WHERE id = ?"             # Actualizar la edad de la mascota si se proporciona
            cursor = conn.cursor()
            cursor.execute(query, (edad,id ))
            conn.commit()
            conn.close()
        
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}"

