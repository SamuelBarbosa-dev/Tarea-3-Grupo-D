"""test_agenda.py — Pruebas unitarias para la clase Agenda con pytest."""

import pytest
from agenda import Agenda


def test_agregar_y_contiene() -> None:
    """Verifica que un contacto agregado se guarde y sea encontrado."""
    agenda = Agenda()
    agenda.agregar("Carlos", "3001234567")
    assert agenda.contiene("Carlos") is True
    assert len(agenda) == 1


def test_orden_alfabetico_estricto() -> None:
    """Comprueba que nombres() entregue la lista siempre ordenada alfabéticamente."""
    agenda = Agenda()
    agenda.agregar("Zapata", "111")
    agenda.agregar("Ana", "222")
    agenda.agregar("Betancur", "333")
    assert agenda.nombres() == ["Ana", "Betancur", "Zapata"]


def test_telefono_de_existente() -> None:
    """Verifica la consulta correcta del teléfono de un contacto."""
    agenda = Agenda()
    agenda.agregar("Luisa", "3109876543")
    assert agenda.telefono_de("Luisa") == "3109876543"


def test_actualizar_telefono_contacto_existente() -> None:
    """Comprueba que agregar un nombre repetido actualice el teléfono sin duplicar."""
    agenda = Agenda()
    agenda.agregar("Mateo", "100")
    agenda.agregar("Mateo", "999")
    assert len(agenda) == 1
    assert agenda.telefono_de("Mateo") == "999"


def test_eliminar_contacto_existente() -> None:
    """Comprueba que un contacto se elimine correctamente y reduzca la longitud."""
    agenda = Agenda()
    agenda.agregar("Beatriz", "555")
    agenda.eliminar("Beatriz")
    assert agenda.contiene("Beatriz") is False
    assert len(agenda) == 0




def test_caso_borde_agenda_vacia() -> None:
    """Manejo de operaciones sobre una agenda recién inicializada."""
    agenda = Agenda()
    assert len(agenda) == 0
    assert agenda.nombres() == []
    assert agenda.contiene("Cualquiera") is False


def test_caso_borde_nombre_vacio_lanza_value_error() -> None:
    """Verifica que intentar agregar un nombre vacío lance ValueError."""
    agenda = Agenda()
    with pytest.raises(ValueError):
        agenda.agregar("", "3000000000")


def test_caso_borde_telefono_de_inexistente_lanza_key_error() -> None:
    """Verifica que solicitar el teléfono de alguien ausente lance KeyError."""
    agenda = Agenda()
    agenda.agregar("Pedro", "123")
    with pytest.raises(KeyError):
        agenda.telefono_de("Maria")


def test_caso_borde_eliminar_inexistente_lanza_key_error() -> None:
    """Verifica que intentar borrar un nombre inexistente lance KeyError."""
    agenda = Agenda()
    with pytest.raises(KeyError):
        agenda.eliminar("Inexistente")


def test_caso_borde_lista_nombres_es_independiente() -> None:
    """Comprueba que modificar la lista retornado por nombres() no afecte la agenda."""
    agenda = Agenda()
    agenda.agregar("Daniel", "777")
    lista_copia = agenda.nombres()
    lista_copia.append("Falso")
    assert agenda.contiene("Falso") is False
    assert len(agenda) == 1"""test_agenda.py — Pruebas unitarias para la clase Agenda con pytest."""

import pytest
from agenda import Agenda



def test_agregar_y_contiene() -> None:
    """Verifica que un contacto agregado se guarde y sea encontrado."""
    agenda = Agenda()
    agenda.agregar("Carlos", "3001234567")
    assert agenda.contiene("Carlos") is True
    assert len(agenda) == 1


def test_orden_alfabetico_estricto() -> None:
    """Comprueba que nombres() entregue la lista siempre ordenada alfabéticamente."""
    agenda = Agenda()
    agenda.agregar("Zapata", "111")
    agenda.agregar("Ana", "222")
    agenda.agregar("Betancur", "333")
    assert agenda.nombres() == ["Ana", "Betancur", "Zapata"]


def test_telefono_de_existente() -> None:
    """Verifica la consulta correcta del teléfono de un contacto."""
    agenda = Agenda()
    agenda.agregar("Luisa", "3109876543")
    assert agenda.telefono_de("Luisa") == "3109876543"


def test_actualizar_telefono_contacto_existente() -> None:
    """Comprueba que agregar un nombre repetido actualice el teléfono sin duplicar."""
    agenda = Agenda()
    agenda.agregar("Mateo", "100")
    agenda.agregar("Mateo", "999")
    assert len(agenda) == 1
    assert agenda.telefono_de("Mateo") == "999"


def test_eliminar_contacto_existente() -> None:
    """Comprueba que un contacto se elimine correctamente y reduzca la longitud."""
    agenda = Agenda()
    agenda.agregar("Beatriz", "555")
    agenda.eliminar("Beatriz")
    assert agenda.contiene("Beatriz") is False
    assert len(agenda) == 0


def test_caso_borde_agenda_vacia() -> None:
    """Manejo de operaciones sobre una agenda recién inicializada."""
    agenda = Agenda()
    assert len(agenda) == 0
    assert agenda.nombres() == []
    assert agenda.contiene("Cualquiera") is False


def test_caso_borde_nombre_vacio_lanza_value_error() -> None:
    """Verifica que intentar agregar un nombre vacío lance ValueError."""
    agenda = Agenda()
    with pytest.raises(ValueError):
        agenda.agregar("", "3000000000")


def test_caso_borde_telefono_de_inexistente_lanza_key_error() -> None:
    """Verifica que solicitar el teléfono de alguien ausente lance KeyError."""
    agenda = Agenda()
    agenda.agregar("Pedro", "123")
    with pytest.raises(KeyError):
        agenda.telefono_de("Maria")


def test_caso_borde_eliminar_inexistente_lanza_key_error() -> None:
    """Verifica que intentar borrar un nombre inexistente lance KeyError."""
    agenda = Agenda()
    with pytest.raises(KeyError):
        agenda.eliminar("Inexistente")


def test_caso_borde_lista_nombres_es_independiente() -> None:
    """Comprueba que modificar la lista retornado por nombres() no afecte la agenda."""
    agenda = Agenda()
    agenda.agregar("Daniel", "777")
    lista_copia = agenda.nombres()
    lista_copia.append("Falso")
    assert agenda.contiene("Falso") is False
    assert len(agenda) == 1
