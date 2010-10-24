'''
Created on Oct 23, 2010

@author: lucas
'''

from Building import Building
from Peasant import Peasant
from Paintable import loadImage

from Constants import *

class PeasantSpawner(Building):

    def __init__(self, x, y, terrain, team):
    
        Building.__init__(self, x,y,terrain, BUILDING_LIFE, BUILDING_REGENERATION, team, "art/building1.png")
    
        if team == 0:
            self.image = loadImage('art/Greek_building.png', (255,255,255))
        else:
            self.image = loadImage('art/egyptian_house.png', (255,255,255))
      
        
        self.peasants = []
        self.numPeasants = 0
        self.maxNumPeasants = MAX_NUMBER_PEASANTS
        
        self.spawTime = PEASANT_SPAW_TIME
        
        self.timer = 0
        
        
    def process(self, terrain, population):
                        
        self.timer += TIME_QUANTUM
        
        if(self.numPeasants < self.maxNumPeasants):
            
            if(self.timer > self.spawTime):                
                                                                
                peasant = Peasant(self.x - 1, self.y - 1, self.team)
                
                if(population.addCreature(self.x - 1, self.y - 1, peasant, terrain)):
                    self.timer = 0
                    self.numPeasants += 1
                    self.peasants.append(peasant)
                else:
                    pass
                
        else:
        
            for i in range(self.numPeasants):
                if(self.peasants[i].isAlive() == False):
                    self.peasants.remove(self.peasants[i])
                    self.numPeasants -= 1
                    return
                    
                
               
        