import sqlite3

class ConexionBD:
    def __init__(self, base_datos):
        try:
            self.conn = sqlite3.connect(base_datos)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}")
    
    def cierre_bd(self):
        self.conn.close()
        print("Base de datos cerrada.")

class IngresoRecordatorio:
    def __init__(self,conexion):
        self.conexion = conexion
    def ingresar_recordatorio(self):
        try:
            titulo_recordatorio = str(input("Ingresa el titulo del recordatorio: "))
            contenido_recordatorio = str(input("Ingresa el contenido del recordatorio: "))
            nombre_user = str(input("Ingresa tu nombre de registro: "))
            apellido_user = str(input("Ingresa tu apellido de registro: "))
            self.conexion.cursor.execute("SELECT usuario_ID FROM usuario WHERE nombre_user = ? AND apellido_user = ?", (nombre_user, apellido_user))
            usuario = self.conexion.cursor.fetchone()
            if usuario:
                usuario_id = usuario[0]
                self.conexion.cursor.execute("INSERT INTO recordatorio_datos (titulo_recordatorio, contenido_recordatorio, usuario_ID) VALUES (?,?,?)",(titulo_recordatorio,contenido_recordatorio,usuario_id))
                self.conexion.conn.commit()
                print(f"Recordatorio insertado con exito.")
            else:
                print("Usuario no registrado, no se puede insertar el recordatorio, por favor registrarse primero.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}")

ruta_db = "C:/Users/POWER/recordatorios_proyecto_2.db"
conexion = ConexionBD(ruta_db)



