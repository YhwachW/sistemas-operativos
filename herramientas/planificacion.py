"""
Simulador de planificación de CPU para comprobar tus ejercicios.

Algoritmos:
  fcfs        First Come, First Served (no apropiativo)
  sjf         SJF no apropiativo (elige la ráfaga más corta y la deja terminar)
  srtf        SJF apropiativo = "SJF Preemptive" de las pautas (Shortest Remaining Time First)
  prio        Prioridad no apropiativa   (número MENOR = prioridad MAYOR, como en las pautas)
  prio_p      Prioridad apropiativa      ("Priority Preemptive")
  rr          Round Robin con la cola del libro (Silberschatz)
  rr_vueltas  Round Robin "por iteraciones" como lo resuelve el profesor en las pautas:
              en cada vuelta atiende a los procesos en orden de llegada.

Uso rápido:
  python planificacion.py                     -> resuelve el ejemplo de la Prueba 1 2024-2
  python planificacion.py datos.txt rr 2      -> lee procesos de un archivo

Formato de datos.txt (una línea por proceso; la prioridad es opcional):
  P1  1,2  3  8
  P2  3,2  2  5
Los decimales pueden ir con coma o con punto. Los cálculos son exactos (fracciones).
"""
from fractions import Fraction as F
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def num(x):
    return F(str(x).strip().replace(',', '.'))


def fmt(x):
    """Muestra un número con hasta 2 decimales y coma decimal, como en las pautas."""
    v = round(float(x), 2)
    s = f"{v:.2f}".rstrip('0').rstrip('.')
    return s.replace('.', ',')


class Proceso:
    def __init__(self, nombre, llegada, rafaga, prioridad=0):
        self.nombre, self.llegada, self.rafaga, self.prioridad = nombre, num(llegada), num(rafaga), int(prioridad)


def simular(procesos, algoritmo, q=None):
    """Devuelve el diagrama de Gantt como lista de (nombre, inicio, fin). 'IDLE' = CPU ociosa."""
    procs = sorted(procesos, key=lambda p: (p.llegada, p.nombre))
    resto = {p.nombre: p.rafaga for p in procs}
    gantt = []
    t = procs[0].llegada

    def agregar(nombre, a, b):
        if b <= a:
            return
        # En Round Robin cada quantum es un tramo aparte (así se dibuja en las pautas).
        if gantt and gantt[-1][0] == nombre and gantt[-1][2] == a and not algoritmo.startswith('rr'):
            gantt[-1] = (nombre, gantt[-1][1], b)
        else:
            gantt.append((nombre, a, b))

    def listos(tiempo):
        return [p for p in procs if p.llegada <= tiempo and resto[p.nombre] > 0]

    def proxima_llegada(tiempo):
        fut = [p.llegada for p in procs if p.llegada > tiempo and resto[p.nombre] > 0]
        return min(fut) if fut else None

    if algoritmo in ('fcfs', 'sjf', 'prio'):
        while any(resto.values()):
            r = listos(t)
            if not r:
                nt = proxima_llegada(t); agregar('IDLE', t, nt); t = nt; continue
            if algoritmo == 'fcfs':
                p = min(r, key=lambda p: (p.llegada, p.nombre))
            elif algoritmo == 'sjf':
                p = min(r, key=lambda p: (p.rafaga, p.llegada, p.nombre))
            else:
                p = min(r, key=lambda p: (p.prioridad, p.llegada, p.nombre))
            agregar(p.nombre, t, t + resto[p.nombre]); t += resto[p.nombre]; resto[p.nombre] = 0
        return gantt

    if algoritmo in ('srtf', 'prio_p'):
        actual = None
        while any(resto.values()):
            r = listos(t)
            if not r:
                nt = proxima_llegada(t); agregar('IDLE', t, nt); t = nt; continue
            if algoritmo == 'srtf':
                clave = lambda p: (resto[p.nombre], 0 if p.nombre == actual else 1, p.llegada, p.nombre)
            else:
                clave = lambda p: (p.prioridad, 0 if p.nombre == actual else 1, p.llegada, p.nombre)
            p = min(r, key=clave)
            actual = p.nombre
            fin = t + resto[p.nombre]
            nt = proxima_llegada(t)
            if nt is not None and nt < fin:
                fin = nt                     # en cada llegada se vuelve a decidir
            agregar(p.nombre, t, fin); resto[p.nombre] -= fin - t; t = fin
        return gantt

    if algoritmo == 'rr':
        if not q:
            raise ValueError('Round Robin necesita un quantum q')
        q = num(q)
        cola, encolados = [], set()

        def encolar_llegadas(hasta):
            for p in procs:
                if p.llegada <= hasta and p.nombre not in encolados and resto[p.nombre] > 0:
                    cola.append(p); encolados.add(p.nombre)
        encolar_llegadas(t)
        while any(resto.values()):
            if not cola:
                nt = proxima_llegada(t); agregar('IDLE', t, nt); t = nt; encolar_llegadas(t); continue
            p = cola.pop(0)
            corre = min(q, resto[p.nombre])
            agregar(p.nombre, t, t + corre); t += corre; resto[p.nombre] -= corre
            encolar_llegadas(t)              # los que llegaron mientras corría entran ANTES
            if resto[p.nombre] > 0:
                cola.append(p)               # ...que el proceso que acaba de salir
        return gantt

    if algoritmo == 'rr_vueltas':
        if not q:
            raise ValueError('Round Robin necesita un quantum q')
        q = num(q)
        while any(resto.values()):
            atendio = False
            for p in procs:                  # una "iteración": todos en orden de llegada
                if resto[p.nombre] <= 0:
                    continue
                if p.llegada > t:
                    if atendio:
                        continue             # todavía no llega: lo verá en la próxima vuelta
                    agregar('IDLE', t, p.llegada); t = p.llegada
                corre = min(q, resto[p.nombre])
                agregar(p.nombre, t, t + corre); t += corre; resto[p.nombre] -= corre
                atendio = True
        return gantt

    raise ValueError(f'Algoritmo desconocido: {algoritmo}')


def tiempos(procesos, gantt):
    """
    Turnaround (T.T.) = fin - llegada
    Waiting    (W.T.) = T.T. - ráfaga            (definición del libro)
    W.T. pauta        = inicio del último tramo - llegada
                        (así aparece calculado en las pautas del curso; coincide con la
                         definición solo si el proceso nunca fue interrumpido)
    """
    res = {}
    for p in procesos:
        tramos = [(a, b) for n, a, b in gantt if n == p.nombre]
        fin = max(b for a, b in tramos)
        ultimo_inicio = max(a for a, b in tramos)
        tt = fin - p.llegada
        res[p.nombre] = (tt, tt - p.rafaga, ultimo_inicio - p.llegada)
    return res


def mostrar(procesos, algoritmo, q=None, titulo=None):
    g = simular(procesos, algoritmo, q)
    print(f"\n== {titulo or algoritmo}{f' (q={q})' if q else ''} ==")
    print('Gantt: ' + '  '.join(f"[{fmt(a)} {n} {fmt(b)}]" for n, a, b in g))
    t = tiempos(procesos, g)
    print(f"{'Proceso':<8}{'Llegada':>8}{'Ráfaga':>8}{'T.T.':>8}{'W.T.':>8}{'W.T.pauta':>11}")
    for p in procesos:
        tt, wt, wtp = t[p.nombre]
        marca = '' if wt == wtp else '  <- distinto'
        print(f"{p.nombre:<8}{fmt(p.llegada):>8}{fmt(p.rafaga):>8}{fmt(tt):>8}{fmt(wt):>8}{fmt(wtp):>11}{marca}")
    n = len(procesos)
    prom = [sum(v[i] for v in t.values()) / n for i in range(3)]
    print(f"{'Promedio':<24}{fmt(prom[0]):>8}{fmt(prom[1]):>8}{fmt(prom[2]):>11}")
    return g, t


def leer(ruta):
    procs = []
    for linea in open(ruta, encoding='utf-8'):
        partes = linea.split()
        if len(partes) >= 3 and not linea.lstrip().startswith('#'):
            procs.append(Proceso(*partes[:4]))
    return procs


if __name__ == '__main__':
    if len(sys.argv) >= 3:
        procs = leer(sys.argv[1])
        mostrar(procs, sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
    else:
        # Prueba 1 2024-2, problema 2
        ps = [Proceso('J1', '1,6', 1), Proceso('J2', '1,3', 2), Proceso('J3', '0,5', 6),
              Proceso('J4', '1,5', 2), Proceso('J5', '5,6', 2)]
        mostrar(ps, 'srtf', titulo='SJF Preemptive (SRTF)')
        mostrar(ps, 'rr_vueltas', 2, titulo='Round Robin por iteraciones (como la pauta)')
        mostrar(ps, 'rr', 2, titulo='Round Robin con cola (libro)')
