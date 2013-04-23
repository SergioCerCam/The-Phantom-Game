# -*- coding: utf-8 -*-

#-Importo las librerias:

import pygame, sys, random
from pygame.locals import *

#---Inicio pygame:

pygame.init()

clock = pygame.time.Clock()

pygame.mixer.music.load("menu.mp3")
pygame.mixer.music.play(-1)

#---Creo la ventana donde se vera el juego:

Ancho = 700
Alto = 429

#---Funcion fondo pantalla:

def load_image(filename, transparent=False):
    try: image = pygame.image.load(filename)
    except pygame.error, message:
        raise SystemExit, message
    image = image.convert()
    if transparent:
        color = image.get_at((0,0))
        image.set_colorkey(color, RLEACCEL)
    return image

#---Funcion para el texto de la pantalla principal y niveles:

def texto(texto, posx, posy, color=(255,255,255), tam=30):
    fuente = pygame.font.Font("METAG.ttf", tam)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect

#---Texto para la pantalla creditos:

def palabras(texto, posx, posy, color=(255,255,255), tam=30):
    fuente = pygame.font.Font("verdana.ttf", tam)
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

#---Funcion para crear el menu principal del juego:

def menu(screen, select):

        if select == 1:
            empezarjuego, empezarjuegox = texto("Empezar Partida", Ancho/1-180, Alto/1-120, (255, 0, 0))
            salirse, salirsex = texto("Salir", Ancho/1-300, Alto/1-80)
            creditos, creditosx = texto("Creditos", Ancho/1-90, Alto/2+180)

        if select == 2:
            empezarjuego, empezarjuegox = texto("Empezar Partida", Ancho/1-180, Alto/1-120)
            salirse, salirsex = texto("Salir", Ancho/1-300, Alto/1-80, (255, 0, 0))
            creditos, creditosx = texto("Creditos", Ancho/1-90, Alto/2+180)

        if select == 3:
            empezarjuego, empezarjuegox = texto("Empezar Partida", Ancho/1-180, Alto/1-120)
            salirse, salirsex = texto("Salir", Ancho/1-300, Alto/1-80)
            creditos, creditosx = texto("Creditos", Ancho/1-90, Alto/2+180, (255, 0, 0))
        
        screen.blit(empezarjuego, empezarjuegox)
        screen.blit(salirse, salirsex)
        screen.blit(creditos, creditosx)


#---Volver al menu principal desde "creditos":

def volver(screen, select):

        if select == 4:
            volver, volverx = texto ("Volver", Ancho/1-115, Alto/1-20, (51, 51, 204))

        screen.blit(volver, volverx)

#---Niveles de dificultad:

def dificultad (screen, select):

        if select == 1:
            level1, level1X = texto("Facil Liquid", Ancho/1-548, Alto/1-160, (153, 255, 0))
            level2, level2X = texto("Normal Solid", Ancho/1-548, Alto/1-120, (0, 0, 0))
            level3, level3X = texto("Dificil Big Boss", Ancho/1-548, Alto/1-80, (0, 0, 0))
            volver, volverX = texto("Volver", Ancho/1-120, Alto/1-20, (0, 0, 0))

        if select == 2:
            level1, level1X = texto("Facil Liquid", Ancho/1-548, Alto/1-160, (0, 0, 0))
            level2, level2X = texto("Normal Solid", Ancho/1-548, Alto/1-120, (255, 153, 0))
            level3, level3X = texto("Dificil Big Boss", Ancho/1-548, Alto/1-80, (0, 0, 0))
            volver, volverX = texto("Volver", Ancho/1-120, Alto/1-20, (0, 0, 0))

        if select == 3:
            level1, level1X = texto("Facil Liquid", Ancho/1-548, Alto/1-160, (0, 0, 0))
            level2, level2X = texto("Normal Solid", Ancho/1-548, Alto/1-120, (0, 0, 0))
            level3, level3X = texto("Dificil Big Boss", Ancho/1-548, Alto/1-80, (255, 0, 0))
            volver, volverX = texto("Volver", Ancho/1-120, Alto/1-20, (0,  0, 0))
        
        if select == 4:
            level1, level1X = texto("Facil Liquid", Ancho/1-548, Alto/1-160, (0, 0, 0))
            level2, level2X = texto("Normal Solid", Ancho/1-548, Alto/1-120, (0, 0, 0))
            level3, level3X = texto("Dificil Big Boss", Ancho/1-548, Alto/1-80, (0, 0, 0))
            volver, volverX = texto("Volver", Ancho/1-120, Alto/1-20, (51, 51, 204))

        screen.blit(level1, level1X)
        screen.blit(level2, level2X)
        screen.blit(level3, level3X)
        screen.blit(volver, volverX)

#---Creacion del escenario del juego:

class mapa(pygame.sprite.Sprite):
    
    def __init__(self, archivotxt):
        pygame.sprite.Sprite.__init__(self)
    
        self.muro = load_image("muro.png")
        self.rect_muro = self.muro.get_rect()
		
	self.comida = load_image("comida1.png", True)
	self.rect_comida = self.comida.get_rect()
		
        self.mapa = importar_mapa(archivotxt)
        self.fila = len(self.mapa)
        self.colu = len(self.mapa)
	self.alimento()

#---Creando los bordes del escenario mediante fil que se multiplicaria por w(weight) para el ancho y col por h(height) para el alto:

    def crear_mapa(self, screen):
        for fil in range(self.fila):
            for col in range(self.colu):
                  if self.mapa[fil][col] == 1:
                        screen.blit(self.muro, (self.rect_muro.w*col, self.rect_muro.h*fil))
		  if self.mapa[fil][col] == 3:
		        screen.blit(self.comida, (self.rect_comida.w*col, self.rect_comida.h*fil))

					
    def alimento(self):
	    a = 1
	    while a:
		    fil = random.randint(1, self.fila-1)
		    col = random.randint(1, self.colu-1)
	            if self.mapa[fil][col] == 0:
			    self.mapa[fil][col] = 3
			    a = 0
		

def lista(cadena):
    lista = []
    for i in range(len(cadena)):
	if cadena[i] == ".":
	    lista.append(0)
        if cadena[i] == "#":
            lista.append(1)

    return lista


def importar_mapa(archivotxt):
    mapa = open(archivotxt, "r")
    mapa = mapa.readlines()
    for i in range(len(mapa)):
        mapa[i] = lista(mapa[i])

    return mapa

#---Funcion para crear la siguiente pantalla cuando el usuario presione "Empezar Partida":

def juego_nuevo(screen):

    fondo = load_image('juego_nuevo.jpg'); 
    screen = pygame.display.set_mode((Ancho, Alto))
    pygame.display.set_caption("Snake Eater")

    select = 1
    
    while True:
        
        keys = pygame.key.get_pressed()
        salir(keys)

        if keys[K_UP] and select != 1:
            select -=1

	elif keys[K_DOWN] and select != 4:
	    select +=1

        if keys[K_SPACE]:
            if select == 4:
                main()
            elif select == 1:
                facil_liquid(screen)
            elif select == 2:
                normal_solid(screen)
            elif select == 3:
                dificil_bigboss(screen)

        screen.blit(fondo, (0,0))
        dificultad(screen, select)
        pygame.display.flip()
        pygame.time.delay(100)
        clock.tick(8)
       
#---Nivel Facil del juego:        

def facil_liquid (screen):
    
    fondo = load_image('fondoliquid.jpg');
    pygame.display.set_caption("Snake Eater")
    clock = pygame.time.Clock()
    importar_mapa = mapa("mapa.txt")
    

    while True:
        time = clock.tick(100)
        keys = pygame.key.get_pressed()
        salir(keys)

        screen.blit(fondo, (0,0))
        importar_mapa.crear_mapa(screen)
        pygame.display.flip()
        pygame.time.delay(100)
 
#---Nivel Normal del juego:

def normal_solid (screen):
    
    fondo = load_image('fondosolid.jpg');
    pygame.display.set_caption("Snake Eater")
    clock = pygame.time.Clock()
    importar_mapa = mapa("mapa.txt")
    

    while True:
        time = clock.tick(100)
        keys = pygame.key.get_pressed()
        salir(keys)

        screen.blit(fondo, (0,0))
        importar_mapa.crear_mapa(screen)
        pygame.display.flip()
        pygame.time.delay(100)

#---Nivel Dificil del juego:

def dificil_bigboss (screen):
    
    fondo = load_image('fondobigboss.jpg');
    pygame.display.set_caption("Snake Eater")
    clock = pygame.time.Clock()
    importar_mapa = mapa("mapa.txt")
    

    while True:
        time = clock.tick(100)
        keys = pygame.key.get_pressed()
        salir(keys)

        screen.blit(fondo, (0,0))
        importar_mapa.crear_mapa(screen)
        pygame.display.flip()       
        pygame.time.delay(100)
 


#---Pantalla de creditos:

def creditos(screen):

    fondo = load_image('creditos.jpg'); 
    screen = pygame.display.set_mode((Ancho, Alto))
    pygame.display.set_caption("Snake Eater")
    
    select = 4
    
    while True:
        
        keys = pygame.key.get_pressed()
        salir(keys)  
 
        tex_img0, tex_rec0 = palabras("Este juego desarrollado", 160, 230, (255, 0, 0), 22)
        tex_img1, tex_rec1 = palabras("en Python, ha sido", 134, 255, (255, 0, 0), 22)
        tex_img2, tex_rec2 = palabras("creado por Sergio CeCampoy", 190, 280, (255, 0, 0), 22)
        tex_img3, tex_rec3 = palabras("y las imagenes y canciones", 181, 305, (255, 0, 0), 22)
        tex_img4, tex_rec4 = palabras("utilizadas pertenezen", 148, 335, (255, 0, 0), 22)
        tex_img5, tex_rec5 = palabras("a la saga de videojuegos", 168, 360, (255, 0, 0), 22)
        tex_img6, tex_rec6 = palabras("Metal Gear Solid", 133, 390, (255, 0, 0), 25)  


        if keys[K_SPACE]:
            if select == 4:
                main()

        screen.blit(fondo, (0,0))
	screen.blit(tex_img0, tex_rec0)
	screen.blit(tex_img1, tex_rec1)
	screen.blit(tex_img2, tex_rec2)
	screen.blit(tex_img3, tex_rec3)
	screen.blit(tex_img4, tex_rec4)
	screen.blit(tex_img5, tex_rec5)
	screen.blit(tex_img6, tex_rec6)
        volver(screen, select)
        pygame.display.flip()
        pygame.time.delay(100)
        clock.tick(8)

#---Funcion principal:

def main():
    
    screen = pygame.display.set_mode((Ancho, Alto))
    pygame.display.set_caption('Snake Eater')
    background_image = load_image('fondoreal.jpg')       
   
#---Especifico que al presionar la tecla enter salga del juego y que entre en los distintos apartados del menu:
    
    select = 1
    
    while True:
        keys = pygame.key.get_pressed()
        salir(keys)
        
        if keys[K_UP] and select != 1:
            select -=1

	elif keys[K_DOWN] and select != 3:
	    select +=1

        elif keys[K_SPACE]:
            if select == 1:
                juego_nuevo(screen)
            elif select == 2:
                sys.exit()
            elif select == 3:
                creditos(screen)
                
        screen.blit(background_image, (0, 0))
	menu(screen, select)
        pygame.display.flip()
	clock.tick(8)

    return 0
    
if __name__== '__main__':
    main()


