# Preguntas de concepto para la Prueba 1

> **Capítulos 1, 3 y 5.** Respuestas cortas, ordenadas por lo que ya salió en pruebas anteriores. Entre paréntesis, dónde apareció cada pregunta.

## Las que más se repiten

**1. Para hacer una llamada al sistema, ¿hay que estar en modo monitor o en modo usuario?** *(2009, 2024-2, 2025-2)*
El proceso la hace **en modo usuario**. La trap cambia a **modo monitor (kernel)**, el SO la atiende y **vuelve a modo usuario** antes de devolverle el control.

**2. En un SMP de 4 procesadores, ¿el SO puede ejecutarse en cualquiera?** *(2009, 2022-2)*
**Sí.** En el multiprocesamiento simétrico, el SO puede correr en cualquier procesador. En el asimétrico, un procesador maestro ejecuta el SO y los demás son esclavos.

**3. Sin memoria virtual, ¿qué problemas hay? ¿Puede haber multiprogramación?** *(2009, 2022-2)*
Un proceso **más grande que la memoria física no puede ejecutarse**, porque debe cargarse completo. **Sí** puede haber multiprogramación, pero limitada a los procesos que quepan completos a la vez.

## Capítulo 1: Introducción

**4. ¿Cuál es la principal ventaja de la multiprogramación?** *(2009)*
Aumenta la **utilización de la CPU**: cuando un proceso espera E/S, la CPU ejecuta otro.

**5. ¿Cómo se garantiza que todo acceso a los dispositivos pase por el SO?** *(2009)*
Haciendo **privilegiadas** las instrucciones de E/S. Solo se ejecutan en modo kernel, así que los procesos deben usar llamadas al sistema.

**6. Describa tres servicios del SO.** *(2009)*
- **Ejecución de programas:** carga, ejecuta y termina programas.
- **Operaciones de E/S:** hace la E/S por los procesos, que no acceden directo al hardware.
- **Sistema de archivos:** permite crear, leer, escribir y borrar archivos.

**7. ¿Una interrupción produce necesariamente un cambio de contexto? ¿Y una llamada al sistema?** *(2013)*
**No en ninguno de los dos casos.** Siempre se pasa a modo kernel y se guarda el estado de la CPU. Solo hay cambio de contexto si el SO termina ejecutando **otro** proceso, por ejemplo, si la llamada bloquea al proceso o si vence el quantum.

**8. ¿Qué intercambia datos entre el controlador de E/S y la memoria sin usar la CPU?** *(2013)*
El **DMA** (acceso directo a memoria). La CPU solo inicia la transferencia y recibe una interrupción al final.

**9. Si no hubiera DMA, ¿qué implicaría para la multiprogramación?** *(2024-2)*
La CPU quedaría **ocupada durante toda la transferencia** y no podría atender otros procesos, así que se perdería el beneficio de la multiprogramación.

**10. ¿Qué es un sistema altamente acoplado?** *(2022-2)*
Varios procesadores que **comparten memoria, reloj y bus**, y se comunican por memoria compartida. Lo contrario es un sistema débilmente acoplado, cuyos nodos se comunican por mensajes en red.

**11. ¿Qué implementan los drivers? ¿Son parte del SO?** *(2022-2)*
Implementan el manejo de un controlador específico y traducen pedidos genéricos a órdenes del hardware. **Sí son parte del SO**: corren en modo kernel.

**12. En un multiprocesador con memoria común, ¿cuál es el principal problema para el SO?** *(2025-2)*
**Proteger las secciones críticas del propio SO**, porque varias CPU pueden ejecutar código del sistema a la vez sobre las mismas estructuras.

## Capítulo 3: Procesos

**13. ¿Por qué el PCB reserva lugar para los registros de la CPU?** *(2022-2)*
Para **guardarlos cuando el proceso pierde la CPU y restaurarlos cuando vuelve**, de modo que continúe exactamente donde quedó.

**14. En un monoprocesador, ¿qué ventaja tienen los hilos a nivel de sistema?** *(2024-2)*
Si un hilo se bloquea en E/S, **otros hilos del mismo proceso pueden seguir ejecutándose**, porque el SO los reconoce por separado. No hay paralelismo real, ya que hay una sola CPU.

**15. Comente: "La permutación de la CPU a otro proceso requiere guardar el estado del anterior y cargar el del nuevo".** *(Guía, 43 a)*
Es el **cambio de contexto**. Es tiempo improductivo (*overhead*) y el estado se guarda en el PCB.

## Capítulo 5: Planificación

**16. En la planificación por prioridades, ¿cómo se evita la inanición?** *(2013)*
Con **envejecimiento (aging)**: se aumenta gradualmente la prioridad de los procesos que llevan mucho tiempo esperando.

**17. ¿Qué quantum es apropiado para Round Robin con 20 procesos en la cola?** *(2025-2)*
- **Ni muy chico ni muy grande:** si es muy chico, hay demasiados cambios de contexto; si es muy grande, se convierte en FCFS.
- **Regla empírica:** cerca del 80 % de las ráfagas debe ser menor que q, y q debe ser mayor que el tiempo de cambio de contexto.
- **Con 20 procesos:** cada uno espera hasta 19 × q para volver a correr, así que q debe ser lo bastante chico para mantener una respuesta interactiva.

## Otras preguntas posibles

Estas no aparecen en las pruebas revisadas: se armaron a partir de los temas de los capítulos, así que tienen menos prioridad.

**18. ¿Qué problema tendría un sistema de tiempo compartido sin timer?**
Un proceso con un ciclo infinito **nunca soltaría la CPU**, y no habría Round Robin. El timer genera una interrupción periódica que le devuelve el control al SO.

**19. ¿Por qué cambiar el timer es una instrucción privilegiada?**
Porque, si no, un programa de usuario podría desactivarlo y **quedarse con la CPU**.

**20. ¿En qué se diferencia una interrupción de una trap?**
La **interrupción** la genera el hardware de forma asíncrona, como el fin de una E/S. La **trap** la causa el programa en ejecución, como una división por cero o una llamada al sistema.

**21. ¿Por qué un proceso no puede pasar directamente de Espera a Ejecución?**
Porque la CPU puede estar ocupada y solo el planificador la asigna. El proceso vuelve primero a **Listo**.

**22. ¿Qué comparten los hilos de un mismo proceso y qué tiene cada uno por separado?**
**Comparten** el código, los datos y los archivos abiertos. **Cada uno tiene** su pila, sus registros y su contador de programa.

**23. ¿Qué diferencia hay entre un planificador de corto plazo y uno de largo plazo?**
El de **corto plazo** elige qué proceso listo recibe la CPU y actúa con mucha frecuencia. El de **largo plazo** decide qué trabajos entran a memoria y controla el grado de multiprogramación.

**24. ¿Qué diferencia hay entre un algoritmo apropiativo y uno no apropiativo?**
En el **apropiativo**, el SO puede quitarle la CPU a un proceso en ejecución. En el **no apropiativo**, el proceso la conserva hasta terminar o bloquearse.

**25. ¿Por qué SJF es óptimo? ¿Cuál es su principal dificultad práctica?**
Da el **menor tiempo de espera promedio** para un conjunto dado de procesos. Su dificultad es que **no se conoce la próxima ráfaga** y hay que estimarla. Además, los procesos largos pueden sufrir inanición.

**26. ¿Qué pasa con Round Robin si el quantum es muy chico? ¿Y si es muy grande?**
Si es **muy chico**, se pierde mucho tiempo en cambios de contexto. Si es **muy grande**, se convierte en **FCFS**.

**27. ¿Qué es el efecto convoy?**
Ocurre cuando **procesos cortos quedan esperando detrás de uno largo**, lo que sube el tiempo de espera promedio. Es típico de FCFS.
