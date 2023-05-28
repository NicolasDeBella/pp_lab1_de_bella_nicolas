
import re
import functions
def imprimir_menu()->None:
    """
    Imprime el menú de opciones.
    Returns:
        None 
    """
    opcion =("\t\t\t\tMENU DE OPCIONES\n\n"
            "1-Mostrar jugadores y su posicion.\n"
            "2-Mostrar estadistica de un jugador seleccionado.\n"
            "3-Exportar a CSV jugador selecionado en el punto dos.\n"
            "4-Mostrar logros de un jugador.\n"
            "5-Mostrar el promedio de puntos por partido de todo el equipo del Dream Team.\n"
            "6-Mostrar si el jugador es miembro del Salón de la Fama del Baloncesto.\n"
            "7-Mostrar el jugador con la mayor cantidad de rebotes totales.\n"
            "8-Mostrar el jugador con la mayor porcentaje de tiros de campo.\n"
            "9-Mostrar el jugador con la mayor cantidad de asistencias totales.\n"
            "10-Mostrar los jugadores que han promediado más puntos por partido que el valor ingresado.\n"
            "11-Mostrar los jugadores que han promediado más rebotes por partido que el valor ingresado.\n"
            "12-Mostrar los jugadores que han promediado más asistencias por partido que el valor ingresado.\n"
            "13-Mostrar el jugador con la mayor cantidad de robos totales.\n"
            "14-Mostrar el jugador con la mayor cantidad de bloqueos totales.\n"
            "15-Mostrar los jugadores con mayor porcentaje de tiros libres que el valor ingresado.\n"
            "16-Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.\n"
            "17-Mostrar el jugador con la mayor cantidad de logros obtenidos.\n"
            "18-Mostrar los jugadores con mayor porcentaje de tiros triples que el valor ingresado.\n"
            "19-Mostrar el jugador con la mayor cantidad de temporadas.\n"
            "20-Mostrar los jugadores, ordenados por posición en la cancha, con mayot porcentaje de tiros de campo que el valor ingresado.\n"
            "23-Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking: puntos, rebotes, asistencias y robos.\n"
            "0-Salir del menu")
    print(opcion)

def menu_principal()->int:
    """
    La funcion solicita al usuario que ingrese una opción del menú principal.
    Returns:
        int: Opción ingresada por el usuario. -1 si la opción no es válida.
    """
    imprimir_menu ()
    opcion = input("Ingrese una opcion: ")
    opcion_valida = re.search(r"^([0-9]|1[0-9]|20|23)$", opcion)
    if opcion_valida:
        return int(opcion)
    else:
        return -1

def dream_team_app(ruta_archivo:str)->None:
    """
    Aplicación principal.
    Parametros:
        nombre_archivo (str): Nombre del archivo JSON que contiene los datos de los héroes.   
    Returns:
        None
    """
    lista_jugadores = functions.abrir_archivo_json(ruta_archivo)
    indice_exportar_csv = None
    flag_case_2 = False

    while True:
        opcion = menu_principal()
        if opcion != -1:
            match opcion:
                case 1:
                   functions.imprimir_jugadores_dream_team(lista_jugadores)          
                case 2:
                   flag_case_2 = True
                   indice_exportar_csv = functions.obtener_imprimir_estadistica_de_jugador(lista_jugadores)      
                case 3:
                    functions.exportar_estadisticas_jugador_csv(lista_jugadores,indice_exportar_csv,flag_case_2)
                case 4:
                    functions.obtener_imprimir_logros(lista_jugadores)          
                case 5:
                    functions.obtener_imprimir_jugador_puntos_por_partido(lista_jugadores)
                case 6:
                    functions.verificar_miembro_salon_fama(lista_jugadores)        
                case 7:
                    functions.obtener_imprimir_jugador_maximo_valor(lista_jugadores,"rebotes_totales")
                case 8:
                    functions.obtener_imprimir_jugador_maximo_valor(lista_jugadores,"porcentaje_tiros_de_campo")          
                case 9:
                    functions.obtener_imprimir_jugador_maximo_valor(lista_jugadores,"asistencias_totales")
                case 10:
                    functions.obtener_imprimir_jugadores_por_estadistica_superior_que_valor_ingresado(lista_jugadores,"promedio_puntos_por_partido")          
                case 11:
                    functions.obtener_imprimir_jugadores_por_estadistica_superior_que_valor_ingresado(lista_jugadores,"promedio_rebotes_por_partido")        
                case 12:
                    functions.obtener_imprimir_jugadores_por_estadistica_superior_que_valor_ingresado(lista_jugadores,"promedio_asistencias_por_partido")
                case 13:
                    functions.obtener_imprimir_jugador_maximo_valor(lista_jugadores,"robos_totales")          
                case 14:
                    functions.obtener_imprimir_jugador_maximo_valor(lista_jugadores,"bloqueos_totales")
                case 15:
                    functions.obtener_imprimir_jugadores_por_estadistica_superior_que_valor_ingresado(lista_jugadores,"porcentaje_tiros_libres")        
                case 16:
                    functions.calcular_imprimir_jugadores_excluyendo_menor_puntos_por_partido(lista_jugadores)
                case 17:
                    functions.obtener_imprimir_jugador_maximo_logro(lista_jugadores)          
                case 18:
                    functions.obtener_imprimir_jugadores_por_estadistica_superior_que_valor_ingresado(lista_jugadores,"porcentaje_tiros_triples")
                case 19:
                    functions.obtener_imprimir_jugador_maximo_valor(lista_jugadores,"temporadas")
                case 20:
                    functions.mostrar_jugadores_por_porcentaje_tiros_superior(lista_jugadores)          
                case 23:
                    functions.calcular_posiciones_rankings(lista_jugadores)
                case 0:
                    respuesta = input("¿Desea salir del programa? (S/N)")
                    if respuesta == "s":
                        print("Salio del programa...")
                        break
                    else:
                        print("Continuando con el programa...")                
            input("Presione Enter para continuar...")
        else:
            print("Opcion invalida")
            input("Presione Enter para continuar...")