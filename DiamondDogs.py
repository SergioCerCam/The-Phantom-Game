# -*- coding: utf-8 -*-

#-Importo las librerias:

import pygame
from pygame.locals import *

#---Inicio pygame:

pygame.init()

#---Creo la ventana donde se vera el juego:

ventana=(690,480)
area = pygame.display.set_mode(ventana)


#---Funcion
def main():
    
    screen = pygame.display.set_mode((ventana))

#---Le pongo un titulo a la ventana del juego que se vera arriba:

    pygame.display.set_caption('The Phantom Game')

#---Le pongo una imagen de fondo a la ventana:
    fondo = pygame.image.load("fondo.jpg").convert()

#---Especifico la posion de la imagen de fondo:
    screen.blit(fondo, (0, 0))

    pygame.display.flip()

#---Creo un bucle para que se pueda cerrar la ventana al darle a la x:

salir=False
while not salir:
    for event in pygame.event.get():
        if event.type == QUIT:
            salir=True

    
if __name__== '__main__':
    main()

