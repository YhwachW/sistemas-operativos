# Lo nuevo de los apuntes de los capítulos 9 y 10

> Los temas de memoria ya están explicados en [06 · Memoria y paginación](../estudio/06-memoria.md) y [07 · Memoria virtual](../estudio/07-memoria-virtual.md). Esta página agrega **lo que aparece en las diapositivas del curso** ([Cap. 9](../Apuntes/Cap%209%20Adm.%20Memoria.pdf) y [Cap. 10](../Apuntes/Cap%2010%202024.pdf)) y no estaba explicado, con ejercicios cortos para practicar.
>
> Ojo con el alcance: las diapositivas del cap. 9 llegan hasta **paginación básica** (no traen TLB, tablas jerárquicas ni segmentación), y las del cap. 10, hasta **asignación global y local** (no traen *thrashing* ni *working set*). Eso último igual está en [07 §6](../estudio/07-memoria-virtual.md#6-asignación-de-marcos-hiperpaginación-y-conjunto-de-trabajo) por si el profesor lo pregunta.

---

## Capítulo 9: Memoria principal

### 1. Por qué hay que proteger la memoria

La CPU solo puede acceder **directamente** a los registros y a la memoria principal. Un registro se lee en un ciclo; la memoria puede tardar muchos ciclos, y por eso hay una **caché** entre ambas.

Cada proceso debe acceder **solo a su espacio de direcciones**. El hardware lo garantiza con los registros **base y límite**: la CPU compara **cada** dirección generada en modo usuario y, si se sale, genera un *trap*. Cargar esos registros es una **instrucción privilegiada**. → [06 §2](../estudio/06-memoria.md#2-protección-con-registros-base-y-límite)

### 2. Enlace (*binding*) de direcciones

Una dirección cambia de forma a lo largo de la vida del programa:

| Etapa | Cómo se ve la dirección | Ejemplo |
|---|---|---|
| Código fuente | **Simbólica** | la variable `contador` |
| Compilado | **Reubicable** | "14 bytes desde el comienzo de este módulo" |
| Enlazado / cargado | **Absoluta** | 74014 |

El enlace puede hacerse al **compilar** (código absoluto), al **cargar** (código reubicable) o al **ejecutar** (el proceso puede moverse; necesita hardware: la MMU). → [06 §1](../estudio/06-memoria.md#cuándo-se-fija-la-dirección-binding)

> **Lógica = física** cuando el enlace es en compilación o en carga. **Lógica ≠ física** solo cuando es en tiempo de ejecución.

### 3. La MMU y el registro de reubicación

La **MMU** es el hardware que, en tiempo de ejecución, traduce direcciones lógicas a físicas. En el esquema más simple, el registro base se llama **registro de reubicación** y su valor **se suma a cada dirección** que genera el proceso:

$$\text{física} = \text{reubicación} + \text{lógica} \qquad (\text{si lógica} < \text{límite})$$

El programa **nunca ve** las direcciones físicas: trabaja solo con direcciones lógicas desde 0.

**Ejercicio:** reubicación = 14.000, límite = 3.500. ¿Qué pasa con las direcciones lógicas 346 y 3.800?
→ 346 < 3.500: física **14.346**. 3.800 ≥ 3.500: **trap** (error de direccionamiento), el SO aborta el acceso.

### 4. Carga dinámica vs. enlace dinámico

Se confunden fácilmente; en una pregunta de concepto hay que distinguirlos.

| | **Carga dinámica** | **Enlace dinámico** |
|---|---|---|
| Qué es | Una rutina **no se carga en memoria hasta que se llama** | El **enlace** con una biblioteca se pospone hasta la ejecución |
| Cómo funciona | Las rutinas están en disco en formato reubicable; se cargan cuando se usan | En el programa queda un **stub** (código auxiliar) que busca la rutina de la biblioteca en memoria, se reemplaza por su dirección y la ejecuta |
| Ventaja | Las rutinas que no se usan **nunca se cargan** (útil para código de casos raros, como el manejo de errores) | Las bibliotecas se **comparten** entre procesos (**bibliotecas compartidas**, DLL en Windows) y se pueden actualizar sin volver a enlazar el programa |
| ¿Necesita al SO? | **No**: lo hace el diseño del programa (el SO puede dar bibliotecas de ayuda) | **Sí**: el SO comprueba si la rutina ya está en memoria y la agrega al espacio de direcciones del proceso |

En el **enlace estático**, en cambio, las bibliotecas se copian dentro del ejecutable: cada programa lleva su propia copia.

> Si se actualiza una biblioteca compartida, puede haber programas que esperan la versión anterior. Por eso se **versionan**.

### 5. Asignación contigua y particiones variables

- La memoria se divide en dos: el **SO en la memoria baja** (junto al vector de interrupciones) y los **procesos de usuario en la alta**.
- Con **particiones variables**, cada proceso recibe un bloque de su tamaño. Al terminar, deja un **hueco**, y los huecos adyacentes **se juntan**.
- El SO mantiene una lista de **particiones asignadas** y de **particiones libres (huecos)**.
- El **grado de multiprogramación** queda limitado por la cantidad de particiones.

**First fit, best fit y worst fit:** elegir el primer hueco que sirva, el más chico que sirva o el más grande. First fit y best fit son mejores que worst fit **en velocidad y en uso de memoria**. Best fit y worst fit deben recorrer **toda** la lista (salvo que esté ordenada por tamaño).

**Ejercicio (Silberschatz 9.x):** huecos de 100, 500, 200, 300 y 600 K; llegan procesos de 212, 417, 112 y 426 K.

| Proceso | First fit | Best fit | Worst fit |
|---|---|---|---|
| 212 K | 500 (queda 288) | 300 (queda 88) | 600 (queda 388) |
| 417 K | 600 (queda 183) | 500 (queda 83) | 500 (queda 83) |
| 112 K | 288 (queda 176) | 200 (queda 88) | 388 (queda 276) |
| 426 K | **espera** | 600 (queda 174) | **espera** |

Best fit es el único que ubica a los cuatro. Otro ejercicio igual está en el [ensayo, problema 5 b](ensayo.md#problema-5-15-pts-conceptos-y-cálculos-cortos).

### 6. Fragmentación, regla del 50 % y compactación

- **Externa:** hay memoria libre suficiente **en total**, pero **no es contigua**.
- **Interna:** el bloque asignado es un poco más grande que lo pedido, y la diferencia queda sin usar **dentro** del bloque.
- **Regla del 50 %:** el análisis estadístico de first fit muestra que, por cada **N** bloques asignados, se pierden **0,5 N** por fragmentación externa. Es decir, **un tercio** de la memoria puede quedar inutilizable.
- **Compactación:** mover los procesos para juntar todos los huecos en uno grande.
  - Solo es posible si la reubicación es **dinámica** (enlace en tiempo de ejecución).
  - Problema con la E/S: un proceso que hace E/S a su buffer no se puede mover. Se soluciona **bloqueándolo** mientras hace E/S, o haciendo la E/S **solo a buffers del SO**.
  - El **almacenamiento de respaldo** (disco de intercambio) tiene el mismo problema de fragmentación.

### 7. Paginación: la dirección en bits

Si el espacio lógico tiene **2ᵐ** direcciones y la página tiene **2ⁿ** bytes:

```
| número de página p  | desplazamiento d |
|      m − n bits     |      n bits      |
```

- **p** se usa como índice en la tabla de páginas, que da el **marco** donde está esa página.
- **d** se copia tal cual: física = marco · 2ⁿ + d.
- El tamaño de página es **potencia de 2**, normalmente entre **512 B y 16 MB**. Así la división por el tamaño es solo "cortar bits".

**Ejemplo de los apuntes:** m = 4, n = 2 (páginas de 4 B, memoria física de 32 B = 8 marcos). La tabla de páginas es 0 → 5, 1 → 6, 2 → 1, 3 → 2.

| Lógica | p, d | Marco | Física |
|---|---|---|---|
| 0 | 0, 0 | 5 | 5 · 4 + 0 = **20** |
| 3 | 0, 3 | 5 | 20 + 3 = **23** |
| 4 | 1, 0 | 6 | **24** |
| 13 | 3, 1 | 2 | 2 · 4 + 1 = **9** |

> Más ejercicios de traducción: [06 §4.1](../estudio/06-memoria.md#41-traducción-con-bits-guía-problema-40) (guía 40) y [ensayo, problema 5 a](ensayo.md#problema-5-15-pts-conceptos-y-cálculos-cortos).

### 8. Fragmentación interna en paginación (ejemplo de los apuntes)

Página de 2.048 B y proceso de 72.766 B → 72.766 / 2.048 = 35,53, así que son **35 páginas completas + 1.086 B** y necesita **36 marcos**.
**Fragmentación interna = 2.048 − 1.086 = 962 B.**

- **Peor caso:** 1 marco − 1 byte (el proceso usa 1 solo byte de la última página).
- **En promedio:** **media página** por proceso.
- **¿Conviene una página chica?** Hay menos fragmentación interna, pero **más entradas en la tabla de páginas** (más memoria para la tabla) y más E/S por byte. Por eso se usan páginas medianas, y algunos sistemas soportan dos tamaños (Solaris: 8 KB y 4 MB).

### 9. Marcos libres

El SO lleva un registro de **todos los marcos libres**. Para ejecutar un proceso de **N páginas** necesita encontrar **N marcos libres** (no importa si están separados), cargarlo y armar su tabla de páginas.

---

## Capítulo 10: Memoria virtual

### 10. Para qué sirve (la lista de los apuntes)

Rara vez se usa el programa completo (código de errores, rutinas poco comunes, arreglos sobredimensionados). Si se puede ejecutar un programa **cargado en parte**:

1. El programa **no está limitado** por el tamaño de la memoria física.
2. Cada programa ocupa menos memoria: **corren más programas a la vez**, y sube el uso de la CPU y el rendimiento **sin empeorar** el tiempo de respuesta ni el de permanencia.
3. Se necesita **menos E/S** para cargar o intercambiar programas, así que cada uno corre más rápido.
4. Varios procesos pueden **compartir** espacio de direcciones (bibliotecas, memoria compartida) y la **creación de procesos es más eficiente**.

La memoria virtual se implementa con **paginación por demanda** o **segmentación por demanda**.

### 11. El espacio de direcciones virtual

- La **pila** empieza en la dirección lógica **máxima** y crece **hacia abajo**; el *heap* y los datos crecen **hacia arriba**.
- El espacio entre ambos es un **hueco** que no ocupa memoria física hasta que alguno crezca hasta una página nueva (**espacio de direcciones disperso**).
- Las **bibliotecas compartidas** se mapean en el espacio virtual de cada proceso, pero existen **una sola vez** en la memoria física.
- Con `fork()` el hijo puede **compartir** las páginas del padre en vez de copiarlas, y por eso crear un proceso es más rápido.

### 12. Paginación por demanda: vocabulario

| Término | Significado |
|---|---|
| **Lazy swapper** (intercambiador perezoso) | Nunca trae una página a memoria si no se necesita. Al que trabaja con páginas se le llama **paginador** (busca página) |
| **Bit válido-inválido** | Cada entrada de la tabla de páginas: **v** = está en memoria; **i** = no está (o no es legal). Al inicio, todas en **i** |
| **Falla de página** | La MMU encuentra el bit en **i** al traducir y genera un *trap* al SO |
| **Paginación por demanda pura** | El proceso empieza **sin ninguna página** en memoria: la primera instrucción ya produce una falla, y cada página falla en su primer acceso |
| **Relleno con ceros bajo demanda** (*zero-fill-on-demand*) | Antes de entregar un marco libre, el SO lo **llena de ceros**, para que un proceso no vea los datos del anterior |
| **Lista de marcos libres** | Los marcos disponibles para atender fallas. Puede ser una lista o un **vector de bits** (1 = usado, 0 = libre). Al encender el sistema, toda la memoria está en la lista |

**Hardware que necesita la paginación por demanda:** (1) tabla de páginas con **bit válido-inválido**, (2) **memoria secundaria** (dispositivo de intercambio con espacio de *swap*) y (3) la posibilidad de **reiniciar instrucciones**.

### 13. Reinicio de instrucciones

Después de una falla, la instrucción se **vuelve a ejecutar desde el principio**. Una sola instrucción puede fallar en **varias** páginas (por ejemplo, `ADD A, B, C` con los tres operandos en memoria: puede fallar al traer la instrucción, al leer A, al leer B o al escribir C).

El caso difícil son las instrucciones que **mueven un bloque** de memoria (o que auto-incrementan registros): si fallan a la mitad, ya modificaron parte del destino. Si el origen y el destino **se superponen**, reiniciar desde cero daría un resultado incorrecto. Soluciones: comprobar **antes** de empezar que todas las páginas estén en memoria, o guardar los valores originales en registros temporales para deshacer.

### 14. Falla de página: los 13 pasos del peor caso

La versión corta (7 pasos) está en [07 §3](../estudio/07-memoria-virtual.md#3-rutina-de-falla-de-página-p2-2025-2-pregunta-1-10-pts). Los apuntes traen la versión **completa**, que muestra **por qué una falla es tan cara**:

1. *Trap* al sistema operativo.
2. Guardar los registros y el estado del proceso.
3. Determinar que la interrupción fue una **falla de página**.
4. Verificar que la referencia sea **legal** y ubicar la página **en el disco**.
5. Leer del disco a un marco libre:
   - esperar en la cola del dispositivo,
   - esperar la búsqueda y la latencia (**tiempo de acceso**),
   - transferir la página al marco (**tiempo de transferencia**).
6. **Mientras espera, darle la CPU a otro proceso.**
7. Recibir la interrupción del disco (E/S terminada).
8. Guardar los registros del **otro** proceso.
9. Determinar que la interrupción vino del disco.
10. Corregir la tabla de páginas: la página ya está en memoria (bit **v**).
11. Esperar a que la CPU vuelva a asignarse a este proceso.
12. Restaurar los registros, el estado y la tabla de páginas.
13. **Reanudar la instrucción** interrumpida.

> El paso 5 explica la fórmula de las pautas: cada página que **entra** cuesta *acceso + transferencia*, y cada víctima modificada que **sale** cuesta lo mismo.

**Tiempo efectivo de acceso** (TEA), con *p* = probabilidad de falla:

$$TEA = (1-p)\cdot t_{mem} + p\cdot t_{falla}$$

*Ejemplo:* t_mem = 200 ns y t_falla = 8 ms = 8.000.000 ns. Con p = 1/1.000: TEA = 0,999 · 200 + 0,001 · 8.000.000 ≈ **8.200 ns**: ¡**41 veces** más lento! Para que la degradación sea menor al 10 % (TEA < 220 ns): 200 + 7.999.800 p < 220 → **p < 0,0000025** (menos de 1 falla cada 400.000 accesos).

### 15. Reemplazo de páginas y bit de modificación

Si no hay marco libre, se elige una **víctima**. Pasos del reemplazo básico:

1. Encontrar la página pedida **en el disco**.
2. Encontrar un marco libre; si no hay, usar el **algoritmo de reemplazo** para elegir un marco víctima y **escribirlo en disco solo si fue modificado**.
3. Traer la página al marco liberado y actualizar las tablas.
4. Reiniciar la instrucción que causó el *trap*.

El **bit de modificación** (*dirty bit*) lo pone el hardware en 1 cuando se escribe en la página. Si la víctima tiene el bit en **0**, su copia en disco sigue igual y **no hay que escribirla**: la falla cuesta la mitad. Las pautas cuentan una salida **por cada reemplazo** (suponen que todas las víctimas están modificadas), salvo que el enunciado diga otra cosa.

El reemplazo es lo que permite ofrecer una **memoria virtual más grande que la física**.

### 16. Los tres algoritmos con la cadena de los apuntes

Cadena de las diapositivas (22 referencias): 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1, con 3 marcos:

| Algoritmo | Fallas | Comentario de los apuntes |
|---|---|---|
| FIFO | **15** | Se implementa con una cola. Sufre la **anomalía de Belady** |
| Óptimo | **9** | No se puede leer el futuro; sirve para **comparar** |
| LRU | **12** | Mejor que FIFO, peor que OPT. Bueno y muy usado; el problema es implementarlo |

> Compruébalo: `python herramientas/reemplazo.py fifo 3 "7,0,1,2,0,3,0,4,2,3,0,3,0,3,2,1,2,0,1,7,0,1"`.
>
> **Belady:** con 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5, FIFO tiene **9 fallas con 3 marcos y 10 con 4**: más marcos dan más fallas.

### 17. Cómo se implementa LRU

| Implementación | Cómo funciona | Costo |
|---|---|---|
| **Contadores** | Cada entrada de la tabla tiene un campo de "hora del último uso"; en cada referencia se copia el reloj. Para reemplazar, se **busca el menor** | Hay que **buscar** en toda la tabla y escribir en memoria en cada acceso |
| **Pila** | Una pila doblemente enlazada de números de página: cada página referenciada se **mueve al tope**. La víctima siempre está en el **fondo** | Cada actualización es más cara (**hasta 6 punteros** por cambio), pero **no hay que buscar** para reemplazar |

**Algoritmos de pila:** LRU y Óptimo cumplen que las páginas en memoria con *n* marcos son siempre un **subconjunto** de las que habría con *n + 1*. Por eso **nunca** tienen la anomalía de Belady. FIFO no es de pila.

### 18. Reemplazo global vs. local

| | **Global** | **Local** |
|---|---|---|
| De dónde sale la víctima | De **todos** los marcos: un proceso puede quitarle un marco a otro | Solo de los marcos **del propio proceso** |
| Ventaja | **Mayor rendimiento** total (es lo más común) | Rendimiento de cada proceso **más predecible** |
| Desventaja | El tiempo de ejecución de un proceso **varía mucho** (depende de lo que hagan los demás) | Puede quedar **memoria sin aprovechar** |

---

## Autoevaluación rápida

1. ¿En qué tipo de enlace las direcciones lógicas y físicas son distintas?
2. ¿Qué diferencia hay entre carga dinámica y enlace dinámico? ¿Cuál necesita ayuda del SO?
3. ¿Por qué la compactación exige reubicación dinámica?
4. Con direcciones de 32 bits y páginas de 4 KB, ¿cuántos bits tiene el desplazamiento y cuántas entradas tiene la tabla de páginas?
5. ¿Qué es la paginación por demanda pura?
6. ¿Para qué sirve el bit de modificación?
7. ¿Por qué LRU no sufre la anomalía de Belady y FIFO sí?
8. ¿Qué implementación de LRU no necesita buscar la víctima?

<details>
<summary>Respuestas</summary>

1. Solo en el enlace **en tiempo de ejecución** (con MMU).
2. Carga dinámica: la rutina se carga cuando se llama, sin ayuda del SO. Enlace dinámico: el enlace con la biblioteca se hace al ejecutar, mediante un *stub*; **necesita al SO** para compartir la biblioteca entre procesos.
3. Porque mover un proceso cambia sus direcciones físicas; si se fijaron al compilar o al cargar, el programa quedaría apuntando al lugar antiguo.
4. 4 KB = 2¹² → **12 bits** de desplazamiento y 20 de página → **2²⁰ = 1.048.576 entradas**.
5. Partir el proceso **sin ninguna página** en memoria: cada página falla en su primer uso.
6. Para no escribir en disco las víctimas que **no** se modificaron.
7. Porque es un **algoritmo de pila**: lo que hay en memoria con *n* marcos siempre está contenido en lo que habría con *n + 1*.
8. La de **pila** (la víctima está en el fondo).

</details>
