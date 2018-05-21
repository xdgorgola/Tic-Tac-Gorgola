tableroVieja = [["v","v","v"],
                ["v","v","v"],
                ["v","v","v"]]


#CONSIDERACIONES RESPECTO AL TABLERO:
# "v": Casilla vacia
# "j": Jugador
# "c": Computadora


#Simplemente pide y refleja una jugada *valga la redundancia* del jugador
def elegirJugada(turno: str, tablero: [[str]]):
    while True:
        jugada = (int(input("Fila: ")),int(input("Columna: ")))
        try:
            assert(0 <= jugada[0] <= 2 and 0 <= jugada[1] <= 2)
            break
        except:
            print("Rango de valores permitidos: 0-2.\nVolviendo a intentar...")
    tablero[jugada[0]][jugada[1]] = turno


#Chequea si en una columna si gano el jugador "turno"
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


#Chequea si en una fila si gano el jugador "turno"
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


#Chequea si el jugador "turno" gano en la diagonal /
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


#Chequea si el jugador "turno" gano en la diagonal \
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


#Chequea si hay un ganador o empate
#TODO-LIST
#Los chequeos de las diagonales se pueden hacer de primero o afuera del for, no hay necesidad de hacerlos todo el tiempo!
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
    #Chequea si no hay casillas vacias y aun no hay ganador para declarar un empate
    if not(any(any(tablero[i][j] == "v" for j in range(0,3)) for i in range(0,3))) and ganador == "nadie":
        return("empate")

    return ganador


#Printea de forma bonita el tablero
def tableroConsola(tablero: [[str]]):
    for i in tablero:
        print(i)
    print("\n\n\n")


#No lo uso en ningun momento????
def printHijo(child: [[[str]]]):
    for i in child:
        for j in i:
            print(j)
        print("\n")


#Retorna todas las posibles jugadas que puede hacer el jugador "turno" en un estado
def posiblesJugadas(tablero: [[str]], turno: str):
    derivados = []
    for i in range(0,3):
        for j in range(0,3):
            tab3 = list(map(list,tablero))
            if tablero[i][j] == "v":
                tab3[i][j] = turno
                derivados.append(tab3)
    return derivados 



#Algoritmo de minimax para determinar la mejor jugada de la computadora!
#TODO-LIST
#El parametro ganador no se usa nunca, quitarlo
#Explicar brevemente el funcionamiento del algoritmos
#Mejorar la condicion terminal con profundidad_actual
#PARAMETROS:
#   tablero: Tablero del juego
#   profundidad_actual: Que tanto va a explorar el algoritmo los posibles estados de la partidad
#   compu: Indica si es el turno de la computadora o el jugador
#
def miniMax(tablero: [[str]], profundidad_actual = 6, compu = True, ganador = "nadie"):
    #print("profundidad_actual: %s"%profundidad_actual)
    #tableroConsola(tablero)
    if profundidad_actual == 0 or chequeTotal(tablero) != "nadie":
        if chequeTotal(tablero) == "c":
            #print("gana compu!!")
            #tableroConsola(tablero)
            return 999+profundidad_actual
        elif chequeTotal(tablero) == "j":
            #print("gana jugador!")
            #tableroConsola(tablero)
            return -999
        #En caso de que no se llegue a un estado terminal
        return 0

    #Turno de la computadora, se trata de maximizar su puntuacion
    if compu:
        #No seria mejor default value o worst?
        bestValue = 0
        for child in posiblesJugadas(tablero,"c"):
            #print("child c")
            #tableroConsola(child)
            v = miniMax(child,profundidad_actual-1,False)
            print(v)
            bestValue = max(bestValue,v)
            #print("best value compu")
            #print(bestValue)
            tableroConsola(child)
        return bestValue
    
    #Turno del jugador, se trata de minimizar su puntuacion
    elif not(compu):
        bestValue = 0
        for child in posiblesJugadas(tablero,"j"):
            #print("child j")
            #tableroConsola(child)
            v = miniMax(child,profundidad_actual-1,True)
            bestValue = min(bestValue,v)
            #print("best value jugador")
            #print(bestValue)
            tableroConsola(child)
        return bestValue


#Turno de la computadora
#TODO-LIST!
#Explicar como funciona brevemente
#Chequear si se puede mejorar
def turnoCompu(tablero: [[str]]):
    puntos = []
    for i in range(0,3):
        tabAux = list(map(list,tablero))
        for j in range(0,3):
            tabAux2 = list(map(list,tabAux))
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


#LOOP del juego
#TODO-LIST
#Convertirlo en una funcion!
#Hacer una funcion que reinicie el tablero!
#Hacer que finalice!
resp = None
turno = "j"
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