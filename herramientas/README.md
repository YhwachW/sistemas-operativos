# Herramientas para comprobar ejercicios

Programas en **Python 3** (sin librerías extra). Sirven para **comprobar** tus resultados después de resolver a mano, no para reemplazar el desarrollo: en la prueba el puntaje está en el procedimiento.

Abre una terminal en esta carpeta (`herramientas/`) y ejecuta los comandos.

## planificacion.py: planificación de CPU

Algoritmos: `fcfs`, `sjf` (no apropiativo), `srtf` (= "SJF Preemptive"), `prio`, `prio_p` (prioridad apropiativa), `rr` (cola del libro) y `rr_vueltas` (por iteraciones, **como el profesor**).

Crea un archivo de texto con una línea por proceso: `nombre llegada ráfaga [prioridad]`. Por ejemplo, `datos.txt`:

```
P1  1,2  3  8
P2  3,2  2  5
P3  5,5  1  4
```

```bash
python planificacion.py datos.txt srtf
python planificacion.py datos.txt rr_vueltas 3
python planificacion.py datos.txt prio_p
```

Muestra el Gantt y una tabla con **T.T.**, **W.T.** (definición del libro: T.T. − ráfaga) y **W.T. pauta** (inicio del último tramo − llegada, como en las pautas; [explicación](../estudio/00-convenciones-del-profesor.md#14-tiempo-de-espera-wt-la-pauta-usa-inicio-del-último-tramo--llegada)).

Sin argumentos, resuelve el Problema 2 del Parcial 2024-2.

## banquero.py: algoritmo del banquero

Edita los datos al final del archivo, o úsalo desde Python:

```python
from banquero import resolver, solicitud, vec
nombres = ['P0', 'P1', 'P2']
asig    = [vec('0 1 0'), vec('2 0 0'), vec('3 0 2')]
maximo  = [vec('7 5 3'), vec('3 2 2'), vec('9 0 2')]
disp = resolver('Mi ejercicio', nombres, asig, maximo, disponible=vec('3 3 2'))   # o total=vec('10 5 7')
solicitud(nombres, asig, maximo, disp, 'P1', vec('1 0 2'))
```

Muestra la necesidad, la secuencia paso a paso (como en clases) y **todas** las secuencias seguras.

## grafo.py: grafo de asignación de recursos

```python
from grafo import analizar
analizar('(P1,R1); (R1,P2); (P2,R2); (R2,P1)', {'R1': 1, 'R2': 1}, 'Mi grafo')
```

`(Pi,Rj)` = Pi **pide** Rj · `(Rj,Pi)` = Rj **asignado** a Pi. Muestra los ciclos, la reducción del grafo y el estado (seguro, inseguro reversible o irreversible).

## memoria.py: el problema "procesos A, B, C"

```python
from memoria import resolver, MB, GB, KB
from fractions import Fraction as F
resolver('Mi ejercicio', 64*MB, 4096,
         {'A': F(3601333, 8),      # bits -> bytes: dividir por 8
          'B': 18000*128,          # palabras x bytes por palabra
          'C': 256000},
         acceso=8, transferencia=12, ejec_pag=60)
```

## reemplazo.py: FIFO, Óptimo y LRU

```bash
python reemplazo.py lru 3 "7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1" 20 30
python reemplazo.py optimo 3 "1,2,3,4,1,2,5,1,2,3,4,5"
python reemplazo.py fifo 4 "1,2,3,4,1,2,5,1,2,3,4,5"
```

Los dos últimos números (opcionales) son el tiempo de acceso y el de transferencia. Muestra la tabla de marcos, las fallas, la tabla de entradas y salidas y el tiempo `(fallas + reemplazos) × (acceso + transferencia)`.

## disco.py: planificación del brazo

```python
from disco import mostrar_todos
mostrar_todos('Mi ejercicio', 53, [98, 183, 37, 122, 14, 124, 65, 67], 199)
```

Muestra la ruta y el total de cilindros de FCFS, SSTF, SCAN, LOOK, C-SCAN y C-LOOK. Los saltos de C-SCAN y C-LOOK se cuentan.
