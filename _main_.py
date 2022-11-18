import funciones

def main():
    jugador_actual=1
    tablero=funciones.inicializarTablero()

    while(True):
        if(funciones.ganador(tablero)==1):
            print("Gana el jugador 1")
            break
        if(funciones.ganador(tablero)==5):
            print("Gana el jugador 2")
            break
        if(funciones.ganador(tablero)==0):
            print("El juego se ha terminado en empate")
            break
        else:
            funciones.pintartablero(tablero)
            jugador_actual=funciones.jugar(jugador_actual,tablero)