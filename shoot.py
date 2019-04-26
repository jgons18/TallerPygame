import pygame

WHITE = (255,255,255)

class shoot(pygame.sprite.Sprite):
#constructor
	def __init__(self,file,color,width,height,speed):
		super().__init__()

		self.image=pygame.Surface([width,height])
		self.image.fill(WHITE)
		self.image.set_colorkey(WHITE)
		#atributos 
		self.width = width
		self.height = height
		self.color = color
		self.speed = speed

		#definir rectangulo
		pygame.draw.rect(self.image,self.color,[0,0,self.width,self.height])

		#si se carga imagen
		self.image=pygame.image.load(file)
		self.image=pygame.transform.scale(self.image,(width,height))

		#definir superfice como rectangulo
		self.rect = self.image.get_rect()


	def moveRight(self, pixels):
		self.rect.x += pixels

	def moveLeft(self, pixels):
		self.rect.x -= pixels	

	def disparar(self,speed):
		self.rect.y -= self.speed * speed / 20

	def changeSpeed(self,speed):
		self.speed = speed