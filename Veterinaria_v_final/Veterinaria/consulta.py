import sqlite3
from tabulate import tabulate

class Consulta:
    def __init__(self, fecha= None, diagnostico= None, tratamiento= None, vacunas= None, id_cita = None, id=None):
        self.id = id 
        self.fecha = fecha
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.vacunas = vacunas
        self.id_cita = id_cita
        self.conn = sqlite3.connect("veterinaria.db")
        
    def guardar_en_db(self):
        query = "INSERT INTO consultas (fecha, diagnostico, tratamiento, vacuna, id_cita) VALUES (?, ?, ?,?,?);"
        
        cursor = self.conn.cursor()
        cursor.execute(query, (self.fecha, self.diagnostico, self.tratamiento, self.vacunas, self.id_cita))
        self.conn.commit()
        self.conn.close()
        
        
       
        
        
    def __str__(self) -> str:
        return f"""
                Fecha: {self.fecha}
                Diagnostico: {self.diagnostico}      
                Tratamiento: {self.tratamiento}
                Vacunas: {self.vacunas}
                N° cita: {self.id_cita}"""    