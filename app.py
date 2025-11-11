from c4_core import *

def pedir_columna():
    valido = False
    while not valido:
        print("Escribe la clumna que quieres seleccionar (entre 0 y 6): ")
        entrada = input()
        if entrada in ["0", "1", "2", "3", "4", "5", "6"]:
            return int(entrada)
        else:
            print("Esa columna no existe")

def jugar():
    print("--- Conectar 4 fichas ---")
    tablero = crear_tablero()
    turno = 1
    juego_activo = True

    while juego_activo:
        mostrar_tablero(tablero)
        print("Le toca al jugador", turno)

        col = pedir_columna()

        if columna_valida(tablero, col):
            exito = colocar_ficha(tablero, col, turno)

            if hay_ganador(tablero, turno):
                mostrar_tablero(tablero)
                print("El jugadorr", turno, "ha ganado , pringao")
                juego_activo = False
            elif tablero_lleno(tablero):
                mostrar_tablero(tablero)
                print("Es un empate , que pena eh")
                juego_activo = False
            else:
                if turno == 1:
                    turno = 2
                else:
                    turno = 1
        else:
            print("Esa columna no existe o esta llena , elige otra")
if __name__ == "__main__":
    jugar()
