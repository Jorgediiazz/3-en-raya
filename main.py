import os
t1=[[1,1,0],[0,0,1],[0,5,5]]
t2=[[1,1,1],[0,0,1],[0,5,5]]
t3=[[5,1,0],[5,0,1],[5,1,5]]
t4=[[0,1,0],[0,1,5],[0,1,5]]
t5=[[5,1,5],[1,5,5],[1,5,1]]

#Esta funcion inicializa un tablero
def inicializarTablero():
    return [[0,0,0],[0,0,0],[0,0,0]]

#Esta funcion nos pinta un tablero dado un tablero
def pintartablero(tablero):
    os.sysitem("clear")
    print(Tablero:)
    for i in range(0,len(tablero)):
        salida=""
        for j in range(0,len(tablero[i])):
            valor=tablero[i][j]
            salida+="|"
            if(valor==1):
                salida+=("X")
            elif(valor == 5):
                salida+=("O")
            else:
                salida+=(" ")
        salida += "|"
        print(salida)

def sumaFila(n,tablero):
    return sum(tablero[n])

def sumaColumna(n,tablero):
    for i in tablero:
        result=tablero[0][n]+tablero[1][n]+tablero[2][n]
    return result

def ganador(tablero):
    result1=""
    result2=""
    result3=""
    dev1=False
    dev2=False
    dev3=False
    f1=sumaFila(0,tablero)
    f2=sumaFila(1,tablero)
    f3=sumaFila(2,tablero)
    c1=sumaColumna(0,tablero)
    c2=sumaColumna(1,tablero)
    c3=sumaColumna(2,tablero)
    d1=sum([tablero[0][0], tablero[1][1], tablero[2][2]])
    d2=sum([tablero[0][2], tablero[1][1], tablero[2][0]])
    if(f1==3 or f2==3 or f3==3 or c1==3 or c2==3 or c3==3 or d1==3 or d2==3):
        dev1=True
        result1="El ganador es el jugador 1"
        return result1
    else:
        if(f1==15 or f2==15 or f3==15 or c1==15 or c2==15 or c3==15 or d1==15 or d2==15):
            dev2=True
            result2="El ganador es el jugador 2"
            return result2
        else:
            if(f1>3 and f2>3 and f3>3 and d1>3 and d2>3):
                dev3=True
                result3="El juego se ha terminado en empate"
                return result3


# Devuelve la columna n del tablero
def columna(n, tablero):
    return [tablero[0][n], tablero[1][n], tablero[2][n]]

# Devuelve True o False si ha colocado la pieza en la posción
def colocarPieza(jug, pos, tablero):
    if(pos=="a0"):
        tablero[0][0]==jug
    elif(pos=="a1"):
        tablero[0][1]==jug
    elif(pos=="a2"):
        tablero[0][2]==jug
    elif(pos=="b0"):
        tablero[1][0]==jug
    elif(pos=="b1"):
        tablero[1][1]==jug
    elif(pos=="b2"):
        tablero[1][2]==jug
    elif(pos=="c0"):
        tablero[2][0]==jug
    elif(pos=="c1"):
        tablero[2][1]==jug
    elif(pos=="c2"):
        tablero[2][2]==jug


# Devuelve True o False si hay una pieza en la posición
def hayPieza(pos, tablero):
    if(pos=="a0"):
        return tablero[0][0]!=0
    elif(pos=="a1"):
        return tablero[0][1]!=0
    elif(pos=="a2"):
        return tablero[0][2]!=0
    elif(pos=="b0"):
        return tablero[1][0]!=0
    elif(pos=="b1"):
        return tablero[1][1]!=0
    elif(pos=="b2"):
        return tablero[1][2]!=0
    elif(pos=="c0"):
        return tablero[2][0]!=0
    elif(pos=="c1"):
        return tablero[2][1]!=0
    elif(pos=="c2"):
        return tablero[2][2]!=0
def jugar(jugador_actual, tablero):
    if(jugador_actual==1):
        print("juega el jugador 1")




print("Jugador 1: X")
print("Jugador 2: O")
pintartablero(t5)
print(ganador(t5))
