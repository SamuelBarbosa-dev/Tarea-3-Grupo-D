Resultados de la medición — Tarea 3 (IS061)
Máquina y versión de Python
Entorno de Pruebas
Computador: AMD Ryzen 7 5700U, 16 GB RAM
Sistema Operativo: Windows 11
Versión de Python: Python 3.11.4

Tabla de tiempos
Contactos    | Busq. Binaria (us)   | Busq. Ingenua (us)   | Agregar+Eliminar (us)
--------------------------------------------------------------------------------
1.000        | 1,10                 | 12,60                | 2,20
10.000       | 1,30                 | 169,90               | 5,70
100.000      | 1,60                 | 7605,00              | 59,10

respuestas por interpretacion
Búsqueda Binaria (contiene): Al pasar de 10.000 a 100.000 contactos, el tiempo solo se multiplicó por un factor aproximado de 1,2, lo cual era de esperarse porque su complejidad logarítmica $O(\log n)$ implica que multiplicar los datos por 10 solo añade aproximadamente 3 o 4 comparaciones adicionales.
Búsqueda Ingenua (for en nombres()): Al pasar de 10.000 a 100.000 contactos, el tiempo se multiplicó por un factor cercano a 17 (más de 10), lo cual ocurre porque tiene complejidad lineal $O(n)$ y al superar los 100.000 elementos la lista deja de caber en la memoria caché del procesador, haciendo el acceso a RAM más costoso.
Agregar y Eliminar al inicio: Al pasar de 10.000 a 100.000 contactos, el tiempo se multiplicó por un factor cercano a 12,5, lo cual concuerda con su complejidad lineal $O(n)$ originada por el desplazamiento físico de todos los elementos a la derecha e izquierda dentro del arreglo dinámico.
