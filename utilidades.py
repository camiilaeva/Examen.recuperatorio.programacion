"""
 Módulo: utilidades.py
 Descripción: Funciones auxiliares base para clasificar caracteres.
             Usadas por validaciones.py, conteos.py y operaciones.py.
"""

def es_letra(caracter: str) -> bool:
    """
    Determina si un carácter es una letra (mayúscula o minúscula).

    Args:
        caracter: Un único carácter a evaluar.

    Returns:
        True si es letra, False en caso contrario.
    """
    return ("A" <= caracter <= "Z") or ("a" <= caracter <= "z")


def es_numero(caracter: str) -> bool:
    """
    Determina si un carácter es un dígito numérico (0-9).

    Args:
        caracter: Un único carácter a evaluar.

    Returns:
        True si es número, False en caso contrario.
    """
    return "0" <= caracter <= "9"


def es_guion_bajo(caracter: str) -> bool:
    """
    Determina si un carácter es un guion bajo (_).

    Args:
        caracter: Un único carácter a evaluar.

    Returns:
        True si es guion bajo, False en caso contrario.
    """
    return caracter == "_"


def es_punto(caracter: str) -> bool:
    """
    Determina si un carácter es un punto (.).

    Args:
        caracter: Un único carácter a evaluar.

    Returns:
        True si es punto, False en caso contrario.
    """
    return caracter == "."


def es_simbolo(caracter: str) -> bool:
    """
    Determina si un carácter es un símbolo permitido (_ o .).

    Args:
        caracter: Un único carácter a evaluar.

    Returns:
        True si es símbolo permitido, False en caso contrario.
    """
    return es_guion_bajo(caracter) or es_punto(caracter)


def es_caracter_valido(caracter: str) -> bool:
    """
    Determina si un carácter es válido para un nombre de usuario.
    Se permiten letras, números, guion bajo y punto.

    Args:
        caracter: Un único carácter a evaluar.

    Returns:
        True si es un carácter válido, False en caso contrario.
    """
    return es_letra(caracter) or es_numero(caracter) or es_simbolo(caracter)