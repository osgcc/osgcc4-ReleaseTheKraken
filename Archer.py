import random

from Creature import Creature
from Paintable import loadImage
from Arrow import Arrow
from Swordsman import Swordsman

from Constants import *

class Archer(Creature):
    
    def __init__(self, x, y, team):
        
        Creature.__init__(self, x, y, ARCHER_SPEED, ARCHER_LIFE, ARCHER_REGENERATION, team)
        
        self.attack = ARCHER_ATTACK
        self.attackSpeed = ARCHER_ATTACK_SPEED
        
        self.lastAttack = 0
        
        if self.team == 0:
            self.image = loadImage("art/greek_archer.png", (255,255,255))
        else:
            self.image = loadImage("art/egytian_archer.png", (255,255,255))
        
    def process(self, powerPopulation, buildingPopulation, terrain):
        
        Creature.process(self, powerPopulation, buildingPopulation, terrain)
        
        self.lastAttack += TIME_QUANTUM
        
        if(self.lastAttack > self.attackSpeed):
            
            for i in range(7):
                for j in range(7):
                    
                    thing = terrain.getThingOcupying(self.x+i-3,self.y+j-3)
                    
                    if(isinstance(thing, Creature)):
                        if(thing.getTeam() != self.team and thing.isAlive()):
                            
                            powerPopulation.addPower(Arrow(self.x, self.y, random.randint(0, self.attack), thing))
                            self.lastAttack = 0
                                                  
                            return
        
            
            if(self.moving == False):
                self.moveEvil(terrain)
     
    def moveEvil(self, terrain):  
      
        for i in range(7):
            for j in range(7):
                
                thing = terrain.getThingOcupying(self.x+i-3,self.y+j-3)
                
                if(isinstance(thing, Swordsman)):
                    
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
                            
                            self.timeMoving = 0
                            return 
                
                elif(isinstance(thing, Creature)):
                    
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
        
             