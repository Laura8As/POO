from base_de_datos import BaseDeDatos
from usuario import Usuario
from dueño import Dueño
from mascota import Mascota
from cita import Cita
from veterinario import Veterinario
from servicio import Servicio
from tabulate import tabulate
class Veterinaria:
    
    def __init__(self):
        self.base_de_datos = BaseDeDatos()  # Crear instancia de la base de datos
        self.mostrar_dueños = Dueño().mostrar_dueños
        self.mostrar_veterinarios = Veterinario().mostrar_veterinarios_disponibles
        self.mostrar_servicios = Servicio().mostrar_servicio
        self.mostrar_citas = Cita().mostrar_citas
        self.cancelar_cita = Cita().cancelar_cita
        self.mostrar_mascotas = Mascota().mostrar_mascotas
        self.historial_medico = Mascota().historial_medico
        self.obtener_servicio = Servicio().obtener_servicio
        

        
    def run(self):
        while True:
            print("\nBienvenido a la Veterinaria")
            print("1. Iniciar Sesión")
            print("2. Registrar Usuario")
            print("3. Salir")
            opcion = input("Ingrese la opción: ")

            if opcion == "1":
                self.iniciar_sesion()
            elif opcion == "2":
                self.registrar_usuario()
            elif opcion == "3":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor ingrese una opción válida.")
                
                
    def registrar_usuario(self):
        print("Registro de Usuario")
        username = input("Ingrese un nombre de usuario: ")
        password = input("Ingrese una contraseña: ")
        nuevo_usuario = Usuario(username, password)
        nuevo_usuario.guardar_en_db()
        print("*****************  Usuario registrado exitosamente *****************")
        self.run()
    
    def registrar_dueño(self):
        print("Registro de Dueños")
        nombre = input("Ingrese el nombre del dueño: ")
        direccion=  input("Ingrese la dirección del dueñoo: ")
        telefono= input("Ingrese el telefono del dueño: ")
        correo= input("Ingrese el correo del dueño: ")
        
        
        nuevo_dueño = Dueño(nombre=nombre, direccion= direccion, telefono= telefono, correo= correo)
        nuevo_dueño.guardar_en_db()
        print("*****************  Dueño registrado exitosamente *****************")
        self.menu_principal()

    
    def registrar_mascota(self):
        print("Registro de mascotas")
        print("Dueños")
        self.mostrar_dueños()
        print("\n")
        nombre = input("Ingrese el nombre de la mascota: ")
        especie = input("Ingrese la especie: ")
        id_dueño = int(input("Ingrese el id del dueño: "))
        edad = int(input("Ingrese  la edad en años: "))
        nueva_mascota = Mascota(nombre=nombre, especie=especie, id_dueño=id_dueño, edad=edad)
        nueva_mascota.guardar_en_db()
        print("*****************  Mascota registrada exitosamente *****************")
        self.menu_principal()
    
    def agendar_cita(self):
        print("Agendar Cita")
        print("Veterinarios")
        self.mostrar_veterinarios()
        print("\n")
        print("Servicios")
        self.mostrar_servicios()
        print("\n")
        fecha= input("ingrese la fecha para la cita: ")
        hora= input("ingrese la hora: ")
        motivo= input("ingrese el motivo: ") 
        id_mascota= int(input("ingrese el id de la mascota: "))
        id_veterinario= int(input("ingrese el id del veterinario: "))
        id_servicio= int(input("ingrese el id del servicio: "))
        servicio = self.obtener_servicio(id_servicio)
        factura= f"""
            El servicio es: {servicio.nombre}
            total a pagar: {servicio.costo} 
        """
        print(factura)
        nueva_cita = Cita(fecha=fecha, hora=hora, motivo=motivo, mascota=id_mascota, veterinario=id_veterinario, servicio=id_servicio)
        nueva_cita.guardar_en_db()
        print("*****************  Cita registrada exitosamente *****************")
        self.menu_principal()

    def cancelar_cita_agendada(self):
        print("Citas Agendadas")
        self.mostrar_citas()
        id_cita = int(input("ingrese el id de la cita: "))
        self.cancelar_cita(id_cita)
        print("*****************  Cita cancelada *****************")
        self.menu_principal()
        
    
    def mostrar_historial_medico(self):
        print("Mascotas")
        self.mostrar_mascotas()
        id_mascota = int(input("ingresa el id de la mascota: "))
        self.historial_medico(id_mascota)
        self.menu_principal()
    
    def iniciar_sesion(self):
        print("Inicio de Sesión")
        username = input("Usuario: ")
        password = input("Contraseña: ")

        if Usuario.verificar_credenciales(username, password):
            print("Inicio de sesión exitoso.")
            self.menu_principal()
        else:
            print("Credenciales incorrectas.")
            self.iniciar_sesion()

    def menu_principal(self):
        while True:
            print("\nMenú Principal")
            print("1. Registrar Dueño")
            print("2. Registrar Mascota")
            print("3. Agendar Cita")
            print("4. Cancelar Cita")
            print("5. Mostrar Historial Médico")
            print("6. Salir")
            opcion = input("Ingrese la opción: ")

            if opcion == "1":
                self.registrar_dueño()
            elif opcion == "2":
                self.registrar_mascota()
            elif opcion == "3":
                self.agendar_cita()
            elif opcion == "4":
                self.cancelar_cita_agendada()
            elif opcion == "5":
                self.mostrar_historial_medico()
            # elif opcion == "6":
            #     self.agregar_servicio()
            # elif opcion == "7":
            #     self.listar_veterinarios()
            # elif opcion == "8":
            #     self.agregar_veterinario()
            elif opcion == "6":
                print("Volviendo al Menú Principal.")
                break
            else:
                print("Opción inválida. Por favor ingrese una opción válida.")

    # Métodos restantes de la clase Veterinaria
