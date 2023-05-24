import json
import re
import main

main.abrir_archivo_json("D:\Escritorio\Progra_PYTHON\Primer_parcial\dt.json")

def imprimir_indices_jugadores()->None:

    indice = input("Ingrese un indice: ")
    indice_validar = re.search(r"^(0-5)+$",indice)

    if indice_validar:
        return int(indice)
    else:
        print("error")
