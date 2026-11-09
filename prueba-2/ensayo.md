# Ensayo de Prueba 2: Sistemas Operativos

> **Capítulos 8, 9 y 10** · 100 puntos · 90 minutos · Exigencia 60 %
>
> Hazla **con reloj y sin apuntes**, como si fuera la prueba real. Puedes usar calculadora. Después corrige con la [pauta](pauta-ensayo.md).
> Deja escrito el procedimiento: en las pautas, el puntaje está en el desarrollo, no solo en el resultado.

---

## Problema 1 (25 pts): Algoritmo del banquero

Un sistema tiene 5 procesos y 3 tipos de recurso, con **A = 8, B = 6 y C = 6** instancias en total. En el instante T₀:

| Proceso | Asignados (A B C) | Máximo (A B C) |
|---|---|---|
| P0 | 1 1 0 | 4 3 2 |
| P1 | 2 0 1 | 3 2 2 |
| P2 | 1 2 1 | 2 3 3 |
| P3 | 0 1 2 | 2 2 4 |
| P4 | 2 1 0 | 5 2 1 |

a) Calcule el vector **Disponible** y la matriz **Necesidad**. (5 pts)

b) ¿El sistema está en **estado seguro**? Justifique con el algoritmo de seguridad, mostrando el vector *Work* en cada paso. (8 pts)

c) ¿Qué procesos pueden ir **primero** en una secuencia segura? Explique por qué los demás no. (3 pts)

d) A partir de T₀, analice **por separado** cada una de estas solicitudes e indique si se conceden de inmediato: (9 pts)
   1. P3 pide (1, 0, 0)
   2. P0 pide (1, 0, 1)
   3. P4 pide (1, 0, 2)

---

## Problema 2 (15 pts): Grafo de asignación de recursos

Hay 4 tipos de recurso: **R1 y R3 tienen 1 instancia**, **R2 y R4 tienen 2 instancias**. El grafo es:

> V = { (R1,P1); (P1,R2); (R2,P2); (R2,P4); (P2,R3); (R3,P3); (P3,R1); (R4,P3); (R4,P4) }

`(Pi,Rj)` = Pi solicita Rj · `(Rj,Pi)` = una instancia de Rj está asignada a Pi.

a) Dibuje el grafo e indique **qué tiene y qué pide** cada proceso. (3 pts)

b) Encuentre los **ciclos**. Según la terminología del curso, ¿en qué estado está el sistema? ¿Hay interbloqueo? Justifique **reduciendo el grafo**. (6 pts)

c) Ahora **P4 solicita R3**. ¿Cambia la conclusión? Indique qué procesos quedan interbloqueados y revise las **cuatro condiciones** de Coffman en este caso. (6 pts)

---

## Problema 3 (25 pts): Paginación

Un sistema tiene una RAM de **128 MB** y bloques (marcos) de **8.192 bytes**. Se cargan tres procesos:

- **Proceso A:** 5.000.000 **bits**
- **Proceso B:** 40.000 **palabras** de 64 bytes
- **Proceso C:** 1,5 **MB**

El SO reparte **todos** los marcos entre los procesos en forma **proporcional** a su número de páginas.

i) ¿Cuántos marcos tiene la RAM? (2 pts)

ii) ¿Cuántas páginas tiene cada proceso? (5 pts)

iii) ¿Cuántos marcos se le asignan a cada proceso? Compruebe que no se exceda la RAM. (5 pts)

iv) ¿Qué tipo de paginación es (por demanda o anticipada)? ¿Habrá reemplazo de páginas? Justifique. (3 pts)

v) Si el tiempo de acceso al disco es **5 ms** y el de transferencia de una página es **15 ms**, ¿cuál es el **tiempo de fallas** del proceso A? (3 pts)

vi) Calcule la **fragmentación interna acumulada** del proceso A. ¿Cuánto sería según la definición del libro? (4 pts)

vii) Si cada página de A tarda **80 ms** en ejecutarse, ¿cuál es su **tiempo de permanencia**? (3 pts)

---

## Problema 4 (20 pts): Reemplazo de páginas

Un proceso tiene **3 marcos** asignados (al inicio, vacíos) y genera la cadena de referencias:

> 2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2, 0, 4, 2, 3, 1, 4, 3, 2

El tiempo de acceso al disco es **4 ms** y el de transferencia es **6 ms**.

a) Simule los algoritmos **FIFO** y **LRU**, marcando cada falla de página. (8 pts)

b) Para cada uno, indique el número de **fallas** y de **reemplazos**, y calcule el **tiempo de fallas** con la tabla *Página | Entradas | Salidas | Total*. (6 pts)

c) ¿Cuántas fallas tendría el algoritmo **Óptimo**? ¿Para qué sirve si no se puede implementar? (3 pts)

d) Si cada referencia tarda **15 ms** en ejecutarse, calcule el **turnaround** del proceso con **LRU**. (3 pts)

---

## Problema 5 (15 pts): Conceptos y cálculos cortos

a) Un sistema tiene direcciones lógicas de **16 bits** y páginas de **1 KB**. (5 pts)
   - ¿Cuántos bits son para el número de página y cuántos para el desplazamiento? ¿Cuántas páginas puede tener un proceso?
   - La tabla de páginas indica que la **página 6 está en el marco 9**. Traduzca la dirección lógica **0x1A3F** a dirección física (en decimal y en hexadecimal).

b) Hay huecos libres de **150 K, 450 K, 250 K, 300 K y 550 K** (en ese orden). Llegan, en orden, procesos de **220 K, 400 K, 130 K y 420 K**. Indique dónde queda cada proceso con **first fit**, **best fit** y **worst fit**. ¿Cuál aprovecha mejor la memoria en este caso? (6 pts)

c) En el problema 4, con LRU, suponga que de las páginas expulsadas **solo 4 estaban modificadas**. Explique para qué sirve el **bit de modificación** y recalcule el tiempo de fallas. (4 pts)
