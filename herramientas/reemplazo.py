"""
Reemplazo de páginas: FIFO, Óptimo y LRU, con la tabla paso a paso.

Además calcula el "tiempo de fallas" como en las pautas del curso:
    cada falla  = 1 ENTRADA (se lee la página desde disco)
    cada reemplazo = 1 SALIDA (la página víctima se escribe a disco)
    tiempo = (entradas + salidas) x (tiempo de acceso + tiempo de transferencia)

Uso:
  python reemplazo.py                      -> ejemplos de las pruebas
  python reemplazo.py lru 3 "7,0,1,2,0,3" [acceso] [transferencia]
"""
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def simular(algoritmo, marcos, cadena):
    """Devuelve (pasos, fallas, reemplazos, entradas_por_pagina, salidas_por_pagina).
    Cada paso = (referencia, contenido_de_los_marcos, hubo_falla, victima)."""
    memoria = [None] * marcos          # contenido de cada marco (posición fija, como en la pizarra)
    llegada = {}                       # para FIFO: cuándo entró cada página
    ultimo_uso = {}                    # para LRU
    pasos, fallas, reemplazos = [], 0, 0
    entradas, salidas = {}, {}
    for i, pag in enumerate(cadena):
        victima = None
        if pag in memoria:
            falla = False
        else:
            falla = True
            fallas += 1
            entradas[pag] = entradas.get(pag, 0) + 1
            if None in memoria:
                pos = memoria.index(None)
            else:
                if algoritmo == 'fifo':
                    pos = min(range(marcos), key=lambda k: llegada[memoria[k]])
                elif algoritmo == 'lru':
                    pos = min(range(marcos), key=lambda k: ultimo_uso[memoria[k]])
                elif algoritmo == 'optimo':
                    def proximo_uso(k):
                        resto = cadena[i + 1:]
                        p = memoria[k]
                        # si no se vuelve a usar, es la mejor víctima; entre varias así, la que entró antes
                        return (len(resto) + 1, -llegada[p]) if p not in resto else (resto.index(p), 0)
                    pos = max(range(marcos), key=proximo_uso)
                else:
                    raise ValueError(algoritmo)
                victima = memoria[pos]
                reemplazos += 1
                salidas[victima] = salidas.get(victima, 0) + 1
            memoria[pos] = pag
            llegada[pag] = i
        ultimo_uso[pag] = i
        pasos.append((pag, list(memoria), falla, victima))
    return pasos, fallas, reemplazos, entradas, salidas


def mostrar(algoritmo, marcos, cadena, acceso=None, transferencia=None, titulo=None):
    pasos, fallas, reemplazos, entradas, salidas = simular(algoritmo, marcos, cadena)
    print(f"\n== {titulo or algoritmo.upper()} con {marcos} marcos ==")
    ancho = max(len(str(x)) for x in cadena) + 1
    print('Ref.   ' + ''.join(f"{str(p):>{ancho}}" for p, *_ in pasos))
    for m in range(marcos):
        fila = ''.join(f"{('' if s[1][m] is None else str(s[1][m])):>{ancho}}" for s in pasos)
        print(f"Marco{m + 1} " + fila)
    print('Falla  ' + ''.join(f"{'*' if f else '':>{ancho}}" for _, _, f, _ in pasos))
    print(f"Fallas de página: {fallas}   Reemplazos (víctimas): {reemplazos}")
    paginas = sorted(set(cadena), key=lambda x: (str(type(x)), x))
    print(f"{'Página':<8}{'Entradas':>9}{'Salidas':>9}{'Total':>7}")
    for p in paginas:
        e, s = entradas.get(p, 0), salidas.get(p, 0)
        print(f"{str(p):<8}{e:>9}{s:>9}{e + s:>7}")
    total = fallas + reemplazos
    print(f"{'Total':<8}{fallas:>9}{reemplazos:>9}{total:>7}")
    if acceso is not None and transferencia is not None:
        t = total * (acceso + transferencia)
        print(f"Tiempo en fallas = {total} x ({acceso} + {transferencia}) = {round(t, 4)}")
    return fallas, reemplazos


def leer_cadena(s):
    return [int(x) for x in s.replace(';', ',').split(',') if x.strip()]


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        alg, marcos, cadena = sys.argv[1], int(sys.argv[2]), leer_cadena(sys.argv[3])
        acc = float(sys.argv[4].replace(',', '.')) if len(sys.argv) > 4 else None
        tra = float(sys.argv[5].replace(',', '.')) if len(sys.argv) > 5 else None
        mostrar(alg, marcos, cadena, acc, tra)
    else:
        mostrar('lru', 3, leer_cadena('7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1'), 20, 30, 'Prueba 2 2025-2: LRU')
