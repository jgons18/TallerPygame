import pygame
import sys
#para hacer k las speed de los coches sea random
import random
#sublibreria para que cargue las funciones y no todo el código
from pygame.locals import *
#esto es que creamos una clase llamada car
from car import car
#clase shoot que utilizaremos para disparar
from shoot import shoot

pygame.init()

#tamaño de la pantalla
screenwidth=800
screenheight=600
#colores
green = (0,205,0)
black = (0,0,0)
grey = (130,130,130)
white = (255,255,255)
red = (255,0,0)
blue=(0,0,255) 
#velocidad inical del playerCar
speed=1
score=0

#definimos tupla, son constantes de dos coordenadas
size=(screenwidth, screenheight)
#creamos la agrupación de los sprites
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Cars racing")

#te da todas las fuentes

#fonts = pygame.font.get_fonts()
#print(fonts)

fonts = pygame.font.SysFont('Arial',30)
font_score = pygame.font.SysFont('Arial',20)

#music
#pygame.mixer.music.load('audio/soundtrack.mp3')
#pygame.mixer.music.play (-1)

#Jugadores = color, anchura, altura, speed
playerCar=car("images/murder.png",red, 60, 80, 70)
#obtenemos la coordenada x del rectangulo
playerCar.rect.x=150-playerCar.image.get_width()/2
playerCar.rect.y=screenheight-100

all_sprites_list=pygame.sprite.Group()

car1=car("images/police.png",black, 60,80,70)
car1.rect.x=250-playerCar.image.get_width()/2
car1.rect.y=screenheight-100

car2=car("images/police.png",white, 60,80,random.randint(50,100))
car2.rect.x=350-playerCar.image.get_width()/2
car2.rect.y=screenheight-600

car3=car("images/police.png",green, 60,80,random.randint(50,100))
car3.rect.x=150-playerCar.image.get_width()/2
car3.rect.y=screenheight-900

car4=car("images/police.png",grey, 60,80,random.randint(50,100))
car4.rect.x=450-playerCar.image.get_width()/2
car4.rect.y=screenheight-900

car5=car("images/police.png",blue, 60,80,random.randint(50,100))
car5.rect.x=450-playerCar.image.get_width()/2
car5.rect.y=screenheight-600

#disparos
bomba = shoot("images/boom.png",grey,40,60,70)    # Nuevo en 0.05
bomba.rect.x=150-bomba.image.get_width()/2
bomba.rect.y=screenheight-100

#creamos lista con todos los sprites
all_sprites_list.add(playerCar)
all_sprites_list.add(car1)
all_sprites_list.add(car2)
all_sprites_list.add(car3)
all_sprites_list.add(car4)
all_sprites_list.add(car5)
all_sprites_list.add(bomba)



#agrupamineot de coahes que llegan

all_coming_cars=pygame.sprite.Group()
all_coming_cars.add(car1,car2,car3,car4,car5)

#defnnir reloj
clock=pygame.time.Clock()
finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(2)


    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(10)
        bomba.moveLeft(10)
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight(10) 
        bomba.moveRight(10)  
    if keys[pygame.K_UP]:
        '''speed +=0.05'''
        playerCar.moveBackward(5)
    if keys[pygame.K_DOWN]:
        '''speed -=0.05 '''
        playerCar.moveForward(5) 
    if keys[pygame.K_SPACE]:
        bomba.disparar(10)  

        #logica del juego
    for car in all_coming_cars:
        car.moveForward(speed)
        if car.rect.y>screenheight:
            car.changeSpeed(random.randint(50,100))
            car.rect.y=-200
            # car.repaint(random.choice(lista_colores))
        #lista de colisiones 
    car_collision_list= pygame.sprite.spritecollide(playerCar,all_coming_cars,False,pygame.sprite.collide_mask)
    for car in car_collision_list:
        print("Car crash")
        #audio explosion
        finished=True
            

    all_sprites_list.update()  
    score +=1 

    screen.fill(green)

    #dibujar carretera
    pygame.draw.rect(screen,grey,[100,0,400, screenheight])
    #punto inicial, punto final y grosor
    pygame.draw.line(screen,white,[200,0],[200,screenheight],5)
    pygame.draw.line(screen,white,[300,0],[300,screenheight],5)
    pygame.draw.line(screen,white,[400,0],[400,screenheight],5)

    #dibujar sprites
    all_sprites_list.draw(screen)

    text = fonts.render("Cars racing",True,black)
    screen.blit(text, (screenwidth-text.get_width()-10,30))
    text_score=font_score.render("Score: "+str(score),True,black)
    screen.blit(text_score,(screenwidth-text_score.get_width()-10,60))
    score +=1
    pygame.display.flip()
    clock.tick(60)

pygame.quit()