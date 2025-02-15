import sqlite3
import pandas as pd

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


class MostrarRecordatorios:
    def __init__(self, conexion):
        self.conexion = conexion

    def mostrar_recordatorio(self):
        try:
            query = """
                        SELECT usuario.nombre_user, usuario.apellido_user, recordatorio_datos.titulo_recordatorio, recordatorio_datos.contenido_recordatorio
                        FROM usuario
                        JOIN recordatorio_datos ON usuario.usuario_ID = recordatorio_datos.usuario_ID
                    """
            resultado_df = pd.read_sql_query(query,self.conexion.conn)
            if not resultado_df.empty:
                print(resultado_df)
            else:
                print("No se encuentran recordatorios.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}")

ruta_db = "C:/Users/POWER/recordatorios_proyecto_2.db"
conexion = ConexionBD(ruta_db)
