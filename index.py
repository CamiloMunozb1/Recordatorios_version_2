from elementos.ingreso_usuario import ConexionBD, IngresosUsuarios




ruta_db = "C:/Users/POWER/recordatorios_proyecto_2.db-journal"    
conexion = ConexionBD(ruta_db)
        

while True:
    print("""
            BIENVENIDO AL SISTEMA DE RECORDATORIOS:
            1. Ingresar el usuario.
            2. Ingresa el titulo del recordatrio.
            3. Ingresa el recordatorio.
            4. Adjunta el recordatorio al calendario.
            5. Mostrar el recordatorio.
            6. Salir.
        """)
    
    try:
        usuario = int(input("Ingresa una opcion: "))
        if usuario == 1:
            ingreso_user = IngresosUsuarios(conexion)
            ingreso_user.ingreso_usuario()
        elif usuario == 2:
            print("Proxima funcionalidad.")
        elif usuario == 3:
            print("Proxima funcionalidad.")
        elif usuario == 4:
            print("Proxima funcionalidad.")
        elif usuario == 5:
            print("Proxima funcionalidad.")
        elif usuario == 6:
            print("Proxima funcionalidad.")
        else:
            print("Ingresa un valor numero en el rango 1 a 6.")
    except ValueError:
        print("Error de digitacion, vuelve a intentar.")