# -*- coding: utf-8 -*-

#-Importo las librerias:

import pygame
from pygame.locals import *

#---Inicio pygame:

pygame.init()

#---Creo la ventana donde se vera el juego:

ventana=(600,450)

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

#---Funcion
def main():
    
    screen = pygame.display.set_mode((ventana))

#---Le pongo un titulo a la ventana del juego que se vera arriba:

    pygame.display.set_caption('The Phantom Game')

#---Le pongo una imagen de fondo a la ventana:

    background_image = load_image('fondo.jpg')

#---Creo un bucle para que se pueda cerrar la ventana al darle a la x:

    salir=False
    while not salir:
        for event in pygame.event.get():
            if event.type == QUIT:
                salir=True

#---Especifico la posion de la imagen de fondo:
                
        screen.blit(background_image, (0, 0))
        pygame.display.flip()

    return 0
    
if __name__== '__main__':
    main()

