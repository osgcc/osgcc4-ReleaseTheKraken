'''
Created on Oct 24, 2010

@author: lucas
'''
import random

from Power import Power 
from Creature import Creature
from Building import Building

from Constants import *

from Paintable import loadImage

class Explosion(Power):

    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        
        self.explosionTime = 0
        
        self.alive = True
        
        self.damageDealt = False
        
        self.images = []
        
        self.images.append(loadImage("art/exp1.png", (119,157,118)))
        self.images.append(loadImage("art/exp2.png", (119,157,118)))
    
    def isAlive(self):
        return self.alive
    
    def process(self, terrain, creaturePopulation, buildingPopulation):
        
        self.explosionTime += TIME_QUANTUM
        
        if(self.damageDealt == False):
            self.damageDealt = True
                      
            for i in range(3):
                for j in range(3):
                    if(abs(i)+abs(j)<=4):
                        thing = terrain.getThingOcupying(self.x+i-1, self.y+j-1)
                            
                        if(isinstance(thing, Creature) or isinstance(thing, Building)):
                            thing.damage(random.randint(150,500))
            
        
        if(self.explosionTime > 200):
            self.alive = False
    
    def paint(self, screen, translation):
        
        if(self.explosionTime < 50):
            screen.blit(self.images[1], (SQUARE_SIZE*self.x -60 + translation[0], SQUARE_SIZE*self.y + translation[1] - 60))
        elif(self.explosionTime < 150):
            screen.blit(self.images[0], (SQUARE_SIZE*self.x -60 + translation[0], SQUARE_SIZE*self.y + translation[1] - 60))
        elif(self.explosionTime < 200):
            screen.blit(self.images[1], (SQUARE_SIZE*self.x -60 + translation[0], SQUARE_SIZE*self.y + translation[1] - 60))
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    