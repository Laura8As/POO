import sqlite3
from tabulate import tabulate


class Dueño:
    def __init__(self,id=0,  nombre="", direccion="", telefono="", correo=""):
        self.id = id                # Identificador único del dueño
        self.nombre = nombre          # Nombre del dueño
        self.direccion = direccion    # Dirección del dueño
        self.telefono = telefono      # Número de teléfono del dueño
        self.correo = correo          # Correo electrónico del dueño
        self.mascotas = []            # Lista para almacenar las mascotas registradas del dueño
        

    def obtener_dueños(self):
        conn = sqlite3.connect("veterinaria.db")
        cursor = conn.cursor()
        dueños =cursor.execute("SELECT * FROM dueños").fetchall()
        conn.close()
        return dueños
    
    def mostrar_dueños(self):
       
        dueños = self.obtener_dueños()
        headers = ["ID", "Nombre", "direccion", "correo"]
        table = tabulate(dueños, headers=headers, tablefmt="grid")
        print(table)    

    
    def guardar_en_db(self):
        query = "INSERT INTO dueños (nombre,direccion,telefono,correo) VALUES (?, ?, ?,?);"
        conn = sqlite3.connect("veterinaria.db")
        cursor = conn.cursor()
        cursor.execute(query, (self.nombre, self.direccion, self.telefono, self.correo))
        conn.commit()
        conn.close()
        
        
   
    

    def actualizar_info(self, nombre=None, direccion=None, telefono=None, correo=None):
        if nombre is not None:
            self.nombre = nombre       # Actualizar el nombre del dueño si se proporciona
        if direccion is not None:
            self.direccion = direccion # Actualizar la dirección del dueño si se proporciona
        if telefono is not None:
            self.telefono = telefono   # Actualizar el número de teléfono del dueño si se proporciona
        if correo is not None:
            self.correo = correo       # Actualizar el correo electrónico del dueño si se proporciona

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Teléfono: {self.telefono}"
