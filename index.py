from elementos.ingreso_usuario import ConexionBD, IngresosUsuarios
from elementos.ingreso_recordatorio import ConexionBD, IngresoRecordatorio
from elementos.mostrar_recordatorio import ConexionBD, MostrarRecordatorios
from elementos.eliminar_recordatorio import ConexionBD, EliminarRecordatorios
from elementos.recordatorio_calendario import ConexionBD, IngresoCalendario

ruta_db = "C:/Users/POWER/recordatorios_proyecto_2.db"
conexion = ConexionBD(ruta_db)
        

while True:
    print("""
            BIENVENIDO AL SISTEMA DE RECORDATORIOS:
            1. Ingresar el usuario.
            2. Ingresa el recordatorio.
            3. Adjunta el recordatorio al calendario.
            4. Mostrar el recordatorio.
            5. Eliminar recordatorio.
            6. Salir.
        """)
    
    try:
        usuario = int(input("Ingresa una opcion: "))
        if usuario == 1:
            ingreso_user = IngresosUsuarios(conexion)
            ingreso_user.ingreso_usuario()
        elif usuario == 2:
            ingreso_recordatorio = IngresoRecordatorio(conexion)
            ingreso_recordatorio.ingresar_recordatorio()
        elif usuario == 3:
            ingreso_calendario = IngresoCalendario(conexion)
            titulo_recordatorio, contenido = ingreso_calendario.registro_calendario()
            if titulo_recordatorio and contenido:
                ingreso_calendario.crear_evento_google_calendar(titulo_recordatorio,contenido)
        elif usuario == 4:
            recordatorio_mostar = MostrarRecordatorios(conexion)
            recordatorio_mostar.mostrar_recordatorio()
        elif usuario == 5:
            eliminar_recordatorio = EliminarRecordatorios(conexion)
            eliminar_recordatorio.eliminacion_recordatorio()
        elif usuario == 6:
            print("Gracias por visitar el sistema de recordatorios.")
            break
        else:
            print("Ingresa un valor numero en el rango 1 a 6.")
    except ValueError:
        print("Error de digitacion, vuelve a intentar.")