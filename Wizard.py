import random

from Creature import Creature
from Building import Building
from Paintable import loadImage
from Lightning import Lightning
from Swordsman import Swordsman

from Constants import *

class Wizard(Creature):
    
    def __init__(self, x, y, team):
        
        Creature.__init__(self, x, y, WIZARD_SPEED, WIZARD_LIFE, WIZARD_REGENERATION, team)
        
        self.attack = WIZARD_ATTACK
        self.attackSpeed = WIZARD_ATTACK_SPEED
        
        self.lastAttack = 0
        
        self.movement = 0
        
        if self.team == 0:
            self.image = loadImage("art/wizard.png", (255,255,255))
        else:
            self.image = loadImage("art/egyptian_magician.png", (255,255,255))
        
        
    def process(self, powerPopulation, buildingPopulation, terrain):
        
        Creature.process(self, powerPopulation, buildingPopulation, terrain)
        
        self.lastAttack += TIME_QUANTUM
        
        if(self.lastAttack > self.attackSpeed):
            
            for i in range(7):
                for j in range(7):
                    
                    thing = terrain.getThingOcupying(self.x+i-3,self.y+j-3)
                    '''If there is a creature near by that's an enemy'''
                    if(isinstance(thing, Creature)):
                        if(thing.getTeam() != self.team and thing.isAlive()):
                            '''move towards it'''
                            
                            powerPopulation.addPower(Lightning(self.x, self.y, random.randint(0, self.attack), thing))
                            self.lastAttack = 0
                                                  
                            return
    
            if(self.moving == False):
                self.moveEvil(terrain)
                
    def movePurposefully(self, terrain, buildingPopulation):
        
        for i in range(7):
            for j in range(7):
                '''Find if there is a building'''
                thing = terrain.getThingOcupying(self.x+i-1,self.y+j-1)
                if isinstance(thing, Building):
                    self.moveDirection = abs(self.x + thing.getX())%4
                       
                elif isinstance(thing, Creature):
                    if(thing.getTeam() != self.team):
                        '''avoid it like the plague'''
                        self.moveDirection = abs(self.x - thing.getX())%4
                        #self.engage(thing) 
                    elif(thing.getTeam() == self.team):
                        self.moveDirection = abs(self.x + thing.getX())%4
                        
                else: 
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
                            
                            terrain.setThingOcupying(self.x, self.y, self)
                            
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
             