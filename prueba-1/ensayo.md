# Ensayo de Prueba 1: Sistemas Operativos

> **Capítulos 1, 3 y 5** · 100 puntos · 90 minutos · Exigencia 60 %
>
> Hazla **con reloj y sin apuntes**, como si fuera la prueba real. Después corrige con la [pauta](pauta-ensayo.md).
> Indica en cada algoritmo qué criterio usas (por ejemplo, "RR por iteraciones en orden de llegada"; "W.T. = T.T. − ráfaga").

---

## Problema 1 (40 pts)

Se tienen los siguientes procesos:

| Proceso | Tpo. llegada | Tpo. ráfaga | Prioridad |
|---|---|---|---|
| A | 0,4 | 5 | 3 |
| B | 1,1 | 3 | 1 |
| C | 2,0 | 7 | 4 |
| D | 3,5 | 2 | 0 |
| E | 4,2 | 4 | 2 |

(Número menor = mayor prioridad.)

i) Simule el comportamiento del sistema mediante un diagrama de Gantt con los algoritmos **FCFS**, **SJF Preemptive**, **Priority Preemptive** y **Round Robin con q = 2**. (24 pts)

ii) Determine, para cada proceso y algoritmo, su **tiempo de permanencia** (turnaround) y su **tiempo de espera**, con los **promedios**. (12 pts)

iii) ¿Cuál es el mejor algoritmo para este grupo de procesos? Justifique. (4 pts)

---

## Problema 2 (15 pts)

En un sistema con planificación por prioridades expulsiva, llega un proceso P en el instante **2** con **prioridad máxima**. Su comportamiento es:

> CPU 3 ut → E/S 4 ut → CPU 2 ut → E/S 1 ut → CPU 5 ut

a) Dibuje la línea de tiempo del proceso y calcule su **tiempo de retorno**. (5 pts)

b) Escriba la **secuencia de transiciones de estado** que recorre P desde que entra hasta que termina. (6 pts)

c) Si en vez de prioridades el sistema usara **Round Robin con q = 2** y P fuera el **único** proceso, ¿qué transiciones **nuevas** aparecerían? ¿Cambia el tiempo de retorno? (Desprecie el costo del cambio de contexto.) (4 pts)

---

## Problema 3 (20 pts)

Responda brevemente, justificando:

a) Para hacer una llamada al sistema, ¿es necesario estar en modo monitor o en modo usuario? Defina el esquema correspondiente. (5 pts)

b) ¿Qué problema tendría un sistema de tiempo compartido si el hardware **no tuviera timer**? (5 pts)

c) Diferencie el multiprocesamiento **simétrico** del **asimétrico**. En un SMP de 4 procesadores, ¿dónde puede ejecutarse el SO? (5 pts)

d) Si la CPU tuviera que mover cada byte de toda operación de E/S (sin DMA), ¿qué consecuencia tendría para la multiprogramación? (5 pts)

---

## Problema 4 (25 pts)

a) ¿Por qué el PCB reserva espacio para los registros de la CPU? (4 pts)

b) En un sistema **monoprocesador**, ¿qué ventaja tiene que el SO soporte hilos a **nivel de kernel**, frente a hilos solo de usuario? (4 pts)

c) Un sistema Round Robin tiene **10 procesos** en la cola de listos y cada cambio de contexto cuesta **0,5 ms**. Para q = 2 ms, q = 10 ms y q = 50 ms calcule: (7 pts)
   - el **porcentaje de CPU** que se pierde en cambios de contexto, y
   - el **tiempo máximo** que espera un proceso para volver a ejecutar.

   Si se exige que todo proceso vuelva a ejecutar en **menos de 100 ms**, ¿qué quantum elegiría?

d) Un planificador SJF estima la próxima ráfaga con promedio exponencial, con **α = 0,5** y estimación inicial **τ₀ = 10 ms**. Las ráfagas reales fueron **6, 4, 6 y 13 ms**. Calcule τ₁, τ₂, τ₃ y τ₄. ¿Qué pasa con la estimación cuando aparece la ráfaga de 13? (6 pts)

e) Compare la **memoria compartida** y el **paso de mensajes** como mecanismos de comunicación entre procesos. (4 pts)
