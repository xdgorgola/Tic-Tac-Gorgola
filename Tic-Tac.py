import copy 
#tableroVieja = [["v","v","v"],
#                ["v","v","j"],
#                ["c","j","j"]]

#PRUEBA
#
#

tableroVieja = [["v","v","v"],
                ["v","v","v"],
                ["v","v","v"]]


def elegirJugada(turno: str, tablero: [[str]]):
    jugada = (int(input("fila> ")),int(input("columna> ")))
    tablero[jugada[0]][jugada[1]] = turno

def chequeoVertical(columna: int, tablero: [[str]], turno: str):
    contador = 0
    for i in range(0,3):
        if tablero[i][columna] == turno:
            contador = contador + 1
    if contador == 3:
        ganador = turno
    else:
        ganador = "nadie"
    return ganador


def chequeoHorizontal(fila: int, tablero: [[str]], turno: str):
    contador = 0
    for i in range(0,3):
        if tablero[fila][i] == turno:
            contador = contador + 1
    if contador == 3:
        ganador = turno
    else:
        ganador = "nadie"
    return ganador


def chequeoDiagonalDer(tablero: [[str]], turno: str):
    contador = 0
    for i in range(0,3):
        if tablero[i][i] == turno:
            contador = contador + 1
    if contador == 3:
        ganador = turno
    else:
        ganador = "nadie"
    return ganador


def chequeoDiagonalIzq(tablero: [[str]], turno: str):
    contador = 0
    for i in range(0,3):
        if tablero[2-i][i] == turno:
            contador = contador + 1
    if contador == 3:
        ganador = turno
    else:
        ganador = "nadie"
    return ganador


def chequeTotal(tablero: [[str]]):
    ganador = "nadie"
    for i in range(0,3):
        for j in range(0,3):
            if tablero[i][j] != "v":
                if ganador == "nadie":
                    ganador = chequeoVertical(j,tablero,tablero[i][j])
                if ganador == "nadie":
                    ganador = chequeoHorizontal(i,tablero,tablero[i][j])
                if ganador == "nadie":
                    ganador = chequeoDiagonalIzq(tablero, tablero[i][j])
                if ganador == "nadie":
                    ganador = chequeoDiagonalDer(tablero, tablero[i][j])
            elif tablero[i][j] == "v":
                pass
    if not(any(any(tablero[i][j] == "v" for j in range(0,3)) for i in range(0,3))) and ganador == "nadie":
        return("empate")

    return ganador


def tableroConsola(tablero: [[str]]):
    for i in tablero:
        print(i)
    print("\n\n\n")


def printHijo(child: [[[str]]]):
    for i in child:
        for j in i:
            print(j)
        print("\n")


def posiblesJugadas(tablero: [[str]], turno: str):
    derivados = []
    for i in range(0,3):
        for j in range(0,3):
            tab3 = copy.deepcopy(tablero)
            if tablero[i][j] == "v":
                tab3[i][j] = turno
                derivados.append(tab3)
    return derivados 


def miniMax(tablero: [[str]], profundidad_actual = 6, compu = True, ganador = "nadie"):
    print("profundidad_actual: %s"%profundidad_actual)
    tableroConsola(tablero)
    if profundidad_actual == 0 or chequeTotal(tablero) != "nadie":
        if chequeTotal(tablero) == "c":
            print("gana compu!!")
            tableroConsola(tablero)
            return 999+profundidad_actual
        elif chequeTotal(tablero) == "j":
            print("gana jugador!")
            tableroConsola(tablero)
            return -999
        return 0
        #elif chequeTotal(tablero) == "empate":
        #    tableroConsola(tablero)
        #    print("empate")
        #    return 0
        #elif chequeTotal(tablero) == "nadie" and profundidad_actual == 0:
        #    tableroConsola(tablero)
        #    print("nadie gana")
        #    return 0

    if compu:
        bestValue = 0
        for child in posiblesJugadas(tablero,"c"):
            #print("child c")
            #tableroConsola(child)
            v = miniMax(child,profundidad_actual-1,False)
            print(v)
            bestValue = max(bestValue,v)
            print("best value compu")
            print(bestValue)
            tableroConsola(child)
        return bestValue
    
    elif not(compu):
        bestValue = 0
        for child in posiblesJugadas(tablero,"j"):
            #print("child j")
            #tableroConsola(child)
            v = miniMax(child,profundidad_actual-1,True)
            bestValue = min(bestValue,v)
            print("best value jugador")
            print(bestValue)
            tableroConsola(child)
        return bestValue


def turnoCompu(tablero: [[str]]):
    puntos = []
    tabAux = copy.deepcopy(tablero)
    for i in range(0,3):
        tabAux = copy.deepcopy(tablero)
        for j in range(0,3):
            tabAux2 = copy.deepcopy(tabAux)
            if tabAux2[i][j] == "v":
                tabAux2[i][j] = "c"
                puntos.append([(i,j),miniMax(tabAux2,4,False)])
                print("xdddddddddddddddddd")
                print(puntos)
    maxJ = puntos[0][0]
    maxP = puntos[0][1]         
    for puntuaciones in puntos:
        print(puntuaciones, "maxP = ", maxP, "maxJ = ", maxJ)
        print(puntuaciones[1])
        if max(maxP, puntuaciones[1]) == maxP:
            pass
        elif max(maxP, puntuaciones[1]) != maxP:
            maxP = puntuaciones[1]
            maxJ = puntuaciones[0]
    print(maxJ)
    return maxJ

resp = None
turno = "c"
while resp != 3:
    tableroConsola(tableroVieja)
    if turno == "j":
        f = int(input("fila> "))
        c = int(input("columna> "))
        tableroVieja[f][c] = "j"
        turno = "c"
    elif turno == "c":
        jugada = turnoCompu(tableroVieja)
        print("jugada final: ",jugada)
        tableroVieja[jugada[0]][jugada[1]] = "c"
        turno = "j"
    print("\n tablero post jugada!")
    tableroConsola(tableroVieja)
    resp = int(input("3 para salir> "))