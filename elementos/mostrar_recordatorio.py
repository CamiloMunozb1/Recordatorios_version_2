import sqlite3  # IMPORTA SQLITE3 PARA EL MANEJO DE LA BASE DE DATOS
import pandas as pd  # IMPORTA PANDAS PARA MANIPULAR Y MOSTRAR LOS DATOS EN TABLA

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
        """ MÉTODO PARA CERRAR LA CONEXIÓN CON LA BASE DE DATOS """
        self.conn.close()
        print("Base de datos cerrada.")

# CLASE PARA MOSTRAR LOS RECORDATORIOS ALMACENADOS EN LA BASE DE DATOS
class MostrarRecordatorios:
    def __init__(self, conexion):
        # RECIBE UNA INSTANCIA DE ConexionBD PARA USAR LA MISMA CONEXIÓN
        self.conexion = conexion

    def mostrar_recordatorio(self):
        # MÉTODO PARA OBTENER Y MOSTRAR LOS RECORDATORIOS CON SU USUARIO RELACIONADO 
        try:
            # CONSULTA QUE UNE LAS TABLAS usuario Y recordatorio_datos PARA OBTENER LOS RECORDATORIOS CON EL NOMBRE DEL USUARIO
            query = """
                SELECT 
                    usuario.nombre_user, 
                    usuario.apellido_user, 
                    recordatorio_datos.titulo_recordatorio, 
                    recordatorio_datos.contenido_recordatorio
                FROM usuario
                JOIN recordatorio_datos ON usuario.usuario_ID = recordatorio_datos.usuario_ID
            """

            # EJECUTA LA CONSULTA Y GUARDA EL RESULTADO EN UN DATAFRAME DE PANDAS
            resultado_df = pd.read_sql_query(query, self.conexion.conn)

            # SI EL DATAFRAME NO ESTÁ VACÍO, IMPRIME LOS RESULTADOS
            if not resultado_df.empty:
                print(resultado_df)
            else:
                print("No se encuentran recordatorios.")
        
        except sqlite3.Error as error:
            # CAPTURA ERRORES RELACIONADOS CON SQLITE
            print(f"Error en la base de datos: {error}")

# SE DEFINE LA RUTA DE LA BASE DE DATOS
ruta_db = "C:/Users/POWER/recordatorios_proyecto_2.db"

# SE CREA UNA INSTANCIA DE ConexionBD PARA MANTENER LA CONEXIÓN ACTIVA
conexion = ConexionBD(ruta_db)
