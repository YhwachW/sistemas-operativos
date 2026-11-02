# Formulario de una página

> Para tener a mano mientras practicas. Cada fórmula tiene el enlace a su explicación.

## Planificación de CPU → [03](03-planificacion-cpu.md)

| Qué | Fórmula |
|---|---|
| Turnaround (T.T., permanencia, retorno) | `fin − llegada` |
| Waiting (W.T.), definición del libro | `T.T. − ráfaga` |
| W.T. como en las pautas | `inicio del último tramo − llegada` ([¿por qué?](00-convenciones-del-profesor.md#14-tiempo-de-espera-wt-la-pauta-usa-inicio-del-último-tramo--llegada)) |
| Respuesta | `primer inicio − llegada` |
| Estimación SJF | $\tau_{n+1} = \alpha t_n + (1-\alpha)\tau_n$ |
| Espera máxima en RR | $(n-1)\cdot q$ |

**Reglas:** prioridad → **número menor gana**. SJF Preemptive → compara la ráfaga **restante**. RR → **por iteraciones en orden de llegada**.

## Interbloqueo → [05](05-interbloqueo.md)

| Qué | Fórmula |
|---|---|
| Necesidad | `Máximo − Asignados` |
| Disponible | `Total − Σ Asignados` |
| Paso del banquero | si `Necesidad[i] ≤ Disponible` → `Disponible += Asignados[i]` |
| Sin deadlock garantizado (n procesos, máx. m c/u) | instancias ≥ $n(m-1)+1$ |

**Grafo:** sin ciclo → seguro. Ciclo con recursos de 1 instancia → deadlock (inseguro **irreversible**). Ciclo con varias instancias → **reducir** el grafo (inseguro **reversible** si se destraba).

## Memoria → [06](06-memoria.md)

| Qué | Fórmula |
|---|---|
| Marcos en RAM | `RAM (bytes) / tamaño de bloque` |
| Páginas de un proceso | `⌈ tamaño en bytes / tamaño de página ⌉` (bits ÷ 8; palabras × tamaño de palabra) |
| Distribución proporcional | $a_i = \lfloor (p_i / \sum p) \cdot m \rfloor$ |
| Tiempo de fallas (anticipada) | `páginas × (acceso + transferencia)` |
| Fragmentación interna (pauta) | `(aᵢ − pᵢ) × bloque + (pᵢ × bloque − tamaño)` |
| Fragmentación interna (libro) | `pᵢ × bloque − tamaño` (solo la última página) |
| Permanencia del proceso | `páginas × ejec. por página + tiempo de fallas` |
| Base y límite | válida si `lógica < límite`; `física = base + lógica` |
| Dirección paginada | `física = marco(p) × tamaño + d` |
| Bits del desplazamiento | `log₂(tamaño de página)` |
| Mapa de bits | `nº de marcos / 8` bytes |

**Unidades:** 1 KB = 1.024 B · 1 MB = 1.024² B = 1.048.576 B · 1 GB = 1.024³ B = 1.073.741.824 B · 1 byte = 8 bits.

## Memoria virtual → [07](07-memoria-virtual.md)

| Qué | Fórmula |
|---|---|
| Reemplazos | `fallas − marcos` (cuando todos los marcos se llenan) |
| Tiempo en fallas (pauta) | `(fallas + reemplazos) × (acceso + transferencia)` |
| Turnaround del proceso | `tiempo en fallas + nº de referencias × ejec. por página` |
| Tiempo efectivo de acceso | $(1-p)\,t_{mem} + p\,t_{falla}$ |

**Víctima:** FIFO → la más antigua · Óptimo → la que se usa más tarde (o nunca) · LRU → la que hace más tiempo que no se usa.

## Disco → [08](08-disco-archivos-y-proteccion.md)

| Qué | Fórmula |
|---|---|
| Tiempo de acceso | búsqueda + rotación + transferencia |
| Capacidad | superficies × pistas × sectores × bytes por sector |
| Clusters de un archivo | `⌈ tamaño / cluster ⌉` |
| Tamaño de la FAT | `clusters × bytes por entrada` (redondeado al paquete) |
| Tiempo de transferencia | `tamaño / velocidad` (manda el más lento) |
| Recorrido del cabezal | suma de `|destino − origen|` de cada movimiento |
