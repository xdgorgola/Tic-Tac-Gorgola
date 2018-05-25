import pygame
import IGT

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


#Retorna todas las posibles jugadas que puede hacer el jugador "turno" en un estado
def posiblesJugadas(tablero: [[str]], turno: str):
    derivados = []
    for i in range(0,3):
        for j in range(0,3):
            if tablero[i][j] == "v":
                derivados.append((i,j))
    return derivados 


def casillasVacias(tablero: [[str]]):
    c = 0
    for i in range(0,3):
        for j in range(0,3):
            if tablero[i][j] == "v":
                c = c + 1
    return c


#Algoritmo de minimax para determinar la mejor jugada de la computadora!
#TODO-LIST
#El parametro ganador no se usa nunca, quitarlo
#Explicar brevemente el funcionamiento del algoritmo ALPHA/BETA
#Cambiar nombre a minimaxAB
#PARAMETROS:
#   tablero: Tablero del juego
#   profundidad_actual: Que tanto va a explorar el algoritmo los posibles estados de la partidad
#   compu: Indica si es el turno de la computadora o el jugador
#

def miniMax(tablero: [[str]], profundidad_actual = 9, compu = True, alpha = -900, beta = 900):
    if chequeTotal(tablero) == "c":
        #print("gana compu!!wo")
        #tableroConsola(tablero)
        return 10+profundidad_actual
    elif chequeTotal(tablero) == "j":
        #print("gana jugador :(")
        #tableroConsola(tablero)
        return -10
    elif chequeTotal(tablero) == "empate":
        #print("hay empate")
        #tableroConsola(tablero)
        return 0
    
    #Turno de la computadora, se trata de maximizar su puntuacion
    if compu:
        bestValue = -900
        jugadasPos = posiblesJugadas(tablero,"c")
        for jugadas in jugadasPos:
            tabAux = list(map(list,tablero))
            tabAux[jugadas[0]][jugadas[1]] = "c"
            value = miniMax(tabAux,profundidad_actual-1,False,alpha,beta)
            bestValue = max(bestValue,value)
            alpha = max(alpha, bestValue)
            if beta <= alpha:
                break
        return bestValue
    
    #Turno del jugador, se trata de minimizar su puntuacion
    elif not(compu):
        bestValue = 900
        jugadasPos = posiblesJugadas(tablero,"j")
        for jugadas in jugadasPos:
            tabAux = list(map(list,tablero))
            tabAux[jugadas[0]][jugadas[1]] = "j"
            value = miniMax(tabAux,profundidad_actual-1,True,alpha,beta)
            bestValue = min(bestValue,value)
            beta = min(beta,bestValue)
            if beta <= alpha:
                break
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
                puntos.append([(i,j),miniMax(tabAux2,9,False,-900,900)])
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



def posClicks(click_event: (int,int)):
    print(click_event)
    mouseX, mouseY = click_event
    listoX, listoY = False, False
    for i in range(0,3):
        if (not(listoX) or not(listoY)):
            if (100+200*i) <= mouseX <= (100+200*(i+1)):
                posibX = i
                listoX = True
            if (100+200*i) <= mouseY <= (100+200*(i+1)):
                posibY = i
                listoY = True
    if listoY and listoX:
        return posibX, posibY



#CONSIDERACIONES RESPECTO AL TABLERO:
# "v": Casilla vacia
# "j": Jugador
# "c": Computadora
tableroVieja = [["v","v","v"],
                ["v","v","v"],
                ["v","v","v"]]

#LOOP del juego
#TODO-LIST
#Convertirlo en una funcion!
#Hacer una funcion que reinicie el tablero!
#Hacer que finalice!
resp = None
turno = "j"
pygame.init()
IGT.dibujarTableroVacio()

#Variable del ciclo
jugando = True
while jugando:
    if turno == "j":
        seleccionando = True
        #TECLAS/MOUSE
        while seleccionando:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        seleccionando, jugando = False, False
                elif event.type == pygame.QUIT:
                    seleccionando, jugando = False, False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #Si el click esta dentro del tablero, procede a calcular sus posiciones respectivas
                    #en el tablero logico
                    if 100 <= event.pos[0] <= 100+200*3 and 100 <= event.pos[1] <= 100+200*3:
                        posX, posY = posClicks(event.pos)
                        IGT.dibujarX(posY,posX)
                        tableroVieja[posY][posX] = "j"
                        turno = "c"
                        seleccionando = False
    elif turno == "c":
        jugada = turnoCompu(tableroVieja)
        print("jugada final: ",jugada)
        tableroVieja[jugada[0]][jugada[1]] = "c"
        turno = "j"
        IGT.dibujarO(jugada[0],jugada[1])
    print("\n tablero post jugada!")
    tableroConsola(tableroVieja)
pygame.quit()