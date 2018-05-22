import pygame
#import Tic-Tac

FPS = 30

#Colores
NEGRO = (0, 0, 0)
GRIS = (186, 184, 184)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
VERDE_ALT = (0, 148, 50)
VERDE_OSCURO = (0, 100, 0)
AZUL = (0, 0, 255)
ARENA = (206,204,126)
MARRON = (128,112,68)

#Ventana
ANCHO = 800
ALTO = 800

#Fuente
pygame.font.init()
sans = pygame.font.SysFont('Comic Sans MS', 100)
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Tic-Tac Toe")
pantalla.fill(BLANCO)


#Dibuja un tablero vacio
def dibujarTableroVacio():
	pantalla.fill(BLANCO)
	tab = pygame.Surface((600,600))
	tab.fill(GRIS)
	for i in range(0,2):
		pygame.draw.line(tab,NEGRO,(200*(i+1),0),(200*(i+1),600),8)
		pygame.draw.line(tab,NEGRO,(0,200*(i+1)),(600,200*(i+1)),8)
	pantalla.blit(tab,(100,100))
	pygame.display.flip()


def dibujarX(posY: int, posX: int):
	tab = pygame.Surface((194,194))
	tab.fill(GRIS)
	pygame.draw.line(tab,MARRON,(0,0),(194,194),8)
	pygame.draw.line(tab,MARRON,(194,0),(0,194),8)
	pantalla.blit(tab,(100*(posX+1),100*(posY+1)))
	pygame.display.flip()


#Inicio pygame
pygame.init()
dibujarTableroVacio()
dibujarX(0,0)
x = int(input(""))
pygame.quit()