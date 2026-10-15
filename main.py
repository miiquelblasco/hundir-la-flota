import numpy as np
import utils as fnc

esloras = [2, 2, 2, 3, 3, 4]

tablero_jugador = fnc.crear_tablero()
flota_jugador = [fnc.Barco(eslora, []) for eslora in esloras]
tablero_jugador = fnc.colocar_flota(flota_jugador, tablero_jugador)

print("Jugador, este es tu tablero:")
print(tablero_jugador)

tablero_ia = fnc.crear_tablero()
flota_ia = [fnc.Barco(eslora, []) for eslora in esloras]
tablero_ia = fnc.colocar_flota(flota_ia, tablero_ia)

while np.sum(tablero_jugador == "o") != 0 and np.sum(tablero_ia == "o") != 0:
    print("---------------- Turno del jugador ---------------")
    print("Tus jugadas anteriores:")
    print(np.where(tablero_ia == "o", "-", tablero_ia))
    peticion_jugador = input("Fila, columna:")
    coordenadas_jug = peticion_jugador.split(",")
    x,y = coordenadas_jug
    x = int(x) - 1
    y = int(y) - 1
    coordenadas_jug = [x, y]
    resultado_jug = fnc.disparar(coordenadas_jug, tablero_ia)
    if resultado_jug[1] == "Tocado" and fnc.comprobar_hundido(coordenadas_jug, flota_ia, tablero_ia):
        print("Has hundido un barco")

    while resultado_jug[1] != "Agua" and np.sum(tablero_ia == "o") != 0:
        peticion_jugador = input("Fila, columna:")
        coordenadas_jug = peticion_jugador.split(",")
        x,y = coordenadas_jug
        x = int(x) - 1
        y = int(y) - 1
        coordenadas_jug = x,y
        resultado_jug = fnc.disparar(coordenadas_jug, tablero_ia)
        if resultado_jug[1] == "Tocado" and fnc.comprobar_hundido(coordenadas_jug, flota_ia, tablero_ia):
            print("Has hundido un barco")

    if np.sum(tablero_ia == "o") == 0:
        print("El jugador gana la partida")
        break

    print("---------------- Turno de la IA ----------------")
    coordenadas_ia = [np.random.randint(0,10), np.random.randint(0,10)]
    resultado_ia = fnc.disparar(coordenadas_ia, tablero_jugador)
    if resultado_ia[1] == "Tocado" and fnc.comprobar_hundido(coordenadas_ia, flota_jugador, tablero_jugador):
                print("La IA ha hunidido uno de tus barcos.")

    while resultado_ia[1] != "Agua" and np.sum(tablero_jugador == "o") != 0:
        coordenadas_ia = [np.random.randint(0,10), np.random.randint(0,10)]
        resultado_ia = fnc.disparar(coordenadas_ia, tablero_jugador)
        if resultado_ia[1] == "Tocado" and fnc.comprobar_hundido(coordenadas_ia, flota_jugador, tablero_jugador):
            print("La IA ha hunidido uno de tus barcos.")

    if np.sum(tablero_jugador == "o") == 0:
        print("La IA gana la partida")
        break




        

