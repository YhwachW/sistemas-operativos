# Sistemas Operativos: material de estudio

Repositorio personal para preparar las pruebas de **Sistemas Operativos** (UTEM, prof. Jorge Morris A.). Están todos los temas que se evalúan, explicados desde cero, con **cada problema de las pruebas 2009-2026 resuelto paso a paso** y **verificado con programas**.

## Por dónde empezar

> 📌 **¿Estudias para la Prueba 1 (capítulos 1, 3 y 5)?** Ve directo a [`prueba-1/`](prueba-1/): qué entra, plan de estudio, ejercicios por nivel y **tres ensayos con pauta**.

1. **[00 · Convenciones del profesor y errores de las pautas](estudio/00-convenciones-del-profesor.md)**: léelo primero. El profesor resuelve Round Robin y calcula el tiempo de espera de una forma distinta al libro, y algunas pautas tienen errores.
2. Estudia los temas en orden (cada uno trae teoría, ejercicios de prueba resueltos y errores típicos).
3. Practica con la [guía](Guias/) y **comprueba** tus resultados con las [herramientas](herramientas/).
4. La noche antes: el [banco de preguntas](estudio/09-preguntas-de-concepto.md) y el [formulario](estudio/formulario.md).

## Temas

| # | Tema | Lo que más se pregunta |
|---|---|---|
| 00 | [Convenciones del profesor y errores de las pautas](estudio/00-convenciones-del-profesor.md) | — |
| 01 | [Conceptos básicos del SO](estudio/01-conceptos-basicos.md) | Llamadas al sistema y modo dual, DMA, SMP, drivers |
| 02 | [Procesos e hilos](estudio/02-procesos-e-hilos.md) | Estados, PCB, hilos de kernel |
| 03 | [Planificación de CPU](estudio/03-planificacion-cpu.md) | **FCFS, SJF, prioridad, Round Robin: T.T. y W.T.** |
| 04 | [Sincronización: semáforos y monitores](estudio/04-sincronizacion.md) | Condición de carrera, semáforos, productor-consumidor |
| 05 | [Interbloqueo (deadlock)](estudio/05-interbloqueo.md) | **Banquero** y grafos de asignación |
| 06 | [Memoria y paginación](estudio/06-memoria.md) | **Procesos A, B, C: marcos, fallas, fragmentación** |
| 07 | [Memoria virtual y reemplazo de páginas](estudio/07-memoria-virtual.md) | **FIFO, Óptimo, LRU con tiempo de fallas** |
| 08 | [Disco, archivos y protección](estudio/08-disco-archivos-y-proteccion.md) | FAT, planificación del disco |
| 09 | [Banco de preguntas de concepto](estudio/09-preguntas-de-concepto.md) | Respuestas modelo |
| 10 | [Índice de pruebas resueltas](estudio/10-pruebas-resueltas.md) | Dónde está cada problema de cada prueba |
| — | [Formulario](estudio/formulario.md) · [Glosario](estudio/glosario.md) | |

## Herramientas para comprobar tus ejercicios

Programas en Python, sin instalar nada extra ([instrucciones](herramientas/README.md)):

| Programa | Para qué |
|---|---|
| [`planificacion.py`](herramientas/planificacion.py) | Gantt, T.T. y W.T. (con la columna "como la pauta") de FCFS, SJF, SRTF, Prioridad y RR |
| [`banquero.py`](herramientas/banquero.py) | Estado seguro, **todas** las secuencias seguras y solicitudes |
| [`grafo.py`](herramientas/grafo.py) | Ciclos y reducción del grafo de asignación de recursos |
| [`memoria.py`](herramientas/memoria.py) | El problema "procesos A, B, C": marcos, fallas, fragmentación, permanencia |
| [`reemplazo.py`](herramientas/reemplazo.py) | FIFO, Óptimo y LRU paso a paso, con la tabla de entradas y salidas |
| [`disco.py`](herramientas/disco.py) | FCFS, SSTF, SCAN, LOOK, C-SCAN, C-LOOK |
| [`diagramas.py`](herramientas/diagramas.py) | Regenera las figuras de `estudio/diagramas/` desde los mismos simuladores |

Los ejercicios de semáforos están como **programas C-- que se ejecutan** en [`estudio/programas/`](estudio/programas/): en jBACI o en el celular con [Mini BACI](https://yhwachw.github.io/mini-baci/). Tus ejercicios propios de jBACI (impresora, tráfico, estacionamiento) están en [`estudio/programas/ejercicios-jbaci/`](estudio/programas/ejercicios-jbaci/).

## Material original

| Carpeta | Contenido |
|---|---|
| [`Pruebas y Pautas/`](Pruebas%20y%20Pautas/) | Pruebas y pautas 2009, 2013, 2022, 2024, 2025 y 2026 |
| [`Apuntes/`](Apuntes/) | Diapositivas de clases: cap. 1 (Introducción), 3 (Procesos), 5 (Planificación) y 8 (Deadlocks), basadas en Silberschatz, *Operating System Concepts*, 10.ª ed. |
| [`Guias/`](Guias/) | Guía de ejercicios (43 problemas) |
| `jBACI/` (solo en tu PC) | Simulador jBACI con sus manuales. Es un clon de [github.com/motib/jbaci](https://github.com/motib/jbaci) y **no se sube** a este repo (es otro repositorio). Tus ejercicios están copiados en `estudio/programas/ejercicios-jbaci/` |
| [`Presentacion jBACI/`](Presentacion%20jBACI/) | Presentación "Cómo usar jBACI" |

## Cómo se verificó

Cada problema numérico de las pautas se recalculó con los programas de [`herramientas/`](herramientas/). Todas las soluciones de semáforos se ejecutaron **3.000 veces** con el intérprete de Mini BACI para confirmar que siempre producen el resultado pedido. Las diferencias con las pautas están documentadas en [00 · Convenciones](estudio/00-convenciones-del-profesor.md#4-errores-conocidos-en-las-pautas).
