"""
 Módulo: operaciones.py
 Descripción: Operaciones sobre el nombre de usuario: búsqueda, espejado,
              reporte estadístico, simetría y ordenamiento.
              RESOLUCIÓN PURA MEDIANTE STRINGS (SIN USO DE LISTAS).
"""

from utilidades import es_simbolo
from conteos import contar_tipos, contar_repetidos_consecutivos


def buscar_caracter(usuario: str, caracter: str) -> tuple:
    """
    Busca un caracter dentro del nombre de usuario y retorna
    cuántas veces aparece y en qué posiciones (como cadena).

    Args:
        usuario:  Nombre de usuario donde buscar.
        caracter: Caracter a buscar (debe ser un solo caracter).

    Returns:
        Tupla (cantidad, posiciones) donde posiciones es un string formateado.
    """
    longitud = len(usuario)
    cantidad = 0
    posiciones = ""  # En lugar de lista, usamos un string vacío

    for i in range(longitud):
        if usuario[i] == caracter:
            cantidad += 1
            # Si es la primera posición encontrada, no lleva coma adelante
            if posiciones == "":
                posiciones = str(i)
            else:
                posiciones = posiciones + ", " + str(i)

    return cantidad, posiciones


def espejado(usuario: str) -> str:
    """
    Genera el nombre de usuario invertido y lo concatena con el original.
    Sin utilizar slicing.

    Args:
        usuario: Nombre de usuario original.

    Returns:
        String con el usuario invertido concatenado con el original.
    """
    longitud = len(usuario)
    invertido = ""

    for i in range(longitud - 1, -1, -1):
        invertido = invertido + usuario[i]

    return invertido + usuario


def reporte_estadistico(usuario: str) -> None:
    """
    Muestra un reporte estadístico completo del nombre de usuario usando f-strings.

    Args:
        usuario: Nombre de usuario a analizar.
    """
    longitud = len(usuario)
    letras, numeros, guiones, puntos = contar_tipos(usuario)
    simbolos = guiones + puntos
    repetidos = contar_repetidos_consecutivos(usuario)

    porcentaje_letras   = (letras   / longitud) * 100
    porcentaje_numeros  = (numeros  / longitud) * 100
    porcentaje_simbolos = (simbolos / longitud) * 100

    print("\n" + "=" * 40)
    print("  REPORTE ESTADISTICO")
    print("=" * 40)
    print(f"  Longitud total        : {longitud}")
    print(f"  Porcentaje de letras  : {porcentaje_letras:.1f}%")
    print(f"  Porcentaje de numeros : {porcentaje_numeros:.1f}%")
    print(f"  Porcentaje de simbolos: {porcentaje_simbolos:.1f}%")
    print(f"  Grupos repetidos cons.: {repetidos}")
    print("=" * 40)


def es_simetrico(usuario: str) -> bool:
    """
    Determina si la primera mitad es igual a la segunda mitad.
    Solo aplica a usuarios con longitud par.

    Args:
        usuario: Nombre de usuario a evaluar.

    Returns:
        True si es simetrico, False en caso contrario.
    """
    longitud = len(usuario)

    if longitud % 2 != 0:
        return False

    mitad = longitud // 2

    for i in range(mitad):
        if usuario[i] != usuario[mitad + i]:
            return False

    return True


def ordenar_caracteres(usuario: str, ascendente: bool) -> str:
    """
    Ordena los caracteres del nombre de usuario usando Bubble Sort
    aplicado directamente sobre strings (reconstrucción por concatenación).
    No usa sorted(), .sort() ni listas.

    Args:
        usuario:    Nombre de usuario cuyos caracteres se ordenarán.
        ascendente: True para orden ascendente, False para descendente.

    Returns:
        String con los caracteres ordenados.
    """
    # Copiamos la cadena original para no mutar el parámetro directamente
    string_ordenado = usuario
    longitud = len(string_ordenado)

    # Lógica de Bubble Sort adaptada a Strings
    for i in range(longitud - 1): # Controla cuantas pasadas le vamos a dar a la palabra para que quede ordenada
        for j in range(longitud - 1 - i): # Recorre la cadena comparando elementos
            
            # Comparamos directamente los caracteres adyacentes por ASCII
            if ascendente:
                condicion = string_ordenado[j] > string_ordenado[j + 1]
            else:
                condicion = string_ordenado[j] < string_ordenado[j + 1]

            if condicion:
                # Reconstruimos el string entero haciendo el intercambio (swap) a mano
                # Armamos: todo lo anterior + el segundo carácter + el primer carácter + todo lo posterior
                anterior = ""
                for k in range(j):
                    anterior = anterior + string_ordenado[k]
                
                posterior = ""
                for k in range(j + 2, longitud):
                    posterior = posterior + string_ordenado[k]
                
                string_ordenado = anterior + string_ordenado[j + 1] + string_ordenado[j] + posterior

    return string_ordenado