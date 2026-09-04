"""agenda.py — TAD Agenda (Tarea 3, IS061 — Estructura de Datos).

Contrato: una agenda de contactos (nombre, telefono) que se mantiene
siempre ordenada alfabéticamente por nombre y no admite nombres
repetidos.

Decisión de diseño: los contactos viven en una única lista de Python
(self._contactos), como pares (nombre, telefono), ordenada por
nombre.
"""

from typing import List, Tuple


class Agenda:
    """Agenda de contactos ordenada por nombre, sin nombres repetidos."""

    def __init__(self) -> None:
        """Crea una agenda vacía.

        Complejidad: O(1)
        """
        self._contactos: List[Tuple[str, str]] = []

    def __len__(self) -> int:
        """Cuántos contactos hay en la agenda.
        Se implementa con len(agenda) lo llama por
        detrás.
        Complejidad: O(1)
        """
        return len(self._contactos)

    def _buscar(self, nombre: str) -> Tuple[bool, int]:
        """Búsqueda binaria manual sobre self._contactos.
        Devuelve una tupla (encontrado, posicion):
        - Si encontrado es True, posicion es el índice
          donde vive ese nombre.
        - Si encontrado es False, posicion es el índice
          donde habría que insertar nombre para conservar el
          orden alfabético (puede ser len(self._contactos), si va
          al final).
        Complejidad: O(log n)
        """
        izquierda = 0
        derecha = len(self._contactos) - 1
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            nombre_medio = self._contactos[medio][0]
            if nombre_medio == nombre:
                return True, medio
            elif nombre_medio < nombre:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        # No se encontró: 'izquierda' quedó exactamente en el hueco
        # que le corresponde a 'nombre' para mantener el orden.
        return False, izquierda

    def contiene(self, nombre: str) -> bool:
        """Indica si nombre está en la agenda.
        Complejidad: O(log n)
        """
        encontrado, _posicion = self._buscar(nombre)
        return encontrado

    def telefono_de(self, nombre: str) -> str:
        """Devuelve el teléfono guardado para nombre.
        Lanza KeyError si ese nombre no está en la agenda.
        Complejidad: O(log n)
        """
        encontrado, posicion = self._buscar(nombre)
        if not encontrado:
            raise KeyError(nombre)
        return self._contactos[posicion][1]

    def nombres(self) -> List[str]:
        """Todos los nombres, en orden alfabético, en una lista nueva.
        La lista devuelta es independiente de la agenda: quien la
        reciba puede modificarla (agregar, quitar, reordenar) sin que
        la agenda se entere, porque es una lista nueva construida a
        partir de los datos internos, no una referencia a ellos.

        Complejidad: O(n)
        """
        return [nombre for nombre, _telefono in self._contactos]

    def agregar(self, nombre: str, telefono: str) -> None:
        """Agrega el contacto (nombre, telefono).

        Si nombre ya existe, actualiza su teléfono en vez de
        duplicar el contacto. Si nombre es la cadena vacía, lanza
        ValueError. El teléfono se guarda siempre como texto
        (str), aunque se reciba como número.

        Encontrar el sitio donde va nombre cuesta O(log n)
        (_buscar), pero abrirle el hueco con list.insert
        cuesta O(n): hay que correr un lugar a la derecha todos los
        contactos que quedan después. Por eso el costo total del
        método es O(n), aunque la búsqueda en sí sea logarítmica.

        Complejidad: O(n)
        """
        if nombre == "":
            raise ValueError("el nombre no puede ser la cadena vacía")
        telefono = str(telefono)
        encontrado, posicion = self._buscar(nombre)
        if encontrado:
            self._contactos[posicion] = (nombre, telefono)
        else:
            self._contactos.insert(posicion, (nombre, telefono))

    def eliminar(self, nombre: str) -> None:
        """Elimina el contacto de nombre ``nombre``.

        Lanza KeyError si ese nombre no está en la agenda.

        Igual que en agregar: encontrar el contacto cuesta
        O(log n), pero cerrar el hueco que deja con list.pop
        cuesta O(n), porque hay que correr un lugar a la izquierda
        todos los contactos que quedaban después de él.

        Complejidad: O(n)
        """
        encontrado, posicion = self._buscar(nombre)
        if not encontrado:
            raise KeyError(nombre)
        self._contactos.pop(posicion)

    def __repr__(self) -> str:  
        return f"Agenda({self._contactos!r})"
