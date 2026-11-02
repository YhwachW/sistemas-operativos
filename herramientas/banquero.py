"""
Algoritmo del banquero (Dijkstra): estado seguro, secuencias seguras y solicitudes.

  Necesidad  = Máximo - Asignados
  Disponible = Total - suma(Asignados)        (si te dan el Total)

Un estado es SEGURO si existe al menos un orden en que todos los procesos pueden
terminar: se busca un proceso con Necesidad <= Disponible, se "deja terminar" y
devuelve lo que tenía (Disponible += Asignados), y se repite.

Uso: edita los datos al final del archivo o importa las funciones.
"""
import sys
from itertools import permutations

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def vec(s):
    return [int(x) for x in str(s).replace(',', ' ').split()]


def le(a, b):
    return all(x <= y for x, y in zip(a, b))


def necesidad(maximo, asignados):
    return [[m - a for m, a in zip(M, A)] for M, A in zip(maximo, asignados)]


def secuencia_codiciosa(nombres, asignados, maximo, disponible, verbose=True):
    """Recorre los procesos en orden (P0, P1, ...) y toma el primero que cabe, como en clases."""
    nec = necesidad(maximo, asignados)
    disp = list(disponible)
    terminado = [False] * len(nombres)
    orden = []
    if verbose:
        print(f"Disponible inicial: {disp}")
    progreso = True
    while progreso:
        progreso = False
        for i, n in enumerate(nombres):
            if not terminado[i] and le(nec[i], disp):
                nuevo = [d + a for d, a in zip(disp, asignados[i])]
                if verbose:
                    print(f"  {n}: Necesidad {nec[i]} <= Disponible {disp}  -> termina y libera {asignados[i]}  -> Disponible {nuevo}")
                disp = nuevo
                terminado[i] = True
                orden.append(n)
                progreso = True
    if all(terminado):
        if verbose:
            print(f"ESTADO SEGURO. Secuencia: {', '.join(orden)}")
        return orden
    if verbose:
        faltan = [n for n, t in zip(nombres, terminado) if not t]
        print(f"ESTADO INSEGURO: {', '.join(faltan)} no pueden terminar con Disponible {disp}")
    return None


def todas_las_secuencias(nombres, asignados, maximo, disponible):
    nec = necesidad(maximo, asignados)
    seguras = []
    for perm in permutations(range(len(nombres))):
        disp = list(disponible)
        ok = True
        for i in perm:
            if not le(nec[i], disp):
                ok = False
                break
            disp = [d + a for d, a in zip(disp, asignados[i])]
        if ok:
            seguras.append([nombres[i] for i in perm])
    return seguras


def solicitud(nombres, asignados, maximo, disponible, proceso, pedido):
    """¿Se puede conceder 'pedido' a 'proceso' de inmediato?"""
    i = nombres.index(proceso)
    nec = necesidad(maximo, asignados)
    print(f"\nSolicitud de {proceso}: {pedido}")
    if not le(pedido, nec[i]):
        print(f"  ERROR: pide más que su necesidad declarada {nec[i]}")
        return False
    if not le(pedido, disponible):
        print(f"  No hay suficientes disponibles {disponible}: {proceso} debe esperar")
        return False
    asig2 = [list(a) for a in asignados]
    asig2[i] = [a + p for a, p in zip(asig2[i], pedido)]
    disp2 = [d - p for d, p in zip(disponible, pedido)]
    print(f"  Se simula la asignación: Asignados[{proceso}] = {asig2[i]}, Disponible = {disp2}")
    ok = secuencia_codiciosa(nombres, asig2, maximo, disp2) is not None
    print('  -> Se CONCEDE (el estado sigue seguro)' if ok else '  -> NO se concede (dejaría el sistema inseguro)')
    return ok


def resolver(titulo, nombres, asignados, maximo, disponible=None, total=None):
    if disponible is None:
        usados = [sum(col) for col in zip(*asignados)]
        disponible = [t - u for t, u in zip(total, usados)]
    print(f"\n######## {titulo}")
    nec = necesidad(maximo, asignados)
    print(f"{'Proc':<6}{'Asignados':<14}{'Máximo':<14}{'Necesidad':<14}")
    for n, a, m, ne in zip(nombres, asignados, maximo, nec):
        print(f"{n:<6}{str(a):<14}{str(m):<14}{str(ne):<14}")
    secuencia_codiciosa(nombres, asignados, maximo, disponible)
    todas = todas_las_secuencias(nombres, asignados, maximo, disponible)
    print(f"Todas las secuencias seguras ({len(todas)}): " + ('; '.join(', '.join(s) for s in todas) if todas else 'ninguna'))
    return disponible


if __name__ == '__main__':
    resolver('Prueba 1 2024-2', ['P0', 'P1', 'P2', 'P3'],
             [vec('1 0 0'), vec('0 1 2'), vec('3 0 0'), vec('0 1 0')],
             [vec('4 2 3'), vec('2 2 3'), vec('4 2 1'), vec('0 2 2')], total=vec('5 3 4'))
