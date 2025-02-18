# IMPORTACIÓN DE CLASES DESDE MÓDULOS EXTERNOS
# Se importan las clases necesarias desde los módulos dentro de la carpeta 'elementos'
from elementos.ingreso_usuario import ConexionBD, IngresosUsuarios
from elementos.ingreso_recordatorio import ConexionBD, IngresoRecordatorio
from elementos.mostrar_recordatorio import ConexionBD, MostrarRecordatorios
from elementos.eliminar_recordatorio import ConexionBD, EliminarRecordatorios
from elementos.recordatorio_calendario import ConexionBD, IngresoCalendario

# DEFINICIÓN DE LA RUTA DE LA BASE DE DATOS
ruta_db = "C:/Users/POWER/recordatorios_proyecto_2.db"

# SE ESTABLECE LA CONEXIÓN A LA BASE DE DATOS
conexion = ConexionBD(ruta_db)

# MENÚ PRINCIPAL DEL PROGRAMA
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
        # SOLICITA UNA OPCIÓN AL USUARIO
        usuario = int(input("Ingresa una opción: "))

        # OPCIÓN 1: INGRESAR USUARIO
        if usuario == 1:
            ingreso_user = IngresosUsuarios(conexion)
            ingreso_user.ingreso_usuario()

        # OPCIÓN 2: INGRESAR RECORDATORIO
        elif usuario == 2:
            ingreso_recordatorio = IngresoRecordatorio(conexion)
            ingreso_recordatorio.ingresar_recordatorio()

        # OPCIÓN 3: ADJUNTAR RECORDATORIO AL CALENDARIO
        elif usuario == 3:
            ingreso_calendario = IngresoCalendario(conexion)
            # OBTIENE EL TÍTULO Y CONTENIDO DEL RECORDATORIO
            titulo_recordatorio, contenido = ingreso_calendario.registro_calendario()
            # VERIFICA QUE AMBOS VALORES NO ESTÉN VACÍOS ANTES DE CREAR EL EVENTO
            if titulo_recordatorio and contenido:
                ingreso_calendario.crear_evento_google_calendar(titulo_recordatorio, contenido)

        # OPCIÓN 4: MOSTRAR RECORDATORIOS
        elif usuario == 4:
            recordatorio_mostar = MostrarRecordatorios(conexion)
            recordatorio_mostar.mostrar_recordatorio()

        # OPCIÓN 5: ELIMINAR RECORDATORIO
        elif usuario == 5:
            eliminar_recordatorio = EliminarRecordatorios(conexion)
            eliminar_recordatorio.eliminacion_recordatorio()

        # OPCIÓN 6: SALIR DEL PROGRAMA
        elif usuario == 6:
            print("Gracias por visitar el sistema de recordatorios.")
            break

        # EN CASO DE INGRESAR UN NÚMERO FUERA DEL RANGO 1-6
        else:
            print("Ingresa un valor numérico en el rango de 1 a 6.")

    # CAPTURA ERROR SI EL USUARIO INGRESA UN VALOR NO NUMÉRICO
    except ValueError:
        print("Error de digitación, vuelve a intentar.")
