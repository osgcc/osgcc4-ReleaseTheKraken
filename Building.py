'''
Created on Oct 23, 2010

@author: lucas
'''

from Paintable import Paintable
from Paintable import loadImage

from Constants import *

import pygame

class Building(Paintable):
    
    def __init__(self, x, y, terrain, life, lifeRegenerationRate, team, image_path):
        
        self.dimension = (2,2)
        
        self.x = x
        self.y = y
        
        self.maxLife = life
        self.currentLife = 1
        
        self.alive = True
        
        self.lifeRegenerationRate = lifeRegenerationRate
        
        self.team = team
                               
        self.removable = True
                               
        for i in range(self.dimension[0]):        
            for j in range(self.dimension[1]):                
                if(terrain.walkable(self.x + i, self.y + j) == False):                    
                    self.alive = False
                    self.removable = False
                                        
                    
        self.image = loadImage(image_path, (255,255,255))
        
        if(self.alive):
            for i in range(self.dimension[0]):        
                for j in range(self.dimension[1]):                
                    terrain.setThingOcupying(x+i, y+j, self)
     
    def isAlive(self):
        return self.alive
     
    def needsRepair(self):
        if(self.isAlive() and self.currentLife < self.maxLife):
            return True
        else:
            return False
     
    def getLife(self):
        return self.currentLife
    
    def getMaxLife(self):
        return self.maxLife
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getTeam(self):
        return self.team
    
    def repair(self, value):
        self.currentLife += value
        
        if(self.currentLife > self.maxLife):
            self.currentLife = self.maxLife
     
    def damage(self, value):
        self.currentLife -= value
        
        if(self.currentLife < 0):
            self.alive = False

    def freeTerrain(self, terrain):   
        if(self.removable):     
            for i in range(self.dimension[0]):        
                for j in range(self.dimension[1]):                
                    terrain.removeThingOcupying(self.x+i, self.y+j)
        
     
    def process(self, terrain, population):
        
        if(self.alive):
            if(self.currentLife < self.maxLife):
                self.currentLife += self.lifeRegenerationRate
            else:
                self.currentLife = self.maxLife
    
               
    def paint(self, screen, translation):
        
        if(self.alive):
            screen.blit(self.image, (SQUARE_SIZE*self.x + translation[0], SQUARE_SIZE*self.y + translation[1]))
        
            pygame.draw.line(screen, (0,0,0), (SQUARE_SIZE*self.x + translation[0], SQUARE_SIZE*self.y + translation[1]), (SQUARE_SIZE*self.x + translation[0] + SQUARE_SIZE*self.dimension[0], SQUARE_SIZE*self.y + translation[1]) )
            pygame.draw.line(screen, (0,255,0), (SQUARE_SIZE*self.x + translation[0], SQUARE_SIZE*self.y + translation[1]), (SQUARE_SIZE*self.x + translation[0] + (SQUARE_SIZE*self.dimension[0]*self.currentLife)/self.maxLife, SQUARE_SIZE*self.y + translation[1]) )
            
   # def __del__(self):
   #     Building = self.__class__.__name__
   #     print self + "destroyed!"     
            
            
            
            
            
            
            
            