import pygame

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
	tab = pygame.Surface((160,160))
	tab.fill(GRIS)
	pygame.draw.line(tab,MARRON,(0,0),(160,160),14)
	pygame.draw.line(tab,MARRON,(160,0),(0,160),14)
	pantalla.blit(tab,(120+200*(posX),120+200*(posY)))
	pygame.display.flip()


def dibujarO(posY: int, posX: int):
	tab = pygame.Surface((160,160))
	tab.fill(GRIS)
	pygame.draw.circle(tab,MARRON,(80,80),80,10)
	pantalla.blit(tab,(120+200*(posX),120+200*(posY)))
	pygame.display.flip()


#Inicio pygame
#pygame.init()
#dibujarTableroVacio()
#for i in range(0,3):
#	for j in range(0,3):
#		dibujarO(i,j)
#x = int(input(""))
#pygame.quit()