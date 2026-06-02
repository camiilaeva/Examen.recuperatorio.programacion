"""
# Módulo: conteos.py
# Descripción: Funciones de conteo de tipos de caracteres en el usuario.
"""

from utilidades import es_letra, es_numero, es_guion_bajo, es_punto


def contar_tipos(usuario: str) -> tuple:
    """
    Cuenta la cantidad de letras, números, guiones bajos y puntos
    presentes en el nombre de usuario.

    Args:
        usuario: Nombre de usuario a analizar.

    Returns:
        Tupla (letras, numeros, guiones, puntos) con los conteos.
    """
    letras = 0
    numeros = 0
    guiones = 0
    puntos = 0

    for i in range(len(usuario)):
        caracter = usuario[i]
        if es_letra(caracter):
            letras += 1
        elif es_numero(caracter):
            numeros += 1
        elif es_guion_bajo(caracter):
            guiones += 1
        elif es_punto(caracter):
            puntos += 1

    return letras, numeros, guiones, puntos


def contar_repetidos_consecutivos(usuario: str) -> int:
    """
    Cuenta la cantidad de grupos de caracteres repetidos consecutivos.

    Ejemplo: 'aa__11bb' tiene 3 grupos (aa, __, 11).

    Args:
        usuario: Nombre de usuario a analizar.

    Returns:
        Cantidad de grupos de caracteres repetidos consecutivos.
    """
    cantidad = 0
    longitud = len(usuario)
    i = 0

    while i < longitud - 1:
        if usuario[i] == usuario[i + 1]:
            cantidad += 1
            c_actual = usuario[i]
            while i < longitud and usuario[i] == c_actual:
                i += 1
        else:
            i += 1

    return cantidad