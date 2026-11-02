"""
Planificación del brazo del disco: FCFS, SSTF, SCAN, LOOK, C-SCAN y C-LOOK.

Convenciones (dilas en la prueba, porque los libros varían):
  - SCAN  : avanza en la dirección indicada hasta el ÚLTIMO cilindro del disco y vuelve.
  - LOOK  : avanza solo hasta la última solicitud en esa dirección y vuelve.
  - C-SCAN: avanza hasta el último cilindro, salta al cilindro 0 y sigue en la misma dirección.
            El salto de regreso SE CUENTA en el total (opción --sin-salto para no contarlo).
  - C-LOOK: avanza hasta la última solicitud, salta a la solicitud más baja y sigue.
            El salto también se cuenta.
  - SSTF  : en empate de distancia, gana la solicitud en la dirección actual.
"""
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def recorrido(algoritmo, inicio, solicitudes, max_cil, sube=True):
    pend = list(solicitudes)
    if algoritmo == 'fcfs':
        return [inicio] + pend
    if algoritmo == 'sstf':
        ruta, pos, dir_sube = [inicio], inicio, sube
        while pend:
            mejor = min(pend, key=lambda c: (abs(c - pos), 0 if (c >= pos) == dir_sube else 1))
            dir_sube = mejor >= pos
            pend.remove(mejor); ruta.append(mejor); pos = mejor
        return ruta
    arriba = sorted(c for c in pend if c >= inicio)
    abajo = sorted((c for c in pend if c < inicio), reverse=True)
    if not sube:
        arriba, abajo = sorted((c for c in pend if c <= inicio), reverse=True), sorted(c for c in pend if c > inicio)
    extremo = max_cil if sube else 0
    otro = 0 if sube else max_cil
    if algoritmo == 'scan':
        return [inicio] + arriba + ([extremo] if abajo and (not arriba or arriba[-1] != extremo) else []) + abajo
    if algoritmo == 'look':
        return [inicio] + arriba + abajo
    if algoritmo == 'cscan':
        resto = sorted(abajo) if sube else sorted(abajo, reverse=True)
        if not resto:
            return [inicio] + arriba
        return [inicio] + arriba + ([extremo] if (not arriba or arriba[-1] != extremo) else []) + [otro] + resto
    if algoritmo == 'clook':
        resto = sorted(abajo) if sube else sorted(abajo, reverse=True)
        return [inicio] + arriba + resto
    raise ValueError(algoritmo)


def total(ruta, contar_salto=True, algoritmo=''):
    t = 0
    for a, b in zip(ruta, ruta[1:]):
        salto = algoritmo in ('cscan', 'clook') and ((a > b) if ruta[1] >= ruta[0] else (a < b))
        if salto and not contar_salto:
            continue
        t += abs(b - a)
    return t


def mostrar_todos(titulo, inicio, solicitudes, max_cil, sube=True, contar_salto=True):
    print(f"\n######## {titulo}")
    print(f"Cabezal en {inicio}, dirección {'ascendente' if sube else 'descendente'}, cilindros 0..{max_cil}")
    for alg in ('fcfs', 'sstf', 'scan', 'look', 'cscan', 'clook'):
        r = recorrido(alg, inicio, solicitudes, max_cil, sube)
        print(f"{alg.upper():<7} total = {total(r, contar_salto, alg):>5}   ruta: {' -> '.join(map(str, r))}")


if __name__ == '__main__':
    mostrar_todos('Guía, problema 20', 125, [100, 110, 200, 30, 405, 450, 335, 140, 135, 192], 499)
