"""
Grafo de asignación de recursos: busca ciclos y decide si hay interbloqueo.

Se escribe como en las pruebas:  V = {(P1,R1); (R1,P2); ...}
   (Pi, Rj) = vector de SOLICITUD : Pi pide una instancia de Rj
   (Rj, Pi) = vector de ASIGNACIÓN: una instancia de Rj está asignada a Pi

Reglas (Silberschatz, cap. 8, y la terminología del curso):
  - Sin ciclos                                  -> no hay deadlock (ESTADO SEGURO)
  - Ciclo y todos sus recursos con 1 instancia   -> deadlock seguro   ("inseguro irreversible")
  - Ciclo con recursos de varias instancias      -> deadlock POSIBLE  ("inseguro reversible"):
    hay que reducir el grafo para saber si de verdad se traba.

La reducción: un proceso cuyas solicitudes se pueden atender con las instancias libres
"termina" y devuelve todo lo que tiene. Los que nunca pueden terminar están interbloqueados.
"""
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def leer(V):
    pares = re.findall(r'\(\s*([A-Za-z]\w*)\s*,\s*([A-Za-z]\w*)\s*\)', V)
    return [(a.upper(), b.upper()) for a, b in pares]


def analizar(V, instancias=None, titulo=None):
    aristas = leer(V)
    es_proc = lambda x: x.startswith('P')
    procs = sorted({x for e in aristas for x in e if es_proc(x)}, key=lambda s: int(s[1:]))
    recs = sorted({x for e in aristas for x in e if not es_proc(x)}, key=lambda s: int(s[1:]))
    asign = {p: {} for p in procs}
    pide = {p: {} for p in procs}
    for a, b in aristas:
        if es_proc(a):
            pide[a][b] = pide[a].get(b, 0) + 1
        else:
            asign[b][a] = asign[b].get(a, 0) + 1
    usadas = {r: sum(asign[p].get(r, 0) for p in procs) for r in recs}
    inst = dict(instancias or {})
    for r in recs:
        inst.setdefault(r, max(usadas[r], 1))   # si no se dice, se asume lo mínimo
    print(f"\n######## {titulo or 'Grafo'}")
    for r in recs:
        print(f"  {r}: {inst[r]} instancia(s), asignadas {usadas[r]}, libres {inst[r] - usadas[r]}")
    for p in procs:
        print(f"  {p}: tiene {asign[p] or '-'}  pide {pide[p] or '-'}")
    # ciclos (búsqueda simple en el grafo dirigido)
    ady = {}
    for a, b in aristas:
        ady.setdefault(a, set()).add(b)
    ciclos = set()

    def dfs(inicio, actual, camino):
        for s in ady.get(actual, ()):
            if s == inicio:
                c = camino[:]
                k = c.index(min(c))
                ciclos.add(tuple(c[k:] + c[:k]))
            elif s not in camino and s > inicio:
                dfs(inicio, s, camino + [s])
    for n in sorted(ady):
        dfs(n, n, [n])
    if ciclos:
        for c in sorted(ciclos, key=len):
            unicos = all(inst[x] == 1 for x in c if not es_proc(x))
            print(f"  Ciclo: {' -> '.join(c)} -> {c[0]}   ({'solo recursos de 1 instancia' if unicos else 'hay recursos con varias instancias'})")
    else:
        print('  No hay ciclos (no hay espera circular).')
    # reducción del grafo
    libres = {r: inst[r] - usadas[r] for r in recs}
    vivos = list(procs)
    orden = []
    cambio = True
    while cambio:
        cambio = False
        for p in list(vivos):
            if all(libres[r] >= n for r, n in pide[p].items()):
                for r, n in asign[p].items():
                    libres[r] += n
                vivos.remove(p)
                orden.append(p)
                cambio = True
    if not vivos:
        estado = 'SEGURO (sin interbloqueo)' if not ciclos else 'hay ciclo pero NO hay interbloqueo (inseguro reversible)'
        print(f"  Reducción: todos terminan -> {', '.join(orden)}")
        print(f"  ESTADO: {estado}")
    else:
        print(f"  Reducción: terminan {', '.join(orden) or 'ninguno'}; quedan trabados {', '.join(vivos)}")
        print('  ESTADO: INTERBLOQUEO (inseguro irreversible)')
    return vivos


if __name__ == '__main__':
    analizar('(p1,r1);(p1,r2);(r1,p2);(r2,p2);(r2,p3);(r2,p4);(r1,p5);(p5,r2);(r1,p3);(r4,p4);(r4,p5);(R1,P6)',
             {'R1': 4, 'R2': 3, 'R3': 1, 'R4': 3}, 'Recuperativa 2026-1 / Guía 29')
