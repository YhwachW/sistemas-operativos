"""
Genera los diagramas SVG de estudio/diagramas/ a partir de los mismos simuladores
que verificaron las pautas (planificacion.py, reemplazo.py, disco.py).

    python herramientas/diagramas.py

Cada SVG trae su propio fondo y se adapta al modo claro u oscuro, para verse bien
en GitHub (que muestra los .svg enlazados como imagen).
"""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from planificacion import Proceso as P, simular as plan  # noqa: E402
from reemplazo import simular as reemplazar  # noqa: E402
from disco import recorrido, total as total_disco  # noqa: E402

SALIDA = os.path.join(os.path.dirname(__file__), '..', 'estudio', 'diagramas')
FONT = "ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"

# Paleta: (relleno, borde) para modo claro y oscuro. Un color fijo por proceso.
PALETA = [
    ('#ddf4ff', '#0969da', '#0c2d6b', '#4493f8'),   # azul
    ('#dafbe1', '#1a7f37', '#0f3a1e', '#3fb950'),   # verde
    ('#fff1e5', '#bc4c00', '#4a2410', '#db6d28'),   # naranjo
    ('#fbefff', '#8250df', '#2e1a4f', '#ab7df8'),   # morado
    ('#ffeff7', '#bf3989', '#4a1530', '#db61a2'),   # rosado
    ('#d8f3f6', '#1b7c83', '#0c3a3e', '#39c5cf'),   # turquesa
    ('#fff8c5', '#9a6700', '#3d2e00', '#d29922'),   # amarillo
]


def css():
    claro = ''.join(f'.p{i}{{fill:{a};stroke:{b}}} .s{i}{{stroke:{b}}} .f{i}{{fill:{b}}} ' for i, (a, b, c, d) in enumerate(PALETA))
    oscuro = ''.join(f'.p{i}{{fill:{c};stroke:{d}}} .s{i}{{stroke:{d}}} .f{i}{{fill:{d}}} ' for i, (a, b, c, d) in enumerate(PALETA))
    return (
        '.card{fill:#ffffff;stroke:#d0d7de} .ink{fill:#1f2328} .muted{fill:#59636e} '
        '.ln{stroke:#1f2328;fill:none} .grid{stroke:#d0d7de;fill:none} .soft{fill:#f6f8fa;stroke:#d0d7de} '
        '.idle{fill:url(#rayas);stroke:#d0d7de} .acc{stroke:#cf222e;fill:none} .acct{fill:#cf222e} '
        '.accf{fill:#ffebe9;stroke:#cf222e} .ok{fill:#1a7f37} .okl{stroke:#1a7f37;fill:none} .okf{fill:#dafbe1;stroke:#1a7f37} '
        '.rayas{stroke:#d0d7de} .dot{fill:#1f2328} ' + claro +
        '@media (prefers-color-scheme: dark){'
        '.card{fill:#0d1117;stroke:#30363d} .ink{fill:#e6edf3} .muted{fill:#9198a1} .ln{stroke:#e6edf3} '
        '.grid{stroke:#30363d} .soft{fill:#161b22;stroke:#30363d} .idle{stroke:#30363d} .acc{stroke:#ff7b72} .acct{fill:#ff7b72} '
        '.accf{fill:#3d1214;stroke:#ff7b72} .ok{fill:#3fb950} .okl{stroke:#3fb950} .okf{fill:#0f3a1e;stroke:#3fb950} '
        '.rayas{stroke:#30363d} .dot{fill:#e6edf3} ' + oscuro + '}'
    )


def svg(w, h, cuerpo, etiqueta):
    defs = (
        '<defs>'
        '<pattern id="rayas" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
        '<line x1="0" y1="0" x2="0" y2="6" class="rayas" stroke-width="2"/></pattern>'
        '<marker id="fl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        '<path d="M0,0 L10,5 L0,10 z" class="dot"/></marker>'
        '<marker id="fla" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        '<path d="M0,0 L10,5 L0,10 z" class="acct"/></marker>'
        '<marker id="flo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        '<path d="M0,0 L10,5 L0,10 z" class="ok"/></marker>'
        '</defs>'
    )
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="{esc(etiqueta)}" font-family="{FONT}">'
            f'<title>{esc(etiqueta)}</title><style>{css()}</style>{defs}'
            f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="10" class="card"/>{cuerpo}</svg>')


def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def txt(x, y, s, cls='ink', size=13, anchor='start', weight=400, extra=''):
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}" {extra}>{esc(s)}</text>'


def coma(t):
    v = round(float(t), 2)
    s = f'{v:.2f}'.rstrip('0').rstrip('.')
    return s.replace('.', ',')


def guardar(nombre, contenido):
    os.makedirs(SALIDA, exist_ok=True)
    with open(os.path.join(SALIDA, nombre), 'w', encoding='utf-8', newline='\n') as f:
        f.write(contenido)
    print('  ', nombre)


# ------------------------------------------------------------------ Gantt
def gantt(nombre, filas, orden, etiqueta, ancho=760):
    """filas: lista de dicts {titulo, segs: [(proc, ini, fin)], nota, resaltar: set de índices}"""
    t0 = min(a for f in filas for _, a, _ in f['segs'])
    t1 = max(b for f in filas for _, _, b in f['segs'])
    L, R = 24, 24
    W = ancho - L - R
    X = lambda t: L + float(t - t0) / float(t1 - t0) * W
    color = {n: i % len(PALETA) for i, n in enumerate(orden)}
    out, y = [], 16
    for f in filas:
        out.append(txt(L, y + 14, f['titulo'], 'ink', 14, weight=600))
        if f.get('nota'):
            out.append(txt(ancho - R, y + 14, f['nota'], 'acct', 12.5, 'end', 600))
        y += 24
        arriba = []       # etiquetas que no caben dentro del bloque
        angosto = any(n != 'IDLE' and (X(b) - X(a)) < 7.5 * len(n) + 10 for n, a, b in f['segs'])
        barra_y = y + (30 if angosto else 14)
        for i, (n, a, b) in enumerate(f['segs']):
            xa, xb = X(a), X(b)
            w = xb - xa
            if n == 'IDLE':
                out.append(f'<rect x="{xa:.1f}" y="{barra_y}" width="{w:.1f}" height="34" class="idle"/>')
                if w > 52:
                    out.append(txt((xa + xb) / 2, barra_y + 21.5, 'ocioso', 'muted', 11.5, 'middle'))
                continue
            c = color.get(n, 0)
            hl = i in f.get('resaltar', set())
            out.append(f'<rect x="{xa:.1f}" y="{barra_y}" width="{w:.1f}" height="34" class="p{c}" stroke-width="{2.5 if hl else 1}"/>')
            if hl:
                out.append(f'<rect x="{xa + 1.5:.1f}" y="{barra_y + 1.5}" width="{w - 3:.1f}" height="31" class="acc" stroke-width="2"/>')
            if w >= 7.5 * len(n) + 10:
                out.append(txt((xa + xb) / 2, barra_y + 21.5, n, 'ink', 12.5, 'middle', 600))
            else:
                arriba.append(((xa + xb) / 2, n))
        if arriba:
            for cx, n in arriba:
                out.append(f'<line x1="{cx:.1f}" y1="{barra_y - 2}" x2="{cx:.1f}" y2="{barra_y - 9}" class="grid"/>')
                out.append(txt(cx, barra_y - 12, n, 'ink', 11.5, 'middle', 600))
        # marcas de tiempo, en dos niveles si chocan
        cortes = sorted({a for _, a, _ in f['segs']} | {b for _, _, b in f['segs']})
        niveles = [[], [], []]
        for t in cortes:
            x = X(t)
            s = coma(t)
            w = 6.6 * len(s) + 4
            nivel = 0
            while nivel < 2 and any(abs(x - px) < (w + pw) / 2 for px, pw in niveles[nivel]):
                nivel += 1
            niveles[nivel].append((x, w))
            yy = barra_y + 34 + 15 + 13 * nivel
            out.append(f'<line x1="{x:.1f}" y1="{barra_y + 34}" x2="{x:.1f}" y2="{yy - 11 if nivel else barra_y + 39}" class="grid"/>')
            out.append(txt(x, yy, s, 'muted', 11.5, 'middle'))
        usados = max(i for i, n in enumerate(niveles) if n) if any(niveles) else 0
        y = barra_y + 34 + 18 + 13 * usados + 16
    guardar(nombre, svg(ancho, y, ''.join(out), etiqueta))


def seg_plan(procs, alg, q=None):
    return plan(procs, alg, q)


def diagramas_planificacion():
    print('Planificación')
    # Parcial 2024-2
    ps = [P('J1', '1,6', 1), P('J2', '1,3', 2), P('J3', '0,5', 6), P('J4', '1,5', 2), P('J5', '5,6', 2)]
    orden = ['J1', 'J2', 'J3', 'J4', 'J5']
    gantt('gantt-2024-2.svg', [
        {'titulo': 'SJF apropiativo (SRTF)', 'segs': plan(ps, 'srtf')},
        {'titulo': 'Round Robin q = 2, por iteraciones', 'segs': plan(ps, 'rr_vueltas', 2)},
    ], orden, 'Parcial 2024-2: Gantt de SJF apropiativo y de Round Robin q=2 por iteraciones; ambos terminan en 13,5')
    # Comparación RR: vueltas vs cola
    v = plan(ps, 'rr_vueltas', 2)
    c = plan(ps, 'rr', 2)
    gantt('rr-iteraciones-vs-cola.svg', [
        {'titulo': 'Por iteraciones en orden de llegada (como la pauta)', 'segs': v,
         'resaltar': {i for i, s in enumerate(v) if s[0] == 'J5'}, 'nota': 'J5 termina en 9,5'},
        {'titulo': 'Con la cola FIFO del libro', 'segs': c,
         'resaltar': {i for i, s in enumerate(c) if s[0] == 'J5'}, 'nota': 'J5 termina en 11,5'},
    ], orden, 'Round Robin q=2: por iteraciones J5 corre de 7,5 a 9,5; con la cola del libro J3 va antes y J5 corre de 9,5 a 11,5')
    # Recuperativa 2024-2 / Examen 2025-1
    ps = [P('Azul', '0,1', 4, 3), P('Monse', '0,8', 2, 0), P('Prg1', '0,5', 3, 2)]
    gantt('gantt-recup-2024-2.svg', [
        {'titulo': 'FCFS', 'segs': plan(ps, 'fcfs')},
        {'titulo': 'SJF apropiativo', 'segs': plan(ps, 'srtf')},
    ], ['Azul', 'Monse', 'Prg1'], 'Recuperativa 2024-2: FCFS y SJF apropiativo; en SJF Prg1 expulsa a Azul en 0,5 y Monse a Prg1 en 0,8')
    # 2009 / Recuperativa 2026-1
    ps = [P('P1', '1,2', 3, 8), P('P2', '3,2', 2, 5), P('P3', '5,5', 1, 4), P('P4', '8,6', 3, 1), P('P5', '10,9', 2, 0)]
    gantt('gantt-2009-recup-2026.svg', [
        {'titulo': 'Prioridad apropiativa (número menor = más prioridad)', 'segs': plan(ps, 'prio_p')},
        {'titulo': 'SJF apropiativo y Round Robin q = 3 (dan lo mismo)', 'segs': plan(ps, 'srtf')},
    ], ['P1', 'P2', 'P3', 'P4', 'P5'], 'P1 2009 y Recuperativa 2026-1: prioridad apropiativa interrumpe dos veces a P1; con SJF y RR no hay interrupciones; la CPU queda ociosa entre 7,2 y 8,6')
    # Examen 2026-1
    ps = [P('1', '2,5', 3), P('2', '1,3', 2), P('3', '1,4', 1)]
    gantt('gantt-examen-2026-1.svg', [
        {'titulo': 'SJF apropiativo', 'segs': plan(ps, 'srtf')},
        {'titulo': 'Round Robin q = 2', 'segs': plan(ps, 'rr_vueltas', 2)},
    ], ['1', '2', '3'], 'Examen 2026-1: en SJF el proceso 3 expulsa al 2 en 1,4; en RR el proceso 1 usa dos quanta seguidos')
    # P1 2025-2
    ps = [P('P1', '1,2', 12, 5), P('P2', '3,2', 9, 4), P('P3', '5,5', 8, 2), P('P4', '8,6', 11, 0), P('P5', '10,9', 14, 4)]
    o = ['P1', 'P2', 'P3', 'P4', 'P5']
    gantt('gantt-2025-2.svg', [
        {'titulo': 'FCFS · T.T. prom. 26,52', 'segs': plan(ps, 'fcfs')},
        {'titulo': 'SJF apropiativo · T.T. prom. 25,92 (el mejor)', 'segs': plan(ps, 'srtf')},
        {'titulo': 'Prioridad apropiativa · T.T. prom. 29,26', 'segs': plan(ps, 'prio_p')},
        {'titulo': 'Round Robin q = 3 por iteraciones · T.T. prom. 40,12', 'segs': plan(ps, 'rr_vueltas', 3)},
    ], o, 'P1 2025-2: los cuatro algoritmos sobre los mismos procesos; SJF apropiativo tiene el menor turnaround promedio', ancho=860)
    # P1 2022-2
    ps = [P('T1', '0,8', 10), P('T2', '2,3', 5), P('T3', '5,2', 2)]
    gantt('gantt-2022-2.svg', [
        {'titulo': 'FCFS', 'segs': plan(ps, 'fcfs')},
        {'titulo': 'SJF no apropiativo', 'segs': plan(ps, 'sjf')},
        {'titulo': 'Round Robin q = 2, por iteraciones', 'segs': plan(ps, 'rr_vueltas', 2)},
    ], ['T1', 'T2', 'T3'], 'P1 2022-2: FCFS, SJF no apropiativo y Round Robin q=2; en SJF no apropiativo T1 no se interrumpe y luego va T3 antes que T2')


# ------------------------------------------------------------------ estados de un proceso
def flecha(x1, y1, x2, y2, etiqueta=None, lx=None, ly=None, anchor='middle', cls='ln', marker='fl', dash=False, curva=None):
    d = f'M{x1},{y1} Q{curva[0]},{curva[1]} {x2},{y2}' if curva else f'M{x1},{y1} L{x2},{y2}'
    s = f'<path d="{d}" class="{cls}" stroke-width="1.6" marker-end="url(#{marker})"{" stroke-dasharray=\"5 4\"" if dash else ""}/>'
    if etiqueta:
        s += txt(lx, ly, etiqueta, 'muted', 12, anchor)
    return s


def nodo_estado(cx, cy, nombre, cls='soft', w=124, h=44):
    return (f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="22" class="{cls}" stroke-width="1.4"/>'
            + txt(cx, cy + 5, nombre, 'ink', 14, 'middle', 600))


def diagrama_estados():
    print('Procesos')
    W, H = 760, 340
    nuevo, terminado = (110, 60), (650, 60)
    listo, ejec = (210, 175), (550, 175)
    espera = (380, 300)
    o = []
    o.append(nodo_estado(*nuevo, 'Nuevo'))
    o.append(nodo_estado(*terminado, 'Terminado'))
    o.append(nodo_estado(*listo, 'Listo', 'p0'))
    o.append(nodo_estado(*ejec, 'Ejecución', 'p1'))
    o.append(nodo_estado(*espera, 'Espera', 'p2'))
    o.append(flecha(130, 83, 185, 152, 'admitido', 142, 128, 'end'))
    o.append(flecha(520, 152, 625, 83, 'exit', 590, 112, 'start'))
    o.append(flecha(272, 166, 488, 166, 'el planificador lo despacha', 380, 140, 'middle', curva=(380, 120)))
    o.append(flecha(488, 186, 272, 186, 'interrupción / fin del quantum', 380, 236, 'middle', curva=(380, 226)))
    o.append(flecha(560, 198, 440, 293, 'pide E/S o un evento', 520, 262, 'start'))
    o.append(flecha(320, 293, 200, 198, 'termina la E/S', 240, 262, 'end'))
    o.append(txt(380, 24, 'De Espera no se pasa directo a Ejecución: primero vuelve a Listo', 'muted', 12, 'middle'))
    guardar('estados-proceso.svg', svg(W, H, ''.join(o),
            'Diagrama de estados de un proceso: Nuevo, Listo, Ejecución, Espera y Terminado, con las transiciones entre ellos'))


def diagrama_memoria_proceso():
    W, H = 520, 300
    x, w = 150, 170
    capas = [('pila', 'variables locales, parámetros', 'p0', 52), (None, None, None, 66),
             ('heap', 'memoria dinámica (malloc / new)', 'p3', 52), ('datos', 'variables globales', 'p1', 44),
             ('texto', 'el código', 'p2', 44)]
    o, y = [], 30
    o.append(txt(x + w / 2, 20, 'dirección alta', 'muted', 11.5, 'middle'))
    for nombre, desc, cls, h in capas:
        if nombre is None:
            o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" class="soft" stroke-dasharray="4 4"/>')
            o.append(txt(x + w / 2, y + h / 2 + 4, 'espacio libre', 'muted', 11.5, 'middle'))
            o.append(f'<path d="M{x + 30},{y + 6} L{x + 30},{y + 24}" class="ln" stroke-width="1.6" marker-end="url(#fl)"/>')
            o.append(f'<path d="M{x + w - 30},{y + h - 6} L{x + w - 30},{y + h - 24}" class="ln" stroke-width="1.6" marker-end="url(#fl)"/>')
            o.append(txt(x - 12, y + 18, 'la pila crece hacia abajo', 'muted', 11.5, 'end'))
            o.append(txt(x - 12, y + h - 8, 'el heap crece hacia arriba', 'muted', 11.5, 'end'))
        else:
            o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" class="{cls}"/>')
            o.append(txt(x + w / 2, y + h / 2 + 5, nombre, 'ink', 14, 'middle', 600))
            o.append(txt(x + w + 14, y + h / 2 + 4, desc, 'muted', 12))
        y += h
    o.append(txt(x + w / 2, y + 18, 'dirección baja', 'muted', 11.5, 'middle'))
    guardar('memoria-proceso.svg', svg(W, y + 30, ''.join(o),
            'Un proceso en memoria: texto y datos abajo, heap que crece hacia arriba, pila que crece hacia abajo'))


# ------------------------------------------------------------------ grafos de recursos
import math  # noqa: E402


def recorte_circulo(cx, cy, r, tx, ty):
    d = math.hypot(tx - cx, ty - cy)
    return cx + (tx - cx) * r / d, cy + (ty - cy) * r / d


def recorte_rect(cx, cy, w, h, tx, ty):
    dx, dy = tx - cx, ty - cy
    sx = (w / 2) / abs(dx) if dx else float('inf')
    sy = (h / 2) / abs(dy) if dy else float('inf')
    s = min(sx, sy)
    return cx + dx * s, cy + dy * s


def grafo_recursos(nombre, procesos, recursos, aristas, etiqueta, titulo, nota, W=640, H=360, leyenda_y=None, anotar=None):
    """procesos: {P: (x,y)}; recursos: {R: (x,y,instancias)};
    aristas: [(origen, destino, 'pide'|'asig', destacada)]"""
    o = [txt(24, 30, titulo, 'ink', 14, weight=600)]
    if nota:
        o.append(txt(W - 24, 30, nota[0], nota[1], 12.5, 'end', 600))
    RW, RH, PR = 62, 36, 23
    for a, b, tipo, dest in aristas:
        pa = procesos.get(a) or recursos[a][:2]
        pb = procesos.get(b) or recursos[b][:2]
        if a in procesos:
            x1, y1 = recorte_circulo(*pa, PR + 2, *pb)
            x2, y2 = recorte_rect(*pb, RW + 6, RH + 6, *pa)
        else:
            x1, y1 = recorte_rect(*pa, RW, RH, *pb)
            x2, y2 = recorte_circulo(*pb, PR + 4, *pa)
        cls = 'acc' if dest else 'ln'
        mk = 'fla' if dest else 'fl'
        dash = ' stroke-dasharray="6 4"' if tipo == 'pide' else ''
        o.append(f'<path d="M{x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f}" class="{cls}" stroke-width="{2.2 if dest else 1.5}"{dash} marker-end="url(#{mk})"/>')
    for r, (x, y, n) in recursos.items():
        o.append(f'<rect x="{x - RW / 2}" y="{y - RH / 2}" width="{RW}" height="{RH}" rx="5" class="soft" stroke-width="1.4"/>')
        abajo = y > max(py for _, py in procesos.values())
        o.append(txt(x, y + RH / 2 + 17 if abajo else y - RH / 2 - 7, r, 'ink', 13, 'middle', 600))
        for k in range(n):
            cx = x - (n - 1) * 7 + k * 14
            o.append(f'<circle cx="{cx}" cy="{y}" r="4" class="dot"/>')
    for p, (x, y) in procesos.items():
        o.append(f'<circle cx="{x}" cy="{y}" r="{PR}" class="p0" stroke-width="1.4"/>')
        o.append(txt(x, y + 5, p, 'ink', 13.5, 'middle', 600))
    for (ax, ay, texto, cls) in (anotar or []):
        o.append(txt(ax, ay, texto, cls, 12, 'start', 600))
    ly = leyenda_y or H - 22
    o.append(f'<path d="M24,{ly - 4} L60,{ly - 4}" class="ln" stroke-width="1.5" stroke-dasharray="6 4" marker-end="url(#fl)"/>')
    o.append(txt(66, ly, 'pide (P → R)', 'muted', 12))
    o.append(f'<path d="M170,{ly - 4} L206,{ly - 4}" class="ln" stroke-width="1.5" marker-end="url(#fl)"/>')
    o.append(txt(212, ly, 'asignado (R → P)', 'muted', 12))
    o.append(f'<path d="M340,{ly - 4} L376,{ly - 4}" class="acc" stroke-width="2.2" marker-end="url(#fla)"/>')
    o.append(txt(382, ly, 'arista del ciclo', 'muted', 12))
    o.append(txt(W - 24, ly, '• = una instancia', 'muted', 12, 'end'))
    guardar(nombre, svg(W, H, ''.join(o), etiqueta))


def diagramas_grafos():
    print('Interbloqueo')
    # Recuperativa 2024-2, problema 5
    procesos = {'P1': (120, 200), 'P2': (320, 200), 'P3': (520, 200)}
    recursos = {'R1': (220, 95, 1), 'R2': (420, 95, 1), 'R3': (320, 300, 2)}
    aristas = [('P1', 'R1', 'pide', True), ('R1', 'P2', 'asig', True), ('P2', 'R2', 'pide', True), ('R2', 'P3', 'asig', True),
               ('P3', 'R3', 'pide', True), ('R3', 'P1', 'asig', True), ('R3', 'P2', 'asig', False)]
    grafo_recursos('grafo-recup-2024-2.svg', procesos, recursos, aristas,
                   'Recuperativa 2024-2: ciclo P1, R1, P2, R2, P3, R3; las dos instancias de R3 las tienen P1 y P2, que también esperan; hay interbloqueo',
                   'Recuperativa 2024-2 · problema 5', ('Interbloqueo: nadie puede soltar nada', 'acct'), H=380)
    # Guía 6: ciclo SIN deadlock
    procesos = {'P1': (150, 205), 'P2': (500, 300), 'P3': (500, 120)}
    recursos = {'R1': (60, 110, 1), 'R2': (340, 300, 2), 'R3': (340, 120, 1)}
    aristas = [('R1', 'P1', 'asig', False), ('R2', 'P2', 'asig', False), ('R2', 'P3', 'asig', True), ('R3', 'P1', 'asig', True),
               ('P1', 'R2', 'pide', True), ('P3', 'R3', 'pide', True)]
    o_extra = None
    procesos['P2'] = (500, 300)
    grafo_recursos('grafo-guia-6.svg', procesos, recursos, aristas,
                   'Guía 6: hay un ciclo P1, R2, P3, R3, pero R2 tiene dos instancias y una la tiene P2, que no pide nada; P2 termina, suelta R2 y el ciclo se rompe',
                   'Guía · problema 6', ('Ciclo sin interbloqueo: P2 lo destraba', 'ok'), H=380,
                   anotar=[(530, 296, 'no pide nada:', 'ok'), (530, 312, 'termina y suelta R2', 'ok')])
    # Recuperativa 2026-1 / Guía 29: sin ciclos
    procesos = {'P1': (90, 110), 'P5': (90, 290), 'P2': (520, 80), 'P3': (520, 160), 'P6': (520, 240), 'P4': (520, 320)}
    recursos = {'R1': (290, 110, 4), 'R2': (290, 220, 3), 'R4': (290, 330, 3)}
    aristas = [('P1', 'R1', 'pide', False), ('P1', 'R2', 'pide', False), ('P5', 'R2', 'pide', False),
               ('R1', 'P2', 'asig', False), ('R1', 'P3', 'asig', False), ('R1', 'P5', 'asig', False), ('R1', 'P6', 'asig', False),
               ('R2', 'P2', 'asig', False), ('R2', 'P3', 'asig', False), ('R2', 'P4', 'asig', False),
               ('R4', 'P4', 'asig', False), ('R4', 'P5', 'asig', False)]
    grafo_recursos('grafo-recup-2026-1.svg', procesos, recursos, aristas,
                   'Recuperativa 2026-1 y guía 29: sin ciclos; P2, P3, P4 y P6 no piden nada, terminan y liberan R1 y R2 para P5 y P1',
                   'Recuperativa 2026-1 · problema 3 (= guía 29)', ('Sin ciclos: estado seguro', 'ok'), W=680, H=410,
                   anotar=[(560, 84, 'no piden nada:', 'ok'), (560, 100, 'terminan primero', 'ok')])


# ------------------------------------------------------------------ grafo de precedencia
def grafo_precedencia(nombre, nodos, aristas, etiqueta, titulo, W=560, H=330):
    o = [txt(24, 30, titulo, 'ink', 14, weight=600)]
    R = 22
    for a, b in aristas:
        (x1, y1), (x2, y2) = nodos[a], nodos[b]
        sx, sy = recorte_circulo(x1, y1, R + 1, x2, y2)
        ex, ey = recorte_circulo(x2, y2, R + 5, x1, y1)
        o.append(f'<path d="M{sx:.1f},{sy:.1f} L{ex:.1f},{ey:.1f}" class="ln" stroke-width="1.5" marker-end="url(#fl)"/>')
    for n, (x, y) in nodos.items():
        entra = sum(1 for a, b in aristas if b == n)
        cls = 'p3' if entra > 1 else 'p0'
        o.append(f'<circle cx="{x}" cy="{y}" r="{R}" class="{cls}" stroke-width="1.4"/>')
        o.append(txt(x, y + 5, n, 'ink', 13.5, 'middle', 600))
    o.append(f'<circle cx="34" cy="{H - 26}" r="8" class="p3" stroke-width="1.4"/>')
    o.append(txt(48, H - 22, 'llegan 2 flechas: necesita join (o un wait por cada flecha)', 'muted', 12))
    guardar(nombre, svg(W, H, ''.join(o), etiqueta))


def diagramas_precedencia():
    print('Sincronización')
    nodos = {'S1': (150, 80), 'S2': (410, 80), 'S3': (80, 175), 'S4': (280, 175), 'S5': (480, 175), 'S6': (180, 265), 'S7': (380, 265)}
    aristas = [('S1', 'S3'), ('S1', 'S4'), ('S2', 'S4'), ('S2', 'S5'), ('S3', 'S6'), ('S4', 'S6'), ('S4', 'S7'), ('S5', 'S7')]
    grafo_precedencia('precedencia-guia-38.svg', nodos, aristas,
                      'Guía 38: S4 espera a S1 y S2, S6 espera a S3 y S4, S7 espera a S4 y S5',
                      'Guía · problema 38', H=330)
    nodos = {'S1': (290, 70), 'S2': (180, 150), 'S3': (460, 150), 'S4': (290, 210), 'S5': (120, 260),
             'S7': (390, 260), 'S8': (480, 300), 'S6': (250, 340), 'S9': (470, 390)}
    aristas = [('S1', 'S2'), ('S1', 'S3'), ('S2', 'S4'), ('S2', 'S5'), ('S4', 'S7'), ('S4', 'S6'), ('S5', 'S6'),
               ('S7', 'S8'), ('S3', 'S8'), ('S6', 'S9'), ('S8', 'S9')]
    grafo_precedencia('precedencia-guia-15.svg', nodos, aristas,
                      'Guía 15: S6 espera a S4 y S5, S8 espera a S7 y S3, S9 espera a S6 y S8 (S9 es el segundo S7 de la figura)',
                      'Guía · problema 15 (el segundo «S7» de la figura se llama S9)', W=580, H=450)


# ------------------------------------------------------------------ base y límite
def diagrama_base_limite():
    print('Memoria')
    W, H = 820, 230
    o = []

    def caja(x, y, w, h, l1, l2=None, cls='soft'):
        s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" class="{cls}" stroke-width="1.4"/>'
        s += txt(x + w / 2, y + (h / 2 + 5 if not l2 else h / 2 - 3), l1, 'ink', 13.5, 'middle', 600)
        if l2:
            s += txt(x + w / 2, y + h / 2 + 15, l2, 'muted', 12, 'middle')
        return s
    o.append(caja(24, 70, 96, 56, 'CPU', 'modo usuario', 'p0'))
    o.append(f'<path d="M120,98 L196,98" class="ln" stroke-width="1.6" marker-end="url(#fl)"/>')
    o.append(txt(158, 88, '0x0B20', 'ink', 12.5, 'middle', 600))
    o.append(txt(158, 116, '= 2848', 'muted', 11.5, 'middle'))
    o.append(f'<path d="M262,62 L320,98 L262,134 L204,98 Z" class="soft" stroke-width="1.4"/>')
    o.append(txt(262, 95, '¿lógica <', 'ink', 12, 'middle', 600))
    o.append(txt(262, 110, 'límite?', 'ink', 12, 'middle', 600))
    o.append(txt(262, 50, 'límite = 0x0C00 (3072)', 'muted', 11.5, 'middle'))
    o.append(f'<path d="M320,98 L418,98" class="okl" stroke-width="1.8" marker-end="url(#flo)"/>')
    o.append(txt(369, 88, 'sí', 'ok', 12.5, 'middle', 600))
    o.append(f'<circle cx="440" cy="98" r="20" class="soft" stroke-width="1.4"/>')
    o.append(txt(440, 104, '+', 'ink', 20, 'middle', 600))
    o.append(f'<path d="M440,30 L440,74" class="ln" stroke-width="1.6" marker-end="url(#fl)"/>')
    o.append(txt(440, 24, 'base = 0x3000', 'muted', 11.5, 'middle'))
    o.append(f'<path d="M460,98 L600,98" class="ln" stroke-width="1.6" marker-end="url(#fl)"/>')
    o.append(txt(530, 88, '0x3B20', 'ink', 12.5, 'middle', 600))
    o.append(txt(530, 116, 'física = base + lógica', 'muted', 11.5, 'middle'))
    o.append(caja(604, 60, 190, 76, 'Memoria física', 'se accede a 0x3B20', 'p1'))
    o.append(f'<path d="M262,134 L262,178" class="acc" stroke-width="1.8" marker-end="url(#fla)"/>')
    o.append(txt(272, 160, 'no', 'acct', 12.5, 'start', 600))
    o.append(caja(150, 182, 224, 36, 'trap al SO: error de dirección', None, 'accf'))
    guardar('base-limite.svg', svg(W, H, ''.join(o),
            'Protección con base y límite: si la dirección lógica es menor que el límite se le suma la base; si no, trap al sistema operativo'))


# ------------------------------------------------------------------ reemplazo de páginas
def tabla_reemplazo(nombre, alg, marcos, cadena, titulo, etiqueta):
    pasos, fallas, reemp, *_ = reemplazar(alg, marcos, cadena)
    cw, ch, L = 30, 30, 88
    W = L + cw * len(cadena) + 24
    H = 56 + ch * (marcos + 2) + 30
    o = [txt(24, 30, titulo, 'ink', 14, weight=600),
         txt(W - 24, 30, f'{fallas} fallas · {reemp} reemplazos', 'acct', 12.5, 'end', 600)]
    y0 = 48
    o.append(txt(L - 12, y0 + ch / 2 + 5, 'Referencia', 'muted', 12, 'end'))
    for m in range(marcos):
        o.append(txt(L - 12, y0 + ch * (m + 1) + ch / 2 + 5, f'Marco {m + 1}', 'muted', 12, 'end'))
    o.append(txt(L - 12, y0 + ch * (marcos + 1) + ch / 2 + 5, 'Falla', 'muted', 12, 'end'))
    previo = [None] * marcos
    for j, (ref, mem, falla, victima) in enumerate(pasos):
        x = L + j * cw
        o.append(f'<rect x="{x}" y="{y0}" width="{cw}" height="{ch}" class="soft"/>')
        o.append(txt(x + cw / 2, y0 + ch / 2 + 5, ref, 'ink', 13, 'middle', 600))
        for m in range(marcos):
            y = y0 + ch * (m + 1)
            nuevo = falla and mem[m] != previo[m]
            cls = 'accf' if nuevo else ('card' if mem[m] is not None else 'card')
            o.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" class="{cls}" stroke-width="{1.4 if nuevo else 1}"/>')
            if mem[m] is not None:
                o.append(txt(x + cw / 2, y + ch / 2 + 5, mem[m], 'ink' if not nuevo else 'acct', 13, 'middle', 600 if nuevo else 400))
        yf = y0 + ch * (marcos + 1)
        if falla:
            o.append(f'<circle cx="{x + cw / 2}" cy="{yf + ch / 2}" r="5" class="acct"/>')
        previo = list(mem)
    yl = H - 16
    o.append(f'<rect x="24" y="{yl - 11}" width="14" height="14" class="accf" stroke-width="1.4"/>')
    o.append(txt(44, yl, 'página que entra en esa referencia (falla)', 'muted', 12))
    guardar(nombre, svg(W, H, ''.join(o), etiqueta))


def diagramas_reemplazo():
    print('Memoria virtual')
    C = lambda s: [int(x) for x in s.split(',')]
    tabla_reemplazo('lru-2025-2.svg', 'lru', 3, C('7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1'),
                    'P2 2025-2 · LRU con 3 marcos', 'LRU con 3 marcos para la cadena de la P2 2025-2: 12 fallas y 9 reemplazos')
    tabla_reemplazo('optimo-2024-2.svg', 'optimo', 3, C('1,1,1,2,0,1,2,0,2,4,5,0,6,5,4,1,3,5,2,4,6'),
                    'P2 2024-2 · Óptimo con 3 marcos', 'Óptimo con 3 marcos para la cadena de la P2 2024-2: 10 fallas y 7 reemplazos')
    tabla_reemplazo('lru-2025-1.svg', 'lru', 3, C('1,3,2,0,1,2,0,2,4,5,0,6,5,4,1,3,5,2,4,6'),
                    'Examen 2025-1 · LRU con 3 marcos', 'LRU con 3 marcos para la cadena del examen 2025-1: 16 fallas y 13 reemplazos')
    tabla_reemplazo('lru-recup-2026-1.svg', 'lru', 3, C('1,2,2,7,1,2,1,2,4,5,0,6,5,4,1,3,5,2,4,6'),
                    'Recuperativa 2026-1 · LRU con 3 marcos', 'LRU con 3 marcos para la cadena de la recuperativa 2026-1: 14 fallas y 11 reemplazos')


# ------------------------------------------------------------------ disco
def diagrama_disco():
    print('Disco')
    inicio, sol, maxc = 125, [100, 110, 200, 30, 405, 450, 335, 140, 135, 192], 499
    algs = [('fcfs', 'FCFS'), ('sstf', 'SSTF'), ('scan', 'SCAN'), ('look', 'LOOK'), ('cscan', 'C-SCAN'), ('clook', 'C-LOOK')]
    pw, ph, gap, L, T = 250, 200, 18, 24, 20
    W = L * 2 + pw * 3 + gap * 2
    H = T + (ph + gap) * 2 + 20
    o = []
    for k, (a, nombre) in enumerate(algs):
        ruta = recorrido(a, inicio, sol, maxc)
        tot = total_disco(ruta, True, a)
        px = L + (k % 3) * (pw + gap)
        py = T + (k // 3) * (ph + gap)
        o.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="8" class="soft" stroke-width="1"/>')
        o.append(txt(px + 12, py + 22, nombre, 'ink', 14, weight=600))
        o.append(txt(px + pw - 12, py + 22, f'{tot} cilindros', 'acct', 12.5, 'end', 600))
        ax0, ax1 = px + 14, px + pw - 14
        ay = py + 40
        X = lambda c: ax0 + c / maxc * (ax1 - ax0)
        o.append(f'<line x1="{ax0}" y1="{ay}" x2="{ax1}" y2="{ay}" class="grid"/>')
        for c in (0, 125, 250, 375, 499):
            o.append(f'<line x1="{X(c):.1f}" y1="{ay - 3}" x2="{X(c):.1f}" y2="{ay + 3}" class="grid"/>')
            o.append(txt(X(c), ay - 6, c, 'muted', 10, 'middle'))
        paso = (ph - 58) / (len(ruta) - 1)
        pts = [(X(c), ay + 10 + i * paso) for i, c in enumerate(ruta)]
        for i in range(len(pts) - 1):
            (x1, y1), (x2, y2) = pts[i], pts[i + 1]
            salto = a in ('cscan', 'clook') and ruta[i + 1] < ruta[i] and i > 0
            o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="{"grid" if salto else "s0"}" stroke-width="{1.4 if salto else 1.8}"{" stroke-dasharray=\"4 3\"" if salto else ""}/>')
        for i, (x, y) in enumerate(pts):
            es_sol = ruta[i] in sol and i > 0
            o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{3.2 if es_sol else 2.4}" class="{"f0" if es_sol else "dot"}"/>')
    o.append(txt(L, H - 8, 'Cabezal en 125, subiendo · cilindros 0 a 499 · tiempo hacia abajo · línea punteada = salto de regreso (se cuenta)', 'muted', 12))
    guardar('disco-guia-20.svg', svg(W, H, ''.join(o),
            'Guía 20: recorrido del cabezal con los seis algoritmos; SSTF recorre 545 cilindros y FCFS 1087'))


# ------------------------------------------------------------------ cómo decidir (flujo)
def diagrama_decision():
    W, H = 800, 560
    o = []
    cx, bw = 250, 330

    def paso(y, num, l1, l2):
        s = f'<rect x="{cx - bw / 2}" y="{y}" width="{bw}" height="54" rx="8" class="soft" stroke-width="1.4"/>'
        s += f'<circle cx="{cx - bw / 2 + 22}" cy="{y + 27}" r="12" class="p0" stroke-width="1.2"/>'
        s += txt(cx - bw / 2 + 22, y + 31.5, num, 'ink', 12.5, 'middle', 700)
        s += txt(cx - bw / 2 + 44, y + 23, l1, 'ink', 13.5, 'start', 600)
        s += txt(cx - bw / 2 + 44, y + 41, l2, 'muted', 12, 'start')
        return s

    def pregunta(y, l1, l2=None):
        s = f'<path d="M{cx},{y} L{cx + 150},{y + 32} L{cx},{y + 64} L{cx - 150},{y + 32} Z" class="soft" stroke-width="1.4"/>'
        s += txt(cx, y + (30 if l2 else 37), l1, 'ink', 13, 'middle', 600)
        if l2:
            s += txt(cx, y + 46, l2, 'ink', 13, 'middle', 600)
        return s

    def resultado(y, cls, l1, l2, l3=None):
        x, w = 560, 220
        s = f'<rect x="{x}" y="{y}" width="{w}" height="{66 if l3 else 54}" rx="8" class="{cls}" stroke-width="1.6"/>'
        s += txt(x + 14, y + 22, l1, 'ink', 13.5, 'start', 700)
        s += txt(x + 14, y + 40, l2, 'muted', 12, 'start')
        if l3:
            s += txt(x + 14, y + 56, l3, 'muted', 12, 'start')
        return s

    def baja(y1, y2, etiqueta=None):
        s = f'<path d="M{cx},{y1} L{cx},{y2}" class="ln" stroke-width="1.6" marker-end="url(#fl)"/>'
        if etiqueta:
            s += txt(cx + 10, (y1 + y2) / 2 + 4, etiqueta, 'muted', 12, 'start', 600)
        return s

    def lado(y, x1, etiqueta, cls='ln', mk='fl'):
        return (f'<path d="M{x1},{y} L556,{y}" class="{cls}" stroke-width="1.6" marker-end="url(#{mk})"/>'
                + txt((x1 + 556) / 2, y - 8, etiqueta, 'muted', 12, 'middle', 600))

    o.append(paso(20, '1', 'Leer y validar el grafo', 'tabla: qué tiene y qué pide cada proceso'))
    o.append(baja(74, 92))
    o.append(paso(94, '2', 'Contar instancias libres', 'libres = instancias − asignadas'))
    o.append(baja(148, 166))
    o.append(pregunta(168, '¿Hay ciclos?'))
    o.append(lado(200, cx + 150, 'no', 'okl', 'flo'))
    o.append(resultado(173, 'okf', 'Estado seguro', 'no hay espera circular;', 'da una secuencia de término'))
    o.append(baja(232, 252, 'sí'))
    o.append(pregunta(254, '¿Algún ciclo con solo', 'recursos de 1 instancia?'))
    o.append(lado(286, cx + 150, 'sí', 'acc', 'fla'))
    o.append(resultado(259, 'accf', 'Interbloqueo seguro', 'inseguro irreversible: ese', 'ciclo no se puede romper'))
    o.append(baja(318, 338, 'no'))
    o.append(paso(340, '3', 'Reducir el grafo', 'termina quien puede; devuelve todo'))
    o.append(baja(394, 412))
    o.append(pregunta(414, '¿Terminan todos?'))
    o.append(lado(446, cx + 150, 'sí', 'okl', 'flo'))
    o.append(resultado(419, 'okf', 'Ciclo sin interbloqueo', 'inseguro reversible;', 'la reducción da el orden'))
    o.append(baja(478, 498, 'no'))
    o.append(f'<rect x="{cx - bw / 2}" y="500" width="{bw}" height="44" rx="8" class="accf" stroke-width="1.6"/>')
    o.append(txt(cx, 518, 'Interbloqueo (inseguro irreversible)', 'ink', 13.5, 'middle', 700))
    o.append(txt(cx, 535, 'separar: en el ciclo vs. bloqueados por arrastre', 'muted', 12, 'middle'))
    o.append(txt(560, 520, 'En todos los casos: revisar', 'muted', 12, 'start', 600))
    o.append(txt(560, 537, 'las 4 condiciones de Coffman', 'muted', 12, 'start', 600))
    guardar('decidir-interbloqueo.svg', svg(W, H, ''.join(o),
            'Cómo decidir con un grafo de recursos: sin ciclos es seguro; un ciclo con recursos de una instancia es interbloqueo; si no, se reduce el grafo y se ve si todos terminan'))


def diagrama_guia7():
    procesos = {'P1': (110, 200), 'P3': (510, 200), 'P2': (510, 70), 'P4': (570, 330)}
    recursos = {'R1': (310, 80, 3), 'R2': (310, 310, 1), 'R3': (310, 200, 1)}
    aristas = [('P1', 'R1', 'pide', False), ('P1', 'R2', 'pide', True), ('R3', 'P1', 'asig', True),
               ('R1', 'P2', 'asig', False), ('R1', 'P3', 'asig', False), ('R1', 'P4', 'asig', False),
               ('R2', 'P3', 'asig', True), ('P4', 'R2', 'pide', False), ('P3', 'R3', 'pide', True)]
    grafo_recursos('grafo-guia-7.svg', procesos, recursos, aristas,
                   'Guía 7: P2 no pide nada y termina; queda el ciclo P1, R2, P3, R3 con recursos de una instancia, así que P1 y P3 están interbloqueados y P4, que espera R2, queda bloqueado por arrastre',
                   'Guía · problema 7', ('Interbloqueo: P1 y P3 · P4 por arrastre', 'acct'), W=700, H=440,
                   anotar=[(540, 66, 'no pide nada:', 'ok'), (540, 82, 'termina y suelta 1 de R1', 'ok'),
                           (440, 360, 'espera R2 (lo tiene P3):', 'acct'), (440, 376, 'bloqueado por arrastre', 'acct')])


# ------------------------------------------------------------------ prueba 1: ensayo
def diagramas_prueba1():
    print('Prueba 1 (ensayo)')
    ps = [P('A', '0,4', 5, 3), P('B', '1,1', 3, 1), P('C', '2', 7, 4), P('D', '3,5', 2, 0), P('E', '4,2', 4, 2)]
    gantt('ensayo-p1-gantt.svg', [
        {'titulo': 'FCFS · T.T. prom. 11,36', 'segs': plan(ps, 'fcfs')},
        {'titulo': 'SJF apropiativo · T.T. prom. 8,98 (el mejor)', 'segs': plan(ps, 'srtf')},
        {'titulo': 'Prioridad apropiativa · T.T. prom. 9,26', 'segs': plan(ps, 'prio_p')},
        {'titulo': 'Round Robin q = 2 por iteraciones · T.T. prom. 13,56', 'segs': plan(ps, 'rr_vueltas', 2)},
    ], ['A', 'B', 'C', 'D', 'E'], 'Ensayo prueba 1, problema 1: los cuatro algoritmos; SJF apropiativo tiene el menor turnaround promedio', ancho=860)
    gantt('ensayo-p2-linea.svg', [
        {'titulo': 'Proceso P con prioridad máxima: llega en 2 y termina en 17', 'segs': [('CPU', F(2), F(5)), ('E/S', F(5), F(9)), ('CPU', F(9), F(11)), ('E/S', F(11), F(12)), ('CPU', F(12), F(17))]},
    ], ['CPU', 'E/S'], 'Ensayo prueba 1, problema 2: CPU de 2 a 5, E/S de 5 a 9, CPU de 9 a 11, E/S de 11 a 12, CPU de 12 a 17; tiempo de retorno 15')


if __name__ == '__main__':
    diagramas_planificacion()
    diagrama_estados()
    diagrama_memoria_proceso()
    diagramas_grafos()
    diagrama_decision()
    diagrama_guia7()
    diagramas_precedencia()
    diagrama_base_limite()
    diagramas_reemplazo()
    diagrama_disco()
    diagramas_prueba1()
