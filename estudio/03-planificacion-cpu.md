# 03 · Planificación de CPU (scheduling)

> **Aparece en casi todas las pruebas** (P1 2009, 2013, 2022, 2024, 2025; exámenes y recuperativas 2025-2026), normalmente por 30 a 40 puntos.
> Apuntes: *Cap 5 2020.pdf*. Antes de practicar, lee las [convenciones del profesor](00-convenciones-del-profesor.md#1-planificación-de-cpu).

## 1. La idea

Un proceso alterna entre **ráfagas de CPU** (calcula) y **ráfagas de E/S** (espera un disco, la red, el teclado). Mientras un proceso espera E/S, la CPU quedaría ociosa: la **multiprogramación** aprovecha ese tiempo dándole la CPU a otro proceso.

El **planificador de corto plazo** (CPU scheduler) decide *a cuál* de los procesos de la cola de listos (*ready queue*) le toca la CPU. El **despachador** (*dispatcher*) hace el cambio de contexto y le entrega la CPU. El tiempo que tarda en hacerlo es la **latencia de despacho**.

### Apropiativo vs. no apropiativo

| | No apropiativo (*non-preemptive*) | Apropiativo (*preemptive*) |
|---|---|---|
| ¿Cuándo se decide? | Solo cuando el proceso que corre **termina** o se **bloquea** (pide E/S) | Además, cuando **llega** un proceso nuevo o vence un quantum |
| ¿Se puede quitar la CPU? | No | Sí, el SO puede expulsar al proceso que corre |
| Ejemplos | FCFS, SJF, Prioridad NA | SRTF (SJF apropiativo), Prioridad apropiativa, Round Robin |

## 2. Lo que se mide

| Término | En las pautas | Fórmula | Qué significa |
|---|---|---|---|
| **Turnaround time** | T.T., tiempo de permanencia, tiempo de retorno | `fin − llegada` | Cuánto estuvo el proceso en el sistema, de punta a punta |
| **Waiting time** | W.T., tiempo de espera | `T.T. − ráfaga` | Cuánto estuvo en la cola de listos sin correr (ver [nota del profesor](00-convenciones-del-profesor.md#14-tiempo-de-espera-wt-la-pauta-usa-inicio-del-último-tramo--llegada)) |
| Tiempo de respuesta | — | `primer inicio − llegada` | Cuánto tardó en empezar a correr por primera vez |
| Utilización de CPU | — | `tiempo ocupada / tiempo total` | % del tiempo que la CPU trabaja |
| Throughput | — | `procesos terminados / tiempo` | Productividad |

Un buen algoritmo **maximiza** utilización y throughput y **minimiza** turnaround, espera y respuesta.

## 3. Receta para resolver cualquier ejercicio

1. **Ordena** los procesos por tiempo de llegada (escribe la tabla de nuevo si viene desordenada).
2. Ubícate en el primer instante de llegada (la CPU no empieza en 0 si nadie llegó en 0).
3. En cada **instante de decisión** mira **quiénes ya llegaron** y aplica la regla del algoritmo:
   - No apropiativos: los instantes de decisión son cuando termina el que corre.
   - Apropiativos: también cada vez que **llega** alguien (y en RR, cada vez que vence el quantum).
4. Dibuja el **diagrama de Gantt** con los tiempos debajo de cada corte.
5. Si un proceso se interrumpe, anota su **ráfaga restante** (en las pautas aparece como "RR": *ráfaga restante*, por ejemplo `2,0 → 1,0 RR`).
6. Al final: `T.T. = fin − llegada` y `W.T. = T.T. − ráfaga`. Saca los promedios.
7. **Comprueba**: la suma de ráfagas tiene que ser igual al tiempo que la CPU estuvo ocupada en el Gantt.

> Comprueba tus resultados con `python herramientas/planificacion.py` (ver [herramientas](../herramientas/README.md)).

## 4. Los algoritmos

### 4.1 FCFS — *First Come, First Served*

- **Regla:** se atiende en orden de llegada y cada uno corre hasta terminar.
- **Ventaja:** simple y justo en orden.
- **Problema:** *efecto convoy*: un proceso largo adelante hace esperar a todos los cortos.

### 4.2 SJF — *Shortest Job First* (no apropiativo)

- **Regla:** cuando la CPU se libera, entre los que **ya llegaron** se elige la ráfaga más corta y se deja terminar.
- **Ventaja:** es el que minimiza el tiempo de espera promedio (si todos llegan juntos).
- **Problema:** hay que conocer (o estimar) la próxima ráfaga; los procesos largos pueden sufrir **inanición**.
- **Estimación de la próxima ráfaga** (promedio exponencial): $\tau_{n+1} = \alpha\, t_n + (1-\alpha)\,\tau_n$, con $0 \le \alpha \le 1$.

### 4.3 SRTF — SJF apropiativo ("SJF Preemptive")

- **Regla:** cada vez que llega un proceso se compara **su ráfaga** con la **ráfaga restante** del que corre. Si el nuevo es menor, lo expulsa.
- En empate, se queda el que estaba corriendo.

### 4.4 Prioridad (apropiativa o no)

- **Regla:** se elige el de **mayor prioridad = número menor**. En la versión apropiativa, si llega uno con número menor, expulsa al que corre.
- **Problema: inanición (*starvation*)**: un proceso de baja prioridad puede esperar para siempre si siguen llegando procesos más prioritarios.
- **Solución: envejecimiento (*aging*)**: subir gradualmente la prioridad de los que llevan mucho esperando (por ejemplo, +1 cada 15 minutos). *(Pregunta 2, P1 2013)*

### 4.5 Round Robin (RR)

- **Regla:** cada proceso corre como máximo un **quantum** `q`; si no termina, vuelve al final y le toca al siguiente.
- **En este curso:** se resuelve **por iteraciones en orden de llegada** (ver [convenciones](00-convenciones-del-profesor.md#13-round-robin-por-iteraciones-vueltas)).
- **Elegir q** *(Problema 6, P1 2025-2)*:
  - Si q es muy chico, hay demasiados cambios de contexto. Por ejemplo, si el cambio tarda 1 ms y q = 4 ms, se pierde 1 de cada 5 ms, un 20 % de la CPU, en trabajo del SO.
  - Si q es muy grande, RR se vuelve FCFS.
  - Regla empírica: q tal que **~80 % de las ráfagas sean más cortas que q**, y siempre mucho mayor que el tiempo de cambio de contexto.
  - Con *n* procesos en la cola, cada uno espera como máximo $(n-1)\cdot q$ para volver a correr. Con 20 procesos y una respuesta deseada de, por ejemplo, 1 s, q ≤ 1 s / 19 ≈ 50 ms.

### 4.6 Colas multinivel (teoría)

- **Multinivel:** varias colas (por ejemplo, interactivos con RR y lotes con FCFS), cada una con su algoritmo y con prioridad entre colas.
- **Multinivel con retroalimentación:** un proceso puede **bajar** de cola si consume todo su quantum (es "CPU-bound") o **subir** si espera mucho (aging).

---

## 5. Ejercicios de prueba resueltos

### 5.1 Parcial N°1 2024-2 — Problema 2 (40 pts): SJF apropiativo y RR (q = 2)

| Proceso | Llegada | Ráfaga |
|---|---|---|
| 1 | 1,6 | 1 |
| 2 | 1,3 | 2 |
| 3 | 0,5 | 6 |
| 4 | 1,5 | 2 |
| 5 | 5,6 | 2 |

**SJF apropiativo, paso a paso:**

| Instante | Qué pasa | Decisión |
|---|---|---|
| 0,5 | Llega J3 (6). Es el único | Corre J3 |
| 1,3 | Llega J2 (2). J3 lleva 0,8 → le quedan **5,2** | 2 < 5,2 → **J2 expulsa a J3** |
| 1,5 | Llega J4 (2). J2 lleva 0,2 → le quedan **1,8** | 2 > 1,8 → sigue J2 |
| 1,6 | Llega J1 (1). A J2 le quedan **1,7** | 1 < 1,7 → **J1 expulsa a J2** |
| 2,6 | Termina J1. Esperan: J2 (1,7), J4 (2), J3 (5,2) | Corre J2 |
| 4,3 | Termina J2. Esperan: J4 (2), J3 (5,2) | Corre J4 |
| 5,6 | Llega J5 (2). A J4 le quedan 0,7 | Sigue J4 |
| 6,3 | Termina J4. Esperan J5 (2), J3 (5,2) | Corre J5 |
| 8,3 | Termina J5 | Corre J3 hasta 13,5 |

```
| J3 | J2 | J1 |  J2  |  J4  |  J5  |      J3      |
0,5  1,3  1,6  2,6    4,3    6,3    8,3           13,5
```

**Round Robin q = 2 por iteraciones** (orden de llegada: J3, J2, J4, J1, J5):

```
|  J3  |  J2  |  J4  |J1|  J5  |  J3  |  J3  |
0,5    2,5    4,5    6,5 7,5   9,5    11,5   13,5
```

| Proceso | SJF-P T.T. | SJF-P W.T. (libro) | W.T. (pauta) | RR T.T. | RR W.T. (libro) | W.T. (pauta) |
|---|---|---|---|---|---|---|
| 1 | 1,0 | 0,0 | 0,0 | 5,9 | 4,9 | 4,9 |
| 2 | 3,0 | 1,0 | 1,3 | 3,2 | 1,2 | 1,2 |
| 3 | 13,0 | 7,0 | 7,8 | 13,0 | 7,0 | 11,0 |
| 4 | 4,8 | 2,8 | 2,8 | 5,0 | 3,0 | 3,0 |
| 5 | 2,7 | 0,7 | 0,7 | 3,9 | 1,9 | 1,9 |
| **Promedio** | **4,9** | **2,3** | **2,52** | **6,2** | **3,6** | **4,4** |

> Los T.T. coinciden exactamente con la pauta. Las diferencias en W.T. son por la [fórmula de la pauta](00-convenciones-del-profesor.md#14-tiempo-de-espera-wt-la-pauta-usa-inicio-del-último-tramo--llegada) (por ejemplo, J3 en RR: último inicio 11,5 − llegada 0,5 = 11,0; con la definición, 13,0 − 6 = 7,0).

### 5.2 Recuperativa 2024-2 / Examen 2025-1 — FCFS y SJF apropiativo (30 pts)

| Proceso | Llegada | Ráfaga | Prioridad |
|---|---|---|---|
| Azul (P1) | 0,1 | 4 | 3 |
| Monse (P2) | 0,8 | 2 | 0 |
| Prg1 (P3) | 0,5 | 3 | 2 |

```
FCFS:            |    Azul    |   Prg1   |  Monse |
                 0,1          4,1        7,1      9,1

SJF apropiativo: |Azul|Prg1|  Monse |  Prg1  |   Azul    |
                 0,1  0,5  0,8      2,8      5,5         9,1
```

- En 0,5 llega Prg1 (3) y a Azul le quedan 3,6 → **Prg1 expulsa a Azul**.
- En 0,8 llega Monse (2) y a Prg1 le quedan 2,7 → **Monse expulsa a Prg1**.

| | FCFS T.T. | FCFS W.T. | SJF-P T.T. | SJF-P W.T. (libro) | W.T. (pauta) |
|---|---|---|---|---|---|
| Azul | 4,0 | 0,0 | 9,0 | 5,0 | 5,4 |
| Monse | 8,3 | 6,3 | 2,0 | 0,0 | 0,0 |
| Prg1 | 6,6 | 3,6 | 5,0 | 2,0 | 2,3 |
| **Promedio** | **6,3** | **3,3** | **5,33** | **2,33** | **2,56** |

### 5.3 P1 2009-2 = Recuperativa 2026-1 — Prioridad apropiativa, SJF apropiativo, RR (q = 3)

| Proceso | Llegada | Ráfaga | Prioridad |
|---|---|---|---|
| P1 | 1,2 | 3 | 8 |
| P2 | 3,2 | 2 | 5 |
| P3 | 5,5 | 1 | 4 |
| P4 | 8,6 | 3 | 1 |
| P5 | 10,9 | 2 | 0 |

```
Prioridad apropiativa:
| P1 |  P2  |P1| P3 |P1| ocioso |  P4  |  P5  |P4|
1,2  3,2    5,2 5,5  6,5 7,2      8,6    10,9   12,9 13,6

SJF apropiativo  (= RR q=3 en este caso, porque ninguna ráfaga pasa de 3):
|  P1  |  P2  | P3 | ocioso |  P4  |  P5  |
1,2    4,2    6,2  7,2      8,6    11,6   13,6
```

> Fíjate en el **tiempo ocioso** de 7,2 a 8,6: nadie ha llegado, así que la CPU espera.

| | Prio T.T. | Prio W.T. (libro / pauta) | SJF-P y RR T.T. | W.T. |
|---|---|---|---|---|
| P1 | 6,0 | 3,0 / 5,3 | 3,0 | 0,0 |
| P2 | 2,0 | 0,0 | 3,0 | 1,0 |
| P3 | 1,0 | 0,0 | 1,7 | 0,7 |
| P4 | 5,0 | 2,0 / 4,3 | 3,0 | 0,0 |
| P5 | 2,0 | 0,0 | 2,7 | 0,7 |
| **Promedio** | **3,2** | **1,0 / 1,92** | **2,68** | **0,48** |

### 5.4 Examen 2026-1 — Problema 3 (20 pts): SJF apropiativo y RR (q = 2)

| Proceso | Llegada | Ráfaga |
|---|---|---|
| 1 | 2,5 | 3 |
| 2 | 1,3 | 2 |
| 3 | 1,4 | 1 |

```
SJF apropiativo: |2|  3 |    2    |     1      |      RR q=2: |    2    |  3 |   1    | 1 |
                 1,3 1,4 2,4       4,3          7,3            1,3       3,3  4,3      6,3 7,3
```

En 1,4 llega J3 (1) y a J2 le quedan 1,9 → J3 expulsa a J2.

| | SJF-P T.T. | W.T. (libro / pauta) | RR T.T. | W.T. (libro / pauta) |
|---|---|---|---|---|
| 1 | 4,8 | 1,8 | 4,8 | 1,8 / 3,8 |
| 2 | 3,0 | 1,0 / 1,1 | 2,0 | 0,0 |
| 3 | 1,0 | 0,0 | 2,9 | 1,9 |
| **Promedio** | **2,93** | **0,93 / 0,97** | **3,23** | **1,23 / 1,9** |

### 5.5 P1 2025-2 — Pregunta 1 (40 pts): los cuatro algoritmos y "el mejor"

| Proceso | Llegada | Ráfaga | Prioridad |
|---|---|---|---|
| P1 | 1,2 | 12 | 5 |
| P2 | 3,2 | 9 | 4 |
| P3 | 5,5 | 8 | 2 |
| P4 | 8,6 | 11 | 0 |
| P5 | 10,9 | 14 | 4 |

```
FCFS:   | P1 1,2–13,2 | P2 –22,2 | P3 –30,2 | P4 –41,2 | P5 –55,2 |

SJF-P:  | P1 1,2–3,2 | P2 –12,2 | P3 –20,2 | P1 –30,2 | P4 –41,2 | P5 –55,2 |
        (en 3,2 llega P2 con 9 y a P1 le quedan 10 → P2 expulsa a P1)

Prio-P: | P1 –3,2 | P2 –5,5 | P3 –8,6 | P4 –19,6 | P3 –24,5 | P2 –31,2 | P5 –45,2 | P1 –55,2 |

RR q=3 (iteraciones): P1 P2 P3 P4 P5 | P1 P2 P3 P4 P5 | P1 P2 P3 P4 P5 | P1 P4 P5 | P5
        1,2 4,2 7,2 10,2 13,2 16,2 19,2 22,2 25,2 28,2 31,2 34,2 37,2 39,2 42,2 45,2 48,2 50,2 53,2 55,2
```

| Algoritmo | T.T. promedio | W.T. promedio (libro) | W.T. promedio (pauta) |
|---|---|---|---|
| FCFS | 26,52 | 15,72 | 15,72 |
| **SJF apropiativo** | **25,92** | **15,12** | **15,52** |
| Prioridad apropiativa | 29,26 (la pauta dice 29,38: [error](00-convenciones-del-profesor.md#4-errores-conocidos-en-las-pautas)) | 18,46 | 19,94 |
| Round Robin q = 3 | 40,12 | 29,32 | 37,72 |

**El mejor rendimiento es SJF apropiativo** (menor T.T. y W.T. promedio). Era de esperar: SJF es el óptimo en tiempo de espera promedio.

### 5.6 P1 2022-2 — Problema 1 (sin pauta): FCFS, SJF no apropiativo, RR (q = 2)

| Job | Ráfaga | Llegada |
|---|---|---|
| T1 | 10 | 0,8 |
| T2 | 5 | 2,3 |
| T3 | 2 | 5,2 |

```
FCFS:    |       T1        |   T2   | T3 |          SJF NA:  |       T1        | T3 |   T2   |
         0,8               10,8     15,8 17,8                 0,8               10,8 12,8     17,8

RR q=2:  | T1 | T2 | T1 | T2 | T3 | T1 |T2| T1 | T1 |
         0,8  2,8  4,8  6,8  8,8  10,8 12,8 13,8 15,8 17,8
```

> En SJF **no apropiativo** T1 no se interrumpe aunque lleguen trabajos más cortos: cuando termina en 10,8, elige T3 (2) antes que T2 (5).
>
> En RR, cuando le toca a T3 en la primera vuelta (4,8) todavía no ha llegado (llega en 5,2), así que se atiende en la segunda vuelta.

| | FCFS T.T. / W.T. | SJF NA T.T. / W.T. | RR T.T. / W.T. |
|---|---|---|---|
| T1 | 10,0 / 0,0 | 10,0 / 0,0 | 17,0 / 7,0 |
| T2 | 13,5 / 8,5 | 15,5 / 10,5 | 11,5 / 6,5 |
| T3 | 12,6 / 10,6 | 7,6 / 5,6 | 5,6 / 3,6 |
| **Promedio** | **12,03 / 6,37** | **11,03 / 5,37** | **11,37 / 5,7** |

### 5.7 P1 2025-2 — Pregunta 2: tiempo de retorno con E/S

> Prioridades expulsivo. Llega un proceso en el instante 4 con prioridad máxima: CPU 4 ut, E/S 5 ut, CPU 7 ut. ¿Tiempo de retorno?

Como tiene prioridad máxima, nadie lo interrumpe: CPU de 4 a 8, E/S de 8 a 13, CPU de 13 a 20.
**Tiempo de retorno = 20 − 4 = 16 ut.** (Durante la E/S no ocupa CPU, pero sigue "dentro del sistema", así que cuenta.)

### 5.8 P1 2013 — Pregunta 1: procesos con ráfagas de CPU y E/S

En la pauta 2013, para FCFS/RR/SJF, el profesor **sumó todas las ráfagas de CPU y de E/S** como si fueran una sola ráfaga de CPU (por ejemplo, A: 1,5 + 2,8 + 2,0 + 2,5 + 0,9 + 0,7 + 2,0 = 12,4). Es una simplificación: en la realidad, durante la E/S la CPU puede atender a otro proceso. Si te sale un ejercicio así, **pregunta si quiere que sumes las ráfagas** (como la pauta) o que la CPU atienda a otro durante la E/S.

### 5.9 Guía de ejercicios (resultados para comprobar)

| Problema | Algoritmo | T.T. prom. | W.T. prom. (libro) |
|---|---|---|---|
| 3 (6 procesos) | FCFS / SJF NA / SJF-P / Prio NA / Prio-P / RR q=1 (iter.) | 7,77 / 6,77 / 6,77 / 7,77 / 8,27 / 9,27 | 4,1 / 3,1 / 3,1 / 4,1 / 4,6 / 5,6 |
| 4 | FCFS / SJF-P / RR q=3 | 5,1 / 5,03 / 5,1 | 2,1 / 2,03 / 2,1 |
| 8 | FCFS / SJF NA / SJF-P / Prio NA / Prio-P / RR q=3 | 5,3 / 4,3 / 4,03 / 4,3 / 4,67 / 5,3 | 2,63 / 1,63 / 1,37 / 1,63 / 2,0 / 2,63 |
| 10 | SJF-P / RR q=3 | 5,0 / 7,88 | 2,5 / 5,38 |

Para ver el Gantt de cada uno: `python herramientas/planificacion.py datos.txt srtf` (ver [herramientas](../herramientas/README.md)).

---

## 6. Errores típicos

- Empezar el Gantt en 0 cuando el primer proceso llega en 0,5.
- Olvidar el **tiempo ocioso** cuando nadie ha llegado.
- En SJF apropiativo, comparar con la ráfaga **original** del que corre en vez de la **restante**.
- En SJF no apropiativo, interrumpir al proceso que corre (no se puede).
- En prioridad, confundir el sentido (aquí **menor número = más prioridad**).
- Calcular W.T. restando la llegada al **primer** inicio (eso es el tiempo de respuesta, no el de espera).
- No escribir los tiempos bajo **cada** corte del Gantt (el profesor da puntaje por el diagrama).
