'''
Created on Oct 23, 2010

@author: lucas
'''

from Building import Building
from Swordsman import Swordsman
from Paintable import loadImage

from Constants import *

class SwordsmanSpawner(Building):

    def __init__(self, x, y, terrain, team):
            
        Building.__init__(self, x,y,terrain, BUILDING_LIFE, BUILDING_REGENERATION, team, "art/building1.png")
        
        if team == 0:
            self.image = loadImage('art/parathonon.png', (255,255,255))
        else:
            self.image = loadImage('art/Pyramid.png', (255,255,255))
        
        self.swordsman = []
        self.numSwordsman = 0
        self.maxNumberSwordsman = MAX_NUMBER_SWORDSMAN
        
        self.spawTime = SWORDSMAN_SPAWN_TIME
        
        self.timer = 0
        
        
    def process(self, terrain, population):
                        
        self.timer += TIME_QUANTUM
        
        if(self.numSwordsman < self.maxNumberSwordsman):
            
            if(self.timer > self.spawTime):                
                                                                
                swordsman = Swordsman(self.x - 1, self.y - 1, self.team)
                
                if(population.addCreature(self.x - 1, self.y - 1, swordsman, terrain)):
                    self.timer = 0
                    self.numSwordsman += 1
                    self.swordsman.append(swordsman)
                else:
                    pass
                
        else:
        
            for i in range(self.numSwordsman):
                if(self.swordsman[i].isAlive() == False):
                    self.swordsman.remove(self.swordsman[i])
                    self.numSwordsman -= 1
                    return
                    
                
               
        