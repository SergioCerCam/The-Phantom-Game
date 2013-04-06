# -*- coding: utf-8 -*-

#-Importo las librerias:

import pygame, sys
from pygame.locals import *

#---Inicio pygame:

pygame.init()

#---Creo la ventana donde se vera el juego:

Ancho = 700
Alto = 429

#---Funcion fondo pantalla
def load_image(filename, transparent=False):
    try: image = pygame.image.load(filename)
    except pygame.error, message:
        raise SystemExit, message
    image = image.convert()
    if transparent:
        color = image.get_at((0,0))
        image.set_colorkey(color, RLEACCEL)
    return image


#---Funcion para el texto de la pantalla
def texto(texto, posx, posy, color=(255,255,255), tam=30):
    fuente = pygame.font.Font("METAG.ttf", tam)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect

#---Funcion para salir utilizando la tecla escape y a traves del menu:

def salir(keys):
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            sys.exit(0)
        if keys[K_ESCAPE]:
            sys.exit(0)

#---Funcion para crear el menu principal del juego

def menu(screen, select):

        if select == 1:
                empezarjuego, empezarjuegox = texto("Empezar Partida", Ancho/1-180, Alto/1-120, (255, 0, 0))
                salirse, salirsex = texto("Salir", Ancho/1-300, Alto/1-80)

        if select == 2:
                empezarjuego, empezarjuegox = texto("Empezar Partida", Ancho/1-180, Alto/1-120)
                salirse, salirsex = texto("Salir", Ancho/1-300, Alto/1-80, (255, 0, 0))
        
        screen.blit(empezarjuego, empezarjuegox)
        screen.blit(salirse, salirsex)



#---Funcion principal
def main():
    
    screen = pygame.display.set_mode((Ancho, Alto))

#---Le pongo un titulo a la ventana del juego que se vera arriba:

    pygame.display.set_caption('Snake Eater')

#---Le pongo una imagen de fondo a la ventana:

    background_image = load_image('fondo.jpg')

#---Añado una musica introductoria para el menu:
    
    pygame.mixer.music.load("menu.mp3")

#---Añado un -1 para que cuando acabe la musica vuelva a empezar:

    pygame.mixer.music.play(-1)

#---Especifico que al presionar la tecla enter salga del juego:
    
    select = 1
    
    while True:
        keys = pygame.key.get_pressed()
        salir(keys)
        
        if keys[K_UP] and select > 1:
            select -=1
	if keys[K_DOWN] and select < 2:
	    select +=2

        elif keys[K_SPACE]:
            if select == 2:
                sys.exit()
                
        screen.blit(background_image, (0, 0))
	menu(screen, select)
        pygame.display.flip()

    return 0
    
if __name__== '__main__':
    main()


