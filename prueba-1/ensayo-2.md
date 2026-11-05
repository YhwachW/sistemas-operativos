# Ensayo 2 de Prueba 1: Sistemas Operativos

> **Capítulos 1, 3 y 5** · 100 puntos · 90 minutos · Exigencia 60 %
>
> Hazla **con reloj y sin apuntes**, como si fuera la prueba real. Después corrige con la [pauta](pauta-ensayo-2.md).
> Indica en cada algoritmo qué criterio usas (por ejemplo, "RR por iteraciones en orden de llegada"; "W.T. = T.T. − ráfaga").

---

## Problema 1 (40 pts)

Se tienen los siguientes procesos:

| Proceso | Tpo. llegada | Tpo. ráfaga | Prioridad |
|---|---|---|---|
| P1 | 1,5 | 4 | 3 |
| P2 | 2,3 | 6 | 1 |
| P3 | 3,0 | 2 | 2 |
| P4 | 4,8 | 3 | 4 |
| P5 | 18,0 | 5 | 0 |

(Número menor = mayor prioridad.)

i) Simule el comportamiento del sistema mediante un diagrama de Gantt con los algoritmos **FCFS**, **SJF Preemptive**, **Priority Preemptive** y **Round Robin con q = 3**. (24 pts)

ii) Determine, para cada proceso y algoritmo, su **tiempo de permanencia** (turnaround) y su **tiempo de espera**, con los **promedios**. (12 pts)

iii) ¿Cuál es el mejor algoritmo para este grupo de procesos? Justifique. (4 pts)

---

## Problema 2 (15 pts)

Dos procesos alternan ráfagas de CPU y de E/S. La CPU se planifica con **FCFS** y cada proceso usa un dispositivo distinto, así que sus E/S pueden ocurrir al mismo tiempo.

| Proceso | Llegada | Comportamiento |
|---|---|---|
| X | 0 | CPU 2 → E/S 6 → CPU 3 |
| Y | 1 | CPU 3 → E/S 5 → CPU 2 |

a) Dibuje el uso de la CPU y de la E/S de cada proceso a lo largo del tiempo. (6 pts)

b) Calcule el **tiempo de retorno** y el **tiempo de espera en la cola de listos** de cada proceso. (4 pts)

c) ¿Hay tiempo ocioso de CPU? Calcule el **porcentaje de utilización de la CPU**. (2 pts)

d) Escriba la **secuencia de transiciones de estado** de Y, indicando el instante de cada una. (3 pts)

---

## Problema 3 (20 pts)

Responda brevemente, justificando:

a) ¿Cuál es la principal ventaja de la multiprogramación? ¿En qué se diferencia de la multitarea (tiempo compartido)? (5 pts)

b) ¿Una interrupción produce necesariamente un cambio de contexto? ¿Y una llamada al sistema? (5 pts)

c) ¿Cómo se puede garantizar que todo acceso a los dispositivos pase por el sistema operativo? (5 pts)

d) ¿Qué implementan los *device drivers*? ¿Son parte del sistema operativo? (5 pts)

---

## Problema 4 (25 pts)

a) Dibuje el diagrama de estados de un proceso e indique la causa de cada transición. ¿Por qué un proceso no puede pasar directamente de **Espera** a **Ejecución**? (6 pts)

b) ¿Cuántos procesos existen en total, contando el original, y cuántas veces se imprime "hola"? Justifique con un árbol de procesos. (6 pts)

```c
int main() {
    fork();
    if (fork() == 0) {
        fork();
    }
    printf("hola\n");
    return 0;
}
```

c) ¿Qué valores de `x` imprimen el hijo y el padre? Justifique. (4 pts)

```c
int main() {
    int x = 5;
    pid_t pid = fork();
    if (pid == 0) {
        x += 15;
        printf("hijo: %d\n", x);
        return 0;
    }
    wait(NULL);
    printf("padre: %d\n", x);
    return 0;
}
```

d) En la planificación por prioridades, ¿qué es la **inanición** y cómo se evita? (4 pts)

e) Explique qué hacen los planificadores de **largo**, **corto** y **mediano** plazo. ¿Cuál se ejecuta con mayor frecuencia y por qué? (5 pts)
