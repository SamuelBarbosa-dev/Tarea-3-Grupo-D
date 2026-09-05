# Tarea-3-Grupo-D

El proyecto es un ejemplo práctico de un Tipo Abstracto de Datos (TAD). La agenda guarda contactos (nombre y teléfono) bajo una regla clave: **los datos siempre se mantienen ordenados alfabéticamente por nombre y no se permiten nombres duplicados**.

Al mantener los contactos siempre ordenados al momento de agregarlos, logramos hacer búsquedas súper rápidas mediante **Búsqueda Binaria** hecha desde cero, garantizando los siguientes costos de tiempo:

* **Búsqueda / Consulta (`contiene`, `telefono_de`):** $O(\log n)$ (Búsqueda binaria propia)
* **Inserción / Eliminación (`agregar`, `eliminar`):** $O(n)$ (Acomodar los elementos en el arreglo)
* **Consulta general (`nombres`, `len`):** $O(n)$ y $O(1)$ respectivamente

##  Requisitos Previos

Solo necesitas tener instalado:
* **Python 3.10** o superior.
* **Pytest** para correr la suite de pruebas unitarias.