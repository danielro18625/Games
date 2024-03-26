import pygame
import time
import random


pygame.init()

blanco = (255,255,255)
negro = (12,50,25)
rojo = (255,0,0)
verde = (0,255,0)

ancho = 800
alto = 600
tamaño_celda = 20
fps = 10


ventana = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption('snake')


reloj=pygame.time.Clock()

serpiente = [(ancho / 2,alto / 2)]
direccion = 'derecha'
comida_x =round(random.randrange(0, ancho - tamaño_celda)/ tamaño_celda) * tamaño_celda
comida_y = round(random.randrange(0, alto - tamaño_celda) / tamaño_celda) * tamaño_celda


def dibujar_serpiente(serpiente):
    for segmento in serpiente: 
        pygame.draw.rect(ventana, verde, (segmento [0], segmento[1], tamaño_celda, tamaño_celda))


def dibujar_comida(comida_x, comida_y):
    pygame.draw.rect(ventana, rojo ,(comida_x, comida_y,tamaño_celda, tamaño_celda))


terminado = False
while not terminado:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminado = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direccion != 'derecha':
                direccion = 'izquierda'
            elif event.key == pygame.K_RIGHT and direccion != 'izquierda':
                direccion = 'derecha'
            elif event.key == pygame.K_UP and direccion != 'abajo':
                direccion = 'arriba'
            elif event.key == pygame.K_DOWN and direccion != 'arriba':
                direccion = 'abajo'

    cabeza_x, cabeza_y = serpiente[0]
    if direccion == 'izquierda':
        cabeza_x -= tamaño_celda
    elif direccion == 'derecha':
        cabeza_x += tamaño_celda
    elif direccion == 'arriba':
        cabeza_y -= tamaño_celda
    elif direccion == 'abajo':
        cabeza_y += tamaño_celda

    nueva_cabeza = (cabeza_x, cabeza_y)

    if cabeza_x < 0 or cabeza_x >= ancho or cabeza_y < 0 or cabeza_y >= alto:
        terminado = True

    if nueva_cabeza in serpiente[1:]:
        terminado = True

    serpiente.insert(0, nueva_cabeza)

    if cabeza_x == cabeza_x and cabeza_y == comida_y:
        comida_x = round(random.randrange(0, ancho - tamaño_celda) / tamaño_celda)*tamaño_celda
        comida_y = round(random.randrange(0, alto - tamaño_celda) / tamaño_celda)*tamaño_celda
    else :
        serpiente.pop()

    ventana.fill(negro)

    dibujar_serpiente(serpiente)
    dibujar_comida(comida_x, comida_y)
    
    pygame.display.update()
    reloj.tick(fps)

pygame.quit()
