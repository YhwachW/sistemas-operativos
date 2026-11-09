# Pauta del ensayo de Prueba 2

> Los resultados se verificaron con [`banquero.py`](../herramientas/banquero.py), [`grafo.py`](../herramientas/grafo.py), [`memoria.py`](../herramientas/memoria.py) y [`reemplazo.py`](../herramientas/reemplazo.py). Corrige con honestidad: si te faltó la justificación, no te des el puntaje completo.

## Problema 1 (25 pts): banquero

### a) Disponible y Necesidad (5 pts)

Suma de asignados = (1+2+1+0+2, 1+0+2+1+1, 0+1+1+2+0) = **(6, 5, 4)**.
**Disponible** = Total − Asignados = (8, 6, 6) − (6, 5, 4) = **(2, 1, 2)**.

**Necesidad = Máximo − Asignados:**

| Proceso | Necesidad (A B C) |
|---|---|
| P0 | 3 2 2 |
| P1 | 1 2 1 |
| P2 | 1 1 2 |
| P3 | 2 1 2 |
| P4 | 3 1 1 |

> Error típico: usar la matriz de **Máximo** en vez de la de **Necesidad** al comparar con *Work*.

### b) Algoritmo de seguridad (8 pts)

| Paso | Proceso | Necesidad ≤ Work | Work después (= Work + Asignados) |
|---|---|---|---|
| — | — | — | (2, 1, 2) |
| 1 | **P2** | (1,1,2) ≤ (2,1,2) ✓ | (3, 3, 3) |
| 2 | **P3** | (2,1,2) ≤ (3,3,3) ✓ | (3, 4, 5) |
| 3 | **P4** | (3,1,1) ≤ (3,4,5) ✓ | (5, 5, 5) |
| 4 | **P0** | (3,2,2) ≤ (5,5,5) ✓ | (6, 6, 5) |
| 5 | **P1** | (1,2,1) ≤ (6,6,5) ✓ | (8, 6, 6) = Total ✓ |

**Estado seguro.** Secuencia segura: **⟨P2, P3, P4, P0, P1⟩**.

> **Comprobación:** al final, *Work* tiene que ser igual al **total** de recursos. Si no, sumaste mal.
>
> Hay **36** secuencias seguras en total (todas empiezan con P2 o P3). Cualquiera que esté bien justificada vale.

### c) ¿Quién puede ir primero? (3 pts)

Con Disponible = (2, 1, 2):

- **P2** (1,1,2) ✓ y **P3** (2,1,2) ✓ **pueden** ir primero.
- P0 (3,2,2): le faltan A y B. P1 (1,2,1): le falta B (pide 2 y hay 1). P4 (3,1,1): le falta A (pide 3 y hay 2).

### d) Solicitudes (9 pts, 3 c/u)

Para cada solicitud se revisa: **(1)** Solicitud ≤ Necesidad, **(2)** Solicitud ≤ Disponible y **(3)** se simula la asignación y se corre el algoritmo de seguridad.

**1. P3 pide (1, 0, 0) → SE CONCEDE.**
(1) (1,0,0) ≤ (2,1,2) ✓. (2) (1,0,0) ≤ (2,1,2) ✓.
(3) Nuevo estado: Disponible = **(1, 1, 2)**, Asignados P3 = (1,1,2), Necesidad P3 = (1,1,2).
Secuencia: P2 (1,1,2) ≤ (1,1,2) ✓ → (2,3,3); P3 (1,1,2) ✓ → (3,4,5); P4 ✓ → (5,5,5); P0 ✓ → (6,6,5); P1 ✓ → (8,6,6). **Seguro.**

**2. P0 pide (1, 0, 1) → NO se concede (P0 espera).**
(1) (1,0,1) ≤ (3,2,2) ✓. (2) (1,0,1) ≤ (2,1,2) ✓.
(3) Nuevo estado: Disponible = **(1, 1, 1)**. Necesidades: P0 (2,2,1), P1 (1,2,1), P2 (1,1,2), P3 (2,1,2), P4 (3,1,1).
**Ninguno** cabe en (1,1,1): a P1 le falta B; a P2, C; a P3, A y C; a P0 y P4, A. **Inseguro**, así que se rechaza y se restaura el estado anterior.

> Ojo: que la solicitud **quepa** en Disponible no basta. Hay que simular y correr la seguridad.

**3. P4 pide (1, 0, 2) → ERROR: excede su máximo declarado.**
(1) La necesidad de P4 es (3, 1, **1**) y pide **2** de C: Solicitud > Necesidad. El proceso pide más de lo que declaró como máximo; **ni siquiera se evalúa** la seguridad.

---

## Problema 2 (15 pts): grafo

### a) Tabla del grafo (3 pts)

| Proceso | Tiene | Pide |
|---|---|---|
| P1 | R1 | R2 |
| P2 | 1 de R2 | R3 |
| P3 | R3, 1 de R4 | R1 |
| P4 | 1 de R2, 1 de R4 | — |

| Recurso | Instancias | Asignadas | Libres |
|---|---|---|---|
| R1 | 1 | 1 (P1) | 0 |
| R2 | 2 | 2 (P2, P4) | 0 |
| R3 | 1 | 1 (P3) | 0 |
| R4 | 2 | 2 (P3, P4) | 0 |

### b) Ciclos y estado (6 pts)

**Ciclo:** P1 → R2 → P2 → R3 → P3 → R1 → P1.
Pasa por **R2, que tiene 2 instancias**, así que según el curso es un **estado inseguro reversible**: *puede* haber interbloqueo, pero hay que reducir el grafo.

**Reducción:**

| Paso | Quién termina | Por qué | Libera |
|---|---|---|---|
| 1 | **P4** | No pide nada | 1 de R2, 1 de R4 |
| 2 | **P1** | Pide R2, y ahora hay 1 libre | R1, R2 |
| 3 | **P3** | Pide R1, ahora libre | R3, R4 |
| 4 | **P2** | Pide R3, ahora libre | R2 |

**Todos terminan: NO hay interbloqueo.** La otra instancia de R2 la tiene **P4**, que está fuera del ciclo; al terminar, rompe la espera circular. Secuencia de término: P4, P1, P3, P2.

### c) P4 pide R3 (6 pts)

Aparece un segundo ciclo: **P1 → R2 → P4 → R3 → P3 → R1 → P1** (además del anterior).
Ahora **nadie** puede empezar la reducción: P1 espera R2 (las dos instancias están en P2 y P4), P2 y P4 esperan R3 (lo tiene P3) y P3 espera R1 (lo tiene P1). **No hay instancias libres de nada.**

**Interbloqueo: P1, P2, P3 y P4 quedan interbloqueados** (todos están en algún ciclo; no hay bloqueados por arrastre). En la terminología del curso: **inseguro irreversible**.

Las cuatro condiciones:

| Condición | En este caso |
|---|---|
| Exclusión mutua | Cada instancia está asignada a un solo proceso |
| Retención y espera | Los 4 procesos tienen al menos un recurso y piden otro |
| Sin expropiación | El SO no le quita los recursos a nadie |
| Espera circular | P1 → P4 (por R2) → P3 (por R3) → P1 (por R1) |

> **Lección:** un ciclo con recursos de varias instancias **no** basta para decir que hay deadlock (parte b), pero **tampoco** asegura que no lo haya (parte c). Lo que decide es la **reducción**.

---

## Problema 3 (25 pts): paginación

### i) Marcos de la RAM (2 pts)

$$\frac{128 \cdot 1024 \cdot 1024}{8192} = \frac{134.217.728}{8.192} = \mathbf{16.384 \text{ marcos}}$$

### ii) Páginas (5 pts)

Todo a **bytes** y se redondea **hacia arriba**:

| Proceso | Bytes | / 8.192 | Páginas |
|---|---|---|---|
| A | 5.000.000 / 8 = 625.000 | 76,29 | **77** |
| B | 40.000 × 64 = 2.560.000 | 312,5 | **313** |
| C | 1,5 × 1.048.576 = 1.572.864 | 192 exacto | **192** |
| | | Suma | **582** |

### iii) Marcos asignados (5 pts)

$a_i = \lfloor p_i / 582 \cdot 16.384 \rfloor$ (se **trunca**):

| Proceso | Cálculo | Marcos |
|---|---|---|
| A | 77/582 × 16.384 = 2.167,6 | **2.167** |
| B | 313/582 × 16.384 = 8.811,3 | **8.811** |
| C | 192/582 × 16.384 = 5.405,0 | **5.405** |
| | Total | 16.383 ≤ 16.384 ✓ (sobra 1 marco) |

### iv) Tipo de paginación (3 pts)

Cada proceso recibe **más marcos que páginas** (A: 2.167 ≥ 77; B: 8.811 ≥ 313; C: 5.405 ≥ 192). Todas las páginas caben a la vez, así que es **paginación anticipada (por adelantado)**: se cargan todas al comienzo y **no hay reemplazo** (no hay víctimas).

### v) Tiempo de fallas de A (3 pts)

Una falla por página: **77 × (5 + 15) = 1.540 ms**.

### vi) Fragmentación interna acumulada de A (4 pts)

- Marcos asignados sin usar: (2.167 − 77) × 8.192 = 2.090 × 8.192 = **17.121.280 B**.
- Sobra en la última página: 77 × 8.192 − 625.000 = 630.784 − 625.000 = **5.784 B**.
- **Total (criterio de la pauta): 17.127.064 B ≈ 16,33 MB.**

Según el **libro**, la fragmentación interna de paginación es solo lo que sobra en la última página: **5.784 B**.

### vii) Permanencia de A (3 pts)

**77 × 80 + 1.540 = 6.160 + 1.540 = 7.700 ms.**

---

## Problema 4 (20 pts): reemplazo de páginas

### a) Simulaciones (8 pts)

**FIFO** (sale la que **entró** hace más tiempo):

```
Ref.    2 3 2 1 5 2 4 5 3 2 5 2 0 4 2 3 1 4 3 2
Marco1  2 2 2 2 5 5 5 5 3 3 3 3 0 0 0 0 1 1 1 1
Marco2    3 3 3 3 2 2 2 2 2 5 5 5 4 4 4 4 4 4 2
Marco3        1 1 1 4 4 4 4 4 2 2 2 2 3 3 3 3 3
Falla   * *   * * * *   *   * * * *   * *     *
```

**LRU** (sale la que hace más tiempo que **no se usa**):

```
Ref.    2 3 2 1 5 2 4 5 3 2 5 2 0 4 2 3 1 4 3 2
Marco1  2 2 2 2 2 2 2 2 3 3 3 3 0 0 0 3 3 3 3 3
Marco2    3 3 3 5 5 5 5 5 5 5 5 5 4 4 4 1 1 1 2
Marco3        1 1 1 4 4 4 2 2 2 2 2 2 2 2 4 4 4
Falla   * *   * *   *   * *     * *   * * *   *
```

Ejemplo de decisión LRU: al llegar el **5** (5ª referencia), los marcos tienen 2, 3, 1. Mirando hacia atrás, el 2 se usó en la ref. 3, el 1 en la 4 y el **3 en la 2**: es el menos usado recientemente y sale.

### b) Fallas y tiempo (6 pts)

| | Fallas | Reemplazos | Entradas + salidas | Tiempo = total × (4 + 6) |
|---|---|---|---|---|
| FIFO | **14** | **11** | 25 | **250 ms** |
| LRU | **13** | **10** | 23 | **230 ms** |

Tabla de LRU (entradas = veces que la página entra; salidas = veces que sale como víctima):

| Página | Entradas | Salidas | Total |
|---|---|---|---|
| 0 | 1 | 1 | 2 |
| 1 | 2 | 2 | 4 |
| 2 | 3 | 2 | 5 |
| 3 | 3 | 2 | 5 |
| 4 | 3 | 2 | 5 |
| 5 | 1 | 1 | 2 |
| **Total** | **13** | **10** | **23** |

> **Comprobación:** reemplazos = fallas − marcos (las 3 primeras fallas llenan marcos vacíos): 13 − 3 = 10 ✓.

### c) Óptimo (3 pts)

**10 fallas** (7 reemplazos, 170 ms). Es el mínimo posible: ningún algoritmo puede tener menos fallas con 3 marcos. No se puede implementar porque requiere **conocer el futuro**, pero sirve como **referencia** para medir qué tan buenos son los otros (LRU queda a 3 fallas del óptimo y FIFO, a 4).

### d) Turnaround con LRU (3 pts)

**230 + 20 × 15 = 230 + 300 = 530 ms.**

---

## Problema 5 (15 pts)

### a) Traducción de direcciones (5 pts)

- 1 KB = 2¹⁰ B → **desplazamiento d = 10 bits**; número de página **p = 16 − 10 = 6 bits** → **2⁶ = 64 páginas**.
- 0x1A3F = 1·4096 + 10·256 + 3·16 + 15 = **6.719**.
  - p = ⌊6.719 / 1.024⌋ = **6**; d = 6.719 − 6·1.024 = **575**.
  - Página 6 → marco 9: física = 9 · 1.024 + 575 = **9.791 = 0x263F**.

> **Atajo en binario:** 0x1A3F = `0001 10|10 0011 1111`. Los 6 bits de arriba son `000110` = 6; los 10 de abajo son el desplazamiento. Se cambian los 6 bits de arriba por el marco 9 = `001001`: `0010 0110 0011 1111` = **0x263F**.

### b) First, best y worst fit (6 pts)

Huecos: 150, 450, 250, 300, 550 (K).

| Proceso | First fit | Best fit | Worst fit |
|---|---|---|---|
| 220 K | 450 → queda 230 | 250 → queda 30 | 550 → queda 330 |
| 400 K | 550 → queda 150 | 450 → queda 50 | 450 → queda 50 |
| 130 K | 150 → queda 20 | 150 → queda 20 | 330 → queda 200 |
| 420 K | **No cabe** (huecos 20, 230, 250, 300, 150): espera | 550 → queda 130 | **No cabe** (huecos 150, 50, 250, 300, 200): espera |

**Best fit** es el único que ubica los 4 procesos. Fíjate en first y worst fit: queda memoria libre de sobra **en total** (950 K y 950 K), pero ningún hueco **solo** alcanza para 420 K. Eso es **fragmentación externa**.

### c) Bit de modificación (4 pts)

Cada marco tiene un **bit de modificación** (*dirty bit*) que el hardware pone en 1 cuando se escribe en la página. Al elegir una víctima:

- si el bit es **1**, la página cambió y hay que **escribirla en disco** (una salida);
- si es **0**, la copia del disco sigue igual y el marco **se sobrescribe sin escribir nada**.

Así se ahorran escrituras. Con LRU: 13 entradas + **4** salidas = 17 → **17 × 10 = 170 ms** (en vez de 230 ms).
