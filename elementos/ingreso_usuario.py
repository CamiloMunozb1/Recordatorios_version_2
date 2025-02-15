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

class IngresosUsuarios:
    def __init__(self,conexion):
        self.conexion = conexion

    def ingreso_usuario(self):
        try:
            nombre_user = str(input("Ingresa tu nombre: "))
            apellido_user = str(input("Ingresa tu apellido: "))
            self.conexion.cursor.execute("INSERT INTO usuario (nombre_user, apellido_user) VALUES (?,?)",(nombre_user,apellido_user))
            self.conexion.conn.commit()
            print(f"el usuario {nombre_user} {apellido_user} registrado con exito.")
        except sqlite3.Error as error:
            print(f"Fallo en la base de datos: {error}")

ruta_db = "C:/Users/POWER/recordatorios_proyecto_2.db"
conexion = ConexionBD(ruta_db)
        