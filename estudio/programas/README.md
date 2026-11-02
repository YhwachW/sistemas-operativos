# Programas de sincronización (C-- para jBACI)

Soluciones de los problemas de semáforos de la guía, escritas en C-- para **ejecutarlas** y ver la concurrencia en acción. Cada una se ejecutó 3.000 veces con el intérprete de Mini BACI.

| Programa | Problema | Qué muestra | Resultado en 3.000 ejecuciones |
|---|---|---|---|
| [`27-contador-X.cm`](27-contador-X.cm) | Guía 27 / Examen 2026-1 | Condición de carrera y su arreglo con `binarysem` | Con mutex: siempre 34.687. Sin mutex: 34.679, 34.680… |
| [`24-e-despues-de-a-o-g.cm`](24-e-despues-de-a-o-g.cm) | Guía 24 | Un semáforo en 0 como "permiso" | `e` siempre después de `a` o de `g` |
| [`39-combinatorio.cm`](39-combinatorio.cm) | Guía 39 | Esperar a que otro proceso termine un cálculo | Siempre "Resultado: 15" (6 sobre 2) |
| [`42a-orden-ABC.cm`](42a-orden-ABC.cm) | Guía 42 a | Turnos en cadena | Siempre ABC ABC ABC ABC |
| [`42b-orden-ABBC.cm`](42b-orden-ABBC.cm) | Guía 42 b | Dar dos permisos y esperar dos avisos | Siempre ABBC ABBC… |
| [`42c-orden-ACBA.cm`](42c-orden-ACBA.cm) | Guía 42 c | Un proceso que trabaja dos veces por vuelta | Siempre ACBA ACBA… |
| [`34-productor-consumidor-mal.cm`](34-productor-consumidor-mal.cm) | Guía 34 | El orden equivocado de los `wait` causa deadlock | Versión mala: 293 deadlocks. Corregida: 0 |
| [`38-grafo-precedencia.cm`](38-grafo-precedencia.cm) | Guía 38 | Grafo de precedencia con un semáforo por arista | Nunca viola el orden |
| [`41-parque.cm`](41-parque.cm) | Guía 41 | Cupos (contador), barrera y guardia (binarios) | Nunca hay más autos dentro que la capacidad |

## Tus ejercicios de jBACI

En [`ejercicios-jbaci/`](ejercicios-jbaci/) hay una copia de los ejercicios de tu carpeta `jBACI/ejercicios/`:

| Archivo | Tema |
|---|---|
| `01-impresora-uno-a-la-vez.cm` | Exclusión mutua con `binarysem` |
| `02-trafico-cruce-uno-a-la-vez.cm` | Un auto a la vez en el cruce |
| `03-trafico-cruce-pantalla-protegida.cm` | Igual, más un semáforo para que la consola no se mezcle |
| `04-trafico-turnos-dos-calles.cm` | Turnos alternados entre dos calles |
| `05-estacionamiento-examen-2025-1.cm` | Examen 2025-1: `semaphore cupos = 5` + `binarysem barrera`. ⚠ El ciclo `dentro = dentro;` está fuera de la barrera ([ver por qué](../04-sincronizacion.md#43-contar-recursos-semáforo-en-n)) |
| `trafficlight.cm` | Borrador: usa `turno` (un `binarysem`) como si fuera un número, así que falla al ejecutarse. La versión corregida está en Mini BACI ("Semáforo de tránsito A/B") |

## Cómo ejecutarlos

- **En el PC con jBACI:** desde la carpeta `jBACI/`, `java -jar jbaci.jar`, abre el `.cm`, presiona **Compile**, después **Run** y luego **Go**.
- **En el celular:** abre [Mini BACI](https://yhwachw.github.io/mini-baci/), toca **Abrir .cm**, elige el archivo y presiona **Compilar y ejecutar**. Puedes ir paso a paso y ver los semáforos y las colas.

Como el orden entre procesos es aleatorio (igual que en jBACI), **ejecuta varias veces**: los programas correctos dan siempre el mismo resultado; los incorrectos (sin mutex, o el productor-consumidor mal ordenado) a veces fallan.
