
import random
import string
import time
from agenda import Agenda

def generar_cadena_random(longitud: int = 10) -> str:
    return "".join(random.choices(string.ascii_letters, k=longitud))

def ejecutar_medicion() -> None:
    random.seed(11)
    tamanos = [100, 10000, 100000]
    print (f"{'Contactos':<12} {'Busq. Binaria (us)':<20} {'Busq. Ingenua (us)':<20} {'Agregar+Eliminar (us)':<20}")
    print ("-"*80)

    for n in tamanos:
        agenda= Agenda()
        for _ in range(n):
            agenda.agregar(generar_cadena_random(), "123456789")
            nombre_ausente = "ZZZZZZZ_NO_EXISTENTE"
            tiempos_binaria = []

#medicion de busqueda Binaria

            for _ in range(10):
                t_inicio = time.perf_counter()
                agenda.contien(nombre_ausente)
                t_fin = time.perf_counter()
                tiempos_binaria.append(t_fin - t_inicio)
            mejor_binaria_us = min(tiempos_binaria) * 1_000_000

#medicion de busqueda Ingenua

            lista_nombres = agenda.nombres()
            tiempos_ingenua = []
            for _ in range(10):
                t_inicio = time.perf_counter()
                encontrado = False
                for nom in lista_nombres:
                    if nom == nombre_ausente:
                        encontrado = True
                        break
                t_fin = time.perf_counter()
                tiempos_ingenua.append(t_fin - t_inicio)
            mejor_ingenua_us = min(tiempos_ingenua) * 1_000_000

#medicion de agregar y eliminar al inicio

            nombre_inicio = "AAAAAAAA_PRIMERO"
            tiempos_agregar_eliminar = []
            for _ in range (10):
                t_inicio = time.perf_counter()
                agenda.agregar(nombre_inicio, "00000000")
                agenda.eliminar(nombre_inicio)
                t_fin = time.perf_counter()
                tiempos_agregar_eliminar.append(t_fin - t_inicio)
            mejor_agregar_us = min(tiempos_agregar_eliminar) * 1_000_000

            n_str = f"{n:,}".replace(",", ".")
            bin_str = f"{mejor_binaria_us:.2f}".replace(".", ",")
            ing_str = f"{mejor_ingenua_us:.2f}".replace(".", ",")
            agr_str = f"{mejor_agregar_us:.2f}".replace(".", ",")

            print(f"{n_str:<12} | {bin_str:<20} | {ing_str:<20} | {agr_str:<20}")

import random
import string
import time
from agenda import Agenda


def generar_cadena_azar(longitud: int = 10) -> str:
    return "".join(random.choices(string.ascii_letters, k=longitud))


def ejecutar_mediciones() -> None:
    # Semilla fija obligatoria por la guía
    random.seed(11)

    tamanos = [1000, 10000, 100000]

    print("\nCalculando tiempos, por favor espera un momento...\n")
    print(f"{'Contactos':<12} | {'Busq. Binaria (us)':<20} | {'Busq. Ingenua (us)':<20} | {'Agregar+Eliminar (us)':<20}")
    print("-" * 80)

    for n in tamanos:
        agenda = Agenda()

        # Llenamos la agenda con n contactos aleatorios
        for _ in range(n):
            agenda.agregar(generar_cadena_azar(), "123456789")

        # Nombre ausente para evaluar el PEOR CASO de la búsqueda
        nombre_ausente = "ZZZZZZZZZZ_NO_EXISTE"

        # 1. Medición: Búsqueda Binaria con contiene(nombre)
        tiempos_binaria = []
        for _ in range(10):
            t_inicio = time.perf_counter()
            agenda.contiene(nombre_ausente)
            t_fin = time.perf_counter()
            tiempos_binaria.append(t_fin - t_inicio)
        mejor_binaria_us = min(tiempos_binaria) * 1_000_000

        # 2. Medición: Búsqueda Ingenua (for e if sobre la lista devuelta por nombres())
        lista_nombres = agenda.nombres()
        tiempos_ingenua = []
        for _ in range(10):
            t_inicio = time.perf_counter()
            encontrado = False
            for nom in lista_nombres:
                if nom == nombre_ausente:
                    encontrado = True
                    break
            t_fin = time.perf_counter()
            tiempos_ingenua.append(t_fin - t_inicio)
        mejor_ingenua_us = min(tiempos_ingenua) * 1_000_000

        # 3. Medición: Agregar + Eliminar al inicio (Peor caso: 'AAAAA' va al principio)
        nombre_inicio = "AAAAAAA_PRIMERO"
        tiempos_agregar_eliminar = []
        for _ in range(10):
            t_inicio = time.perf_counter()
            agenda.agregar(nombre_inicio, "000000000")
            agenda.eliminar(nombre_inicio)
            t_fin = time.perf_counter()
            tiempos_agregar_eliminar.append(t_fin - t_inicio)
        mejor_agregar_us = min(tiempos_agregar_eliminar) * 1_000_000

        # Formato exigido: miles con punto (.) y decimales con coma (,)
        n_str = f"{n:,}".replace(",", ".")
        bin_str = f"{mejor_binaria_us:.2f}".replace(".", ",")
        ing_str = f"{mejor_ingenua_us:.2f}".replace(".", ",")
        agr_str = f"{mejor_agregar_us:.2f}".replace(".", ",")

        print(f"{n_str:<12} | {bin_str:<20} | {ing_str:<20} | {agr_str:<20}")


if __name__ == "__main__":
    ejecutar_mediciones()
