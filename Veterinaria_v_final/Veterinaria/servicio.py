import sqlite3
from tabulate import tabulate
class Servicio:
    def __init__(self, id=None, nombre=None, costo=None):
        self.id = id          # Identificador único del servicio
        self.nombre = nombre  # Nombre del servicio (ej. Vacunación, Cirugía, etc.)
        self.costo = costo    # Costo del servicio
        self.conn = sqlite3.connect("veterinaria.db")
    
    def mostrar_servicio(self):
        conn = sqlite3.connect("veterinaria.db")
        cursor = conn.cursor()
        veterinarios =cursor.execute("SELECT * FROM servicios").fetchall()
        conn.close()
        dueños = veterinarios
        headers = [ "ID", "nombre", "costo"]
        table = tabulate(dueños, headers=headers, tablefmt="grid")
        print(table)
        
    def obtener_servicio(self, id):
        conn = sqlite3.connect("veterinaria.db")
        cursor = conn.cursor()
        query = "SELECT * FROM servicios WHERE id={}".format(id)      # Actualizar la especie de la mascota si se proporciona
        temp = cursor.execute(query).fetchall()
        conn.close()
        # print(temp)
        servicio = Servicio(temp[0][0], temp[0][1], temp[0][2])     
        # return {"nombre":"hola", "costo":100}
        return servicio
    def __str__(self):
        return f"ID: {self.id}, Servicio: {self.nombre}, Costo: {self.costo}"
