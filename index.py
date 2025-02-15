from elementos.ingreso_usuario import ConexionBD, IngresosUsuarios
from elementos.ingreso_recordatorio import ConexionBD, IngresoRecordatorio
from elementos.mostrar_recordatorio import ConexionBD, MostrarRecordatorios


ruta_db = "C:/Users/POWER/recordatorios_proyecto_2.db"
conexion = ConexionBD(ruta_db)
        

while True:
    print("""
            BIENVENIDO AL SISTEMA DE RECORDATORIOS:
            1. Ingresar el usuario.
            2. Ingresa el recordatorio.
            3. Adjunta el recordatorio al calendario.
            4. Mostrar el recordatorio.
            5. Salir.
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
            print("Proxima funcionalidad.")
        elif usuario == 4:
            recordatorio_mostar = MostrarRecordatorios(conexion)
            recordatorio_mostar.mostrar_recordatorio()
        elif usuario == 5:
            print("Proxima funcionalidad.")
        else:
            print("Ingresa un valor numero en el rango 1 a 6.")
    except ValueError:
        print("Error de digitacion, vuelve a intentar.")