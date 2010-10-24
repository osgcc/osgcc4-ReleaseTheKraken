'''
Created on Oct 23, 2010

@author: lucas
'''

from Building import Building
from Archer import Archer
from Paintable import loadImage

from Constants import *

class ArcherSpawner(Building):

    def __init__(self, x, y, terrain, team):
        
        Building.__init__(self, x,y,terrain, BUILDING_LIFE, BUILDING_REGENERATION, team, "art/building1.png")
        
        if team == 0:
            self.image = loadImage('art/armory.png', (255,255,255))
        else:
            self.image = loadImage('art/egyptian_armory.png', (255,255,255))
            
        
        self.archers = []
        self.numArchers = 0
        self.maxNumberArchers = MAX_NUMBER_ARCHERS
        
        self.spawTime = ARCHER_SPAWN_TIME
        
        self.timer = 0
        
        
    def process(self, terrain, population):
                        
        self.timer += TIME_QUANTUM
        
        if(self.numArchers < self.maxNumberArchers):
            
            if(self.timer > self.spawTime):                
                                                                
                archer = Archer(self.x - 1, self.y - 1, self.team)
                
                if(population.addCreature(self.x - 1, self.y - 1, archer, terrain)):
                    self.timer = 0
                    self.numArchers += 1
                    self.archers.append(archer)
                else:
                    pass
        else:
            
            for i in range(self.numArchers):
                if(self.archers[i].isAlive() == False):
                    self.archers.remove(self.archers[i])
                    self.numArchers -= 1
                    return
                    
                
               
        