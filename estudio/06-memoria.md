# 06 · Administración de memoria y paginación

> **Aparece en todas las segundas pruebas, exámenes y recuperativas** (2024-2, 2025-1, 2025-2, 2026-1). El problema estrella es el de "RAM de X MB y procesos A, B, C".
> Lee las [convenciones de memoria del profesor](00-convenciones-del-profesor.md#2-memoria): cambian el resultado.

## 1. Dirección lógica vs. física

- **Dirección lógica (virtual):** la que genera el programa (la CPU). Cada proceso "cree" que su memoria empieza en 0.
- **Dirección física:** la posición real en la RAM.
- La **MMU** (*Memory Management Unit*) traduce de lógica a física **en cada acceso**, por hardware.

### Cuándo se fija la dirección (*binding*)

| Momento | Cuándo pasa | Consecuencia |
|---|---|---|
| Compilación | Si se sabe de antemano dónde se cargará | Código absoluto; si cambia el lugar, hay que recompilar |
| Carga | El cargador ajusta las direcciones al cargar | No se puede mover una vez cargado |
| Ejecución | La MMU traduce en cada acceso | **Se puede mover el proceso** (swapping, paginación). Es lo que usan los SO modernos |

> **Examen 2025-1, pregunta 1:** un archivo ejecutable corresponde a *secciones de código de máquina que el cargador lleva a la memoria principal para ejecutarlas* (alternativa **C**).

## 2. Protección con registros base y límite

Cada proceso tiene dos registros:

- **Base:** dónde empieza su memoria física.
- **Límite:** cuánto puede usar.

Traducción: si `dirección lógica < límite`, entonces `física = base + lógica`. Si no, el hardware genera una **interrupción (trap) de protección** y el SO aborta el acceso. Cargar base y límite son **instrucciones privilegiadas**: solo el SO puede hacerlo, en **modo kernel**. Así, gracias al **modo dual**, un proceso de usuario no puede salirse de su espacio.

### P1 2025-2, Pregunta 3 (20 pts)

Base = 0x3000, Límite = 0x0C00 (3072 bytes). Dirección lógica 0x0B20, en modo usuario.

- **b) ¿Es válida?** 0x0B20 = 11·256 + 2·16 + 0 = **2848**, y 0x0C00 = 12·256 = **3072**. Como 2848 < 3072, **es válida**.
- **c) Dirección física** = 0x3000 + 0x0B20 = **0x3B20** (12288 + 2848 = 15136).

> **Hexadecimal a decimal:** 0x0B20 = 0·16³ + 11·16² + 2·16¹ + 0·16⁰. Las letras valen A = 10, B = 11, C = 12, D = 13, E = 14, F = 15.

## 3. Asignación contigua y fragmentación

En la asignación contigua, cada proceso ocupa **un solo bloque** continuo de RAM. Para elegir un hueco libre hay tres estrategias:

- **First fit:** el primero que alcance.
- **Best fit:** el más chico que alcance.
- **Worst fit:** el más grande.

| | Fragmentación **interna** | Fragmentación **externa** |
|---|---|---|
| Qué es | Espacio **dentro** de lo asignado que el proceso no usa | Huecos **entre** asignaciones; en total alcanzan, pero ninguno solo |
| Dónde aparece | Particiones fijas, **paginación** (en la última página) | Particiones variables, **segmentación** |
| Solución | Bloques más chicos | Compactación, o **paginación** |

> **Guía 43 c):** "espacio no ocupado *dentro de una partición* que no se puede reasignar" es la definición de **fragmentación interna**. Ojo: si el espacio estuviera **entre** particiones, sería externa.

## 4. Paginación

- La memoria física se divide en **marcos** (*frames*, "bloques") de tamaño fijo.
- El proceso se divide en **páginas** del mismo tamaño.
- Cada página puede ir en **cualquier** marco libre, así que no necesita estar contigua. Una **tabla de páginas** por proceso dice en qué marco está cada página.

$$\text{dirección lógica} = (\underbrace{p}_{\text{nº de página}},\ \underbrace{d}_{\text{desplazamiento}}) \quad\Rightarrow\quad \text{física} = \text{marco}(p)\cdot\text{tamaño} + d$$

**Propiedades clave:**

- **Fragmentación externa = 0.** Cualquier marco libre sirve. *(Examen 2025-1, pregunta 2: alternativa **C, "es cero"**.)*
- **Fragmentación interna:** solo en la **última página** de cada proceso, en promedio media página.
- Para saber qué marcos están libres se usa un **mapa de bits** (1 bit por marco) o una lista de marcos libres.

### 4.1 Traducción con bits (Guía, problema 40)

> Memoria física 256 MB; palabra de 4 bytes; direcciones virtuales de 32 bits = 22 bits de página + 10 de desplazamiento; **direccionamiento por palabra**.

| Pregunta | Cálculo | Respuesta |
|---|---|---|
| Tamaño de página | 2¹⁰ palabras × 4 B | **1024 palabras = 4 KB** |
| Espacio de direccionamiento | 2³² palabras × 4 B | **2³² palabras = 16 GB** |
| Nº de marcos | 256 MB / 4 KB = 2²⁸ / 2¹² | **2¹⁶ = 65.536 marcos** |
| Campo "nº de marco" en la tabla | log₂(65.536) | **16 bits** |

### 4.2 Tamaño del mapa de bits (P2 2024-2, iv)

Un bit por marco: 262.144 marcos → 262.144 bits / 8 = 32.768 bytes = **32 KB**.

---

## 5. El problema típico: "RAM de X MB, procesos A, B y C"

Aparece casi igual en P2 2024-2 (1.024 MB), P2 2025-2 (64 MB), Examen 2026-1 (64 MB), Recuperativa 2026-1 (1 GB) y en la guía (14 y 30).

**Enunciado (P2 2025-2):** RAM de 64 MB, bloques de 4096 bytes.
Proceso A: 3.601.333 **bits** · Proceso B: 18.000 **palabras** de 128 bytes · Proceso C: 256.000 **bytes**.

### Paso 1: marcos en la RAM

$$\frac{64 \cdot 1024 \cdot 1024}{4096} = \frac{67.108.864}{4096} = \mathbf{16.384 \text{ marcos}}$$

### Paso 2: páginas de cada proceso (pasa todo a **bytes** y redondea **hacia arriba**)

| Proceso | A bytes | / 4096 | Páginas |
|---|---|---|---|
| A | 3.601.333 bits / 8 = 450.166,625 B | 109,9 | **110** |
| B | 18.000 × 128 = 2.304.000 B | 562,5 | **563** |
| C | 256.000 B | 62,5 | **63** |
| | | Suma | **736** |

> Se redondea **hacia arriba**: aunque sobre un pedacito, ocupa una página entera.

### Paso 3: distribución proporcional de marcos (redondeando **hacia abajo**)

$$a_i = \left\lfloor \frac{p_i}{\sum p}\cdot m\right\rfloor$$

| Proceso | Cálculo | Marcos asignados |
|---|---|---|
| A | 110/736 × 16.384 = 2.448,7 | **2.448** |
| B | 563/736 × 16.384 = 12.532,9 | **12.532** |
| C | 63/736 × 16.384 = 1.402,4 | **1.402** |
| | Total | 16.382 ≤ 16.384 ✓ |

> **Comprueba siempre** que el total no se pase de los marcos de la RAM. Por eso se trunca.

### Paso 4: ¿qué tipo de paginación es?

Cada proceso recibió **más marcos que páginas** (A: 2.448 ≥ 110), así que todas sus páginas caben de una vez: es **paginación anticipada (por adelantado)**. Se cargan todas al inicio y **no hay víctimas** (nunca hay que reemplazar).

### Paso 5: tiempo de fallas del proceso A

Cada página produce **una** falla (se trae una vez desde disco):

$$T = 110 \times (\underbrace{3}_{\text{acceso}} + \underbrace{20}_{\text{transferencia}}) = 110 \times 23 = \mathbf{2.530\ ms}$$

### Paso 6: fragmentación interna acumulada de A (criterio de la pauta)

- Marcos asignados que A no usa: (2.448 − 110) × 4096 = 2.338 × 4096 = **9.576.448 B**.
- Lo que sobra en la última página: 110 × 4096 − 450.166,625 = 450.560 − 450.166,625 = **393,4 B**.
- **Total: 9.576.841 B ≈ 9,13 MB.**

> La pauta da 410 B en la última página porque redondea a 109,9 páginas antes de multiplicar. Lo exacto es 393 B. La diferencia es mínima, pero si quieres ser exacto, trabaja con los bytes.
>
> En el libro, la fragmentación interna sería **solo** los 393 B: los marcos no usados no cuentan, porque en la práctica nadie le asigna a un proceso más marcos de los que tiene. El profesor cuenta todo lo asignado y no usado.

### Paso 7: tiempo de permanencia de A

$$T = 110 \times \underbrace{100}_{\text{ejecución por página}} + 2.530 = \mathbf{13.530\ ms}$$

### Las variantes

| Prueba | RAM | Acceso + transf. | Ejec./pág. | Marcos de A | T fallas A | Permanencia A |
|---|---|---|---|---|---|---|
| P2 2024-2 | 1.024 MB → 262.144 marcos | 8 + 12 = 20 | — | 39.179 | 2.200 ms | — |
| P2 2025-2 | 64 MB → 16.384 | 3 + 20 = 23 | 100 | 2.448 | 2.530 ms | 13.530 ms |
| Examen 2026-1 | 64 MB → 16.384 | 8 + 12 = 20 | 60 | 2.448 | 2.200 ms | **8.800 ms** (la pauta dice 8.200: [error](00-convenciones-del-profesor.md#4-errores-conocidos-en-las-pautas)) |
| Recup. 2026-1 | 1 GB → 262.144 | 32 + 60 = 92 | — | 4.699 (A tiene 9 páginas) | 828 ms | — |
| Guía 14 | 64 MB → 16.384 | 8 + 12 = 20 | — | A: 1.026 pág., 2.314 marcos | 20.520 ms | — |
| Guía 30 | 32 MB, bloques 2048 → 16.384 | 22 + 40 = 62 | — | A: 283 pág., 1.733 marcos | 17.546 ms | — |

**Recuperativa 2026-1:** A = 33 KB = 33.792 B → 8,25 → **9** páginas; B = 128 KB → 32; C = 612 KB → 153; D = 1,2 MB = 1.258.291,2 B → 307,2 → **308**. Suma 502. Marcos: A 4.699, B 16.710, C 79.896, D 160.837 (total 262.142). Como todos tienen más marcos que páginas, es **paginación anticipada**.

> **P2 2024-2, i) "ubicación física":** dibuja la memoria física como una columna de marcos y los bloques de cada proceso uno tras otro: A en los marcos 0 a 39.178, B en 39.179 a 239.703 y C en 239.704 a 262.141. Al lado, la **tabla de páginas** de cada proceso (página → marco). Es lo que hace la pauta.

---

## 6. Otros ejercicios de memoria

### 6.1 P2 2024-2, Problema 1: ¿cabe el programa? (20 pts)

RAM de 64 KB con marcos de 512 B → 65.536 / 512 = **128 marcos**.

| Parte | Bytes | / 512 | Páginas |
|---|---|---|---|
| Código | 32.768 | 64 | **64** |
| Datos | 16.386 | 32,004 | **33** |
| Pila | 15.870 | 30,996 | **31** |
| | | Total | **128** |

128 páginas ≤ 128 marcos → **sí cabe, justo**. Cada parte se pagina **por separado**: los datos ocupan 2 bytes más que 32 páginas y necesitan una página extra.

### 6.2 Recuperativa 2024-2 y 2026-1: fragmentación interna y externa

Páginas de 2.048 B, memoria física de 8 MB → 8·1024·1024 / 2048 = **4.096 marcos**.

- **Proceso 1 (31.566 B):** 31.566 / 2.048 = 15,4, así que necesita **16 páginas**. Las 15 completas ocupan 30.720 B y en la 16 usa 31.566 − 30.720 = 846 B. **Fragmentación interna = 2.048 − 846 = 1.202 B.**
- **Proceso 2 (18.432 B):** 18.432 / 2.048 = **9 páginas exactas**. **Fragmentación interna = 0 B.**
- **Fragmentación externa: 0 para ambos**, porque la paginación no la produce.

### 6.3 Guía 33 / 37: ¿agregar un marco o reemplazar una página?

Que el administrador mire la **frecuencia de fallas de página** (*Page Fault Frequency*) o el **conjunto de trabajo** (*working set*) del proceso:

- Si la tasa de fallas es **alta**, el proceso está **expandiendo** su localidad y necesita más marcos: **agregar un marco**.
- Si la tasa es **baja**, está **cambiando** de localidad dentro de lo que ya tiene: **reemplazar** una de sus propias páginas (reemplazo local).

Se fijan un umbral superior y uno inferior de fallas por unidad de tiempo.

---

## 7. Segmentación (teoría)

En vez de páginas del mismo tamaño, el programa se divide en **segmentos lógicos** de tamaño variable: código, datos, pila, una función, etc. La dirección es `(segmento, desplazamiento)`. La tabla de segmentos tiene **base y límite** por segmento.

- Tiene **fragmentación externa** (tamaños variables) y **no tiene interna**.
- Es más natural para compartir y proteger (por ejemplo, el segmento de código como solo lectura).
- **Segmentación paginada:** cada segmento se pagina. Combina las ventajas de ambas.

## 8. Swapping

**Swapping:** sacar un proceso **completo** de la RAM al disco (*swap out*) y traerlo después (*swap in*). Si en vez de completo se intercambia **por partes** (páginas) a medida que se necesitan, es **paginación por demanda** *(Examen 2025-1, pregunta 5: alternativa **C**)*. Sigue en [07 · Memoria virtual](07-memoria-virtual.md).
