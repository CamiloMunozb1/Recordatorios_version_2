import sqlite3  # IMPORTA SQLITE3 PARA LA BASE DE DATOS
import urllib.parse  # PARA ENCODING DE URLS
import webbrowser  # PARA ABRIR EL NAVEGADOR

# CLASE PARA MANEJAR LA CONEXIÓN A LA BASE DE DATOS
class ConexionBD:
    def __init__(self, base_datos):
        try:
            self.conn = sqlite3.connect(base_datos)  # CONECTAR A LA BASE DE DATOS
            self.cursor = self.conn.cursor()  # CREAR UN CURSOR PARA EJECUTAR CONSULTAS
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}")  # MENSAJE DE ERROR EN CASO DE FALLA
    
    def cierre_bd(self):
        self.conn.close()  # CERRAR LA CONEXIÓN A LA BASE DE DATOS
        print("Base de datos cerrada.")  # MENSAJE INDICANDO QUE SE CERRÓ LA BASE DE DATOS

# CLASE PARA MANEJAR EL INGRESO DE RECORDATORIOS AL CALENDARIO
class IngresoCalendario:
    def __init__(self, conexion):
        self.conexion = conexion  # RECIBE LA CONEXIÓN COMO PARÁMETRO
    
    def registro_calendario(self):
        try:
            # SOLICITAR DATOS DEL USUARIO
            titulo_recordatorio = str(input("Ingresa el titulo del recordatorio: "))
            nombre_user = str(input("Ingresa el nombre de registro: "))
            apellido_user = str(input("Ingresa el apellido de registro: "))
            
            # BUSCAR EL ID DEL USUARIO EN LA BASE DE DATOS
            self.conexion.cursor.execute("SELECT usuario_ID FROM usuario WHERE nombre_user = ? AND apellido_user = ?",(nombre_user,apellido_user))
            usuario = self.conexion.cursor.fetchone()
            
            if usuario:
                usuario_id = usuario[0]
                
                # BUSCAR EL CONTENIDO DEL RECORDATORIO ASOCIADO AL USUARIO
                self.conexion.cursor.execute("SELECT contenido_recordatorio FROM recordatorio_datos WHERE titulo_recordatorio = ? AND usuario_id = ?", (titulo_recordatorio, usuario_id))
                recordatorio = self.conexion.cursor.fetchone()
                
                if recordatorio:
                    return titulo_recordatorio, recordatorio[0]  # RETORNAR TÍTULO Y CONTENIDO DEL RECORDATORIO
                else:
                    print("No se encontró ningún recordatorio con ese título.")  # MENSAJE SI NO SE ENCUENTRA EL RECORDATORIO
            else:
                print("No se encontró ese nombre registrado.")  # MENSAJE SI EL USUARIO NO EXISTE
            
            return None, None  # RETORNAR VALORES NULOS SI NO SE ENCUENTRAN DATOS
        
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}")  # MENSAJE DE ERROR EN CASO DE FALLA

    # MÉTODO PARA CREAR UN EVENTO EN GOOGLE CALENDAR
    def crear_evento_google_calendar(self, titulo_recordatorio, contenido_recordatorio):
        try:
            # SOLICITAR LA FECHA DEL RECORDATORIO
            fecha_recordatorio = str(input("Ingresa la fecha del recordatorio (YYYY-MM-DD): "))
            
            # FORMATEAR LAS FECHAS PARA GOOGLE CALENDAR
            fecha_inicio = f"{fecha_recordatorio.replace('-','')}T090000Z"
            fecha_fin = f"{fecha_recordatorio.replace('-','')}T100000Z"
            
            # URL BASE PARA CREAR UN EVENTO EN GOOGLE CALENDAR
            google_url = "https://calendar.google.com/calendar/render?action=TEMPLATE"
            
            # PARÁMETROS QUE SE ENVIARÁN EN LA URL
            parametros = {
                "text": titulo_recordatorio,
                "details": contenido_recordatorio,
                "dates": f"{fecha_inicio}/{fecha_fin}",
            }
            
            # CREAR LA URL DEL EVENTO CON LOS PARÁMETROS
            url_recordatorio = google_url + "&" + urllib.parse.urlencode(parametros)
            
            # IMPRIMIR LA URL DEL RECORDATORIO
            print(f"Se agrega el recordatorio aquí: {url_recordatorio}.")
            
            # ABRIR LA URL EN EL NAVEGADOR PARA CREAR EL EVENTO
            webbrowser.open(url_recordatorio)
        
        except ValueError:
            print("Error de digitación, por favor intentarlo nuevamente.")  # MENSAJE SI HAY ERROR DE FORMATO

# EJECUCIÓN PRINCIPAL DEL PROGRAMA
if __name__ == "__main__":
    ruta_db = "C:/Users/POWER/recordatorios_proyecto_2.db"  # RUTA DE LA BASE DE DATOS
    conexion = ConexionBD(ruta_db)  # CREAR CONEXIÓN A LA BASE DE DATOS

    ingreso = IngresoCalendario(conexion)  # CREAR INSTANCIA DE LA CLASE IngresoCalendario
    titulo_recordatorio, contenido = ingreso.registro_calendario()  # OBTENER DATOS DEL RECORDATORIO
    
    if contenido:
        ingreso.crear_evento_google_calendar(titulo_recordatorio, contenido)  # CREAR EVENTO SI SE OBTIENEN DATOS

