# Resultados de la medición — Tarea 3 (IS061)

# Máquina y versión de Python

- Python: 3.11.15
- Sistema: Linux x86_64 (glibc 2.39)
- Procesador: Intel(R) Xeon(R) Processor @ 2.80GHz, 2 núcleos
- Semilla fijada al inicio de `medicion.py`: `random.seed(11)`
- Cada tiempo es el mejor de 9 repeticiones (mínimo, no promedio), tal como pide el enunciado.

# Tabla de tiempos

| Contactos | `contiene()` – binaria (µs) | búsqueda lineal ingenua (µs) | `agregar` + `eliminar` peor caso (µs) |
| 1.000   | 1,33 | 18,80 | 2,72 |
| 10.000  | 1,60 | 219,07 | 29,66 |
| 100.000 | 2,85 | 3.137,43 | 268,64 |

Metodología de cada columna (detallada como comentario en `medicion.py`):

- `contiene()` – binaria: se busca siempre un nombre ausente de la agenda (el peor caso real; buscar uno que sí está depende de dónde cayó en el orden y no es una comparación justa).
- búsqueda lineal ingenua: recorre con un `for` + `if` la lista que devuelve `agenda.nombres()` — pedida una sola vez, fuera del cronómetro — buscando el mismo nombre ausente. No usa `in`.
- `agregar` + `eliminar` peor caso: se agrega un contacto que queda de primero en el orden alfabético (`"AAAAAAAAAA"`) y se elimina inmediatamente después, dentro del mismo bloque cronometrado. Se miden juntos porque, si se repitiera solo `agregar` con el mismo nombre, a partir de la segunda repetición ya no estaría insertando sino *actualizando* un contacto existente (O(log n) en vez de O(n)); la pareja agregar+eliminar deja la agenda igual que estaba antes de cada repetición, así que las 9 repeticiones miden siempre una inserción real en el peor caso.

# Interpretación (10.000 → 100.000 contactos)

`contiene()` (búsqueda binaria): el tiempo se multiplicó por = 1,78×, muy por debajo del 10× que creció el tamaño de la agenda, porque el costo de la búsqueda binaria depende de log₂(n) y no de n: log₂(100.000) / log₂(10.000) ≈ 16,6 / 13,3 = 1,25, un número muy cercano al observado (el resto es ruido de medición, inevitable en tiempos de pocos microsegundos).

Búsqueda lineal ingenua: el tiempo se multiplicó por =14,3×, por encima del 10× esperado por el tamaño, porque el algoritmo es O(n) y en principio 10 veces más elementos debería costar 10 veces más — pero con 100.000 nombres la lista ya no cabe completa en la memoria caché rápida del procesador, así que buena parte de los accesos tiene que ir hasta la memoria RAM principal, más lenta, y eso encarece cada elemento adicional por encima de lo que predice solo el tamaño.

`agregar` + `eliminar` (peor caso): el tiempo se multiplicó por = 9,06×, muy cercano al 10× esperado, porque tanto insertar como eliminar en la posición 0 son operaciones O(n): hay que correr un lugar a todos los demás contactos, así que su costo escala casi exactamente proporcional al tamaño de la agenda.

# Nota

Los tiempos exactos dependen del computador donde se corrió `medicion.py` (aquí, la máquina descrita arriba) y no se califican; lo que importa, y lo que muestra esta tabla, son las proporciones: la búsqueda binaria casi no cambia, agregar/eliminar se multiplica por algo cercano a diez, y la búsqueda uno por uno se multiplica por más de diez debido al efecto de la caché del procesador.

