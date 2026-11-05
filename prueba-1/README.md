# Prueba 1: capítulos 1, 3 y 5

| Capítulo | Tema | Dónde estudiarlo |
|---|---|---|
| **1** | Introducción: qué es un SO, interrupciones, E/S y DMA, modo dual, llamadas al sistema, multiprocesadores | [01 · Conceptos básicos](../estudio/01-conceptos-basicos.md) |
| **3** | Procesos: estados, PCB, cambio de contexto, planificadores, creación, IPC, hilos | [02 · Procesos e hilos](../estudio/02-procesos-e-hilos.md) |
| **5** | Planificación de CPU: FCFS, SJF, SRTF, prioridad, Round Robin, quantum | [03 · Planificación de CPU](../estudio/03-planificacion-cpu.md) |

> **No entra:** memoria y paginación, ni el cap. 8: [banquero e interbloqueo](../estudio/05-interbloqueo.md) pasan a la **siguiente prueba**. Ojo: en las P1 anteriores **sí** venía el banquero (2009, 2013, 2022, 2024), así que esas preguntas no te sirven para esta prueba.

## Qué esperar

En las P1 anteriores, lo que corresponde a estos capítulos se repartió así:

| Tipo de pregunta | Puntaje típico | Apareció en |
|---|---|---|
| **Planificación de CPU** (Gantt, T.T., W.T., promedios, "¿cuál es mejor?") | **40 pts**: casi la mitad de la prueba | 2009, 2013, 2022-2, 2024-2, 2025-2 (todas) |
| Preguntas de concepto del cap. 1 (llamada al sistema, DMA, SMP, interrupciones) | 10 a 30 pts | Todas |
| Conceptos de procesos e hilos (PCB, hilos de kernel) | 10 a 20 pts | 2022-2, 2024-2 |
| Teoría de planificación (inanición y aging, elegir el quantum) | 10 a 20 pts | 2013, 2025-2 |
| Proceso con CPU y E/S (tiempo de retorno, estados) | 10 pts | 2025-2 |

**Conclusión:** si dominas la planificación de CPU y te sabes las ~15 preguntas de concepto que se repiten, tienes cubierta la mayor parte de la prueba.

## Plan de estudio (7 sesiones)

| Sesión | Qué hacer | Material |
|---|---|---|
| 1 | Leer los capítulos 1 y 3 completos; hacer tu propio resumen del modo dual, las llamadas al sistema y los estados de un proceso | [01](../estudio/01-conceptos-basicos.md), [02](../estudio/02-procesos-e-hilos.md) |
| 2 | Leer **primero** las [convenciones del profesor](../estudio/00-convenciones-del-profesor.md#1-planificación-de-cpu) y después el capítulo 5 completo | [03](../estudio/03-planificacion-cpu.md) |
| 3 | Resolver **a mano** los ejercicios de planificación de nivel 1 y 2, y comprobarlos con `planificacion.py` | [ejercicios.md](ejercicios.md) |
| 4 | Ejercicios de nivel 3 y todas las preguntas de concepto, **sin mirar** las respuestas | [ejercicios.md](ejercicios.md) |
| 5 | Hacer el **ensayo 1 con reloj (90 min)** y corregirlo con la pauta | [ensayo.md](ensayo.md) → [pauta-ensayo.md](pauta-ensayo.md) |
| 6 | Repasar lo que fallaste y hacer el **ensayo 2**: tiempo ocioso, CPU con E/S y `fork` | [ensayo-2.md](ensayo-2.md) → [pauta-ensayo-2.md](pauta-ensayo-2.md) |
| 7 | Hacer el **ensayo 3**: algoritmos no apropiativos, cambio de contexto y elección del quantum | [ensayo-3.md](ensayo-3.md) → [pauta-ensayo-3.md](pauta-ensayo-3.md) |

## Lo que debes saber (marca lo que ya dominas)

### Capítulo 1: Introducción

- [ ] Qué es un SO: intermediario, administrador de recursos y programa de control
- [ ] Servicios del SO (al menos 3, con una línea de explicación cada uno)
- [ ] Cómo se atiende una interrupción, qué es una trap y el vector de interrupciones
- [ ] **¿Una interrupción o una llamada al sistema implican siempre un cambio de contexto?** (No: explica por qué)
- [ ] E/S por interrupciones vs. **DMA**, y qué pasa con la multiprogramación sin DMA
- [ ] Multiprogramación vs. multitarea (tiempo compartido); ventaja principal de la multiprogramación
- [ ] **Modo dual**: bit de modo, instrucciones privilegiadas, por qué la E/S es privilegiada
- [ ] **¿Una llamada al sistema se hace en modo usuario o monitor?** (sale casi siempre)
- [ ] Timer: para qué sirve y por qué cambiarlo es privilegiado
- [ ] SMP vs. AMP, multinúcleo, NUMA, clúster, sistema altamente acoplado
- [ ] Qué hace un driver y si es parte del SO
- [ ] Jerarquía de almacenamiento y caché
- [ ] Sin memoria virtual: qué problemas hay y si puede haber multiprogramación

### Capítulo 3: Procesos

- [ ] Programa vs. proceso; partes de un proceso en memoria (texto, datos, heap y pila)
- [ ] **Diagrama de estados** y cada transición con su causa (sin pasar de Espera a Ejecución)
- [ ] Contenido del **PCB** y **por qué guarda los registros**
- [ ] **Cambio de contexto**: qué es y por qué es tiempo perdido
- [ ] Planificadores de largo, corto y mediano plazo; colas
- [ ] Creación de procesos: `fork`, `exec`, `wait`, zombi y huérfano
- [ ] IPC: memoria compartida vs. paso de mensajes (ventajas y desventajas)
- [ ] **Hilos**: qué comparten, beneficios, hilos de usuario vs. de kernel y la ventaja en un monoprocesador

### Capítulo 5: Planificación de CPU

- [ ] Ráfagas de CPU y E/S; apropiativo vs. no apropiativo; despachador
- [ ] Criterios: utilización, throughput, **turnaround**, **waiting**, respuesta (fórmulas)
- [ ] Dibujar Gantt de **FCFS, SJF NA, SJF apropiativo (SRTF), Prioridad (NA y apropiativa), Round Robin**
- [ ] Llegadas con decimales, **tiempo ocioso** y ráfaga **restante** al expulsar
- [ ] RR **por iteraciones** (como el profesor) vs. cola del libro
- [ ] W.T. del libro (T.T. − ráfaga) vs. W.T. de la pauta (inicio del último tramo − llegada)
- [ ] Decir **cuál algoritmo es mejor** para un conjunto de procesos y por qué
- [ ] **Inanición y aging**
- [ ] Elegir el **quantum** (muy chico o muy grande) y calcular el costo del cambio de contexto
- [ ] Estimar la próxima ráfaga con el promedio exponencial
- [ ] Tiempo de retorno de un proceso con ráfagas de CPU y E/S

## Archivos de esta carpeta

| Archivo | Para qué |
|---|---|
| [ejercicios.md](ejercicios.md) | Todos los ejercicios de las pruebas anteriores y de la guía **que entran**, por nivel, con enlace a la solución |
| [ensayo.md](ensayo.md) · [pauta](pauta-ensayo.md) | Ensayo 1 al estilo del profesor (100 pts, 90 min) |
| [ensayo-2.md](ensayo-2.md) · [pauta](pauta-ensayo-2.md) | Ensayo 2: tiempo ocioso, procesos con E/S y `fork` |
| [ensayo-3.md](ensayo-3.md) · [pauta](pauta-ensayo-3.md) | Ensayo 3: no apropiativos, cambio de contexto y quantum |

Para la noche anterior: el [banco de preguntas](../estudio/09-preguntas-de-concepto.md#sistema-operativo-y-hardware) (secciones "Sistema operativo y hardware" y "Procesos, hilos y planificación") y la sección de planificación del [formulario](../estudio/formulario.md).
