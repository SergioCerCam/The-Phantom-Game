# -*- coding: utf-8 -*-

#-Importo las librerias:

import pygame, sys, random
from pygame.locals import *

#---Inicio pygame:

pygame.init()

#---Reloj para gestionar el tiempo y que el juego vaya a una velocidad determinada:

clock = pygame.time.Clock()

#---Cancion principal del juego:

pygame.mixer.music.load("menu.mp3")
pygame.mixer.music.play(-1)

#---Creo la ventana donde se vera el juego:

Ancho = 700
Alto = 433

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

    if select == 6:
        volver, volverx = texto ("Volver", Ancho/1-115, Alto/1-20, (51, 51, 204))

    screen.blit(volver, volverx)

#---Menu de niveles de dificultad:

def dificultad (screen, select):

    if select == 1:
        level1, level1X = texto("Facil Liquid", Ancho/1-543, Alto/1-200, (153, 255, 0))
	level4, level4X = texto("Facil Solidus", Ancho/1-540, Alto/1-160, (0, 0, 0))
	level5, level5X = texto("Normal Naked", Ancho/1-536, Alto/1-120, (0, 0, 0))
        level2, level2X = texto("Normal Solid", Ancho/1-554, Alto/1-80, (0, 0, 0))
        level3, level3X = texto("Dificil Big Boss", Ancho/1-548, Alto/1-40, (0, 0, 0))
        volver, volverX = texto("Volver", Ancho/1-120, Alto/1-20, (0, 0, 0))

    if select == 2:
        level1, level1X = texto("Facil Liquid", Ancho/1-543, Alto/1-200, (0, 0, 0))
	level4, level4X = texto("Facil Solidus", Ancho/1-540, Alto/1-160, (167, 185, 34))
	level5, level5X = texto("Normal Naked", Ancho/1-536, Alto/1-120, (0, 0, 0))
        level2, level2X = texto("Normal Solid", Ancho/1-554, Alto/1-80, (0, 0, 0))
        level3, level3X = texto("Dificil Big Boss", Ancho/1-548, Alto/1-40, (0, 0, 0))
        volver, volverX = texto("Volver", Ancho/1-120, Alto/1-20, (0, 0, 0))

    if select == 3:
        level1, level1X = texto("Facil Liquid", Ancho/1-543, Alto/1-200, (0, 0, 0))
	level4, level4X = texto("Facil Solidus", Ancho/1-540, Alto/1-160, (0, 0, 0))
	level5, level5X = texto("Normal Naked", Ancho/1-536, Alto/1-120, (237, 195, 80))
        level2, level2X = texto("Normal Solid", Ancho/1-554, Alto/1-80, (0, 0, 0))
        level3, level3X = texto("Dificil Big Boss", Ancho/1-548, Alto/1-40, (0, 0, 0))
        volver, volverX = texto("Volver", Ancho/1-120, Alto/1-20, (0, 0, 0))

    if select == 4:
        level1, level1X = texto("Facil Liquid", Ancho/1-543, Alto/1-200, (0, 0, 0))
	level4, level4X = texto("Facil Solidus", Ancho/1-540, Alto/1-160, (0, 0, 0))
	level5, level5X = texto("Normal Naked", Ancho/1-536, Alto/1-120, (0, 0, 0))
        level2, level2X = texto("Normal Solid", Ancho/1-554, Alto/1-80, (255, 153, 0))
        level3, level3X = texto("Dificil Big Boss", Ancho/1-548, Alto/1-40, (0, 0, 0))
        volver, volverX = texto("Volver", Ancho/1-120, Alto/1-20, (0, 0, 0))

    if select == 5:
        level1, level1X = texto("Facil Liquid", Ancho/1-543, Alto/1-200, (0, 0, 0))
	level4, level4X = texto("Facil Solidus", Ancho/1-540, Alto/1-160, (0, 0, 0))
	level5, level5X = texto("Normal Naked", Ancho/1-536, Alto/1-120, (0, 0, 0))
        level2, level2X = texto("Normal Solid", Ancho/1-554,Alto/1-80, (0, 0, 0))
        level3, level3X = texto("Dificil Big Boss", Ancho/1-548, Alto/1-40, (255, 0, 0))
        volver, volverX = texto("Volver", Ancho/1-120, Alto/1-20, (0,  0, 0))
        
    if select == 6:
        level1, level1X = texto("Facil Liquid", Ancho/1-543, Alto/1-200, (0, 0, 0))
	level4, level4X = texto("Facil Solidus", Ancho/1-540, Alto/1-160, (0, 0, 0))
	level5, level5X = texto("Normal Naked", Ancho/1-536, Alto/1-120, (0, 0, 0))
        level2, level2X = texto("Normal Solid", Ancho/1-554, Alto/1-80, (0, 0, 0))
        level3, level3X = texto("Dificil Big Boss", Ancho/1-548, Alto/1-40, (0, 0, 0))
        volver, volverX = texto("Volver", Ancho/1-120, Alto/1-20, (51, 51, 204))


    screen.blit(level1, level1X)
    screen.blit(level4, level4X)
    screen.blit(level5, level5X)
    screen.blit(level2, level2X)
    screen.blit(level3, level3X)
    screen.blit(volver, volverX)

#---Creacion del escenario del juego:
#---Aqui vamos a ir cargando las imagenes que serán utilizadas en el mapa como son los muros de los bordes del mapa, la serpiente y la comida:

class Mapa(pygame.sprite.Sprite):

    def __init__(self, archivotxt):
        pygame.sprite.Sprite.__init__(self)
		
        self.bloque = load_image("muro.png")
        self.rect_bloque = self.bloque.get_rect()
		
        self.snake = load_image("serpiente.png")
        self.rect_snake = self.snake.get_rect()
		
        self.comida = load_image("comida.png", True)
        self.rect_comida = self.comida.get_rect()

#---Aqui almacenamos el mapa en self.mapa y con self.fila y self.colu se recorreran mas adelante el mapa con el tamaño de las filas y las columnas y el alimento:		

        self.mapa = importar_mapa(archivotxt)
        self.fila = len(self.mapa)
        self.colu = len(self.mapa[0])
        self.alimento()
	
#---Aqui se dibuja el mapa de una forma muy sencilla, se recorre el mapa con self.fila y self.colu, de forma que cuando encuentre un 1 dibuje un sprite bloque etc. Despues mediante self.rect_bloque.w*columna y self.rect_bloque.h*fila lo que hace es localizar el ancho por la columna y la altura por la fila.

#---Para crear los distintos objetos, asignare los elemetos de la siguiente manera:
#---0 = Espacio libre en el mapa
#---1 = Bloque en el mapa
#---2 = Cuerpo de la serpiente
#---3 = Comida
#---5 = Cabeza de las serpiente


    def crear_mapa(self, screen):
        for fila in range(self.fila):
            for columna in range(self.colu):
                if self.mapa[fila][columna] == 1:
                    screen.blit(self.bloque, (self.rect_bloque.w*columna, self.rect_bloque.h*fila))
                if self.mapa[fila][columna] == 2 or self.mapa[fila][columna] == 5:
                    screen.blit(self.snake, (self.rect_snake.w*columna, self.rect_snake.h*fila))
                if self.mapa[fila][columna] == 3:
                    screen.blit(self.comida, (self.rect_comida.w*columna, self.rect_comida.h*fila))
			
#---Creamos el alimento con un modulo "random.randint" para que el alimento vaya apareciendo por el mapa de forma aleatoria en un espacio libre (0)
		
    def alimento(self):
        a = 1
        while a:
            fil = random.randint(1, self.fila-1)
            col = random.randint(1, self.colu-1)
            if self.mapa[fil][col] == 0:
                self.mapa[fil][col] = 3
                a = 0

#---Aqui se crea la serpiente:

class Snake:

    def __init__(self, importar_mapa):
        self.snake = []
        for t in range(importar_mapa.fila):
            for s in range(importar_mapa.colu):
                if importar_mapa.mapa[t][s] == 2:
                    for n in range(4):
                        self.snake.append([t, s-n])
                    break

        self.ultimo = 1
        self.actualizar(importar_mapa)
	
#---Aqui se va actualizando la serpiente conforme va comiendo comida, de forma que se le va añadiendo un cuerpo (2):
	
    def actualizar(self, mapa):
        for x in range(mapa.fila):
            for y in range(mapa.colu):
                if mapa.mapa[x][y] == 2:
                    mapa.mapa[x][y] = 0
		
        mapa.mapa[self.snake[0][0]][self.snake[0][1]] = 5
        for i in range(1, len(self.snake)):
            mapa.mapa[self.snake[i][0]][self.snake[i][1]] = 2

#---Aqui vamos a definir el movimiento de la serpiente:
#---Tambien definimos que al presionar la tecla no coja mas que un valor, por que si no se añaderian mas trozos de la cuenta a la serpiente y no funcionaria bien.
						
    def mover(self, mapa, keys):

        if keys[K_UP]:

            if self.ultimo != 3:
                nuevo = [self.snake[0][0]-1, self.snake[0][1]]
                self.snake = comienzo(self.snake, nuevo)
                if mapa.mapa[nuevo[0]][nuevo[1]] != 3:
                    self.snake.pop()
                self.ultimo = 4

        elif keys[K_DOWN]:

            if self.ultimo != 4:
                nuevo = [self.snake[0][0]+1, self.snake[0][1]]
                self.snake = comienzo(self.snake, nuevo)
                if mapa.mapa[nuevo[0]][nuevo[1]] != 3:
                    self.snake.pop()
                self.ultimo = 3

        elif keys[K_LEFT]:

            if self.ultimo != 1:
                nuevo = [self.snake[0][0], self.snake[0][1]-1]
                self.snake = comienzo(self.snake, nuevo)
                if mapa.mapa[nuevo[0]][nuevo[1]] != 3:
                    self.snake.pop()
                self.ultimo = 2

        elif keys[K_RIGHT]:

            if self.ultimo != 2:
                nuevo = [self.snake[0][0], self.snake[0][1]+1]
                self.snake = comienzo(self.snake, nuevo)
                if mapa.mapa[nuevo[0]][nuevo[1]] != 3:
                    self.snake.pop()
                self.ultimo = 1

#---En esta parte lo que hacemos es que la serpiete se mueva sola:

        else:

            if self.ultimo == 1:
                nuevo = [self.snake[0][0], self.snake[0][1]+1]
                self.snake = comienzo(self.snake, nuevo)
                if mapa.mapa[nuevo[0]][nuevo[1]] != 3:
                    self.snake.pop()

            if self.ultimo == 2:
                nuevo = [self.snake[0][0], self.snake[0][1]-1]
                self.snake = comienzo(self.snake, nuevo)
                if mapa.mapa[nuevo[0]][nuevo[1]] != 3:
                    self.snake.pop()

            if self.ultimo == 3:
                nuevo = [self.snake[0][0]+1, self.snake[0][1]]
                self.snake = comienzo(self.snake, nuevo)
                if mapa.mapa[nuevo[0]][nuevo[1]] != 3:
                    self.snake.pop()

            if self.ultimo == 4:
                nuevo = [self.snake[0][0]-1, self.snake[0][1]]
                self.snake = comienzo(self.snake, nuevo)
                if mapa.mapa[nuevo[0]][nuevo[1]] != 3:
                    self.snake.pop()
				
        if mapa.mapa[self.snake[0][0]][self.snake[0][1]] == 3:
            mapa.alimento()
            return 1
        return 0
		


def comienzo(lista, elemento):
    nueva = [elemento]
    nueva += lista
    return nueva

#---Creamos una lista para que cuando recorra y encuentre una serie de caracteres, muestre las distintas imagenes del mapa:		
	
def listarCadena(cadena):
    lista = []
    for i in range(len(cadena)):
        if cadena[i] == ".":
            lista.append(0)
        if cadena[i] == "#":
            lista.append(1)
        if cadena[i] == "*":
            lista.append(2)
    return lista

#---Funcion para importar el mapa, leerlo e interpretarlo:

def importar_mapa(archivotxt):
    mapa = open(archivotxt, "r")
    mapa = mapa.readlines()

    for i in range(len(mapa)):
        mapa[i] = listarCadena(mapa[i])
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

	elif keys[K_DOWN] and select != 6:
	    select +=1

        if keys[K_SPACE]:
            if select == 4:
                main()
            elif select == 1:
                facil_liquid(screen)
	    elif select == 2:
		facil_solidus(screen)
	    elif select == 3:
		normal_naked(screen)
            elif select == 4:
                normal_solid(screen)
            elif select == 5:
                dificil_bigboss(screen)


        screen.blit(fondo, (0,0))
        dificultad(screen, select)
        pygame.display.flip()
        pygame.time.delay(100)
        clock.tick(8)
       
#---Nivel Facil del juego:   
#---Se crean las distintas pantallas antes de empezar, la puntuacion, sonidos, importaciones, velocidad y teclas:     

def facil_liquid (screen):

    pygame.mixer.music.load("start.mp3")
    pygame.mixer.music.play(1)
    previo = load_image('previo.jpg');
    screen.blit(previo, (0,0))	
    pygame.display.flip()
    pygame.time.delay(5200)   
    puntos = 0
    clock = pygame.time.Clock()
    
    pygame.mixer.music.load("liquid.mp3")
    pygame.mixer.music.play(-1)
    fondo = load_image('fondoliquid.jpg');
    pygame.display.set_caption("Snake Eater")
    clock = pygame.time.Clock()
    importar_mapa = Mapa("mapa.txt")
    serpiente = Snake(importar_mapa)
    

    while True:

        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        salir(keys)

#---Aqui creamos la puntuacion y que cuando la serpiente choque con un bloque (1) or con sigo misma (2) salga al menu principal:

	puntos += serpiente.mover(importar_mapa, keys)
	if importar_mapa.mapa[serpiente.snake[0][0]][serpiente.snake[0][1]] == 1 or importar_mapa.mapa[serpiente.snake[0][0]][serpiente.snake[0][1]] == 2:
		break      
	  
        textoY, textoX = texto("Puntuacion "+str(puntos), 95, 400, (255, 255, 255), 18)
        serpiente.actualizar(importar_mapa)
        screen.blit(fondo, (0,0))
        screen.blit(textoY, textoX)
        importar_mapa.crear_mapa(screen)
        pygame.display.flip()
        pygame.time.delay(100)     
 

def facil_solidus (screen):

    pygame.mixer.music.load("start.mp3")
    pygame.mixer.music.play(1)
    previo = load_image('previo.jpg');
    screen.blit(previo, (0,0))	
    pygame.display.flip()
    pygame.time.delay(5200)   
    puntos = 0
    clock = pygame.time.Clock()
    
    pygame.mixer.music.load("liquid.mp3")
    pygame.mixer.music.play(-1)
    fondo = load_image('fondoliquid.jpg');
    pygame.display.set_caption("Snake Eater")
    clock = pygame.time.Clock()
    importar_mapa = Mapa("mapa.txt")
    serpiente = Snake(importar_mapa)
    

    while True:

        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        salir(keys)


	puntos += serpiente.mover(importar_mapa, keys)
	if importar_mapa.mapa[serpiente.snake[0][0]][serpiente.snake[0][1]] == 1 or importar_mapa.mapa[serpiente.snake[0][0]][serpiente.snake[0][1]] == 2:
		break      
	  
        textoY, textoX = texto("Puntuacion "+str(puntos), 95, 400, (255, 255, 255), 18)
        serpiente.actualizar(importar_mapa)
        screen.blit(fondo, (0,0))
        screen.blit(textoY, textoX)
        importar_mapa.crear_mapa(screen)
        pygame.display.flip()
        pygame.time.delay(100)  


#---Nivel Normal del juego:

def normal_naked (screen):

    pygame.mixer.music.load("start.mp3")
    pygame.mixer.music.play(1)
    previo = load_image('previo.jpg');
    screen.blit(previo, (0,0))	
    pygame.display.flip()
    pygame.time.delay(5200)   
    puntos = 0
    clock = pygame.time.Clock()
    
    pygame.mixer.music.load("liquid.mp3")
    pygame.mixer.music.play(-1)
    fondo = load_image('fondoliquid.jpg');
    pygame.display.set_caption("Snake Eater")
    clock = pygame.time.Clock()
    importar_mapa = Mapa("mapa.txt")
    serpiente = Snake(importar_mapa)
    

    while True:

        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        salir(keys)


	puntos += serpiente.mover(importar_mapa, keys)
	if importar_mapa.mapa[serpiente.snake[0][0]][serpiente.snake[0][1]] == 1 or importar_mapa.mapa[serpiente.snake[0][0]][serpiente.snake[0][1]] == 2:
		break      
	  
        textoY, textoX = texto("Puntuacion "+str(puntos), 95, 400, (255, 255, 255), 18)
        serpiente.actualizar(importar_mapa)
        screen.blit(fondo, (0,0))
        screen.blit(textoY, textoX)
        importar_mapa.crear_mapa(screen)
        pygame.display.flip()
        pygame.time.delay(100)  


def normal_solid (screen):

    pygame.mixer.music.load("start.mp3")
    pygame.mixer.music.play(1)
    previo = load_image('previo.jpg');
    screen.blit(previo, (0,0))	
    pygame.display.flip()
    pygame.time.delay(5200)   
    puntos = 0
    clock = pygame.time.Clock()

    pygame.mixer.music.load("solid.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(5)
    fondo = load_image('fondosolid.jpg');
    pygame.display.set_caption("Snake Eater")
    clock = pygame.time.Clock()
    importar_mapa = Mapa("mapa2.txt")
    serpiente = Snake(importar_mapa)
    

    while True:

        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        salir(keys)

	puntos += serpiente.mover(importar_mapa, keys)
	if importar_mapa.mapa[serpiente.snake[0][0]][serpiente.snake[0][1]] == 1 or importar_mapa.mapa[serpiente.snake[0][0]][serpiente.snake[0][1]] == 2:
		break

        textoY, textoX = texto("Puntuacion "+str(puntos), 95, 400, (255, 255, 255), 18)
        serpiente.actualizar(importar_mapa)
        screen.blit(fondo, (0,0))
        screen.blit(textoY, textoX)
        importar_mapa.crear_mapa(screen)
        pygame.display.flip()
        pygame.time.delay(80)

#---Nivel Dificil del juego:

def dificil_bigboss (screen):
  
    pygame.mixer.music.load("bigboss.mp3")
    pygame.mixer.music.play(-1)
    previo = load_image('previobb.jpg');
    screen.blit(previo, (0,0))	
    pygame.display.flip()
    pygame.time.delay(28500)   
    puntos = 0
    clock = pygame.time.Clock()
    
    fondo = load_image('fondobigboss.jpg');
    pygame.display.set_caption("Snake Eater")
    clock = pygame.time.Clock()
    importar_mapa = Mapa("mapa3.txt")
    serpiente = Snake(importar_mapa)
    

    while True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        salir(keys)

	puntos += serpiente.mover(importar_mapa, keys)
	if importar_mapa.mapa[serpiente.snake[0][0]][serpiente.snake[0][1]] == 1 or importar_mapa.mapa[serpiente.snake[0][0]][serpiente.snake[0][1]] == 2:
		break

        textoY, textoX = texto("Puntuacion "+str(puntos), 95, 400, (255, 255, 255), 18)
        serpiente.actualizar(importar_mapa)
        screen.blit(fondo, (0,0))
        screen.blit(textoY, textoX)
        importar_mapa.crear_mapa(screen)
        pygame.display.flip()
        pygame.time.delay(70)
 
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
        pygame.time.delay(70)
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
