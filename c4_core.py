import numpy as np

# Crear tabla
def crear_tablero():
    return np.zeros((6, 7), dtype=int)

# Mostrar el tablero
def mostrar_tablero(tablero):
    for fila in range(6):
        linea = ""
        for col in range(7):
            if tablero[fila, col] == 0:
                linea = linea + " . "
            elif tablero[fila, col] == 1:
                linea = linea + " X "
            else:
                linea = linea + " O "
        print(linea)

# Colocar ficha 
def colocar_ficha(tablero, columna, jugador):
    fila = 5 
    colocado = False
    while fila >= 0 and not colocado:
        if tablero[fila, columna] == 0:
            tablero[fila, columna] = jugador
            colocado = True
        else:
            fila = fila - 1
    return colocado

# Verificar si una columna es válida
def columna_valida(tablero, columna):
    if columna < 0 or columna > 6:
        return False
    if tablero[0, columna] != 0:
        return False
    return True

# Ver si alguien a ganado
def hay_ganador(tablero, jugador):
    for fila in range(6):
        for col in range(4):
            if (tablero[fila, col] == jugador and tablero[fila, col+1] == jugador and tablero[fila, col+2] == jugador and tablero[fila, col+3] == jugador):
                return True
    for fila in range(3):
        for col in range(7):
            if (tablero[fila, col] == jugador and tablero[fila+1, col] == jugador and tablero[fila+2, col] == jugador and tablero[fila+3, col] == jugador):
                return True
    for fila in range(3):
        for col in range(4):
            if (tablero[fila, col] == jugador and tablero[fila+1, col+1] == jugador and tablero[fila+2, col+2] == jugador and tablero[fila+3, col+3] == jugador):
                return True
    for fila in range(3, 6):
        for col in range(4):
            if (tablero[fila, col] == jugador and tablero[fila-1, col+1] == jugador and tablero[fila-2, col+2] == jugador and tablero[fila-3, col+3] == jugador):
                return True
    return False

# Ver si la tabla esta llena
def tablero_lleno(tablero):
    for fila in range(6):
        for col in range(7):
            if tablero[fila, col] == 0:
                return False
    return True
