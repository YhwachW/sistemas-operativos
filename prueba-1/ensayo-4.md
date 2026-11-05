# Ensayo 4 de Prueba 1: Sistemas Operativos

> **Capítulos 1, 3 y 5** · 100 puntos · 90 minutos · Exigencia 60 %
>
> Sigue el formato que te anticiparon, que **no está confirmado**: SJF, SJF Preemptive, Round Robin, un problema teórico y otro ejercicio de SJF/FCFS en lugar del banquero. Los problemas y su puntaje son una estimación.
>
> Hazla **con reloj y sin apuntes**. Después corrige con la [pauta](pauta-ensayo-4.md). Indica qué criterio usas (por ejemplo, "RR por iteraciones en orden de llegada"; "W.T. = T.T. − ráfaga").

---

## Problema 1: SJF no apropiativo (20 pts)

| Proceso | Tpo. llegada | Tpo. ráfaga |
|---|---|---|
| J1 | 1,2 | 6 |
| J2 | 2,0 | 4 |
| J3 | 3,1 | 1 |
| J4 | 4,5 | 3 |
| J5 | 5,7 | 2 |

a) Dibuje el diagrama de Gantt. (8 pts)

b) Calcule el **turnaround** y el **tiempo de espera** de cada proceso, con los **promedios**. (8 pts)

c) J3 llega en 3,1 y solo necesita 1 ut. ¿Por qué no parte de inmediato? (4 pts)

---

## Problema 2: SJF Preemptive (20 pts)

| Proceso | Tpo. llegada | Tpo. ráfaga |
|---|---|---|
| A | 0,3 | 7 |
| B | 1,0 | 5 |
| C | 1,8 | 2 |
| D | 2,5 | 1 |
| E | 6,2 | 3 |

a) Dibuje el diagrama de Gantt y justifique cada expulsión, indicando la ráfaga **restante** que compara. (10 pts)

b) Calcule el **turnaround** y el **tiempo de espera** de cada proceso, con los **promedios**. (8 pts)

c) Cuando llega E, ¿expulsa al proceso que está corriendo? Justifique. (2 pts)

---

## Problema 3: Round Robin (20 pts)

Con **q = 2**:

| Proceso | Tpo. llegada | Tpo. ráfaga |
|---|---|---|
| R1 | 0,5 | 5 |
| R2 | 1,2 | 3 |
| R3 | 2,0 | 6 |
| R4 | 6,0 | 2 |
| R5 | 9,0 | 4 |

a) Dibuje el diagrama de Gantt, indicando cada vuelta. (10 pts)

b) Calcule el **turnaround** y el **tiempo de espera** de cada proceso, con los **promedios**. (8 pts)

c) ¿En qué se convertiría este algoritmo si q fuera mayor que todas las ráfagas? (2 pts)

---

## Problema 4: Teórico (20 pts)

Responda brevemente, justificando:

a) Para hacer una llamada al sistema, ¿es necesario estar en modo monitor o en modo usuario? Explique el recorrido completo. (5 pts)

b) ¿Qué es el cambio de contexto? ¿Por qué se considera tiempo perdido y qué papel cumple el PCB? (5 pts)

c) ¿Qué es el DMA? ¿Qué implicaría para la multiprogramación no tenerlo? (5 pts)

d) ¿Por qué SJF es óptimo? ¿Cuál es su principal dificultad práctica y qué riesgo tiene para los procesos largos? (5 pts)

---

## Problema 5: FCFS y SJF (20 pts)

| Proceso | Tpo. llegada | Tpo. ráfaga |
|---|---|---|
| F1 | 0,7 | 9 |
| F2 | 1,5 | 2 |
| F3 | 2,2 | 6 |
| F4 | 3,0 | 1 |
| F5 | 20,0 | 3 |

a) Dibuje el diagrama de Gantt con **FCFS** y con **SJF no apropiativo**. (8 pts)

b) Calcule el **turnaround** y el **tiempo de espera** de cada proceso en ambos algoritmos, con los **promedios**. (6 pts)

c) ¿Cuál es mejor para este grupo? ¿Algún proceso empeora al cambiar de FCFS a SJF? ¿Qué es el **efecto convoy** y cómo se observa aquí? (6 pts)
