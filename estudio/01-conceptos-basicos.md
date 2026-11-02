# 01 · Conceptos básicos: qué es y cómo funciona un sistema operativo

> Las preguntas de "responda brevemente" de casi todas las pruebas salen de aquí (P1 2009, 2013, 2022, 2024, 2025; recuperativas).
> Apuntes: *Cap 1 2020.pdf* (Silberschatz, cap. 1 y 2).

## 1. ¿Qué es un sistema operativo?

Es el programa que hace de **intermediario entre el usuario (y sus programas) y el hardware**. Tiene dos papeles:

- **Administrador de recursos:** reparte la CPU, la memoria, los dispositivos y los archivos entre los procesos, de forma eficiente y justa.
- **Programa de control:** vigila la ejecución de los programas para evitar errores y usos indebidos.

Sus **objetivos**: ejecutar programas y facilitar la resolución de problemas, ser **cómodo** de usar y usar el hardware de forma **eficiente**.

El sistema computacional tiene 4 partes: **hardware**, **sistema operativo**, **programas de aplicación** y **usuarios**. El **kernel** (núcleo) es la parte del SO que está siempre en memoria.

## 2. Servicios del sistema operativo

*(P1 2009, pregunta c: "Describa tres servicios")*

| Servicio | Qué hace |
|---|---|
| **Ejecución de programas** | Carga el programa en memoria, lo ejecuta y lo termina (normal o con error) |
| **Operaciones de E/S** | Da una interfaz abstracta a los dispositivos; el usuario no maneja los detalles de bajo nivel, y el acceso es más eficiente y seguro |
| **Sistema de archivos** | Crear, leer, escribir, borrar y buscar archivos y directorios; almacenamiento persistente |
| **Comunicaciones** | Intercambio de información entre procesos, en la misma máquina o en red, por memoria compartida o mensajes |
| **Detección de errores** | Detecta errores de hardware y de programas y reacciona sin botar todo el sistema |
| **Asignación de recursos, contabilidad y protección** | En sistemas multiusuario: quién usa qué, cuánto, y que nadie acceda a lo que no le corresponde |

## 3. Interrupciones

Un SO es **manejado por interrupciones**: no hace nada hasta que algo lo despierta.

- Una **interrupción** es una señal de hardware (por ejemplo, "el disco terminó") que detiene lo que hace la CPU y salta al SO.
- Una **trap** (excepción) es una "interrupción por software": un error (división por cero, acceso inválido) o una **llamada al sistema**.

**Qué pasa en una interrupción:**

1. El hardware **guarda el estado** de la CPU (contador de programa y registros) y pasa a **modo kernel**.
2. Con el **vector de interrupciones** (una tabla de direcciones) salta a la **rutina de servicio** de esa interrupción.
3. La rutina atiende el evento.
4. Se **restaura el estado** y se vuelve a lo que se estaba haciendo, o el planificador elige otro proceso.

### P1 2013, Pregunta 3: ¿una interrupción produce *necesariamente* un cambio de contexto? ¿Y una llamada al sistema?

**No necesariamente, en ninguno de los dos casos.** Siempre hay un **cambio de modo** (usuario → kernel) y se **guarda el estado** de la CPU para poder volver. Pero si, al terminar de atender, el SO **vuelve al mismo proceso**, no hubo cambio de contexto (no se cambió de proceso).

Hay cambio de contexto solo si el SO decide ejecutar **otro** proceso. Por ejemplo:

- La interrupción despierta a un proceso más prioritario, o es el timer que marca el fin del quantum.
- La llamada al sistema **bloquea** al proceso (pidió E/S y tiene que esperar).

> La pauta 2013 responde describiendo cómo el SO atiende interrupciones y los tipos de llamadas al sistema. Si te lo preguntan, da la respuesta corta de arriba y **después** explica el mecanismo.

## 4. Estructura de E/S y DMA

- Cada dispositivo tiene un **controlador** (hardware con registros y un búfer local).
- El SO habla con cada controlador mediante un **driver** (manejador de dispositivo).
- **E/S por interrupciones:** la CPU inicia la operación, sigue con otra cosa, y el controlador **interrumpe** cuando termina. El problema es que, si la CPU mueve cada byte, en dispositivos rápidos hay una interrupción por byte.
- **DMA (*Direct Memory Access*):** el controlador transfiere **bloques completos** directamente entre el dispositivo y la memoria, **sin pasar por la CPU**. Hay **una interrupción por bloque**, no por byte.

> **P1 2013, Pregunta 5:** el elemento que intercambia datos entre el controlador de E/S y la memoria sin la CPU es el **DMA**.

### Parcial 2024-2, Problema 4: sin DMA, ¿qué implica para la multiprogramación?

Si la CPU tiene que mover **cada byte** leído o escrito, queda **ocupada durante toda la transferencia** y no puede ejecutar otros procesos. La multiprogramación existe justamente para aprovechar la CPU mientras otros esperan E/S, así que pierde gran parte de su beneficio. Con DMA, la CPU solo inicia la transferencia y recibe una interrupción al final; mientras tanto ejecuta otros procesos, lo que permite **más grado de multiprogramación**.

## 5. Jerarquía de almacenamiento y caché

| Nivel | Velocidad | Tamaño | ¿Volátil? |
|---|---|---|---|
| Registros | La más rápida | Bytes | Sí |
| Caché (L1, L2, L3) | | KB a MB | Sí |
| Memoria principal (RAM) | | GB | Sí |
| SSD / memoria no volátil | | GB a TB | No |
| Disco duro (HDD) | | TB | No |
| Cinta, discos ópticos | La más lenta | Enorme | No |

- **Caché:** copiar lo que se usa más a un nivel más rápido. Funciona por **localidad**.
- Problema: **coherencia**. Si hay copias en varios niveles (o en varias CPU), todas deben ver el mismo valor.

## 6. Multiprogramación y multitarea

- **Multiprogramación:** tener **varios procesos en memoria**. Cuando el que corre espera E/S, la CPU pasa a otro.
- **Multitarea (tiempo compartido):** cambiar de proceso **muy seguido** (quantum), para que cada usuario sienta que tiene la máquina para él. Así se logran respuestas interactivas, en menos de un segundo.

> **P1 2009 a): ¿Principal ventaja de la multiprogramación?** **Aumentar la utilización de la CPU**: con varios procesos cargados, cuando uno pide E/S se ejecuta otro y la CPU no queda ociosa.

## 7. Modo dual (usuario / kernel) y protección

El hardware tiene un **bit de modo**:

- **Modo kernel** (monitor, supervisor, privilegiado), bit = 0: se pueden ejecutar **todas** las instrucciones, incluidas las **privilegiadas** (E/S, manejo de interrupciones, timer, registros de memoria).
- **Modo usuario**, bit = 1: si un programa intenta una instrucción privilegiada, el hardware genera una **trap** y el SO toma el control.

**Paso de un modo a otro:** una interrupción, una trap o una llamada al sistema pasan a modo kernel; al volver al proceso, se pasa a modo usuario.

**Timer:** el SO programa un temporizador antes de entregarle la CPU a un proceso. Cuando vence, hay una interrupción y el SO recupera el control, aunque el proceso tenga un ciclo infinito. Modificar el timer es una instrucción privilegiada.

> **P1 2009 b): ¿Cómo garantizar que todo acceso a dispositivos pase por el SO?** Haciendo que las instrucciones de E/S (las que acceden a los dispositivos) sean **privilegiadas**. Así solo el SO, en modo kernel, puede ejecutarlas, y los procesos deben **pedírselo** con una llamada al sistema.

## 8. Llamadas al sistema

Una **llamada al sistema** (*system call*) es la forma en que un programa le pide un servicio al SO (leer un archivo, crear un proceso, pedir memoria…). Normalmente se llama a través de una **API** (por ejemplo, POSIX o Win32) y la biblioteca hace la llamada real.

> **¿Hay que estar en modo monitor o en modo usuario para hacer una llamada al sistema?** *(P1 2009 d, Recuperativa 2024-2 P3, P1 2025-2 P5: sale casi siempre)*
>
> La llamada **la hace un proceso de usuario, en modo usuario**. La instrucción de llamada (una *trap*) cambia a **modo kernel (monitor)**; el SO atiende el pedido en modo kernel y, **antes de devolverle el control al proceso, vuelve a modo usuario**.
>
> Esquema: `proceso (modo usuario) → trap → SO atiende (modo kernel) → retorno (modo usuario)`.

Tipos de llamadas: control de procesos (crear, terminar, esperar), manejo de archivos, manejo de dispositivos, información del sistema, comunicaciones y protección.

## 9. Sistemas multiprocesador

| Tipo | Qué es |
|---|---|
| **Multiprocesador (altamente acoplado)** | Varias CPU que **comparten memoria, reloj y bus**. Ventajas: más rendimiento, economía de escala y mayor confiabilidad |
| **SMP (simétrico)** | **Todas** las CPU son iguales y **cualquiera** puede ejecutar procesos de usuario o del SO |
| **AMP (asimétrico)** | Una CPU **maestra** ejecuta el SO y reparte el trabajo; las demás (esclavas) ejecutan solo lo que se les asigna |
| **Multinúcleo** | Varias CPU (núcleos) en un mismo chip |
| **NUMA** | Cada CPU tiene memoria local (rápida); acceder a la de otra es más lento |
| **Clúster (débilmente acoplado)** | Varios computadores unidos por red, que comparten almacenamiento. Se usan para **alta disponibilidad** y alto rendimiento |

> **P1 2009 f / P1 2022-2 iv: SMP con 4 procesadores, ¿el SO corre en cualquiera?** **Sí.** En multiprocesamiento **simétrico**, los procesos del SO pueden ejecutarse en **cualquier** procesador, sin restricción. Si fuera **asimétrico**, el SO correría en un procesador **maestro** que controla a los demás (esclavos).
>
> **P1 2022-2 i: ¿Qué es un sistema altamente acoplado (integrado)?** Varios procesadores que **comparten la memoria principal, el reloj y el bus**, y se comunican por memoria compartida (un multiprocesador). Lo opuesto es un sistema **débilmente acoplado** (distribuido): cada nodo tiene su memoria y se comunica por **mensajes en una red**.
>
> **P1 2025-2, Pregunta 4:** con varias CPU y una única memoria común, el principal problema del SO es **proteger sus secciones críticas**, porque dos CPU pueden ejecutar código del SO a la vez sobre las mismas estructuras. Ver [04 · Sincronización](04-sincronizacion.md#2-la-sección-crítica-y-sus-3-requisitos).

## 10. Drivers (manejadores de dispositivo)

> **P1 2022-2 ii: ¿Qué implementan los device drivers? ¿Son parte del SO?**
>
> Un driver **implementa el manejo de un controlador de dispositivo específico**: conoce sus registros y protocolos y **traduce** los pedidos genéricos del SO ("leer el bloque 25") a órdenes concretas para ese hardware. También atiende sus interrupciones.
>
> **Sí, forman parte del SO.** Se ejecutan en **modo kernel**, porque usan instrucciones privilegiadas y acceden directamente al hardware. Le dan al resto del SO una interfaz uniforme, aunque muchas veces los escribe el fabricante del dispositivo y se cargan como módulos.

## 11. Otros temas del capítulo 1

- **Virtualización:** un *hipervisor* (VMM) permite correr varios SO invitados sobre un mismo hardware.
- **Sistemas distribuidos:** varias máquinas en red que cooperan.
- **Entornos de cómputo:** tradicional, móvil, cliente-servidor, *peer-to-peer*, nube (SaaS, PaaS, IaaS) y sistemas embebidos de **tiempo real**, que tienen plazos estrictos.
- **Arranque (*boot*):** el programa de arranque (*bootstrap*, en firmware) inicializa el hardware, carga el kernel en memoria y le pasa el control.
- **Del código fuente al ejecutable:** compilador → objeto → enlazador → ejecutable → cargador (lo lleva a memoria). Un **ejecutable** son secciones de código de máquina que el cargador lleva a la memoria principal (Examen 2025-1, pregunta 1, alternativa **C**).
