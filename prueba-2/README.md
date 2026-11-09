# Prueba 2: capítulos 8, 9 y 10

| Capítulo | Tema | Dónde estudiarlo |
|---|---|---|
| **8** | Interbloqueo: 4 condiciones, grafo de asignación, prevención, evitación (**banquero**), detección y recuperación | [05 · Interbloqueo](../estudio/05-interbloqueo.md) |
| **9** | Memoria principal: base y límite, enlace de direcciones, MMU, carga y enlace dinámico, asignación contigua, fragmentación, **paginación** | [06 · Memoria](../estudio/06-memoria.md) + [lo nuevo de los apuntes](apuntes-cap-9-y-10.md#capítulo-9-memoria-principal) |
| **10** | Memoria virtual: paginación por demanda, falla de página, **reemplazo FIFO, Óptimo y LRU**, Belady, asignación global y local | [07 · Memoria virtual](../estudio/07-memoria-virtual.md) + [lo nuevo de los apuntes](apuntes-cap-9-y-10.md#capítulo-10-memoria-virtual) |

Diapositivas: [Cap. 8](../Apuntes/Cap%208-2020%20%5BAutoguardado%5D.pdf) · [Cap. 9](../Apuntes/Cap%209%20Adm.%20Memoria.pdf) · [Cap. 10](../Apuntes/Cap%2010%202024.pdf)

> **No entra:** planificación de CPU ni sincronización (son de la P1 o del examen), ni **disco y FAT** (cap. 11 en adelante), aunque venían en las P2 2024-2 y 2025-2.
>
> Lee las [convenciones del profesor](../estudio/00-convenciones-del-profesor.md) secciones **2 (memoria)** y **3 (interbloqueo)**: la distribución proporcional, la "fragmentación acumulada", las entradas + salidas y "seguro / reversible / irreversible" **no son como en el libro**.

## Qué esperar

En las pruebas anteriores, lo que corresponde a estos capítulos se repartió así:

| Tipo de pregunta | Puntaje típico | Apareció en |
|---|---|---|
| **Paginación "RAM de X MB, procesos A, B, C"** (marcos, páginas, reparto, tipo, fallas, fragmentación, permanencia) | **30 a 40 pts** | P2 2024-2, P2 2025-2, Examen 2026-1, Recup. 2026-1 |
| **Banquero** (necesidad, estado seguro, solicitudes) | **20 a 35 pts** | P1 2009, 2013, 2022-2, Parcial 2024-2, Recup. 2024-2, Examen 2025-1, Examen 2026-1 |
| **Reemplazo de páginas** (FIFO, Óptimo, LRU con tiempo de fallas) | 10 a 30 pts | P2 2024-2, Examen 2025-1, P2 2025-2, Recup. 2026-1 |
| **Grafo de asignación** (ciclos, 4 condiciones, reducción) | 10 a 25 pts | Recup. 2024-2, Recup. 2026-1 |
| Fragmentación interna/externa, ¿cabe el programa?, base y límite | 15 a 20 pts | P2 2024-2, Recup. 2024-2, P1 2025-2, Recup. 2026-1 |
| Conceptos (falla de página, paginación por demanda, memoria virtual) | 10 a 25 pts | P2 2025-2, Examen 2025-1 |

**Conclusión:** banquero + procesos A, B, C + reemplazo de páginas suman **casi toda la prueba**. Son mecánicos: si los practicas hasta hacerlos sin dudar, tienes la mayor parte asegurada.

## Plan de estudio (7 sesiones)

| Sesión | Qué hacer | Material |
|---|---|---|
| 1 | Leer las diapositivas del cap. 8 y el [capítulo 05](../estudio/05-interbloqueo.md) completo. Hacer a mano el ejemplo de las diapositivas (P0 a P4, A = 10, B = 5, C = 7) | [05](../estudio/05-interbloqueo.md), [convenciones §3](../estudio/00-convenciones-del-profesor.md#3-interbloqueo-deadlock) |
| 2 | Banquero y grafos de nivel 1 y 2, comprobando con `banquero.py` y `grafo.py` | [ejercicios.md](ejercicios.md) |
| 3 | Leer las diapositivas del cap. 9, el [capítulo 06](../estudio/06-memoria.md) y la [parte del cap. 9 de los apuntes](apuntes-cap-9-y-10.md#capítulo-9-memoria-principal). Resolver la P2 2025-2 P4 (procesos A, B, C) **sin mirar** | [06](../estudio/06-memoria.md), [convenciones §2](../estudio/00-convenciones-del-profesor.md#2-memoria) |
| 4 | Leer las diapositivas del cap. 10, el [capítulo 07](../estudio/07-memoria-virtual.md) y la [parte del cap. 10 de los apuntes](apuntes-cap-9-y-10.md#capítulo-10-memoria-virtual). Resolver FIFO, Óptimo y LRU con la cadena de las diapositivas (15, 9 y 12 fallas) | [07](../estudio/07-memoria-virtual.md) |
| 5 | Ejercicios de nivel 3 y todas las [preguntas de concepto](preguntas-de-concepto.md) **sin mirar** las respuestas | [ejercicios.md](ejercicios.md) |
| 6 | Hacer el **ensayo con reloj (90 min)** y corregirlo con la pauta | [ensayo.md](ensayo.md) → [pauta-ensayo.md](pauta-ensayo.md) |
| 7 | Repasar lo que fallaste. La noche antes: preguntas de concepto y el [formulario](../estudio/formulario.md) | [preguntas-de-concepto.md](preguntas-de-concepto.md) |

## Lo que debes saber (marca lo que ya dominas)

### Capítulo 8: Interbloqueo

- [ ] Modelo del sistema: tipos de recurso con instancias; solicitud → uso → liberación
- [ ] **Las 4 condiciones** (exclusión mutua, retención y espera, sin expropiación, espera circular)
- [ ] Leer un grafo `V = {(Pi,Rj); (Rj,Pi)}`: tabla "tiene / pide" e instancias libres
- [ ] Encontrar **todos los ciclos** y decidir: **seguro / inseguro reversible / inseguro irreversible**
- [ ] **Reducir el grafo** y separar interbloqueados de bloqueados por arrastre
- [ ] Prevención: cómo romper **cada** condición y su costo
- [ ] Prevención vs. evitación vs. detección vs. ignorar
- [ ] **Banquero:** Disponible, Necesidad = Máximo − Asignados, algoritmo de seguridad con *Work*
- [ ] Comprobar que *Work* final = **total**
- [ ] **Solicitud:** ≤ Necesidad (si no, error), ≤ Disponible (si no, espera), simular y revisar seguridad
- [ ] Recuperación: abortar procesos (criterios para elegir) o expropiar recursos
- [ ] Regla n(m − 1) + 1

### Capítulo 9: Memoria principal

- [ ] Registros **base y límite**: validar una dirección y traducirla (también en hexadecimal)
- [ ] Enlace en compilación, carga y ejecución; dirección lógica vs. física; MMU y registro de reubicación
- [ ] **Carga dinámica vs. enlace dinámico** (stub, bibliotecas compartidas)
- [ ] Particiones variables: **first, best y worst fit** con una lista de huecos
- [ ] Fragmentación **interna vs. externa**, regla del 50 %, compactación
- [ ] Paginación: dividir la dirección en **p y d** con m y n bits; traducir con la tabla de páginas
- [ ] Fragmentación interna de un proceso (lo que sobra en la última página)
- [ ] **Problema A, B, C:** marcos, páginas (hacia arriba), reparto proporcional (truncando), tipo de paginación, tiempo de fallas, **fragmentación acumulada**, permanencia
- [ ] Tamaño del **mapa de bits** de marcos libres

### Capítulo 10: Memoria virtual

- [ ] Ventajas de la memoria virtual; espacio de direcciones virtual (pila hacia abajo, bibliotecas compartidas)
- [ ] Paginación **por demanda vs. anticipada** (espacio vs. tiempo); demanda **pura**
- [ ] **Bit válido-inválido** y cuándo se produce una falla de página
- [ ] **Pasos de la falla de página** (versión corta y los 13 del peor caso)
- [ ] Tiempo efectivo de acceso con probabilidad de falla
- [ ] **FIFO, Óptimo y LRU** a mano: tabla de marcos, fallas y reemplazos
- [ ] **Tiempo de fallas = (fallas + reemplazos) × (acceso + transferencia)**, con la tabla de entradas y salidas
- [ ] Turnaround = tiempo de fallas + referencias × ejecución
- [ ] **Bit de modificación** y cómo cambia el tiempo
- [ ] **Anomalía de Belady**; LRU y Óptimo como algoritmos de pila
- [ ] Implementación de LRU con **contadores** o **pila**
- [ ] Reemplazo **global vs. local**

## Archivos de esta carpeta

| Archivo | Para qué |
|---|---|
| [apuntes-cap-9-y-10.md](apuntes-cap-9-y-10.md) | Lo que traen las diapositivas de los cap. 9 y 10 y no estaba en el material de estudio, con ejercicios cortos y autoevaluación |
| [ejercicios.md](ejercicios.md) | Todos los ejercicios de pruebas anteriores y de la guía **que entran**, por nivel, con enlace a la solución |
| [ensayo.md](ensayo.md) · [pauta](pauta-ensayo.md) | Ensayo al estilo del profesor (100 pts, 90 min): banquero, grafo, procesos A, B, C, FIFO/LRU y conceptos |
| [preguntas-de-concepto.md](preguntas-de-concepto.md) | 39 preguntas de concepto de los capítulos 8, 9 y 10, con la respuesta lista |

### Herramientas para comprobar

```bash
cd herramientas
python banquero.py          # edita los datos al final, o úsalo desde Python
python reemplazo.py lru 3 "2,3,2,1,5,2,4,5,3,2,5,2,0,4,2,3,1,4,3,2" 4 6
```

Para `grafo.py` y `memoria.py`, mira los ejemplos en [herramientas/README.md](../herramientas/README.md).
