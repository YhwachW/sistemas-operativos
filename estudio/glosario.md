# Glosario

| Término | Significado |
|---|---|
| **Aging (envejecimiento)** | Subir gradualmente la prioridad de un proceso que lleva mucho esperando, para evitar la inanición |
| **Banquero (algoritmo del)** | Algoritmo de evitación de deadlock: solo asigna recursos si el sistema queda en estado seguro |
| **Bloque / marco (frame)** | Trozo de memoria física de tamaño fijo donde cabe una página |
| **Cambio de contexto** | Guardar el estado de un proceso en su PCB y cargar el de otro. Es tiempo improductivo |
| **Condición de carrera** | El resultado depende del orden en que se intercalan procesos que acceden a datos compartidos |
| **Conjunto de trabajo (working set)** | Páginas que un proceso usó en sus últimas Δ referencias |
| **Deadlock (interbloqueo, abrazo mortal)** | Procesos que se esperan mutuamente para siempre |
| **Despachador (dispatcher)** | Módulo que le entrega la CPU al proceso elegido (cambio de contexto + modo usuario + salto) |
| **DMA** | Acceso directo a memoria: el controlador transfiere bloques sin la CPU |
| **Espera activa (busy waiting)** | Esperar dando vueltas en un ciclo (gasta CPU) |
| **Estado seguro** | Existe un orden en que todos los procesos pueden terminar |
| **Exclusión mutua** | Solo un proceso a la vez en la sección crítica |
| **Falla de página (page fault)** | Se referencia una página que no está en RAM; el SO la trae desde disco |
| **Fragmentación externa** | Memoria libre repartida en huecos que, por separado, no alcanzan |
| **Fragmentación interna** | Memoria asignada que no se usa (por ejemplo, el final de la última página) |
| **Hilo (thread)** | Unidad de ejecución dentro de un proceso; comparte código, datos y archivos con los otros hilos |
| **Hiperpaginación (thrashing)** | El sistema pasa más tiempo trayendo páginas que ejecutando |
| **Inanición (starvation)** | Un proceso nunca consigue lo que espera (CPU o recurso) |
| **Interrupción** | Señal de hardware que detiene a la CPU y salta al SO |
| **Kernel** | Núcleo del SO, siempre en memoria |
| **LRU** | *Least Recently Used*: reemplaza la página usada hace más tiempo |
| **Modo dual** | Modo usuario / modo kernel (monitor), según el bit de modo |
| **Monitor** | Construcción con variables compartidas y procedimientos, donde solo un proceso está dentro a la vez |
| **Multiprogramación** | Varios procesos en memoria para aprovechar la CPU durante la E/S |
| **Multitarea (tiempo compartido)** | Cambiar de proceso muy seguido para dar respuesta interactiva |
| **PCB** | Bloque de control de proceso: estado, PC, registros, memoria, E/S y prioridad |
| **Paginación anticipada (por adelantado)** | Se cargan todas las páginas al inicio |
| **Paginación por demanda** | Se carga cada página solo cuando se usa |
| **Quantum** | Tiempo máximo de CPU por turno en Round Robin |
| **Ráfaga (burst)** | Tramo continuo de uso de CPU (o de E/S) |
| **Sección crítica** | Código que accede a datos compartidos |
| **Semáforo** | Entero manejado solo con `wait` (P) y `signal` (V), ambos atómicos |
| **SMP / AMP** | Multiprocesamiento simétrico (todas las CPU iguales) / asimétrico (maestro-esclavo) |
| **SRTF** | *Shortest Remaining Time First* = SJF apropiativo |
| **Swapping** | Sacar un proceso completo de la RAM al disco y traerlo después |
| **Llamada al sistema (system call)** | Pedido de un programa al SO; pasa a modo kernel con una trap |
| **TLB** | Caché de la tabla de páginas en la MMU |
| **Trap** | Interrupción por software (error o llamada al sistema) |
| **Turnaround** | Tiempo total en el sistema: fin − llegada |
| **Waiting time** | Tiempo en la cola de listos: turnaround − ráfaga |
