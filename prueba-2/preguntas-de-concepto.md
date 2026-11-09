# Preguntas de concepto: capítulos 8, 9 y 10

> Respuestas listas para escribir en la prueba. Tápalas, contesta en voz alta o en papel, y después compara.
> Las que dicen *(prueba)* ya salieron en una prueba anterior.

## Capítulo 8: Interbloqueo

**1. ¿Qué es un interbloqueo (deadlock)?**
Un conjunto de procesos en el que **cada uno espera un recurso que tiene otro del mismo conjunto**, así que ninguno puede avanzar nunca. Cada proceso usa un recurso en el orden: **solicitud → uso → liberación**.

**2. Las 4 condiciones necesarias.** *(Recup. 2024-2)*
**Exclusión mutua** (el recurso lo usa uno a la vez), **retención y espera** (tiene uno y espera otro), **sin expropiación** (solo se libera voluntariamente) y **espera circular** (P0 espera a P1, …, Pn espera a P0). Deben darse **las cuatro a la vez**.

**3. Si el grafo tiene un ciclo, ¿hay deadlock?**
Depende. Si **todos** los recursos del ciclo tienen **1 instancia**: **sí** (inseguro irreversible). Si alguno tiene **varias**: **puede** que sí o que no (inseguro reversible); hay que **reducir** el grafo. **Sin ciclos, nunca hay deadlock** (estado seguro).

**4. ¿Qué es un estado seguro?**
Existe una **secuencia de todos los procesos** ⟨P1, …, Pn⟩ tal que lo que cada Pi aún puede pedir se puede satisfacer con lo disponible **más** lo que liberan todos los Pj anteriores. **Seguro → no hay deadlock. Inseguro → puede haberlo** (no es seguro que lo haya).

**5. Un estado inseguro podría ser causado por…** *(Examen 2025-1)*
**Los recursos escasos**: con pocos recursos disponibles, ningún proceso puede completar su necesidad.

**6. Cuatro formas de manejar el deadlock.**
**Prevención** (romper una condición), **evitación** (banquero: no entrar nunca a un estado inseguro), **detección y recuperación**, e **ignorarlo** (lo que hacen la mayoría de los SO).

**7. ¿Cómo se previene rompiendo cada condición?**
- **Exclusión mutua:** solo con recursos compartibles (archivos de solo lectura); con una impresora no se puede.
- **Retención y espera:** pedir **todo al inicio**, o pedir solo cuando no se tiene nada. Desventajas: baja utilización e **inanición**.
- **Sin expropiación:** si lo que pide no está disponible, **libera todo** lo que tiene y se reinicia cuando pueda obtener todo.
- **Espera circular:** **numerar** los recursos y pedirlos en **orden creciente**.

**8. ¿Prevención y evitación son lo mismo?**
**No.** La prevención **restringe cómo se piden** los recursos para que una condición nunca se cumpla. La evitación deja pedir libremente, pero **antes de conceder** comprueba con información previa (los **máximos declarados**) que el sistema siga seguro.

**9. ¿Qué necesita saber de antemano el banquero?**
El **máximo** de cada tipo de recurso que cada proceso puede llegar a pedir. Además, un proceso que recibe todo lo que necesita debe **devolverlo en un tiempo finito**.

**10. Pasos del algoritmo de solicitud.**
(1) Si Solicitud > Necesidad: **error** (excede su máximo). (2) Si Solicitud > Disponible: **espera**. (3) Simular la asignación (Disponible −, Asignado +, Necesidad −) y correr la seguridad: si queda **seguro** se concede; si no, **espera** y se restaura el estado.

**11. ¿Cuándo se usa el grafo y cuándo el banquero para evitar?**
**Una instancia** por tipo de recurso: el **grafo** (con aristas de reclamo). **Varias instancias**: el **banquero**.

**12. ¿Cómo se recupera de un deadlock terminando procesos? ¿A quién se elige?**
Abortar **todos** los interbloqueados, o **uno a la vez** hasta romper el ciclo. Para elegir: **prioridad**, cuánto ha calculado y cuánto le falta, **recursos** que usó y que necesita, **cuántos** procesos habrá que terminar y si es **interactivo o por lotes**.

**13. 4 instancias, 3 procesos, cada uno necesita como máximo 2: ¿puede haber deadlock?** *(Guía 13)*
**No.** En el peor caso, cada uno tiene 1 y queda **1 libre**, que completa a alguno. En general, alcanza con n(m − 1) + 1 instancias.

## Capítulo 9: Memoria principal

**14. Dirección lógica vs. física.**
La **lógica** (o virtual) la genera la **CPU**; la **física** es la que ve la **unidad de memoria**. Son distintas solo con enlace **en tiempo de ejecución**, donde las traduce la **MMU**.

**15. ¿Cómo se protege la memoria de un proceso?**
Con registros **base y límite**: la CPU revisa **cada** acceso en modo usuario y, si se sale, genera un **trap**. Cargar esos registros es una **instrucción privilegiada** (solo en modo kernel).

**16. ¿En qué momentos se puede hacer el enlace de direcciones?**
**Compilación** (código absoluto; si cambia el lugar, hay que recompilar), **carga** (código reubicable) y **ejecución** (el proceso puede moverse; necesita hardware: la MMU).

**17. Carga dinámica vs. enlace dinámico.**
**Carga dinámica:** una rutina no se carga hasta que se llama; **no necesita al SO**. **Enlace dinámico:** el enlace con una biblioteca se pospone a la ejecución mediante un **stub**; permite **bibliotecas compartidas** y **necesita al SO**. → [apuntes §4](apuntes-cap-9-y-10.md#4-carga-dinámica-vs-enlace-dinámico)

**18. First fit, best fit y worst fit: ¿cuál es mejor?**
**First fit y best fit** son mejores que worst fit en **velocidad y aprovechamiento**. First fit suele ser el **más rápido**; best fit deja el sobrante **más chico**, pero debe recorrer toda la lista.

**19. Fragmentación interna vs. externa.**
**Interna:** sobra espacio **dentro** del bloque asignado (paginación, en la última página). **Externa:** el espacio libre **total** alcanza, pero **no es contiguo** (particiones variables, segmentación). → [06 §3](../estudio/06-memoria.md#3-asignación-contigua-y-fragmentación)

**20. ¿Qué dice la regla del 50 %?**
Con first fit, por cada **N** bloques asignados se pierden **0,5 N** por fragmentación externa: hasta **un tercio** de la memoria puede quedar inutilizable.

**21. ¿Qué es la compactación y qué requiere?**
Mover los procesos para juntar los huecos en **uno grande**. Requiere **reubicación dinámica** (enlace en tiempo de ejecución) y cuidar los procesos que hacen **E/S** (bloquearlos, o hacer E/S solo en buffers del SO).

**22. Fragmentación externa en paginación.** *(Examen 2025-1)*
**Es cero**: cualquier marco libre sirve para cualquier página. La interna es, en promedio, **media página** por proceso.

**23. ¿Conviene usar páginas pequeñas?**
Tienen menos fragmentación interna, pero hacen **más grande la tabla de páginas** (más entradas) y aumentan la E/S por byte. Hay un compromiso; por eso hay sistemas con **dos tamaños** de página.

**24. ¿Por qué el tamaño de página es potencia de 2?**
Porque así la dirección lógica se divide directamente en bits: los **m − n** bits altos son el **número de página** y los **n** bajos, el **desplazamiento**. No hay que dividir.

## Capítulo 10: Memoria virtual

**25. ¿Qué es la memoria virtual y qué ventajas tiene?** *(Guía 43)*
La **separación** entre la memoria lógica del usuario y la física: solo una parte del programa necesita estar en memoria. El programa puede ser **más grande que la RAM**, caben **más procesos** (más uso de CPU), hay **menos E/S** y se pueden **compartir** páginas y crear procesos más rápido.

**26. Sin memoria virtual, ¿puede haber multiprogramación?** *(P1 2009, P1 2022-2)*
**Sí**, pero limitada a los procesos que quepan **completos** en la RAM a la vez. Un proceso más grande que la RAM **no puede ejecutarse**.

**27. ¿Qué es una falla de página y cuándo ocurre?**
Cuando el proceso referencia una página cuyo **bit válido-inválido está en *i*** (no está en memoria). La MMU genera un **trap** al SO, que trae la página del disco.

**28. Pasos para atender una falla de página.** *(P2 2025-2)*
Trap al SO → verificar que la referencia sea legal → buscar la página en el disco → buscar un marco libre (o elegir una víctima y escribirla si está modificada) → leer la página → actualizar la tabla (bit **v**) → **reiniciar la instrucción**. → [los 13 pasos completos](apuntes-cap-9-y-10.md#14-falla-de-página-los-13-pasos-del-peor-caso)

**29. ¿Qué hace la CPU mientras se lee la página del disco?**
**Se le asigna a otro proceso** (paso 6 del peor caso). Cuando termina la E/S, el proceso que falló vuelve a la cola de listos.

**30. Paginación por demanda vs. anticipada.** *(Examen 2025-1, Guía 43 d)*
**Por demanda** privilegia el **espacio** (solo se cargan las páginas usadas). **Anticipada** privilegia el **tiempo** (se cargan todas al inicio y no hay fallas después).

**31. ¿Qué es la paginación por demanda pura?**
Empezar el proceso **sin ninguna página** en memoria: cada página falla en su primer acceso.

**32. ¿Qué hardware necesita la paginación por demanda?**
Tabla de páginas con **bit válido-inválido**, **memoria secundaria** (espacio de intercambio) y la capacidad de **reiniciar instrucciones**.

**33. ¿Para qué sirve el bit de modificación?**
Para saber si la víctima **cambió** desde que se cargó. Si no cambió, **no se escribe en disco**, y la falla cuesta la mitad.

**34. ¿Qué es la anomalía de Belady?**
Que con **FIFO**, **más marcos** pueden producir **más fallas** (1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5: 9 fallas con 3 marcos, 10 con 4). LRU y Óptimo **no** la tienen, porque son **algoritmos de pila**.

**35. ¿Por qué no se usa el algoritmo Óptimo? ¿Para qué sirve?**
Necesita **conocer el futuro** (las referencias que vendrán). Sirve como **referencia**: ningún algoritmo puede tener menos fallas, así que se usa para medir a los demás.

**36. ¿Cómo se implementa LRU?**
Con **contadores** (hora del último uso en cada entrada; hay que buscar el menor) o con una **pila** doblemente enlazada (la referenciada va al tope; la víctima está en el fondo y no hay que buscarla, pero cada actualización es más cara).

**37. Reemplazo global vs. local.**
**Global:** la víctima puede ser de cualquier proceso; da **mayor rendimiento**, pero el tiempo de cada proceso varía. **Local:** solo de sus propios marcos; el rendimiento es **más predecible**, pero puede quedar memoria sin aprovechar.

**38. ¿Qué es el relleno con ceros bajo demanda?**
Antes de asignar un marco libre, el SO lo **llena de ceros**, para que el proceso no vea los datos de otro.

**39. ¿Qué es la hiperpaginación (thrashing)?**
Un proceso con **menos marcos** de los que su localidad necesita pasa más tiempo **trayendo páginas que ejecutando**. La CPU parece ociosa, el SO sube la multiprogramación y empeora. → [07 §6](../estudio/07-memoria-virtual.md#6-asignación-de-marcos-hiperpaginación-y-conjunto-de-trabajo)
