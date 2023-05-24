import json
import re

def abrir_archivo_json(ruta:str)->dict:
    """
    La funcion abre y carga un archivo JSON en una estructura de datos Python.
    Args:
        ruta (str): El nombre o la ruta del archivo JSON.
    Returns:
        dict: La estructura de datos cargada desde el archivo JSON.
    """
    with open(ruta) as archivo:
        data = json.load(archivo)
        return data["jugadores"]
    
#--------------------------------------------------------------------------------------------


def mostrar_jugadores_dream_team(lista_jugadores:str)->None:

    if len(lista_jugadores) > 0:
        for jugador in lista_jugadores:
            print("{0} | {1}".format(jugador['nombre'], jugador['posicion']))
    else:
        print("Lista vacia")

#--------------------------------------------------------------------------------------------

"""2) Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas
completas, incluyendo temporadas jugadas, puntos totales, promedio de puntos por
partido, rebotes totales, promedio de rebotes por partido, asistencias totales,
promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de
tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples."""


def imprimir_indices_jugadores()->None:

    indice = input("Ingrese un indice:  ")
    indice_validar = re.search(r"^[0-9]+$",indice)

    if indice_validar:
        return int(indice)
    else:
        return -1






















#--------------------------------------------------------------------------------------------


def imprimir_menu()->None:
    """
    Imprime el menú de opciones.
    Returns:
        None 
    """
    opcion =("\t\t\t\tMENU DE OPCIONES\n\n"
            "1-Mostrar jugadores y su posicion\n"
            "2-\n"
            "3-\n"
            "4-\n"
            "5-\n"
            "6-\n"
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
    opcion_valida = re.search(r"^[0-6]$", opcion)
    if opcion_valida:
        return int(opcion)
    else:
        return -1

def dream_team_app(ruta_archivo:str)->None:
    """
    Aplicación principal.
    Args:
        nombre_archivo (str): Nombre del archivo JSON que contiene los datos de los héroes.   
    Returns:
        None
    """
    lista_jugadores = abrir_archivo_json(ruta_archivo)
    
    while True:
        opcion = menu_principal()
        if opcion != -1:
            match opcion:
                case 1:
                   mostrar_jugadores_dream_team(lista_jugadores)          
                case 2:
                   pass        
                case 3:
                    pass
                case 4:
                    pass          
                case 5:
                    pass
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



indice = imprimir_indices_jugadores()
if indice != -1:
    print(indice)
else:
    print("error")
#dream_team_app('D:\Escritorio\Progra_PYTHON\Primer_parcial\dt.json')

