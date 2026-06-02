# 🚀 Sistema de Procesamiento de Usuarios (Examen recuperatorio)

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-2.0+-F05032?style=for-the-badge&logo=git&logoColor=white)
![Estructuras de Datos](https://img.shields.io/badge/Listas-No_Permitidas-red?style=for-the-badge)
![Estado](https://img.shields.io/badge/Estado-Completado_/%_Aprobación_Directa-brightgreen?style=for-the-badge)

Este proyecto corresponde a la resolución del **Examen Recuperatorio de Programación I**. El software implementa un sistema modular completo para la gestión, validación, análisis estadístico y transformación algorítmica de nombres de usuario ingresados por consola.

---

## 🎯 Restricciones de la Cátedra (Desafío Técnico)
Para la aprobación directa del parcial, el diseño de este sistema se rigió bajo estrictas limitaciones técnicas impuestas por la cátedra, orientadas a evaluar la lógica pura de algoritmos:
* 🚫 **Sin el uso de Listas, Arrays o Diccionarios:** Toda la estructura de datos se maneja mediante variables atómicas y manipulación secuencial de cadenas.
* 🚫 **Sin Métodos Avanzados de Strings:** Prohibido el uso de funciones nativas de ordenamiento o inversión como `.sort()`, `sorted()`, `.reverse()`, u operadores de pertenencia avanzada (`in`).
* 🚫 **Sin Slicing Complejo:** No se permite el uso de atajos como `[::-1]` para invertir cadenas.

---

## 📂 Arquitectura del Proyecto (Estructura Modular)

El sistema está completamente modularizado en **5 componentes interconectados**, respetando el principio de separación de responsabilidades:

* **`main.py`** 🧠: El cerebro organizativo y punto de entrada. Maneja el bucle principal de la interfaz (`while True`), captura las interacciones del operador y despliega un menú robusto con barreras defensivas de selección.
* **`validaciones.py`** 🛡️: Capa encargada de las reglas de negocio. Evalúa la longitud de las entradas, verifica la presencia obligatoria de caracteres mediante una sola pasada y clasifica al usuario en categorías (*Básico, Intermedio, Avanzado*).
* **`operaciones.py`** ⚙️: El núcleo algorítmico pesado. Contiene las funciones de búsqueda indexada, cálculo de simetría en paralelo, duplicación de strings por espejado y el algoritmo clave de la entrega.
* **`conteos.py`** 📊: Módulo especializado en métricas analíticas. Desglosa de forma detallada las cantidades por tipo y detecta grupos consecutivos usando un algoritmo de corte de control adaptado.
* **`utilidades.py`** ⚛️: La base atómica del software. Centraliza las validaciones de bajo nivel mediante la lectura directa de posiciones en la tabla **ASCII** usando la función `ord()`.

---

## 🛠️ Algoritmos Destacados

### 1. Ordenamiento por Reconstrucción (Bubble Sort a puro String)
Debido a la **inmutabilidad de los strings** en Python, el tradicional intercambio (*swap*) de elementos se resolvió de forma puramente matemática desarmando dinámicamente la cadena en tres secciones mediante bucles y volviéndola a concatenar en una sola pasada:
$$\text{Nueva Cadena} = \text{Tramo Anterior} + \text{Carácter Derecho} + \text{Carácter Izquierdo} + \text{Tramo Posterior}$$

### 2. Validación de Simetría Eficiente
Aplica un descarte temprano si la longitud es impar. En cadenas pares, procesa de forma paralela el índice `i` de la primera mitad con la posición proyectada en la segunda mitad (`mitad + i`), reduciendo a la mitad los ciclos de CPU del bucle.

---

## 💻 Tecnologías Utilizadas

* **Lenguaje:** Python 3.x 🐍
* **Entorno de Desarrollo:** Visual Studio Code 💻
* **Control de Versiones:** Git & GitHub 🚀
* **Terminal Emuladora:** MINGW64 / Git Bash 🛠️

---

## 👤 Desarrollado por:
* **Camila Eva Velásquez** — *Programming Student* 💻

---
<p align="center">
  <b>Examen Programación I - Proyecto Libre de Estructuras Complejas</b>
</p>
