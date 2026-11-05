# Ensayo 3 de Prueba 1: Sistemas Operativos

> **Capítulos 1, 3 y 5** · 100 puntos · 90 minutos · Exigencia 60 %
>
> Hazla **con reloj y sin apuntes**, como si fuera la prueba real. Después corrige con la [pauta](pauta-ensayo-3.md).
> Indica en cada algoritmo qué criterio usas (por ejemplo, "RR por iteraciones en orden de llegada"; "W.T. = T.T. − ráfaga").

---

## Problema 1 (40 pts)

Se tienen los siguientes procesos:

| Proceso | Tpo. llegada | Tpo. ráfaga | Prioridad |
|---|---|---|---|
| T1 | 0,6 | 8 | 3 |
| T2 | 1,4 | 4 | 1 |
| T3 | 2,7 | 9 | 5 |
| T4 | 3,3 | 5 | 2 |
| T5 | 4,9 | 2 | 4 |
| T6 | 6,2 | 3 | 0 |

(Número menor = mayor prioridad.)

i) Simule el comportamiento del sistema mediante un diagrama de Gantt con los algoritmos **FCFS**, **SJF no apropiativo**, **Prioridad no apropiativa** y **Round Robin con q = 3**. (20 pts)

ii) Determine, para cada proceso y algoritmo, su **tiempo de permanencia** (turnaround) y su **tiempo de espera**, con los **promedios**. (12 pts)

iii) ¿Cuál de los cuatro es el mejor para este grupo de procesos? Justifique. (4 pts)

iv) Dibuje **SJF Preemptive** y calcule su turnaround promedio. ¿Mejora a SJF no apropiativo? ¿Por qué? (4 pts)

---

## Problema 2 (15 pts)

Un sistema usa **Round Robin con q = 2** por iteraciones. Cada vez que la CPU pasa de un proceso a otro, el **cambio de contexto cuesta 0,5 ut**. El primer proceso no paga ese costo.

| Proceso | Llegada | Ráfaga |
|---|---|---|
| X | 0 | 5 |
| Y | 1 | 3 |
| Z | 2 | 4 |

a) Dibuje el diagrama de Gantt con los cambios de contexto y calcule el **turnaround** de cada proceso y su promedio. (5 pts)

b) ¿Qué porcentaje del tiempo total se pierde en cambios de contexto? (3 pts)

c) ¿Cuál sería el turnaround promedio con un cambio de contexto de costo 0? ¿Qué concluye? (3 pts)

d) Escriba la **secuencia de transiciones de estado** de Y. (4 pts)

---

## Problema 3 (20 pts)

Responda brevemente, justificando:

a) Describa **tres servicios** que entrega el sistema operativo. (4 pts)

b) ¿Qué es un sistema **altamente acoplado**? ¿Qué es lo contrario? (4 pts)

c) En un multiprocesador con memoria común, ¿cuál es el principal problema que debe resolver el sistema operativo? (4 pts)

d) Sin memoria virtual, ¿qué problemas hay? ¿Puede haber multiprogramación? (4 pts)

e) Diferencie una **interrupción** de una **trap**, y dé un ejemplo de cada una. (4 pts)

---

## Problema 4 (25 pts)

a) Diferencie **programa** y **proceso**. Nombre las partes de un proceso en memoria. (4 pts)

b) Explique qué hacen `fork`, `exec` y `wait`. ¿Cuándo un proceso queda **zombi** y cuándo queda **huérfano**? (5 pts)

c) ¿Qué comparten los hilos de un mismo proceso y qué tiene cada uno por separado? Nombre dos beneficios de usar hilos. (5 pts)

d) Un planificador SJF estima la próxima ráfaga con promedio exponencial, con **α = 0,25** y estimación inicial **τ₀ = 8 ms**. Las ráfagas reales fueron **4, 12 y 6 ms**. Calcule τ₁, τ₂ y τ₃. ¿Qué significaría usar α = 0? ¿Y α = 1? (5 pts)

e) En un sistema Round Robin, las últimas diez ráfagas de CPU duraron **2, 3, 3, 4, 4, 5, 6, 6, 7 y 20 ms**. Hay **20 procesos** en la cola de listos y cada cambio de contexto cuesta **1 ms**. (6 pts)

   - Según la regla empírica del 80 %, ¿qué quantum entero elegiría?
   - Para ese quantum, calcule el **porcentaje de CPU** que se pierde y el **tiempo máximo** que espera un proceso para volver a ejecutar.
   - ¿Qué ocurre si q = 1 ms? ¿Y si q es mayor que todas las ráfagas?
