'''
Created on Oct 24, 2010

@author: lucas
'''

import random
from math import sqrt
from Creature import Creature
from Paintable import loadImage
from Building import Building

from Constants import *

class Swordsman(Creature):
    
    def __init__(self, x, y, team):
        
        Creature.__init__(self, x, y, SWORDSMAN_SPEED, SWORDSMAN_LIFE, SWORDSMAN_REGENERATION, team)
        
        self.attack = SWORDSMAN_ATTACK
        self.attackSpeed = SWORDSMAN_ATTACK_SPEED
        
        self.lastAttack = 0
        
        if self.team == 0:
            self.image = loadImage("art/greek_swordsman.png", (255,255,255))
        else:
            self.image = loadImage("art/egyptian_swordsman.png", (255,255,255))
            
        
    def process(self, powerPopulation, buildingPopulation, terrain):
        
        Creature.process(self, powerPopulation, buildingPopulation, terrain)
        
        self.lastAttack += TIME_QUANTUM
        
        if(self.lastAttack > self.attackSpeed):
                        
            for i in range(3):
                for j in range(3):
                    
                    thing = terrain.getThingOcupying(self.x+i-1,self.y+j-1)
                    
                    if(isinstance(thing, Creature) or isinstance(thing, Building)):
                        if(thing.getTeam() != self.team and thing.isAlive()):
                            
                            thing.damage(random.randint(0, self.attack))
                            self.lastAttack = 0
                                                  
                            return
            
            if(self.moving == False):
                self.moveEvil(terrain)
                        
    
    def moveEvil(self, terrain):  
          
        for i in range(7):
            for j in range(7):
                
                thing = terrain.getThingOcupying(self.x+i-3,self.y+j-3)
                
                if(isinstance(thing, Creature) or isinstance(thing, Building)):
                    
                    if(thing.getTeam() != self.team):
                        if(i-5<0 and j-5<0):
                            if(random.randint(0,1)==0):
                                self.moveDirection = 1
                            else:
                                self.moveDirection = 3
                        elif(i-5>0 and j-5>0):
                            if(random.randint(0,1)==0):
                                self.moveDirection = 0
                            else:
                                self.moveDirection = 2
                        elif(i-5>0 and j-5<0):
                            if(random.randint(0,1)==0):
                                self.moveDirection = 3
                            else:
                                self.moveDirection = 0
                        elif(i-5<0 and j-5>0):
                            if(random.randint(0,1)==0):
                                self.moveDirection = 2
                            else:
                                self.moveDirection = 1
                        elif(i-5<0):
                                self.moveDirection = 2
                        elif(i-5>0):
                                self.moveDirection = 3
                        elif(j-5<0):
                                self.moveDirection = 0
                        elif(j-5>0):
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
                
                        
                        

                        
                        
                        
                        
                        
                        
                        
                        
                                        