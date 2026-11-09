# Ejercicios para la Prueba 2 (capítulos 8, 9 y 10)

> Todos los problemas de pruebas anteriores y de la guía **que entran**, ordenados por dificultad. Cada uno enlaza a su solución paso a paso.
> **Método:** resuélvelo en papel, **después** compruébalo con la herramienta y recién entonces mira la solución.

## Nivel 1: mecánica básica

| Ejercicio | Tema | Solución | Comprobar con |
|---|---|---|---|
| P1 2025-2, P3 | Base y límite en hexadecimal | [06 §2](../estudio/06-memoria.md#p1-2025-2-pregunta-3-20-pts) | — |
| Recuperativa 2024-2, P2 / 2026-1, P4 | Fragmentación interna (páginas de 2.048 B) | [06 §6.2](../estudio/06-memoria.md#62-recuperativa-2024-2-y-2026-1-fragmentación-interna-y-externa) | — |
| P2 2024-2, P1 | ¿Cabe el programa? (64 KB, 512 B) | [06 §6.1](../estudio/06-memoria.md#61-p2-2024-2-problema-1-cabe-el-programa-20-pts) | — |
| Guía 40 | Traducción con bits | [06 §4.1](../estudio/06-memoria.md#41-traducción-con-bits-guía-problema-40) | — |
| Apuntes cap. 9 | Traducción con m = 4, n = 2, y first/best/worst fit | [apuntes §5 y §7](apuntes-cap-9-y-10.md#5-asignación-contigua-y-particiones-variables) | — |
| Examen 2025-1, P2 | LRU con 3 marcos | [07 §5.3](../estudio/07-memoria-virtual.md#53-examen-2025-1-problema-2-10-pts-lru-con-3-marcos) | `reemplazo.py lru` |
| Recuperativa 2026-1, P2 | LRU con 3 marcos | [07 §5.4](../estudio/07-memoria-virtual.md#54-recuperativa-2026-1-problema-2-10-pts-lru-con-3-marcos) | `reemplazo.py lru` |
| Guía 13 | 4 instancias, 3 procesos, máximo 2 | [05 §4](../estudio/05-interbloqueo.md#guía-13-4-instancias-de-un-recurso-3-procesos-cada-uno-necesita-como-máximo-2) | — |

## Nivel 2: problemas completos de prueba

| Ejercicio | Tema | Solución | Comprobar con |
|---|---|---|---|
| Parcial 2024-2, P1 | Banquero, 4 procesos y 3 recursos | [05 §6.1](../estudio/05-interbloqueo.md#61-parcial-n1-2024-2-problema-1-35-pts) | `banquero.py` |
| Recuperativa 2024-2, P3 (= P1 2013 A) | Banquero Pa, Pb, Pc | [05 §6.2](../estudio/05-interbloqueo.md#62-recuperativa-2024-2--p1-2013-forma-a-20-pts) | `banquero.py` (⚠️ la pauta se equivoca) |
| P1 2009-2, P1 | Banquero con 4 recursos y solicitud | [05 §6.4](../estudio/05-interbloqueo.md#64-p1-2009-2-problema-1-30-pts-4-tipos-de-recurso) | `banquero.py` |
| P1 2022-2, P4 | Banquero con 12 instancias | [05 §6.3](../estudio/05-interbloqueo.md#63-p1-2022-2-problema-4-sin-pauta-12-instancias-de-r0) | `banquero.py` |
| Guía 1, 2, 16 | Banquero | [05 §6.6](../estudio/05-interbloqueo.md#66-guía-problemas-1-2-16-y-32) | `banquero.py` |
| Guía 5, 6, 7 | Grafos de asignación | [05 §3.3](../estudio/05-interbloqueo.md#33-guía-problemas-5-6-y-7) | `grafo.py` |
| P2 2025-2, P2 | LRU con tiempo y turnaround | [07 §5.1](../estudio/07-memoria-virtual.md#51-p2-2025-2-pregunta-2-30-pts-lru-con-3-marcos) | `reemplazo.py lru` |
| P2 2024-2, P3 | Óptimo con 3 marcos | [07 §5.2](../estudio/07-memoria-virtual.md#52-p2-2024-2-problema-3-20-pts-óptimo-con-3-marcos) | `reemplazo.py optimo` |
| Guía 11 y 36 | FIFO, Óptimo y LRU | [07 §5.5](../estudio/07-memoria-virtual.md#55-guía-para-practicar-y-comprobar) | `reemplazo.py` |
| P2 2025-2, P4 | Procesos A, B, C con 64 MB | [06 §5](../estudio/06-memoria.md#5-el-problema-típico-ram-de-x-mb-procesos-a-b-y-c) | `memoria.py` |
| P2 2024-2, P2 | Procesos A, B, C con 1.024 MB (+ mapa de bits) | [06 §5](../estudio/06-memoria.md#las-variantes) y [§4.2](../estudio/06-memoria.md#42-tamaño-del-mapa-de-bits-p2-2024-2-iv) | `memoria.py` |
| Examen 2026-1, P2 | Procesos A, B, C con permanencia | [06 §5](../estudio/06-memoria.md#las-variantes) | `memoria.py` (⚠️ 8.800, no 8.200) |
| Guía 14 y 30 | Procesos A, B, C | [06 §5](../estudio/06-memoria.md#las-variantes) | `memoria.py` |

## Nivel 3: los más difíciles

| Ejercicio | Tema | Solución | Comprobar con |
|---|---|---|---|
| Exámenes 2025-1 P1 y 2026-1 P4 | Banquero "N1 = N2 = 3, Mi,j = 2", 3 casos | [05 §6.5](../estudio/05-interbloqueo.md#65-exámenes-2025-1-y-2026-1-n1--n2--3-mij--2-20-30-pts) | `banquero.py` |
| Recuperativa 2024-2, P5 | Grafo con las 4 condiciones | [05 §3.1](../estudio/05-interbloqueo.md#31-recuperativa-2024-2-problema-5-25-pts) | `grafo.py` |
| Recuperativa 2026-1, P3 (= Guía 29) | Grafo con vectores | [05 §3.2](../estudio/05-interbloqueo.md#32-recuperativa-2026-1-problema-3--guía-problema-29) | `grafo.py` |
| Recuperativa 2026-1, P5 | Procesos A, B, C, **D** con 1 GB | [06 §5](../estudio/06-memoria.md#las-variantes) | `memoria.py` |
| Guía 9 | Comentar los tres gráficos de paginación | [07 §6](../estudio/07-memoria-virtual.md#guía-problema-9-comentar-los-tres-gráficos) | — |

## Preguntas de desarrollo

| Ejercicio | Tema | Solución |
|---|---|---|
| P2 2025-2, P1 | Rutina de falla de página | [07 §3](../estudio/07-memoria-virtual.md#3-rutina-de-falla-de-página-p2-2025-2-pregunta-1-10-pts) y [los 13 pasos](apuntes-cap-9-y-10.md#14-falla-de-página-los-13-pasos-del-peor-caso) |
| Examen 2025-1, parte I | Selección múltiple (memoria y deadlock) | [preguntas de concepto](preguntas-de-concepto.md) |
| Guía 25, 31 | Detección vs. prevención en sistemas distribuidos | [05 §4](../estudio/05-interbloqueo.md#guía-25-detección-o-prevención-para-la-red-de-la-empresa-2yk) |
| Guía 33, 37 | ¿Agregar un marco o reemplazar? | [06 §6.3](../estudio/06-memoria.md#63-guía-33--37-agregar-un-marco-o-reemplazar-una-página) |
| Guía 43 | Comente (memoria virtual, fragmentación, paginación) | [09 · Memoria](../estudio/09-preguntas-de-concepto.md#memoria) |
| P1 2009 e / P1 2022-2 P2 | Sin memoria virtual | [07 §1](../estudio/07-memoria-virtual.md#1-la-idea) |

> **No entran** en esta prueba (son del cap. 11 en adelante), aunque venían en algunas P2 anteriores: **disco y FAT** (P2 2025-2 P3), **transferencia RAM → disco** (P2 2024-2 P4) y **planificación del brazo** (guía 17, 20, 21, 22, 26). Si el profesor dice que sí entran, están en [08](../estudio/08-disco-archivos-y-proteccion.md).
