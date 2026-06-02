"""
 Módulo: validaciones.py
 Descripción: Validación de formato y categoría de nombres de usuario.
 
"""

from utilidades import es_letra, es_numero, es_simbolo, es_caracter_valido


def validar_usuario(usuario: str) -> tuple:
    """
    Valida si el nombre de usuario cumple todas las reglas del sistema.

    Reglas:
        - No puede estar vacio.
        - Debe tener entre 6 y 15 caracteres.
        - No puede comenzar con un numero.
        - No puede contener espacios.
        - Debe contener al menos una letra.
        - Solo puede contener letras, numeros, guion bajo y punto.

    Args:
        usuario: Nombre de usuario a validar.

    Returns:
        Tupla (bool, str) con el resultado y un mensaje descriptivo.
    """
    longitud = len(usuario)

    if longitud == 0:
        return False, "El nombre de usuario no puede estar vacio."

    if longitud < 6 or longitud > 15:
        return False, "Debe tener entre 6 y 15 caracteres (tiene " + str(longitud) + ")."

    if es_numero(usuario[0]):
        return False, "No puede comenzar con un numero."

    tiene_letra = False
    for i in range(longitud):
        caracter = usuario[i]

        if caracter == " ":
            return False, "No puede contener espacios."

        if not es_caracter_valido(caracter):
            return False, "Caracter no permitido: '" + caracter + "'."

        if es_letra(caracter):
            tiene_letra = True

    if not tiene_letra:
        return False, "Debe contener al menos una letra."

    return True, "Nombre de usuario valido."


def validar_formato(usuario: str) -> str:
    """
    Determina la categoria del nombre de usuario: Basico, Intermedio,
    Avanzado o Sin categoria.

    Criterios:
        Basico:      solo letras, longitud entre 6 y 8.
        Intermedio:  letras y numeros, sin simbolos, al menos 8 caracteres.
        Avanzado:    letras, numeros y simbolos, al menos 12 caracteres,
                     no termina en simbolo.
        Sin categoria: no cumple ninguno de los anteriores.

    Args:
        usuario: Nombre de usuario ya validado.

    Returns:
        String con la categoria correspondiente.
    """
    longitud = len(usuario)

    tiene_letra = False
    tiene_numero = False
    tiene_simbolo = False

    for i in range(longitud):
        caracter = usuario[i]
        if es_letra(caracter):
            tiene_letra = True
        elif es_numero(caracter):
            tiene_numero = True
        elif es_simbolo(caracter):
            tiene_simbolo = True

    ultimo_es_simbolo = es_simbolo(usuario[longitud - 1])

    if tiene_letra and not tiene_numero and not tiene_simbolo:
        if 6 <= longitud <= 8:
            return "Basico"

    if tiene_letra and tiene_numero and not tiene_simbolo:
        if longitud >= 8:
            return "Intermedio"

    if tiene_letra and tiene_numero and tiene_simbolo:
        if longitud >= 12 and not ultimo_es_simbolo:
            return "Avanzado"

    return "Sin categoria"