'''
Created on Oct 23, 2010

@author: lucas
'''

from Building import Building   
from Constants import *

class Armory(Building):
    
    def __init__(self, x, y, terrain, life, lifeRegenerationRate, team, image_path):
        
        Building.__init__(self, x, y, terrain, life, lifeRegenerationRate, team, image_path)
     
    def damage(self, value):
        self.currentLife -= value
        
        if(self.currentLife < 0):
            self.currentLife = False
           
     
    def process(self, terrain, population):
        
            if(self.currentLife < self.maxLife):
                self.currentLife += self.lifeRegenerationRate
            else:
                self.currentLife = self.maxLife
    
               
    def paint(self, screen, translation):
        
        if(self.alive):
            screen.blit(self.image, (SQUARE_SIZE*self.x + translation[0], SQUARE_SIZE*self.y + translation[1]))
            
            
            
            
            
            
            
            
            
            