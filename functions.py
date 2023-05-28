import json
import re

def abrir_archivo_json(ruta:str)->dict:
    """
    La funcion abre y carga un archivo JSON en una estructura de datos Python.
    Parametros:
        ruta (str): El nombre o la ruta del archivo JSON.
    Returns:
        dict: La estructura de datos cargada desde el archivo JSON.
    """
    with open(ruta) as archivo:
        data = json.load(archivo)
        return data["jugadores"]
    

def imprimir_jugadores_dream_team(lista_jugadores:str)->None:
    """Imprime el nombre y la posición de los jugadores de la lista.
    Parametros:
        lista_jugadores (list): Lista de diccionarios de jugadores.
    Returns:
        None"""
    if len(lista_jugadores) > 0:
        for jugador in lista_jugadores:
            print("{0} | {1}".format(jugador['nombre'], jugador['posicion']))
    else:
        print("Lista vacia")


def pedir_datos_enteros(mensaje: str, mensaje_error: str)->int:
    """
    Solicita al usuario ingresar un dato de tipo entero y lo valida.
    Parametros:
        mensaje (str): Mensaje que se muestra al solicitar el dato.
        mensaje_error (str): Mensaje de error que se muestra al ingresar un dato no válido.  
    Returns:
        int: Dato entero ingresado y validado.
    """
    dato = input(mensaje)

    while not dato.isdigit():
        dato = input(mensaje_error)
    
    return int(dato)


def imprimir_indice_jugador()->None:
    """
    Imprime el índice y nombre de cada jugador.
    Returns:
        None
    """
    print ( "\t\tINDICES JUGADORES\n"
            "0-Michael Jordan\n"
            "1-Magic Johnson\n"
            "2-Larry Bird\n"
            "3-Charles Barkley\n"
            "4-Scottie Pippen\n"
            "5-David Robinson\n"
            "6-Patrick Ewing\n"
            "7-Karl Malone\n"
            "8-John Stockton\n"
            "9-Clyde Drexler\n"
            "10-Chris Mullin\n"
            "11-Christian Laettner")
    
            
def obtener_indice_jugador()->int:
    """
    Solicita al usuario que ingrese un índice válido de jugador.
    Returns:
        int: El índice ingresado por el usuario o -1 si es inválido.
    """
    imprimir_indice_jugador()
    indice = pedir_datos_enteros("Ingrese el indice del jugador:  ","El dato ingresado no es numerico, vuelva a intentarlo: ")
    indice_validar = re.search(r"^([0-9]|10|11)$",str(indice))

    if indice_validar:
        return int(indice)
    else:
        return -1


def obtener_imprimir_estadistica_de_jugador(lista_jugadores:list)->int:
    """
    Imprime las estadísticas de un jugador seleccionado por el usuario.
    Parametros:
        lista_jugadores (list): La lista de jugadores.
    Returns:
        indice (int): indcie del jugador sleccionado
    """
    if len(lista_jugadores) > 0:
        indice = obtener_indice_jugador()  
        if indice >= 0 and indice < len(lista_jugadores) and indice != -1:
            jugador = lista_jugadores[indice]["estadisticas"]
            print("Seleccionaste a {0}, sus estadisticas son:".format(lista_jugadores[indice]["nombre"]))
            for clave, valor in jugador.items():
                print("{0}: {1}".format(clave, valor))
            return indice     
        else:
            print("Índice inválido")
    else:
        print("Lista vacía")


def guardar_archivo(ruta:str, contenido:str)->None:
    """
    La funcion guarda el contenido en un archivo de texto en la ruta especificada. 
    Parametros:
        ruta (str): La ruta del archivo.
        contenido (str): El contenido a guardar.     
    Returns:
        None
    """
    with open(ruta, "w") as archivo:
        archivo.write(contenido)


def exportar_estadisticas_jugador_csv(lista_jugadores:list,indice:int,flag:bool)->None:
    """
    Exporta las estadísticas de un jugador a un archivo CSV.
    Parametros:
        lista_jugadores (list): Una lista que contiene información de los jugadores.
        indice (int): El índice del jugador cuyas estadísticas se desean exportar.
        flag (bool): valor booleano que me va a indicar si se ingreso al punto anterior para sabre si se genero un el indice.
    Returns:
        None
    """
    if len(lista_jugadores) > 0 and flag == True and type(indice) == int:

        nombre_jugador = lista_jugadores[indice]["nombre"]
        nombre_jugador = re.sub(" ",".", nombre_jugador)
        ruta_archivo = "{0}.csv".format(nombre_jugador)
        jugador = lista_jugadores[indice]
        lista_cabecera = []
        lista_valores = []

        for clave, valor in jugador.items():

            if clave in ["nombre", "posicion"]:
                lista_cabecera.append(re.sub("_"," ",clave))
                lista_valores.append(str(valor))
            elif clave == "estadisticas":
                for clave_estadistica, valor_estadistica in valor.items():
                    lista_cabecera.append(re.sub("_"," ",clave_estadistica))
                    lista_valores.append(str(valor_estadistica))

        valores = " || ".join(lista_valores)
        cabecera = " || ".join(lista_cabecera)
        contenido_archivo = "{0}\n{1}".format(cabecera,valores)
        
        if len(contenido_archivo) > 0:
            guardar_archivo(ruta_archivo, contenido_archivo)
            print("Se creó el archivo: {0}".format(ruta_archivo))    
        else:
            print("Error al crear el archivo: {0}".format(ruta_archivo))
        
    else:
        print("Necesita ingresar al punto anterior para generar el indice")


def imprimir_nombre_jugadores(lista_jugadores:list)->None:
    """
    Imprime los nombres de los jugadores en la lista de jugadores.
    Parametros:
        lista_jugadores (list): La lista de jugadores.
    Returns:
        None
    """
    if len(lista_jugadores) > 0:
        for jugador in lista_jugadores:
            print(jugador["nombre"])
    else:
        print("No se pudieron imprimir los nombres")


def pedir_nombre_jugador()->str:
    """
    Pide al usuario que ingrese el nombre de un jugador y devuelve el nombre en minúscula y sin espacios adicionales.
    Returns:
        str: El nombre del jugador ingresado.
    """
    nombre_jugador = input("Ingrese el nombre del jugador: ")
    nombre_jugador = nombre_jugador.lower().strip()
    return nombre_jugador


def obtener_imprimir_logros(lista_jugadores:list)->None:
    """
    Obtiene el nombre de un jugador de la lista, busca sus logros y los imprime en caso de encontrar al jugador.
    Parametros:
        lista_jugadores (list): La lista de jugadores.
    Returns:
        None
    """
    if len(lista_jugadores) > 0:
        imprimir_nombre_jugadores(lista_jugadores)
        nombre = pedir_nombre_jugador()
        encontrado = False
        for jugadores in lista_jugadores:
            if jugadores["nombre"].lower().strip() == nombre:
                print("Los logros de {0} son:\n{1}".format(nombre.capitalize(), "\n".join(jugadores["logros"])))
                encontrado = True
                break
        if encontrado == False:
            print("Jugador no encontrado")           
    else:
        print("Lista vacia")


def ordenar_por_sortquick(lista_original:list,key:str,orden:str)->list:
    """
    La funcion ordena una lista de elementos utilizando el algoritmo de ordenación quicksort.
    Parametros:
        lista_original (list): La lista original de elementos.
        key (str): La clave por la cual se realizará la comparación y ordenación de los elementos.
        orden (str): El orden en el que se desea ordenar la lista ("ascendente" o "descendente").
    Returns:
        list: La lista ordenada según el criterio especificado.
    """
    lista_derecha = []
    lista_izquierda = []
    if(len(lista_original)<=1):
        return lista_original
    else:
        pivot = lista_original[0]
        for elemento in lista_original[1:]:
            if orden == "ascendente" and elemento[key] > pivot[key] or orden == "descendente" and elemento[key] < pivot[key]:
                lista_derecha.append(elemento)
            else:
                lista_izquierda.append(elemento)

    lista_izquierda = ordenar_por_sortquick(lista_izquierda,key,orden)
    lista_izquierda.append(pivot)
    lista_derecha = ordenar_por_sortquick(lista_derecha,key,orden)
    lista_izquierda.extend(lista_derecha) 

    return lista_izquierda


def obtener_imprimir_jugador_puntos_por_partido(lista_jugadores:list)->None:
    """
    Obtiene la lista de jugadores e imprime los jugadores con sus respectivos puntos por partido.
    Parametros:
        lista_jugadores (list): La lista de jugadores.
    Returns:
        None
    """
    if len(lista_jugadores) > 0:
        lista_ordenada = ordenar_por_sortquick(lista_jugadores,"nombre","ascendente")
        if len(lista_ordenada) > 0:
            print("Promedio de puntos por partido:") 
            for jugador in lista_ordenada:
                print("{0} | {1}".format(jugador["nombre"],jugador["estadisticas"]["promedio_puntos_por_partido"]))
        else:
            print("Lista ordenada vacia")
    else:
        print("Lista vacia")


def verificar_miembro_salon_fama(lista_jugadores:list)->None:
    """
    Verifica si un jugador es miembro del Salón de la Fama del Baloncesto.
    Parametros:
        lista_jugadores (list): Lista de jugadores con sus datos.
    Returns:
        None: Esta función no devuelve ningún valor, solo imprime los resultados.
    """
    if len(lista_jugadores) > 0:
        imprimir_nombre_jugadores(lista_jugadores)
        nombre_jugador = pedir_nombre_jugador()
        encontrado = False

        for jugador in lista_jugadores:
            if jugador["nombre"].lower().strip() == nombre_jugador:
                encontrado = True
                if "Miembro del Salon de la Fama del Baloncesto" in jugador["logros"]:
                    print("El jugador {0} es Miembro del Salon de la Fama del Baloncesto".format(nombre_jugador.capitalize()))
                else:
                    print("El jugador {0} no es Miembro del Salon de la Fama del Baloncesto".format(nombre_jugador.capitalize()))
                break
        
        if encontrado == False:
            print("Jugador no encontrado")     
    else:
        print("Lista vacía")



def obtener_imprimir_jugador_maximo_valor(lista_jugadores: list, key: str)->None:
    """
    Calcula e imprime el jugador o los jugadores con el máximo valor para una clave específica dentro de la lista de jugadores.
    Parámetros:
        lista_jugadores (list): Lista de diccionarios que representan a los jugadores.
        key (str): Clave para la cual se desea obtener el máximo valor.
    Retorna:
        None
    """
    if len(lista_jugadores) > 0:
        
        maximo = float(lista_jugadores[0]["estadisticas"][key])
        nombres_jugadores = []
        for jugador in lista_jugadores:
            valor_actual = float(jugador["estadisticas"][key])
            
            if valor_actual > maximo:
                maximo = valor_actual
                nombres_jugadores = [jugador["nombre"]]
            elif valor_actual == maximo:
                nombres_jugadores.append(jugador["nombre"])
        
        nombres_jugadores_str = ", ".join(nombres_jugadores)
        if len(nombres_jugadores) == 1:
            print("{0} es el jugador con el valor máximo de {1}, con un total de {2}".format(nombres_jugadores_str, re.sub("_", " ", key), maximo))
        elif len(nombres_jugadores) > 1:  
            print("{0} son los jugadores con el valor máximo de {1}, con un total de {2}".format(nombres_jugadores_str, re.sub("_", " ", key), maximo))
        else:
            print("No hay jugadores con el valor máximo de {0}".format(re.sub("_", " ", key)))
    else: 
        print("Lista vacía")
    

def obtener_imprimir_jugadores_por_estadistica_superior_que_valor_ingresado(lista_jugadores:list,key:str)->None:
    """
    Busca e imprime los nombres de los jugadores cuya estadística es superior al valor ingresado.
    Parámetros:
    - lista_jugadores: Una lista que contiene información de los jugadores.
    - key: Una cadena de texto que representa la estadística específica a comparar.
    Returns:
        None
    """
    if len(lista_jugadores) > 0:
        valor_ingresado = pedir_datos_enteros("Ingrese un valor: ","El dato ingresado no es numerico, vuelva a intentarlo: ")
        lista_auxiliar_nombres = []
        for jugadores in lista_jugadores:
            if  float(valor_ingresado) < float(jugadores["estadisticas"][key]):
                lista_auxiliar_nombres.append(jugadores["nombre"])

        if len(lista_auxiliar_nombres) > 0:
            print("Los jugadores que superan el valor de {0} en {1} son: ".format(valor_ingresado,re.sub("_"," ",key)))
            print("\n".join(lista_auxiliar_nombres))
        else:
            print("Ningun jugador supera el valor ingresado de {0}.".format(re.sub("_"," ",key)))
    else:
        print("Lista vacia")


def obtener_valor_minimo_puntos_por_partido(lista_jugadores:list)->int:
    """
    Recibe una lista de jugadores y devuelve el valor mínimo de los puntos promedio por partido de todos los jugadores de la lista. 
    Parámetros:
        lista_jugadores (list): Una lista de jugadores, donde cada jugador es un diccionario con información de sus estadísticas.
    Returns:
        int: El valor mínimo de los puntos promedio por partido de los jugadores en la lista, o -1 si la lista está vacía.
    """

    if len(lista_jugadores) > 0:
        minimo = lista_jugadores[0]["estadisticas"]["promedio_puntos_por_partido"]
        for jugador in lista_jugadores:
            if jugador["estadisticas"]["promedio_puntos_por_partido"] < minimo:
                minimo = jugador["estadisticas"]["promedio_puntos_por_partido"]
        return minimo
    else:
        return -1


def calcular_imprimir_jugadores_excluyendo_menor_puntos_por_partido(lista_jugadores:list)->None:
    """
    Calcula e imprime el promedio de los puntos promedio por partido de los jugadores en la lista, 
    excluyendo al jugador con el valor mínimo de puntos. 
    Parámetros:
        lista_jugadores (list): Una lista de jugadores, donde cada jugador es un diccionario con información de sus estadísticas.
    Returns:
        None
    """

    if len(lista_jugadores) > 0:
        promedio_excluyendo_menor_puntos_por_partido = obtener_valor_minimo_puntos_por_partido(lista_jugadores)

        if promedio_excluyendo_menor_puntos_por_partido != -1:
            for jugadores in lista_jugadores:
                if jugadores["estadisticas"]["promedio_puntos_por_partido"] != promedio_excluyendo_menor_puntos_por_partido:
                    print("{0} | {1}".format(jugadores['nombre'], jugadores["estadisticas"]["promedio_puntos_por_partido"]))
        else:
            print("No se pudo obtener el menor punto del promedio de puntos por partido")
    else:
        print("Lista vacia")


def obtener_imprimir_jugador_maximo_logro(lista_jugadores:list)->None:
    """
    Calcula e imprime el jugador o los jugadores con la mayor cantidad de logros obtenidos dentro de la lista de jugadores.
    Parámetros:
        lista_jugadores (list): Lista de diccionarios que representan a los jugadores.
    Retorna:
        None
    """
    if len(lista_jugadores) > 0:
        
        maximo = len(lista_jugadores[0]["logros"])
        nombres_jugadores = []
        for jugador in lista_jugadores:
            valor_actual = len(jugador["logros"])
            
            if valor_actual > maximo:
                maximo = valor_actual
                nombres_jugadores = [jugador["nombre"]]
            elif valor_actual == maximo:
                nombres_jugadores.append(jugador["nombre"])
        
        nombres_jugadores_str = ", ".join(nombres_jugadores)
        if len(nombres_jugadores) == 1:
            print("{0} es el jugador que mayores logros tiene, con un total de {1} logros".format(nombres_jugadores_str,maximo))
        else:  
            print("{0} son los jugadores que mayores logros tiene, con un total de {1} logros".format(nombres_jugadores_str,maximo))
    else: 
        print("Lista vacía")


def mostrar_jugadores_por_porcentaje_tiros_superior(lista_jugadores:list)->None:
    """
    Imprime los jugadores cuyo porcentaje de tiros de campo es superior a un valor dado.
    Args:
        lista_jugadores (list): Una lista de jugadores en formato de diccionario.
    Returns:
        None
    """
    if len(lista_jugadores) > 0:
        lista_ordenada_por_posicion = ordenar_por_sortquick(lista_jugadores,"posicion","ascendente")
        valor = pedir_datos_enteros("Ingrese un valor: ","El dato ingresado no es numerico, vuelva a intentarlo: ")
        lista_auxiliar_nombre = []
        
        for jugadores in lista_ordenada_por_posicion:
            if jugadores["estadisticas"]["porcentaje_tiros_de_campo"] > valor:
                lista_auxiliar_nombre.append(jugadores["nombre"])
        
        nombres = "\n".join(lista_auxiliar_nombre)
        if len(lista_auxiliar_nombre) > 1:
            print("{0}\nJugadores que superan el valor de {1} en porcentaje tiros de campo".format(nombres,valor))
        elif len(lista_jugadores) == 1:
            print("{0} es el jugador que superan el valor de {0} en porcentaje tiros de campo".format(nombres,valor))
        else:
            print("No hay jugadores que superen ese valor")           
    else:
        print("Lista vacia")  


def calcular_posiciones_rankings(lista_jugadores:list)->None:
    """
    Calcula las posiciones de los jugadores en un ranking y guarda la información en un archivo CSV.
    Parametros:
        lista_jugadores (list): Una lista de diccionarios, donde cada diccionario representa un jugador y sus estadísticas.
    Returns:
        None
    """
    if len(lista_jugadores) > 0:

        ruta_archivo = "ranking_jugadores.csv"
        lista_contenido_archivo = []
        
        for jugadores in lista_jugadores:
            lista_valores = []
            lista_cabecera = []

            for clave, valor in jugadores.items():
                if clave in ["nombre"]:
                    lista_cabecera.append(re.sub("_"," ",clave))
                    lista_valores.append(valor)
                elif clave == "estadisticas":
                    for clave_estadistica, valor_estadistica in valor.items():
                        if clave_estadistica in ["puntos_totales","rebotes_totales",
                                                 "asistencias_totales", 
                                                 "promedio_asistencias_por_partido",
                                                 "robos_totales"]:
                            lista_cabecera.append(re.sub("_"," ",clave_estadistica))
                            lista_valores.append(str(valor_estadistica))

            valores = " || ".join(lista_valores)
            lista_contenido_archivo.append(valores)
        cabecera = " || ".join(lista_cabecera)
        contenido_archivo =  "{0}\n{1}".format(cabecera,"\n".join(lista_contenido_archivo))
        
        if len(contenido_archivo) > 0:
            guardar_archivo(ruta_archivo, contenido_archivo)
            print("Se creó el archivo: {0}".format(ruta_archivo))    
        else:
            print("Error al crear el archivo: {0}".format(ruta_archivo))  
    else:
        print("Lista vacia")