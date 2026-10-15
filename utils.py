import numpy as np

def crear_tablero(tamano = 10):
    tablero = np.full((tamano, tamano), "-")
    return tablero

def colocar_barcos(barco, tablero):
    for celda in barco:
        x,y = celda
        if x > 9 and y > 9:
            raise ValueError(f"Alguna de las celdas excede el tamaño del tablero: ({x},{y})")
        if tablero[x,y] != "-":    
            raise ValueError(f"Alguna de las celdas seleccionadas ya ha sido ocupada: ({x},{y})")
        tablero[x,y] = "o"
    return tablero    

def colocar_flota(flota, tablero):
    for barco in flota:
        casillas = barco.crear_barco(tablero)   # pide posición mirando el tablero actual
        colocar_barcos(casillas, tablero)       # pinta ese barco en el tablero
    return tablero

def disparar(casilla, tablero):
    x,y = casilla
    if tablero[x,y] == "o": 
        tablero[x,y] = "x"
        print(f"Barco tocado en ({x+1},{y+1})")
        resultado = "Tocado"
        return tablero, resultado
    if tablero[x,y] == "x" or tablero[x,y] == "A":
        print(f"La casilla ({x+1},{y+1}), ya había sido disparada")
        resultado = "Repetido"
        return tablero, resultado
    tablero[x,y] = "A"
    print(f"Ningun barco ha sido tocado en ({x+1},{y+1})")
    resultado = "Agua"
    return tablero, resultado

def comprobar_hundido(casilla, flota, tablero):
    casilla = tuple(casilla)                  
    for barco in flota:                       
        if casilla in barco.coordenadas:      
            for c in barco.coordenadas:     
                if tablero[c] != "x":        
                    return False              
            return True                       
    return False                              

class Barco:
    def __init__(self, eslora, coordenadas):
        self.eslora = eslora
        self.coordenadas = coordenadas

        
    def crear_barco(self, tablero):
        horizontal = bool(np.random.randint(0,2))
        if horizontal:
            en_proceso = True
            while en_proceso:
                y = np.random.randint(0, ((11 - self.eslora)))
                x = np.random.randint(0, 10)
                lista = []
                for i in range(self.eslora):
                    if tablero[x,(y+i)] != "-":   
                        break
                    lista.append((x,(y+i)))
                if len(lista) == self.eslora:
                    en_proceso = False
            self.coordenadas = lista        
            return lista

        if not horizontal:
            en_proceso = True
            while en_proceso:
                y = np.random.randint(0, 10)
                x = np.random.randint(0, (11 - self.eslora))
                lista = []
                for i in range(self.eslora):
                    if tablero[(x + i),y] != "-":   
                        break
                    lista.append(((x + i),y))
                if len(lista) == self.eslora:
                    en_proceso = False
            self.coordenadas = lista
            return lista
        

