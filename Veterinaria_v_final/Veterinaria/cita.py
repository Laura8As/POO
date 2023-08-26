import sqlite3
from tabulate import tabulate

class Cita:
    def __init__(self,  fecha=None, hora=None, motivo=None, mascota=None, veterinario=None,servicio=None, id=None):
        self.id = id                        # Identificador único de la cita
        self.fecha = fecha                  # Fecha de la cita
        self.hora = hora                    # Hora de la cita
        self.motivo = motivo                # Motivo de la cita
        self.mascota = mascota              # Mascota involucrada en la cita
        self.veterinario = veterinario      # Veterinario asignado a la cita
        self.servicio = servicio
        self.conn = sqlite3.connect("veterinaria.db")

    def obtener_citas(self):
        conn = sqlite3.connect("veterinaria.db")
        cursor = conn.cursor()
        duennos =cursor.execute("SELECT * FROM citas").fetchall()
        conn.close()
        return duennos
    
    def mostrar_citas(self):
       
        citas = self.obtener_citas()
        headers = ["ID", "fecha", "hora", "motivo", "mascota", "veterinario","servicio"]
        table = tabulate(citas, headers=headers, tablefmt="grid")
        print(table)    
    
    def guardar_en_db(self):
        query = "INSERT INTO citas (fecha, hora, motivo, id_mascota, id_veterinario,id_servicio) VALUES (?, ?, ?,?,?,?);"
        cursor = self.conn.cursor()
        cursor.execute(query, (self.fecha, self.hora, self.motivo, self.mascota, self.veterinario, self.servicio))
        self.conn.commit()
        # self.conn.close()
    
    def reprogramar_cita(self, fecha=None, hora=None, id=None):
      
        conn = sqlite3.connect("veterinaria.db")
        if fecha is not None:
            query = "UPDATE citas SET fecha = ? WHERE id = ?"     # Actualizar el nombre de la mascota si se proporciona
            cursor = conn.cursor()
            cursor.execute(query, (fecha,id ))
            conn.commit()
            conn.close()
        if hora is not None:
            query = "UPDATE citas SET hora = ? WHERE id = ?"      # Actualizar la especie de la mascota si se proporciona
            cursor = conn.cursor()
            cursor.execute(query, (hora,id ))
            conn.commit()
            conn.close()
        
    def cancelar_cita(self, id):
        query = "DELETE FROM citas WHERE id ={}".format(id)
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()
        self.conn.close()
    
    def __str__(self):
        return f"ID: {self.id}, Fecha: {self.fecha}, Hora: {self.hora}, Motivo: {self.motivo}, Mascota: {self.mascota.nombre}, Veterinario: {self.veterinario.nombre}"

