""" 
 Módulo: main.py
 Descripción: Programa principal del Sistema de Procesamiento de Nombres
              de Usuario. Gestiona el menú e integra todos los módulos.
""" 

from validaciones import validar_usuario, validar_formato
from conteos import contar_tipos
from operaciones import (
    buscar_caracter,
    espejado,
    reporte_estadistico,
    es_simetrico,
    ordenar_caracteres,
)

def mostrar_menu() -> None:
    """Muestra el menú principal del programa."""
    print(f"\n{'=' * 45}")
    print("  SISTEMA DE PROCESAMIENTO DE USUARIOS")
    print(f"{'=' * 45}")
    print("  1. Ingresar nombre de usuario")
    print("  2. Validar formato del usuario")
    print("  3. Contar tipos de caracteres")
    print("  4. Buscar carácter específico")
    print("  5. Mostrar usuario espejado")
    print("  6. Generar reporte estadístico")
    print("  7. Verificar si el usuario es simétrico")
    print("  8. Ordenar caracteres del usuario")
    print("  9. Salir")
    print(f"{'=' * 45}")


def pedir_opcion() -> str:
    """
    Solicita al usuario que ingrese una opción del menú.

    Returns:
        String con la opción ingresada.
    """
    opcion = input("  Ingresá una opción (1-9): ")
    return opcion


def opcion_valida(opcion: str) -> bool:
    """
    Verifica si la opción ingresada es un número entre 1 y 9.

    Args:
        opcion: String con la opción del usuario.

    Returns:
        True si es válida, False en caso contrario.
    """
    if len(opcion) != 1:
        return False
    return "1" <= opcion <= "9"


def hay_usuario(usuario: str) -> bool:
    """
    Verifica si ya se ingresó un nombre de usuario.

    Args:
        usuario: Nombre de usuario actual.

    Returns:
        True si hay un usuario cargado, False en caso contrario.
    """
    if len(usuario) > 0:
        return True
    else:
        return False



def opcion_ingresar_usuario() -> str:
    """
    Solicita y valida el ingreso de un nombre de usuario.

    Returns:
        El nombre de usuario válido ingresado.
    """
    while True:
        usuario = input("\n  Ingresá el nombre de usuario: ")
        valido, mensaje = validar_usuario(usuario)
        if valido:
            print(f"  {mensaje}")
            return usuario
        else:
            print(f"  {mensaje}")


def opcion_validar_formato(usuario: str) -> None:
    """
    Muestra la categoría del nombre de usuario.

    Args:
        usuario: Nombre de usuario a categorizar.
    """
    categoria = validar_formato(usuario)
    print(f"\n  Usuario  : {usuario}")
    print(f"  Categoría: {categoria}")


def opcion_contar_tipos(usuario: str) -> None:
    """
    Muestra la cantidad de cada tipo de carácter en el usuario.

    Args:
        usuario: Nombre de usuario a analizar.
    """
    letras, numeros, guiones, puntos = contar_tipos(usuario)
    print(f"\n  Usuario analizado: {usuario}")
    print(f"  Letras      : {letras}")
    print(f"  Números     : {numeros}")
    print(f"  Guiones (_) : {guiones}")
    print(f"  Puntos  (.) : {puntos}")


def opcion_buscar_caracter(usuario: str) -> None:
    """
    Solicita un carácter y muestra cuántas veces aparece y en qué posiciones.

    Args:
        usuario: Nombre de usuario donde buscar.
    """
    caracter = input("\n  Ingresá el carácter a buscar: ")

    if len(caracter) != 1:
        print("Debés ingresar un único carácter.")
        return

    cantidad, posiciones_str = buscar_caracter(usuario, caracter)

    if cantidad == 0:
        print(f"  El carácter '{caracter}' no aparece en '{usuario}'.")
    else:
        print(f"\n  Carácter '{caracter}' en '{usuario}':")
        print(f"  Apariciones : {cantidad}")
        print(f"  Posiciones  : {posiciones_str}")

def opcion_espejado(usuario: str) -> None:
    """
    Muestra el nombre de usuario invertido concatenado con el original.

    Args:
        usuario: Nombre de usuario a espejear.
    """
    resultado = espejado(usuario)
    print(f"\n  Usuario  : {usuario}")
    print(f"  Espejado : {resultado}")


def opcion_simetrico(usuario: str) -> None:
    """
    Informa si el nombre de usuario es simétrico.

    Args:
        usuario: Nombre de usuario a evaluar.
    """
    if es_simetrico(usuario):
        print(f"\n  '{usuario}' ES simétrico.")
    else:
        print(f"\n  '{usuario}' NO es simétrico.")


def opcion_ordenar(usuario: str) -> None:
    """
    Solicita el tipo de orden y muestra el usuario con sus caracteres ordenados.

    Args:
        usuario: Nombre de usuario a ordenar.
    """
    print("\n  Tipo de orden:")
    print("    1. Ascendente")
    print("    2. Descendente")

    orden = input("  Ingresá una opción (1 o 2): ")

    if orden == "1":
        resultado = ordenar_caracteres(usuario, True)
        print(f"\n  Ordenamiento Ascendente : {resultado}")
    elif orden == "2":
        resultado = ordenar_caracteres(usuario, False)
        print(f"\n  Ordenamiento Descendente: {resultado}")
    else:
        print("  Opción inválida.")


# =============================================================================
# Programa principal
# =============================================================================

def main() -> None:
    """Función principal que ejecuta el menú."""
    usuario = ""

    print("\n  Bienvenido al Sistema de Procesamiento de Nombres de Usuario.")

    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if not opcion_valida(opcion):
            print("  Opción inválida. Ingresá un número del 1 al 9.")
            continue

        if opcion == "9":
            print("\n  Hasta luego.\n")
            break

        if opcion == "1":
            usuario = opcion_ingresar_usuario()

        elif opcion == "2":
            if not hay_usuario(usuario):
                print("  Primero ingresá un nombre de usuario (opción 1).")
            else:
                opcion_validar_formato(usuario)

        elif opcion == "3":
            if not hay_usuario(usuario):
                print("  Primero ingresá un nombre de usuario (opción 1).")
            else:
                opcion_contar_tipos(usuario)

        elif opcion == "4":
            if not hay_usuario(usuario):
                print("  Primero ingresá un nombre de usuario (opción 1).")
            else:
                opcion_buscar_caracter(usuario)

        elif opcion == "5":
            if not hay_usuario(usuario):
                print("  Primero ingresá un nombre de usuario (opción 1).")
            else:
                opcion_espejado(usuario)

        elif opcion == "6":
            if not hay_usuario(usuario):
                print("  Primero ingresá un nombre de usuario (opción 1).")
            else:
                reporte_estadistico(usuario)

        elif opcion == "7":
            if not hay_usuario(usuario):
                print("  Primero ingresá un nombre de usuario (opción 1).")
            else:
                opcion_simetrico(usuario)

        elif opcion == "8":
            if not hay_usuario(usuario):
                print("  Primero ingresá un nombre de usuario (opción 1).")
            else:
                opcion_ordenar(usuario)


main()