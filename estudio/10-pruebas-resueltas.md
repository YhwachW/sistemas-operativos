# 10 · Índice de pruebas: dónde está resuelto cada problema

> Cada problema de cada prueba enlaza a la sección donde se explica y se resuelve paso a paso.
> **Verificación** = si los números de la pauta coinciden con los recalculados con [`herramientas/`](../herramientas/):
> ✅ coincide · ⚠️ difiere (ver [errores conocidos](00-convenciones-del-profesor.md#4-errores-conocidos-en-las-pautas)) · 📝 sin pauta (resuelto aquí).
>
> Los PDF originales están en [`Pruebas y Pautas/`](../Pruebas%20y%20Pautas/).

## Qué se pregunta (frecuencia)

| Tema | Pruebas donde aparece | Puntaje típico |
|---|---|---|
| Planificación de CPU | 2009, 2013, 2022-2, 2024-2 (P1 y Recup.), 2025-1, 2025-2, 2026-1 (Examen y Recup.) | 20 a 40 |
| Banquero / estado seguro | 2009, 2013, 2022-2, 2024-2 (P1 y Recup.), 2025-1, 2026-1 | 20 a 35 |
| Paginación "procesos A, B, C" | 2024-2 P2, 2025-2 P2, 2026-1 (Examen y Recup.) | 30 a 40 |
| Reemplazo de páginas | 2024-2 P2, 2025-1, 2025-2 P2, Recup. 2026-1 | 10 a 30 |
| Preguntas de concepto | Todas | 10 a 30 |
| Grafo de asignación de recursos | Recup. 2024-2, Recup. 2026-1 | 10 a 25 |
| Sincronización / semáforos | Examen 2025-1, Examen 2026-1 | 15 a 20 |
| Fragmentación | Recup. 2024-2, Recup. 2026-1 | 15 a 20 |
| Base y límite, FAT, disco | P1 2025-2, P2 2025-2, P2 2024-2 | 20 |

---

## PAUTA P1 2009-2

| Problema | Tema | Dónde | Verificación |
|---|---|---|---|
| 1 (30 pts) | Banquero con 4 recursos y solicitud de P1 | [05 §6.4](05-interbloqueo.md#64-p1-2009-2-problema-1-30-pts-4-tipos-de-recurso) | ✅ |
| 2 (40 pts) | Prioridad-P, SJF-P, RR q=3 | [03 §5.3](03-planificacion-cpu.md#53-p1-2009-2--recuperativa-2026-1--prioridad-apropiativa-sjf-apropiativo-rr-q--3) | ✅ (W.T. con la [regla de la pauta](00-convenciones-del-profesor.md#14-tiempo-de-espera-wt-la-pauta-usa-inicio-del-último-tramo--llegada)) |
| 3 a-f (30 pts) | Conceptos | [09](09-preguntas-de-concepto.md#sistema-operativo-y-hardware) | — |

## Pauta P1 2013-2 (formas A, B y C)

| Problema | Tema | Dónde | Verificación |
|---|---|---|---|
| 1 (40 pts) | FCFS, RR y SJF con ráfagas de CPU y E/S | [03 §5.8](03-planificacion-cpu.md#58-p1-2013--pregunta-1-procesos-con-ráfagas-de-cpu-y-es) | La pauta suma CPU + E/S |
| 2 (20 pts) | Inanición y aging | [03 §4.4](03-planificacion-cpu.md#44-prioridad-apropiativa-o-no) | — |
| 3 (10 pts) | ¿Interrupción = cambio de contexto? | [01 §3](01-conceptos-basicos.md#p1-2013-pregunta-3-una-interrupción-produce-necesariamente-un-cambio-de-contexto-y-una-llamada-al-sistema) | — |
| 4 (20 pts) | Banquero Pa, Pb, Pc | [05 §6.2](05-interbloqueo.md#62-recuperativa-2024-2--p1-2013-forma-a-20-pts) | ✅ forma A b) · ⚠️ a) es ambigua · ⚠️ forma C a) |
| 5 (10 pts) | DMA | [01 §4](01-conceptos-basicos.md#4-estructura-de-es-y-dma) | — |

## P1 2022-2 (sin pauta)

| Problema | Tema | Dónde | Verificación |
|---|---|---|---|
| 1 (40 pts) | FCFS, SJF NA, RR q=2 | [03 §5.6](03-planificacion-cpu.md#56-p1-2022-2--problema-1-sin-pauta-fcfs-sjf-no-apropiativo-rr-q--2) | 📝 |
| 2 (20 pts) | Sin memoria virtual | [07 §1](07-memoria-virtual.md#1-la-idea) | 📝 |
| 3 (20 pts) | Acoplado, drivers, PCB, SMP | [09](09-preguntas-de-concepto.md#sistema-operativo-y-hardware) | 📝 |
| 4 (20 pts) | Banquero con 12 instancias | [05 §6.3](05-interbloqueo.md#63-p1-2022-2-problema-4-sin-pauta-12-instancias-de-r0) | 📝 |

## Pauta Parcial N°1 2024-2

| Problema | Tema | Dónde | Verificación |
|---|---|---|---|
| 1 (35 pts) | Banquero, 4 procesos y 3 recursos | [05 §6.1](05-interbloqueo.md#61-parcial-n1-2024-2-problema-1-35-pts) | ✅ |
| 2 (40 pts) | SJF-P y RR q=2 | [03 §5.1](03-planificacion-cpu.md#51-parcial-n1-2024-2--problema-2-40-pts-sjf-apropiativo-y-rr-q--2) | ✅ T.T. · W.T. con la regla de la pauta |
| 3 (10 pts) | Hilos a nivel de sistema | [02 §8](02-procesos-e-hilos.md#8-hilos-threads) | — |
| 4 (15 pts) | Sin DMA y multiprogramación | [01 §4](01-conceptos-basicos.md#parcial-2024-2-problema-4-sin-dma-qué-implica-para-la-multiprogramación) | — |

## Pauta Prueba N°2 2024-2

| Problema | Tema | Dónde | Verificación |
|---|---|---|---|
| 1 (20 pts) | ¿Cabe el programa? (64 KB, 512 B) | [06 §6.1](06-memoria.md#61-p2-2024-2-problema-1-cabe-el-programa-20-pts) | ✅ |
| 2 (40 pts) | Procesos A, B, C con 1.024 MB | [06 §5](06-memoria.md#5-el-problema-típico-ram-de-x-mb-procesos-a-b-y-c) | ✅ (⚠️ 410 vs. 393 B) |
| 3 (20 pts) | Óptimo con 3 marcos | [07 §5.2](07-memoria-virtual.md#52-p2-2024-2-problema-3-20-pts-óptimo-con-3-marcos) | ✅ |
| 4 (20 pts) | Transferencia RAM → disco | [08 §6](08-disco-archivos-y-proteccion.md#6-transferencia-ram--disco-p2-2024-2-problema-4-20-pts) | ✅ |

## Pauta Recuperativa 2024-2

| Problema | Tema | Dónde | Verificación |
|---|---|---|---|
| 1 (30 pts) | FCFS y SJF-P | [03 §5.2](03-planificacion-cpu.md#52-recuperativa-2024-2--examen-2025-1--fcfs-y-sjf-apropiativo-30-pts) | ✅ |
| 2 (15 pts) | Fragmentación (2048 B, 8 MB) | [06 §6.2](06-memoria.md#62-recuperativa-2024-2-y-2026-1-fragmentación-interna-y-externa) | ✅ |
| 3 (10 pts) | Llamada al sistema | [01 §8](01-conceptos-basicos.md#8-llamadas-al-sistema) | — |
| 3 bis (20 pts) | Banquero Pa, Pb, Pc | [05 §6.2](05-interbloqueo.md#62-recuperativa-2024-2--p1-2013-forma-a-20-pts) | ⚠️ partir con Pc también es seguro |
| 5 (25 pts) | Grafo con 4 condiciones | [05 §3.1](05-interbloqueo.md#31-recuperativa-2024-2-problema-5-25-pts) | ⚠️ menciona un R4 que no existe (la conclusión es correcta) |

## Pauta Examen 2025-1

| Problema | Tema | Dónde | Verificación |
|---|---|---|---|
| I (25 pts) | Selección múltiple: C, C, A, A, C | [09](09-preguntas-de-concepto.md#memoria) | — |
| 1 (20 pts) | Banquero, 3 casos | [05 §6.5](05-interbloqueo.md#65-exámenes-2025-1-y-2026-1-n1--n2--3-mij--2-20-30-pts) | ✅ |
| 2 (10 pts) | LRU con 3 marcos | [07 §5.3](07-memoria-virtual.md#53-examen-2025-1-problema-2-10-pts-lru-con-3-marcos) | ✅ |
| 3 (30 pts) | FCFS y SJF-P | [03 §5.2](03-planificacion-cpu.md#52-recuperativa-2024-2--examen-2025-1--fcfs-y-sjf-apropiativo-30-pts) | ✅ |
| 4 (15 pts) | Estacionamiento con semáforos | [04 §4.3](04-sincronizacion.md#43-contar-recursos-semáforo-en-n) | ✅ |

## Pauta Prueba N°1 2025-2

| Problema | Tema | Dónde | Verificación |
|---|---|---|---|
| 1 (40 pts) | FCFS, SJF-P, Prioridad-P y RR q=3 | [03 §5.5](03-planificacion-cpu.md#55-p1-2025-2--pregunta-1-40-pts-los-cuatro-algoritmos-y-el-mejor) | ✅ (⚠️ T.T. de P5 en Prioridad) |
| 2 (10 pts) | Tiempo de retorno con E/S | [03 §5.7](03-planificacion-cpu.md#57-p1-2025-2--pregunta-2-tiempo-de-retorno-con-es) | ✅ |
| 3 (20 pts) | Base y límite | [06 §2](06-memoria.md#p1-2025-2-pregunta-3-20-pts) | ✅ |
| 4 (10 pts) | Multiprocesador con memoria común | [01 §9](01-conceptos-basicos.md#9-sistemas-multiprocesador) | — |
| 5 (10 pts) | Llamada al sistema | [01 §8](01-conceptos-basicos.md#8-llamadas-al-sistema) | — |
| 6 (10 pts) | Quantum para 20 procesos | [03 §4.5](03-planificacion-cpu.md#45-round-robin-rr) | — |

## Pauta Prueba P2 2025-2

| Problema | Tema | Dónde | Verificación |
|---|---|---|---|
| 1 (10 pts) | Rutina de falla de página | [07 §3](07-memoria-virtual.md#3-rutina-de-falla-de-página-p2-2025-2-pregunta-1-10-pts) | — |
| 2 (30 pts) | LRU, tiempo y turnaround | [07 §5.1](07-memoria-virtual.md#51-p2-2025-2-pregunta-2-30-pts-lru-con-3-marcos) | ✅ |
| 3 (20 pts) | Disco y FAT | [08 §4](08-disco-archivos-y-proteccion.md#4-ejercicio-de-fat-p2-2025-2-pregunta-3-20-pts) | ✅ |
| 4 (40 pts) | Procesos A, B, C con 64 MB | [06 §5](06-memoria.md#5-el-problema-típico-ram-de-x-mb-procesos-a-b-y-c) | ✅ (⚠️ 410 vs. 393 B) |

## Pauta Examen 2026-1

| Problema | Tema | Dónde | Verificación |
|---|---|---|---|
| 1 (20 pts) | Variable X compartida | [04 §1](04-sincronizacion.md#1-el-problema-la-condición-de-carrera) | ✅ |
| 2 (30 pts) | Procesos A, B, C con 64 MB | [06 §5](06-memoria.md#las-variantes) | ⚠️ permanencia: 8.800, no 8.200 |
| 3 (20 pts) | SJF-P y RR q=2 | [03 §5.4](03-planificacion-cpu.md#54-examen-2026-1--problema-3-20-pts-sjf-apropiativo-y-rr-q--2) | ✅ |
| 4 (30 pts) | Banquero, 3 casos | [05 §6.5](05-interbloqueo.md#65-exámenes-2025-1-y-2026-1-n1--n2--3-mij--2-20-30-pts) | ✅ |

## Pauta Recuperativa 2026-1

| Problema | Tema | Dónde | Verificación |
|---|---|---|---|
| 1 (30 pts) | Prioridad-P, SJF-P, RR q=3 (= 2009) | [03 §5.3](03-planificacion-cpu.md#53-p1-2009-2--recuperativa-2026-1--prioridad-apropiativa-sjf-apropiativo-rr-q--3) | ✅ |
| 2 (10 pts) | LRU con 3 marcos | [07 §5.4](07-memoria-virtual.md#54-recuperativa-2026-1-problema-2-10-pts-lru-con-3-marcos) | ✅ |
| 3 (10 pts) | Grafo con vectores (= Guía 29) | [05 §3.2](05-interbloqueo.md#32-recuperativa-2026-1-problema-3--guía-problema-29) | ✅ |
| 4 (20 pts) | Fragmentación interna y externa | [06 §6.2](06-memoria.md#62-recuperativa-2024-2-y-2026-1-fragmentación-interna-y-externa) | ✅ |
| 5 (30 pts) | Procesos A, B, C, D con 1 GB | [06 §5](06-memoria.md#las-variantes) | ✅ |

## Guía de ejercicios (2009)

| Problemas | Dónde |
|---|---|
| 1, 2, 16, 32 (banquero) | [05 §6.6](05-interbloqueo.md#66-guía-problemas-1-2-16-y-32) |
| 3, 4, 8, 10 (planificación) | [03 §5.9](03-planificacion-cpu.md#59-guía-de-ejercicios-resultados-para-comprobar) |
| 5, 6, 7, 29 (grafos) | [05 §3](05-interbloqueo.md#3-grafo-de-asignación-de-recursos) |
| 9 (gráficos de paginación) | [07 §6](07-memoria-virtual.md#guía-problema-9-comentar-los-tres-gráficos) |
| 11, 36 (reemplazo) | [07 §5.5](07-memoria-virtual.md#55-guía-para-practicar-y-comprobar) |
| 12, 23 (Bernstein) | [04 §7.1](04-sincronizacion.md#71-condiciones-de-bernstein-pueden-ir-en-paralelo) |
| 13, 25, 31 (deadlock, teoría) | [05 §4](05-interbloqueo.md#4-cómo-se-maneja-el-deadlock) |
| 14, 30 (procesos A, B, C) | [06 §5](06-memoria.md#las-variantes) |
| 15, 38 (fork/join) | [04 §7.2](04-sincronizacion.md#72-grafos-de-precedencia-con-forkjoin) |
| 17, 20, 21, 22, 26 (disco) | [08](08-disco-archivos-y-proteccion.md) |
| 24, 27, 34, 39, 41, 42 (semáforos) | [04](04-sincronizacion.md) y [programas](programas/) |
| 28 (matriz de acceso) | [08 §7](08-disco-archivos-y-proteccion.md#guía-problema-28) |
| 33, 37 (marcos por proceso) | [06 §6.3](06-memoria.md#63-guía-33--37-agregar-un-marco-o-reemplazar-una-página) |
| 35 (transiciones de estado) | [02 §2](02-procesos-e-hilos.md#guía-problema-35-transiciones-de-un-proceso) |
| 40 (traducción con bits) | [06 §4.1](06-memoria.md#41-traducción-con-bits-guía-problema-40) |
| 43 (comente) | [09](09-preguntas-de-concepto.md) |

> **No resueltos:** el 18 y el 19 dependen de figuras que no se pueden leer con certeza (el 19 no tiene etiquetas en los nodos). Resuélvelos con el mismo método de los problemas 7 y 38.
