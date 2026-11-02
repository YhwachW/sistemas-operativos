# 09 · Banco de preguntas de concepto (respuestas modelo)

> Todas las preguntas teóricas de las pruebas y la guía, con una respuesta corta lista para escribir. Para repasar la noche antes. El enlace de cada una lleva a la explicación completa.
>
> **Cómo responder en la prueba:** primero la respuesta directa (sí/no, el nombre del concepto) y después **una o dos frases de por qué**. El profesor da puntaje por la justificación.

## Sistema operativo y hardware

**¿Principal ventaja de la multiprogramación?** *(P1 2009)*
Aumenta la **utilización de la CPU**: hay varios procesos cargados y, cuando uno espera E/S, la CPU ejecuta otro. → [01 §6](01-conceptos-basicos.md#6-multiprogramación-y-multitarea)

**¿Cómo garantizar que todo acceso a dispositivos pase por el SO?** *(P1 2009)*
Haciendo **privilegiadas** las instrucciones de E/S: solo se pueden ejecutar en modo kernel, así que los procesos deben pedírselo al SO con llamadas al sistema. → [01 §7](01-conceptos-basicos.md#7-modo-dual-usuario--kernel-y-protección)

**Tres servicios del SO.** *(P1 2009)*
Ejecución de programas; operaciones de E/S; manejo del sistema de archivos; comunicaciones; detección de errores; asignación de recursos, contabilidad y protección. → [01 §2](01-conceptos-basicos.md#2-servicios-del-sistema-operativo)

**Para hacer una llamada al sistema, ¿modo monitor o usuario?** *(P1 2009, Recup. 2024-2, P1 2025-2: muy repetida)*
La llamada la hace el proceso **en modo usuario**. La trap cambia a **modo monitor (kernel)**, el SO la atiende y **vuelve a modo usuario** antes de devolverle el control. → [01 §8](01-conceptos-basicos.md#8-llamadas-al-sistema)

**¿Una interrupción produce necesariamente un cambio de contexto? ¿Y una llamada al sistema?** *(P1 2013)*
**No** en ninguno de los dos casos. Siempre hay cambio a modo kernel y se guarda el estado de la CPU, pero solo hay cambio de contexto si el SO termina ejecutando **otro** proceso (por ejemplo, si la llamada bloquea al proceso o la interrupción es el fin del quantum). → [01 §3](01-conceptos-basicos.md#3-interrupciones)

**¿Qué usa el SO para que el controlador de E/S y la memoria intercambien datos sin la CPU?** *(P1 2013)*
El **DMA** (acceso directo a memoria). → [01 §4](01-conceptos-basicos.md#4-estructura-de-es-y-dma)

**Sin DMA (la CPU mueve cada byte), ¿qué pasa con la multiprogramación?** *(Parcial 2024-2)*
La CPU queda **ocupada durante toda la transferencia** y no puede atender otros procesos, así que se pierde el beneficio de la multiprogramación. El DMA libera a la CPU y permite **mayor grado de multiprogramación**. → [01 §4](01-conceptos-basicos.md#parcial-2024-2-problema-4-sin-dma-qué-implica-para-la-multiprogramación)

**SMP con 4 procesadores: ¿el SO corre en cualquiera?** *(P1 2009, P1 2022-2)*
**Sí.** En el multiprocesamiento **simétrico**, los procesos del SO pueden correr en **cualquier** procesador. En el asimétrico, un procesador maestro ejecuta el SO y los demás son esclavos. → [01 §9](01-conceptos-basicos.md#9-sistemas-multiprocesador)

**¿Qué es un sistema altamente acoplado?** *(P1 2022-2)*
Varios procesadores que **comparten memoria, reloj y bus** y se comunican por memoria compartida. Lo contrario es débilmente acoplado (distribuido), donde los nodos se comunican por mensajes en red. → [01 §9](01-conceptos-basicos.md#9-sistemas-multiprocesador)

**¿Qué implementan los device drivers? ¿Son parte del SO?** *(P1 2022-2)*
Implementan el manejo de un controlador específico (registros, comandos, interrupciones) y traducen pedidos genéricos a órdenes del hardware. **Sí son parte del SO**: corren en modo kernel con acceso directo al hardware. → [01 §10](01-conceptos-basicos.md#10-drivers-manejadores-de-dispositivo)

**Multiprocesador con memoria común: ¿principal problema para el SO?** *(P1 2025-2)*
**Proteger las secciones críticas del propio SO**, porque varias CPU pueden ejecutar código del sistema a la vez sobre las mismas estructuras. → [04 §2](04-sincronizacion.md#2-la-sección-crítica-y-sus-3-requisitos)

## Procesos, hilos y planificación

**¿Por qué el PCB reserva lugar para los registros de la CPU?** *(P1 2022-2)*
Para **guardarlos cuando el proceso pierde la CPU y restaurarlos cuando vuelve**, de modo que continúe exactamente donde quedó (cambio de contexto). → [02 §3](02-procesos-e-hilos.md#3-pcb-bloque-de-control-de-proceso)

**Ventaja de los hilos a nivel de sistema en un monoprocesador.** *(Parcial 2024-2)*
Si un hilo se bloquea en E/S, **otros hilos del mismo proceso pueden seguir ejecutándose**, porque el SO los reconoce como unidades de ejecución independientes. → [02 §8](02-procesos-e-hilos.md#8-hilos-threads)

**"La permutación de la CPU a otro proceso requiere guardar el estado del anterior y cargar el del nuevo."** *(Guía 43 a)*
Es el **cambio de contexto**. Es tiempo improductivo (*overhead*) y el estado se guarda en el PCB. → [02 §4](02-procesos-e-hilos.md#4-cambio-de-contexto)

**Prioridades: ¿cómo se evita la inanición (starvation)?** *(P1 2013)*
Con **envejecimiento (aging)**: se aumenta gradualmente la prioridad de los procesos que llevan mucho tiempo esperando. → [03 §4.4](03-planificacion-cpu.md#44-prioridad-apropiativa-o-no)

**¿Quantum apropiado para RR, con 20 procesos en el peor caso?** *(P1 2025-2)*
Ni muy chico (demasiados cambios de contexto: si el cambio cuesta 1 ms y q = 4 ms, se pierde un 20 % de la CPU) ni muy grande (se vuelve FCFS). Empíricamente, que ~80 % de las ráfagas sean menores que q y siempre mayor que el tiempo de cambio de contexto. Con 20 procesos, cada uno espera hasta 19 × q para volver a correr: q debe ser lo bastante chico para que eso dé una respuesta interactiva. → [03 §4.5](03-planificacion-cpu.md#45-round-robin-rr)

**Tiempo de retorno de un proceso con CPU 4, E/S 5 y CPU 7 que llega en t = 4 con prioridad máxima.** *(P1 2025-2)*
Termina en 4 + 4 + 5 + 7 = 20, así que el retorno es **20 − 4 = 16 ut**. → [03 §5.7](03-planificacion-cpu.md#57-p1-2025-2--pregunta-2-tiempo-de-retorno-con-es)

## Sincronización e interbloqueo

**Dos procesos incrementan X = 34.657 a la vez: ¿qué pasa y cómo se evita?** *(Examen 2026-1, guía 27)*
**Condición de carrera**: ambos pueden leer 34.657 y guardar 34.658, y se pierde un incremento. Se evita con **exclusión mutua** sobre la sección crítica (`X = X + 1`), por ejemplo con un **semáforo binario**: `wait(mutex); X = X + 1; signal(mutex);`. → [04 §1](04-sincronizacion.md#1-el-problema-la-condición-de-carrera)

**Las 4 condiciones del deadlock.** *(Recup. 2024-2)*
**Exclusión mutua, retención y espera, sin expropiación y espera circular**, todas a la vez. → [05 §2](05-interbloqueo.md#2-las-cuatro-condiciones-deben-darse-las-cuatro-a-la-vez)

**¿Detección o prevención para una red de computadores?** *(Guía 25)*
**Prevención**, ordenando los recursos para romper la espera circular: detectar en un sistema distribuido es caro. → [05 §4](05-interbloqueo.md#guía-25-detección-o-prevención-para-la-red-de-la-empresa-2yk)

**¿Por qué detectar deadlocks es más caro en un sistema distribuido?** *(Guía 31)*
Nadie ve el estado completo: hay que **intercambiar mensajes** para armar el grafo global, con retardos, información desactualizada y posibles falsos deadlocks. → [05 §4](05-interbloqueo.md#guía-31-por-qué-detectar-es-más-caro-en-un-sistema-distribuido)

**4 instancias de un recurso, 3 procesos que necesitan como máximo 2: ¿libre de deadlock?** *(Guía 13)*
**Sí.** En el peor caso cada uno tiene 1 (3 asignadas) y queda 1 libre, que completa a alguno; ese termina y libera. → [05 §4](05-interbloqueo.md#guía-13-4-instancias-de-un-recurso-3-procesos-cada-uno-necesita-como-máximo-2)

**Un estado inseguro podría ser causado por…** *(Examen 2025-1, pregunta 3)*
**A) Los recursos escasos.** Con pocos recursos disponibles, ningún proceso puede completar su necesidad.

## Memoria

**Sin memoria virtual, ¿qué problemas hay? ¿Puede haber multiprogramación?** *(P1 2009, P1 2022-2)*
Un proceso **más grande que la memoria física no puede ejecutarse**, porque debe cargarse completo. **Sí** puede haber multiprogramación, pero limitada a los procesos que quepan **completos** a la vez. → [07 §1](07-memoria-virtual.md#1-la-idea)

**"Técnica que permite simular más memoria de la que realmente existe…"** *(Guía 43 b)*
**Memoria virtual.** → [07 §1](07-memoria-virtual.md#1-la-idea)

**"Espacio no ocupado dentro de una partición, que no se puede reasignar…"** *(Guía 43 c)*
**Fragmentación interna.** Si los huecos estuvieran entre particiones, sería externa. → [06 §3](06-memoria.md#3-asignación-contigua-y-fragmentación)

**"La paginación por demanda privilegia el espacio; la anticipada, el tiempo de acceso."** *(Guía 43 d, Examen 2025-1 pregunta 4)*
**Verdadero (alternativa A).** Por demanda, solo se cargan las páginas que se usan (ahorra memoria). Anticipada, se cargan todas al inicio y se evitan las fallas posteriores (ahorra tiempo). → [07 §2](07-memoria-virtual.md#2-paginación-por-demanda-vs-anticipada)

**Fragmentación externa en paginación.** *(Examen 2025-1, pregunta 2)*
**C) Es cero.** Cualquier marco libre sirve para cualquier página. → [06 §4](06-memoria.md#4-paginación)

**Swapping por partes en vez del proceso completo.** *(Examen 2025-1, pregunta 5)*
**C) Paginación por demanda.** → [06 §8](06-memoria.md#8-swapping)

**Un archivo ejecutable corresponde a…** *(Examen 2025-1, pregunta 1)*
**C) Secciones de código de máquina que el cargador lleva a la memoria principal para ejecutarlas.** → [06 §1](06-memoria.md#1-dirección-lógica-vs-física)

**Pasos de la rutina de falla de página.** *(P2 2025-2)*
Trap al SO → ubicar la página en disco → buscar un marco libre (si no hay, algoritmo de reemplazo; escribir la víctima a disco y actualizar su entrada) → leer la página al marco → actualizar la tabla de páginas → reiniciar la instrucción y volver al proceso. → [07 §3](07-memoria-virtual.md#3-rutina-de-falla-de-página-p2-2025-2-pregunta-1-10-pts)

**¿Agregar un marco o reemplazar una página del proceso?** *(Guía 33 / 37)*
Mirar la **frecuencia de fallas** (o el conjunto de trabajo): si es alta, el proceso está expandiéndose y se le **agrega un marco**; si es baja, está cambiando de localidad y se **reemplaza** una de sus páginas. → [06 §6.3](06-memoria.md#63-guía-33--37-agregar-un-marco-o-reemplazar-una-página)

**Base 0x3000, límite 0x0C00, dirección lógica 0x0B20: ¿es válida? ¿Cuál es la física?** *(P1 2025-2)*
2848 < 3072, así que **es válida**. Física = 0x3000 + 0x0B20 = **0x3B20**. → [06 §2](06-memoria.md#p1-2025-2-pregunta-3-20-pts)

## Disco y archivos

**Relacionar la planificación del brazo con el sistema de archivos.** *(Guía 17)*
La forma de asignar bloques (contigua, enlazada o indexada) y la ubicación de directorios y FAT determinan **cuánto se mueve el brazo**. Si los datos están dispersos, la planificación importa más; conviene ubicar los metadatos en los cilindros del medio. → [08 §2](08-disco-archivos-y-proteccion.md#guía-17-brazo-del-disco-y-sistema-de-archivos)

**Transferir 1 GB de RAM (6 GB/s) a un disco (150 MB/s).** *(P2 2024-2)*
≈ **6,83 s**: manda el componente **más lento** (el disco), que es el cuello de botella. → [08 §6](08-disco-archivos-y-proteccion.md#6-transferencia-ram--disco-p2-2024-2-problema-4-20-pts)
