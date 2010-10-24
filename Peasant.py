'''
Created on Oct 23, 2010

@author: lucas
'''

import random

from Creature import Creature
from Building import Building

from Constants import *

class Peasant(Creature):
    
    def __init__(self, x, y, team):
        
        Creature.__init__(self, x, y, PEASANT_SPEED, PEASANT_LIFE, PEASANT_REGENERATION, team)
        
        self.buildTime = 0
        
    def process(self, powerPopulation, buildingPopulation, terrain):
        
        Creature.process(self, powerPopulation, buildingPopulation, terrain)
        
        self.buildTime += TIME_QUANTUM
        
        if(self.repair(terrain) == False):
            
            if(self.buildTime > PEASANT_BUILD_INTERVAL):
                
                self.buildTime = 0
                
                if(random.randint(0,100) < PEASANT_BUILD_CHANCE):
                    self.buildRandomBuilding(buildingPopulation, terrain)  
                    
                else:                    
                    if(self.moving == False):
                        self.moveEvil(terrain)
                        #self.movePurposefully(terrain, buildingPopulation)
            else:
                                
                if(self.moving == False):
                    self.moveEvil(terrain)
                    #self.movePurposefully(terrain, buildingPopulation)
                    
  
    def moveEvil(self, terrain):
       
        for i in range(7):
            for j in range(7):
                
                thing = terrain.getThingOcupying(self.x+i-3,self.y+j-3)
                
                if(isinstance(thing, Creature) or isinstance(thing, Building)):
                    
                    if(thing.getTeam() != self.team):
                        if(i-5>0 and j-5>0):
                            if(random.randint(0,1)==0):
                                self.moveDirection = 1
                            else:
                                self.moveDirection = 3
                        elif(i-5<0 and j-5<0):
                            if(random.randint(0,1)==0):
                                self.moveDirection = 0
                            else:
                                self.moveDirection = 2
                        elif(i-5<0 and j-5>0):
                            if(random.randint(0,1)==0):
                                self.moveDirection = 3
                            else:
                                self.moveDirection = 0
                        elif(i-5>0 and j-5<0):
                            if(random.randint(0,1)==0):
                                self.moveDirection = 2
                            else:
                                self.moveDirection = 1
                        elif(i-5>0):
                                self.moveDirection = 2
                        elif(i-5<0):
                                self.moveDirection = 3
                        elif(j-5>0):
                                self.moveDirection = 0
                        elif(j-5<0):
                                self.moveDirection = 1
                        
                        
                        newX = self.x + DIRECTION[self.moveDirection][0]
                        newY = self.y + DIRECTION[self.moveDirection][1]
                        
                        if(terrain.walkable(newX, newY)):                        
                            self.moving = True
                            
                            self.x = newX
                            self.y = newY
                            
                            terrain.setThingOcupying(self.x, self.y, self)
                            
                            self.timeMoving = 0
                            return        
            
        self.moveRandomly(terrain)
       
    def moveRandomly(self, terrain):  
     
        if(random.randint(0,5) == 0):
            self.moveDirection = random.randint(0,3)
        
        newX = self.x + DIRECTION[self.moveDirection][0]
        newY = self.y + DIRECTION[self.moveDirection][1]
        
        if(terrain.walkable(newX, newY)):
                        
            self.moving = True
            self.timeMoving = 0
            
            self.x = newX
            self.y = newY
        
            terrain.setThingOcupying(self.x, self.y, self)
            
        else:
            
            self.moving = False    
                
    def buildRandomBuilding(self, buildingPopulation, terrain):
        
        buildingPopulation.addBuilding(self.x+1, self.y+1, random.randint(1,4), self.team, terrain)
        
        
    def repair(self, terrain):
        
        for i in range(3):
                for j in range(3):
                    
                    thing = terrain.getThingOcupying(self.x+i-1,self.y+j-1)
                    
                    if(isinstance(thing, Building)):
                        if(thing.needsRepair() and thing.getTeam() == self.team):
                            
                            thing.repair(PEASANT_REPAIR_RATE) 
                            
                            return True
                        
        return False