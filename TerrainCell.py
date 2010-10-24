
import pygame
import random

from Paintable import Paintable
from Paintable import loadImage

from Constants import *

class TerrainCell(Paintable):
	
	def __init__(self, x, y, type):
		
		self.type = type
		
		self.x = x
		self.y = y
		
		self.thingOcupying = None
		
		if(self.type == 0):
			self.image = loadImage("art/terrain1.png")
		elif(self.type == 1):
			self.image = loadImage("art/terrain1.png")
		elif(self.type == 2):
			#self.image = []
			#self.image.append(loadImage("art/water3.png"))
			#self.image.append(loadImage("art/water1.png"))
			#self.image.append(loadImage("art/water2.png"))	
			#self.randomFactor = random.randint(0, 1000)
			self.image = loadImage("art/terrain2.png")	
			self.thingOcupying = WATER
		elif(self.type == 3):
			self.image = loadImage("art/terrain3.png")
			self.thingOcupying = ROCK
						
		
		
	def getType(self):
		return self.type
		
	def setThingOcupying(self, creature):
		
		self.thingOcupying = creature
		
	def getThingOcupying(self):
		
		return self.thingOcupying
	
		
	def paint(self, screen, translation):
		
		#if(self.type == 2):
		#	screen.blit(self.image[((self.randomFactor+pygame.time.get_ticks())/600)%3], (self.x + translation[0], self.y + translation[1]))
		#else:
		#if(self.thingOcupying == None):
			screen.blit(self.image, (self.x + translation[0], self.y + translation[1]))
		
		
		
		