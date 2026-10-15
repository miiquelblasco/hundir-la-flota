# Hundir la flota

Versión en Python del clásico juego de mesa **Hundir la flota**, para jugar desde la terminal contra la máquina.

## Cómo ejecutarlo

Necesitas Python 3 y la librería `numpy`:

```bash
pip install numpy
```

Después, desde la carpeta del proyecto:

```bash
python main.py
```

## Cómo se juega

- Cada jugador tiene un tablero de 10x10 con **6 barcos** colocados al azar: 3 de eslora 2, 2 de eslora 3 y 1 de eslora 4.
- Al empezar se muestra tu tablero con tus barcos.
- En tu turno ves el tablero de la máquina **sin sus barcos**, solo con tus disparos anteriores, y escribes la casilla a la que quieres disparar con el formato `fila,columna`, con números del 1 al 10. Por ejemplo: `3,7`.
- Si aciertas, vuelves a disparar. Si disparas a una casilla repetida, también repites sin perder el turno. Si das en agua, pasa el turno a la máquina.
- La máquina dispara al azar a tu tablero, con las mismas reglas.
- Cuando todas las casillas de un barco han sido tocadas, se avisa de que ese barco está **hundido**.
- Gana quien hunda primero todos los barcos del rival.

### Símbolos del tablero

| Símbolo | Significado |
|:-:|---|
| `-` | Casilla sin disparar |
| `o` | Barco (solo se ven los tuyos) |
| `x` | Barco tocado |
| `A` | Agua |

## Estructura del proyecto

```
main.py    -> flujo de la partida: preparación, turnos y fin del juego
utils.py   -> funciones y clase Barco con la lógica del juego
```

## Cómo está hecho

### Tablero

El tablero es un array de `numpy` de 10x10 lleno de `-`, creado con `crear_tablero()`. Internamente todas las coordenadas empiezan en 0, como los índices de numpy; solo se convierten a base 1 al hablar con el jugador (al leer su entrada y al mostrar mensajes).

### La clase `Barco`

Cada barco es un objeto que guarda su **eslora** y sus **coordenadas**. El método `crear_barco(tablero)` le asigna una posición aleatoria válida:

1. Elige al azar si el barco es horizontal o vertical.
2. Elige la casilla inicial limitando el rango del `randint` según la eslora (`11 - eslora`), de forma que el barco **nunca puede salirse del tablero**.
3. Comprueba que todas sus casillas estén libres. Si alguna está ocupada, descarta esa posición y prueba otra dentro de un bucle `while`, hasta encontrar un hueco válido.
4. Guarda las casillas en el propio objeto (`self.coordenadas`).

### Colocar la flota

`colocar_flota(flota, tablero)` recorre la lista de barcos y, para cada uno, primero calcula su posición y después lo pinta en el tablero con `colocar_barcos`. El orden es importante: como cada barco se pinta antes de crear el siguiente, el siguiente ya "ve" los anteriores y los barcos nunca se superponen.

### Disparar

`disparar(casilla, tablero)` cambia la casilla a `x` si había un barco o a `A` si era agua, y devuelve el resultado (`"Tocado"`, `"Agua"` o `"Repetido"`). Ese resultado es lo que usa el bucle de turnos para decidir si el jugador repite o pasa el turno.

### Barcos hundidos

Como cada barco recuerda sus coordenadas, `comprobar_hundido(casilla, flota, tablero)` busca qué barco contiene la casilla tocada y revisa si todas sus casillas son ya `x`. Así se puede saber qué barco se ha hundido aunque esté pegado a otro.

### Flujo de la partida (`main.py`)

- Un bucle principal se repite mientras los dos tableros sigan teniendo alguna `o` (se cuentan con `np.sum(tablero == "o")`).
- Dentro, el turno del jugador y el de la máquina son bucles propios, porque se sigue disparando mientras no se falle.
- La victoria se comprueba justo después de cada turno, para que el perdedor no siga disparando cuando ya no le quedan barcos al rival.
- El tablero de la máquina se enseña con `np.where(tablero_ia == "o", "-", tablero_ia)`, que crea una copia donde sus barcos aparecen como agua sin disparar.

## Limitaciones

**La entrada del jugador no está validada.** El juego espera exactamente dos números del 1 al 10 separados por una coma. Si se escribe otra cosa:

- Texto, letras o un formato distinto (por ejemplo `hola` o `3`) hacen que el programa se cierre con un error.
- Un número mayor que 10 (por ejemplo `11,5`) también cierra el programa.
- Un `0` no da error, pero por cómo numpy trata los índices negativos, el disparo acaba en la **fila o columna 10** sin avisar.

Una mejora futura sería una función que pida las coordenadas dentro de un bucle, compruebe el formato y el rango (usando `try`/`except` para los valores no numéricos) y vuelva a preguntar hasta recibir una entrada válida.
