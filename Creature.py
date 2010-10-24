
import random

from Paintable import loadImage

from Constants import *

import pygame

class Creature():

	def __init__(self, x, y, speed, life, lifeRegenerationRate, team):
		
		self.x = x
		self.y = y
		
		self.speed = speed
		
		self.currentLife = life
		self.maxLife = life
		
		self.lifeRegenerationRate = lifeRegenerationRate
		
		self.moving = False
		self.moveDirection = 0
		self.timeMoving = 0
		
		self.team = team
		
		
		self.alive = True
		
		if self.team == 0:
			self.image = loadImage("art/peasant.png", (255,255,255))
		else:
			self.image = loadImage("art/Egyptian_peasant.png", (255,255,255))
			
	def getX(self):
		return self.x
	
	def getY(self):
		return self.y
	
	def freeTerrain(self, terrain):
		terrain.removeThingOcupying(self.x, self.y)
		if(self.moving):
			terrain.removeThingOcupying(self.x - DIRECTION[self.moveDirection][0], self.y - DIRECTION[self.moveDirection][1])
	
	def isAlive(self):
		return self.alive
	
	def getTeam(self):
		return self.team
		
	def damage(self, value):
		self.currentLife -= value
		
		if(self.currentLife < 0):
			self.currentLife = 0
			self.alive = False
		
	def process(self, powerPopulation, buildingPopulation, terrain):
		
		if(self.currentLife < self.maxLife):
			self.currentLife += self.lifeRegenerationRate
		else:
			self.currentLife = self.maxLife
		
		if (self.moving):
			
			self.timeMoving += TIME_QUANTUM
			
			if(self.timeMoving > self.speed):
				
				self.moving = False
				
				terrain.removeThingOcupying(self.x - DIRECTION[self.moveDirection][0], self.y - DIRECTION[self.moveDirection][1])
	
	def paint(self, screen, translation):
		
		if(self.moving):
			screen.blit(self.image, (SQUARE_SIZE*(self.x - DIRECTION[self.moveDirection][0]) + translation[0] + SQUARE_SIZE*DIRECTION[self.moveDirection][0]*self.timeMoving/self.speed, SQUARE_SIZE*(self.y - DIRECTION[self.moveDirection][1]) + translation[1] + SQUARE_SIZE*DIRECTION[self.moveDirection][1]*self.timeMoving/self.speed))
			pygame.draw.line(screen, (0,0,0), ((SQUARE_SIZE*(self.x - DIRECTION[self.moveDirection][0]) + translation[0] + SQUARE_SIZE*DIRECTION[self.moveDirection][0]*self.timeMoving/self.speed, SQUARE_SIZE*(self.y - DIRECTION[self.moveDirection][1]) + translation[1] + SQUARE_SIZE*DIRECTION[self.moveDirection][1]*self.timeMoving/self.speed)), ((SQUARE_SIZE*(self.x - DIRECTION[self.moveDirection][0]) + translation[0] + SQUARE_SIZE*DIRECTION[self.moveDirection][0]*self.timeMoving/self.speed + SQUARE_SIZE, SQUARE_SIZE*(self.y - DIRECTION[self.moveDirection][1]) + translation[1] + SQUARE_SIZE*DIRECTION[self.moveDirection][1]*self.timeMoving/self.speed)) )
			pygame.draw.line(screen, (0,255,0), ((SQUARE_SIZE*(self.x - DIRECTION[self.moveDirection][0]) + translation[0] + SQUARE_SIZE*DIRECTION[self.moveDirection][0]*self.timeMoving/self.speed, SQUARE_SIZE*(self.y - DIRECTION[self.moveDirection][1]) + translation[1] + SQUARE_SIZE*DIRECTION[self.moveDirection][1]*self.timeMoving/self.speed)), ((SQUARE_SIZE*(self.x - DIRECTION[self.moveDirection][0]) + translation[0] + SQUARE_SIZE*DIRECTION[self.moveDirection][0]*self.timeMoving/self.speed + (SQUARE_SIZE*self.currentLife)/self.maxLife, SQUARE_SIZE*(self.y - DIRECTION[self.moveDirection][1]) + translation[1] + SQUARE_SIZE*DIRECTION[self.moveDirection][1]*self.timeMoving/self.speed)) )
		else:
			screen.blit(self.image, (SQUARE_SIZE*self.x + translation[0], SQUARE_SIZE*self.y + translation[1]))		
			pygame.draw.line(screen, (0,0,0), (SQUARE_SIZE*self.x + translation[0], SQUARE_SIZE*self.y + translation[1]), (SQUARE_SIZE*self.x + translation[0] + SQUARE_SIZE, SQUARE_SIZE*self.y + translation[1]) )
			pygame.draw.line(screen, (0,255,0), (SQUARE_SIZE*self.x + translation[0], SQUARE_SIZE*self.y + translation[1]), (SQUARE_SIZE*self.x + translation[0] + (SQUARE_SIZE*self.currentLife)/self.maxLife, SQUARE_SIZE*self.y + translation[1]) )
	
		
		