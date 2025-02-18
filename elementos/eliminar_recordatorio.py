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

# CLASE PARA ELIMINAR UN RECORDATORIO ESPECÍFICO
class EliminarRecordatorios:
    def __init__(self, conexion):
        # RECIBE UNA INSTANCIA DE ConexionBD PARA USAR LA CONEXIÓN
        self.conexion = conexion

    def eliminacion_recordatorio(self):
        # MÉTODO PARA ELIMINAR UN RECORDATORIO DE UN USUARIO ESPECÍFICO
        try:
            # SOLICITA AL USUARIO EL TÍTULO DEL RECORDATORIO Y SUS DATOS
            titulo_recordatorio = input("Ingresa el título del recordatorio: ").strip()
            nombre_user = input("Ingresa tu nombre de registro: ").strip()
            apellido_user = input("Ingresa tu apellido de registro: ").strip()

            # CONSULTA SI EXISTE EL USUARIO EN LA BASE DE DATOS
            self.conexion.cursor.execute(
                "SELECT usuario_ID FROM usuario WHERE nombre_user = ? AND apellido_user = ?",
                (nombre_user, apellido_user)
            )
            usuario = self.conexion.cursor.fetchone()

            if usuario:
                usuario_id = usuario[0]

                # VERIFICA SI EXISTE UN RECORDATORIO CON EL TÍTULO Y EL ID DEL USUARIO
                self.conexion.cursor.execute(
                    "SELECT * FROM recordatorio_datos WHERE titulo_recordatorio = ? AND usuario_ID = ?",
                    (titulo_recordatorio, usuario_id)
                )
                recordatorio = self.conexion.cursor.fetchone()

                if recordatorio:
                    # SI EXISTE, SE ELIMINA EL RECORDATORIO
                    self.conexion.cursor.execute(
                        "DELETE FROM recordatorio_datos WHERE titulo_recordatorio = ? AND usuario_ID = ?",
                        (titulo_recordatorio, usuario_id)
                    )
                    self.conexion.conn.commit()
                    print("Recordatorio eliminado con éxito.")
                else:
                    print("No se encontró un recordatorio con ese título para este usuario.")
            else:
                print("Usuario no encontrado en la base de datos.")

        except sqlite3.Error as error:
            # CAPTURA ERRORES RELACIONADOS CON SQLITE
            print(f"Error en la base de datos: {error}.")

# SE DEFINE LA RUTA DE LA BASE DE DATOS
ruta_db = "C:/Users/POWER/recordatorios_proyecto_2.db"

# SE CREA UNA INSTANCIA DE ConexionBD PARA MANTENER LA CONEXIÓN ACTIVA
conexion = ConexionBD(ruta_db)
