# Ejercicios para la Prueba 1 (capítulos 1, 3 y 5)

> Resuelve **a mano primero** y recién después mira la solución o compruébala con `python herramientas/planificacion.py` ([cómo usarlo](../herramientas/README.md#planificacionpy-planificación-de-cpu)).

## A. Planificación de CPU

### Nivel 1: para calentar (3 procesos, un algoritmo a la vez)

| # | Fuente | Datos | Pide | Solución |
|---|---|---|---|---|
| 1 | Guía, problema 4 | 1 (0,0; 3), 2 (0,8; 2), 3 (0,9; 4) | FCFS, SJF apropiativo, RR q=3 | [03 §5.9](../estudio/03-planificacion-cpu.md#59-guía-de-ejercicios-resultados-para-comprobar) |
| 2 | Recuperativa 2024-2 = Examen 2025-1 | Azul (0,1; 4), Monse (0,8; 2), Prg1 (0,5; 3) | FCFS y SJF apropiativo | [03 §5.2](../estudio/03-planificacion-cpu.md#52-recuperativa-2024-2--examen-2025-1--fcfs-y-sjf-apropiativo-30-pts) |
| 3 | Examen 2026-1 | 1 (2,5; 3), 2 (1,3; 2), 3 (1,4; 1) | SJF apropiativo y RR q=2 | [03 §5.4](../estudio/03-planificacion-cpu.md#54-examen-2026-1--problema-3-20-pts-sjf-apropiativo-y-rr-q--2) |
| 4 | P1 2022-2 | T1 (0,8; 10), T2 (2,3; 5), T3 (5,2; 2) | FCFS, SJF no apropiativo, RR q=2 | [03 §5.6](../estudio/03-planificacion-cpu.md#56-p1-2022-2--problema-1-sin-pauta-fcfs-sjf-no-apropiativo-rr-q--2) |

### Nivel 2: varios algoritmos, prioridades y tiempo ocioso

| # | Fuente | Datos (llegada; ráfaga; prioridad) | Pide | Solución |
|---|---|---|---|---|
| 5 | Guía, problema 8 | 1 (1,6; 1; 0), 2 (1,3; 4; 1), 3 (0,4; 3; 3) | Todos los algoritmos, RR q=3 | [03 §5.9](../estudio/03-planificacion-cpu.md#59-guía-de-ejercicios-resultados-para-comprobar) |
| 6 | Guía, problema 10 | 1 (2,5; 1), 2 (1,3; 4), 3 (1,4; 3), 4 (1,5; 2) | SJF apropiativo, RR q=3 | [03 §5.9](../estudio/03-planificacion-cpu.md#59-guía-de-ejercicios-resultados-para-comprobar) |
| 7 | P1 2009-2 = Recuperativa 2026-1 | P1 (1,2; 3; 8), P2 (3,2; 2; 5), P3 (5,5; 1; 4), P4 (8,6; 3; 1), P5 (10,9; 2; 0) | Prioridad apropiativa, SJF apropiativo, RR q=3 | [03 §5.3](../estudio/03-planificacion-cpu.md#53-p1-2009-2--recuperativa-2026-1--prioridad-apropiativa-sjf-apropiativo-rr-q--3) |
| 8 | Parcial 2024-2 | 1 (1,6; 1), 2 (1,3; 2), 3 (0,5; 6), 4 (1,5; 2), 5 (5,6; 2) | SJF apropiativo y RR q=2 | [03 §5.1](../estudio/03-planificacion-cpu.md#51-parcial-n1-2024-2--problema-2-40-pts-sjf-apropiativo-y-rr-q--2) |

### Nivel 3: nivel de prueba (5-6 procesos, 4 algoritmos y "¿cuál es mejor?")

| # | Fuente | Datos (llegada; ráfaga; prioridad) | Pide | Solución |
|---|---|---|---|---|
| 9 | P1 2025-2 | P1 (1,2; 12; 5), P2 (3,2; 9; 4), P3 (5,5; 8; 2), P4 (8,6; 11; 0), P5 (10,9; 14; 4) | FCFS, SJF-P, Prioridad-P, RR q=3 y el mejor | [03 §5.5](../estudio/03-planificacion-cpu.md#55-p1-2025-2--pregunta-1-40-pts-los-cuatro-algoritmos-y-el-mejor) |
| 10 | Guía, problema 3 | 1 (0,8; 3; 3), 2 (1,8; 5; 0), 3 (3,2; 2; 0), 4 (9,1; 5; 3), 5 (12,7; 5; 5), 6 (2,6; 2; 3) | Todos los algoritmos, RR q=1 | [03 §5.9](../estudio/03-planificacion-cpu.md#59-guía-de-ejercicios-resultados-para-comprobar) |
| 11 | **Ensayo** | A (0,4; 5; 3), B (1,1; 3; 1), C (2,0; 7; 4), D (3,5; 2; 0), E (4,2; 4; 2) | Los 4 algoritmos y el mejor | [pauta del ensayo](pauta-ensayo.md#problema-1-40-pts) |

> **Trampas que ponen a prueba:**
> - el ej. 3 tiene un tramo de solo 0,1;
> - el ej. 7 tiene tiempo ocioso;
> - en el ej. 4, con SJF **no** apropiativo no se interrumpe a T1;
> - en el ej. 6 hay **dos expulsiones seguidas**: en 1,4 el proceso 3 expulsa al 2, y en 1,5 el 4 expulsa al 3.

### Procesos con CPU y E/S

| # | Fuente | Pide | Solución |
|---|---|---|---|
| 12 | P1 2025-2, pregunta 2 | Tiempo de retorno de un proceso con CPU 4, E/S 5, CPU 7 | [03 §5.7](../estudio/03-planificacion-cpu.md#57-p1-2025-2--pregunta-2-tiempo-de-retorno-con-es) |
| 13 | Guía, problema 35 | Transiciones de estado con ráfagas de CPU, impresora y disco | [02 §2](../estudio/02-procesos-e-hilos.md#guía-problema-35-transiciones-de-un-proceso) |
| 14 | P1 2013, pregunta 1 | Planificar procesos con varias ráfagas de CPU y E/S | [03 §5.8](../estudio/03-planificacion-cpu.md#58-p1-2013--pregunta-1-procesos-con-ráfagas-de-cpu-y-es) (ojo con el criterio de la pauta) |

## B. Preguntas de concepto que ya salieron

Respóndelas en voz alta o por escrito **antes** de abrir la respuesta. Todas están en el [banco de preguntas](../estudio/09-preguntas-de-concepto.md).

| # | Pregunta | Salió en | Cap. |
|---|---|---|---|
| 15 | ¿Cuál es la principal ventaja de la multiprogramación? | 2009 | 1 |
| 16 | ¿Cómo garantizar que todo acceso a dispositivos pase por el SO? | 2009 | 1 |
| 17 | Describa tres servicios del SO | 2009 | 1 |
| 18 | Para hacer una llamada al sistema, ¿hay que estar en modo monitor o en modo usuario? | 2009, 2024-2, **2025-2** | 1 |
| 19 | ¿Una interrupción produce necesariamente un cambio de contexto? ¿Y una llamada al sistema? | 2013 | 1 |
| 20 | ¿Qué elemento intercambia datos entre el controlador de E/S y la memoria sin la CPU? | 2013 | 1 |
| 21 | Sin DMA, ¿qué implica para la multiprogramación? | 2024-2 | 1 |
| 22 | SMP con 4 procesadores: ¿el SO puede correr en cualquiera? | 2009, 2022-2 | 1 |
| 23 | ¿Qué es un sistema altamente acoplado? | 2022-2 | 1 |
| 24 | ¿Qué implementan los drivers? ¿Son parte del SO? | 2022-2 | 1 |
| 25 | Multiprocesador con memoria común: ¿principal problema para el SO? | 2025-2 | 1 |
| 26 | Sin memoria virtual: ¿qué problemas hay? ¿Puede haber multiprogramación? | 2009, 2022-2 | 1 |
| 27 | ¿Por qué el PCB reserva lugar para los registros de la CPU? | 2022-2 | 3 |
| 28 | Ventaja de los hilos a nivel de sistema en un monoprocesador | 2024-2 | 3 |
| 29 | "La permutación de la CPU a otro proceso requiere guardar…": comente | Guía 43 a | 3 |
| 30 | Planificación por prioridades: ¿cómo se evita la inanición? | 2013 | 5 |
| 31 | ¿Qué quantum es apropiado para RR con 20 procesos en la cola? | 2025-2 | 5 |

## C. Para practicar con la herramienta

Inventa tus propios ejercicios: escribe 4 o 5 procesos con llegadas decimales en un archivo y compara tu Gantt con el del programa.

```bash
python herramientas/planificacion.py mis-datos.txt srtf
python herramientas/planificacion.py mis-datos.txt prio_p
python herramientas/planificacion.py mis-datos.txt rr_vueltas 2
```
