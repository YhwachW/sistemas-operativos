"""
Paginación: el problema típico de "RAM de X MB, procesos A, B y C, bloques de 4096 bytes".

Pasos (como en las pautas):
  1. Marcos en RAM          = RAM en bytes / tamaño de bloque
  2. Páginas de cada proceso = techo(tamaño en bytes / tamaño de página)
       - si te lo dan en bits: dividir por 8
       - si te lo dan en palabras: multiplicar por el tamaño de la palabra
  3. Distribución proporcional: a_i = (páginas_i / suma de páginas) x marcos   (se trunca)
  4. Si a_i >= páginas_i  -> paginación anticipada (por adelantado): todas las páginas
     se cargan una vez y no hay víctimas. Tiempo de fallas = páginas x (acceso + transferencia).
  5. Fragmentación interna "acumulada" (criterio de las pautas):
       (marcos asignados - páginas) x tamaño de bloque   +   lo que sobra en la última página
     OJO: en el libro, la fragmentación interna es SOLO lo que sobra en la última página.
  6. Tiempo de permanencia = páginas x tiempo de ejecución por página + tiempo de fallas.
"""
import math
import sys
from fractions import Fraction as F

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

KB, MB, GB = 1024, 1024 ** 2, 1024 ** 3


def miles(x):
    if isinstance(x, F) or isinstance(x, float):
        x = round(float(x), 2)
        ent = int(x)
        dec = f"{x - ent:.2f}"[1:] if x != ent else ''
        return f"{ent:,}".replace(',', '.') + dec.replace('.', ',')
    return f"{x:,}".replace(',', '.')


def resolver(titulo, ram_bytes, bloque, procesos, acceso=None, transferencia=None, ejec_pag=None, detalle='A'):
    """procesos: dict nombre -> tamaño en BYTES (puede ser fracción si venía en bits)."""
    print(f"\n######## {titulo}")
    marcos = ram_bytes // bloque
    print(f"Marcos en RAM = {miles(ram_bytes)} B / {miles(bloque)} B = {miles(marcos)} marcos")
    pags = {}
    for n, b in procesos.items():
        pags[n] = math.ceil(F(b) / bloque)
        print(f"Proceso {n}: {miles(F(b))} B / {bloque} = {round(float(F(b) / bloque), 3)} -> {pags[n]} páginas")
    suma = sum(pags.values())
    print(f"Suma de páginas = {suma}")
    asig = {}
    for n in procesos:
        exacto = F(pags[n], suma) * marcos
        asig[n] = math.floor(exacto)
        print(f"a{n} = ({pags[n]}/{suma}) x {marcos} = {round(float(exacto), 2)} -> {miles(asig[n])} marcos")
    print(f"Total asignado = {miles(sum(asig.values()))} de {miles(marcos)} (sobran {marcos - sum(asig.values())})")
    tipo = 'ANTICIPADA (por adelantado)' if all(asig[n] >= pags[n] for n in procesos) else 'POR DEMANDA (faltan marcos)'
    print(f"Tipo de paginación: {tipo}")
    n = detalle
    if n in procesos:
        sobra_ultima = pags[n] * bloque - F(procesos[n])
        libres = asig[n] - pags[n]
        print(f"\nProceso {n}:")
        print(f"  Sobra en la última página = {pags[n]} x {bloque} - {miles(F(procesos[n]))} = {round(float(sobra_ultima), 3)} B")
        print(f"  Marcos asignados sin usar = {asig[n]} - {pags[n]} = {libres} -> {miles(libres * bloque)} B")
        frag = libres * bloque + sobra_ultima
        print(f"  Fragmentación interna acumulada (criterio pauta) = {round(float(frag), 3)} B = {round(float(frag) / MB, 2)} MB")
        if acceso is not None:
            tf = pags[n] * (acceso + transferencia)
            print(f"  Tiempo de fallas = {pags[n]} x ({acceso} + {transferencia}) = {tf}")
            if ejec_pag is not None:
                print(f"  Tiempo de permanencia = {pags[n]} x {ejec_pag} + {tf} = {pags[n] * ejec_pag + tf}")
    return marcos, pags, asig


if __name__ == '__main__':
    resolver('Prueba 2 2025-2 (64 MB)', 64 * MB, 4096,
             {'A': F(3601333, 8), 'B': 18000 * 128, 'C': 256000}, 3, 20, 100)
