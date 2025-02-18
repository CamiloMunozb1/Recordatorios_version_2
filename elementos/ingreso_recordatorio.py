import sqlite3  # IMPORTA SQLITE3 PARA EL MANEJO DE LA BASE DE DATOS

# CLASE PARA ESTABLECER LA CONEXIÓN CON LA BASE DE DATOS
class ConexionBD:
    def __init__(self, base_datos):
        try:
            # INTENTA ESTABLECER UNA CONEXIÓN CON LA BASE DE DATOS
            self.conn = sqlite3.connect(base_datos)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            # SI OCURRE UN ERROR AL CONECTAR, SE MUESTRA UN MENSAJE
            print(f"Error en la base de datos: {error}")
    
    def cierre_bd(self):
        # MÉTODO PARA CERRAR LA CONEXIÓN CON LA BASE DE DATOS 
        self.conn.close()
        print("Base de datos cerrada.")

# CLASE PARA INGRESAR RECORDATORIOS A LA BASE DE DATOS
class IngresoRecordatorio:
    def __init__(self, conexion):
        # RECIBE UNA INSTANCIA DE ConexionBD PARA UTILIZAR LA MISMA CONEXIÓN
        self.conexion = conexion  

    def ingresar_recordatorio(self):
        # MÉTODO PARA INGRESAR UN NUEVO RECORDATORIO EN LA BASE DE DATOS 
        try:
            # SOLICITA LOS DATOS AL USUARIO
            titulo_recordatorio = str(input("Ingresa el título del recordatorio: "))
            contenido_recordatorio = str(input("Ingresa el contenido del recordatorio: "))
            nombre_user = str(input("Ingresa tu nombre de registro: "))
            apellido_user = str(input("Ingresa tu apellido de registro: "))

            # CONSULTA SI EL USUARIO EXISTE EN LA BASE DE DATOS
            self.conexion.cursor.execute(
                "SELECT usuario_ID FROM usuario WHERE nombre_user = ? AND apellido_user = ?", 
                (nombre_user, apellido_user)
            )
            
            usuario = self.conexion.cursor.fetchone()  # OBTIENE EL ID DEL USUARIO SI EXISTE

            if usuario:
                usuario_id = usuario[0]  # EXTRAE EL ID DEL USUARIO
                
                # INSERTA EL RECORDATORIO EN LA TABLA recordatorio_datos
                self.conexion.cursor.execute(
                    "INSERT INTO recordatorio_datos (titulo_recordatorio, contenido_recordatorio, usuario_ID) VALUES (?, ?, ?)", 
                    (titulo_recordatorio, contenido_recordatorio, usuario_id)
                )

                # CONFIRMA LOS CAMBIOS EN LA BASE DE DATOS
                self.conexion.conn.commit()
                
                print(f"Recordatorio insertado con éxito.")
            else:
                # MENSAJE SI EL USUARIO NO EXISTE EN LA BASE DE DATOS
                print("Usuario no registrado, no se puede insertar el recordatorio. Por favor, regístrese primero.")

        except sqlite3.Error as error:
            # CAPTURA ERRORES RELACIONADOS CON SQLITE
            print(f"Error en la base de datos: {error}")

# SE DEFINE LA RUTA DE LA BASE DE DATOS
ruta_db = "C:/Users/POWER/recordatorios_proyecto_2.db"

# SE CREA UNA INSTANCIA DE ConexionBD PARA MANTENER LA CONEXIÓN ACTIVA
conexion = ConexionBD(ruta_db)


