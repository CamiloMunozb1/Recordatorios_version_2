import sqlite3  # IMPORTA LA BIBLIOTECA SQLITE3 PARA CONECTAR A LA BASE DE DATOS

# CLASE PARA MANEJAR LA CONEXIÓN A LA BASE DE DATOS
class ConexionBD:
    def __init__(self, base_datos):
        try:
            # SE INTENTA ESTABLECER UNA CONEXIÓN CON LA BASE DE DATOS
            self.conn = sqlite3.connect(base_datos)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            # SI OCURRE UN ERROR AL CONECTAR, SE MUESTRA UN MENSAJE
            print(f"Error en la base de datos: {error}")
    
    def cierre_bd(self):
        """ CIERRA LA CONEXIÓN CON LA BASE DE DATOS """
        self.conn.close()
        print("Base de datos cerrada.")

# CLASE PARA REGISTRAR USUARIOS EN LA BASE DE DATOS
class IngresosUsuarios:
    def __init__(self, conexion):
        # RECIBE UNA INSTANCIA DE ConexionBD PARA REUTILIZAR LA CONEXIÓN
        self.conexion = conexion  

    def ingreso_usuario(self):
        """ MÉTODO PARA INGRESAR UN NUEVO USUARIO EN LA BASE DE DATOS """
        try:
            # SOLICITA DATOS AL USUARIO
            nombre_user = str(input("Ingresa tu nombre: "))
            apellido_user = str(input("Ingresa tu apellido: "))
            
            # INSERTA LOS DATOS EN LA TABLA usuario
            self.conexion.cursor.execute(
                "INSERT INTO usuario (nombre_user, apellido_user) VALUES (?, ?)", 
                (nombre_user, apellido_user)
            )
            
            # CONFIRMA LOS CAMBIOS EN LA BASE DE DATOS
            self.conexion.conn.commit()
            
            print(f"El usuario {nombre_user} {apellido_user} registrado con éxito.")
        
        except sqlite3.Error as error:
            # CAPTURA ERRORES RELACIONADOS CON SQLITE
            print(f"Fallo en la base de datos: {error}")

# SE DEFINE LA RUTA DE LA BASE DE DATOS
ruta_db = "C:/Users/POWER/recordatorios_proyecto_2.db"

# SE CREA UNA INSTANCIA DE ConexionBD PARA ESTABLECER LA CONEXIÓN
conexion = ConexionBD(ruta_db)
