import sqlite3
import urllib.parse
import webbrowser

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

class IngresoCalendario:
    def __init__(self, conexion):
        self.conexion = conexion
    def registro_calendario(self):
        titulo_recordatorio = str(input("Ingresa el titulo del recordatorio: "))
        nombre_user = str(input("Ingresa el nombre de registro: "))
        apellido_user = str(input("Ingresa el apellido de registro: "))
        self.conexion.cursor.execute("SELECT usuario_ID FROM usuario WHERE nombre_user = ? AND apellido_user = ?",(nombre_user,apellido_user))
        usuario = self.conexion.cursor.fetchone()
        if usuario:
            usuario_id = usuario[0]
            self.conexion.cursor.execute("SELECT contenido_recordatorio FROM recordatorio_datos WHERE titulo_recordatorio = ? AND usuario_id = ?", (titulo_recordatorio, usuario_id))
            recordatorio = self.conexion.cursor.fetchone()
            if recordatorio:
                return  titulo_recordatorio,recordatorio[0]
            else:
                print("No se encontro ningun recordatorio con ese recordatorio.")
        else:
            print("No se encontro ese nombre registrado.")
        return None, None

    def crear_evento_google_calendar(self,titulo_recordatorio, contenido_recordatorio):
        fecha_recordatorio = str(input("Ingresa la fecha del recordatorio (YYYY-MM-DD): "))
        fecha_inicio = f"{fecha_recordatorio.replace("-","")}T090000Z"
        fecha_fin = f"{fecha_recordatorio.replace("-","")}T100000Z"
        google_url = "https://calendar.google.com/calendar/render?action=TEMPLATE"
        parametros = {
            "text" : titulo_recordatorio,
            "detalles": contenido_recordatorio,
            "fechas" : f"{fecha_inicio}/{fecha_fin}",
        }
        url_recordatorio = google_url + "&" + urllib.parse.urlencode(parametros)
        print(f"Se agrega el recordatorio aqui:{url_recordatorio}.")
        webbrowser.open(url_recordatorio)

if __name__ == "__main__":
    ruta_db = "C:/Users/POWER/recordatorios_proyecto_2.db"
    conexion = ConexionBD(ruta_db)

    ingreso =  IngresoCalendario(conexion)
    titulo_recordatorio, contenido = ingreso.registro_calendario()
    if contenido:
        ingreso.crear_evento_google_calendar(titulo_recordatorio, contenido)


