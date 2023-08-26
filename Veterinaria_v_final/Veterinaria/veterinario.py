import sqlite3
from tabulate import tabulate


class Veterinario:
    def __init__(self, id=None, nombre=None, especializacion=None, horarios_disponibles=None):
        self.id = id                            # Identificador único del veterinario
        self.nombre = nombre                    # Nombre del veterinario
        self.especializacion = especializacion  # Especialización del veterinario
        self.horarios_disponibles = horarios_disponibles  # Lista de horarios disponibles del veterinario
        self.conn = sqlite3.connect("veterinaria.db")

    def mostrar_veterinarios_disponibles(self):
        
        cursor = self.conn.cursor()
        veterinarios =cursor.execute("SELECT * FROM veterinarios").fetchall()
        self.conn.close()
        dueños = veterinarios
        headers = [ "ID", "nombre", "especializacion", "horarios_disponibles"]
        table = tabulate(dueños, headers=headers, tablefmt="grid")
        print(table)    

    
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Especialización: {self.especializacion}"


