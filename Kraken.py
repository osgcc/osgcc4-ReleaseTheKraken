'''
Created on Oct 24, 2010

@author: lucas
'''

import pygame

from Creature import Creature

from Paintable import loadImage

from Building import Building
from Constants import *

from Explosion import Explosion

import random

class Kraken(Creature):
    
    def __init__(self, x, y):
        
        Creature.__init__(self, x, y, KRAKEN_SPEED, KRAKEN_LIFE, KRAKEN_REGENERATION, 2)
        
        self.attack = KRAKEN_ATTACK
        self.attackSpeed = KRAKEN_ATTACK_SPEED
        
        self.lastAttack = 0
        
        self.image = loadImage("art/kraken.png", (255,255,255))
    
    
    def process(self, powerPopulation, buildingPopulation, terrain):
        
        if(self.currentLife < self.maxLife):
            self.currentLife += self.lifeRegenerationRate
        else:
            self.currentLife = self.maxLife
        
        if (self.moving):
            
            self.timeMoving += TIME_QUANTUM
            
            if(self.timeMoving > self.speed):
                
                self.moving = False
                
                terrain.removeThingOcupyingKraken(self.x - DIRECTION[self.moveDirection][0], self.y - DIRECTION[self.moveDirection][1])
                
        
        self.lastAttack += TIME_QUANTUM
        
        if(self.lastAttack > self.attackSpeed):
                        
            for i in range(3):
                for j in range(3):
                    
                    thing = terrain.getThingOcupying(self.x+i-1,self.y+j-1)
                    
                    if(isinstance(thing, Creature) or isinstance(thing, Building)):
                        if(thing.getTeam() != self.team and thing.isAlive()):
                            
                            if(random.randint(0, 5) == 0):
                                self.BreathFire(powerPopulation)
                            else:
                                thing.damage(random.randint(0, self.attack))
                            
                            
                            self.lastAttack = 0
                                                  
                            return
        
            
            
            if(self.moving == False):
                self.moveEvil(terrain)
        
        if(random.randint(0, 500) == 0):
            self.BreathFire(powerPopulation)            
                
    def BreathFire(self, powerPopulation):
        
        for i in range(5):
            powerPopulation.addPower(Explosion(self.x + 2*(i+1)*DIRECTION[self.moveDirection][0], self.y + 2*(i+1)*DIRECTION[self.moveDirection][1]))
                
    def moveEvil(self, terrain):  
          
        for i in range(11):
            for j in range(11):
                
                thing = terrain.getThingOcupying(self.x+i-5,self.y+j-5)
                
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
                        
                        if(terrain.krakenWalkable(newX, newY)):                        
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
        
        if(terrain.krakenWalkable(newX, newY)):
                        
            self.moving = True
            self.timeMoving = 0
            
            self.x = newX
            self.y = newY
        
            terrain.setThingOcupying(self.x, self.y, self)
            
        else:
            
            self.moving = False      
    
    def paint(self, screen, translation):
        
        if(self.moving):
            screen.blit(self.image, (-30+SQUARE_SIZE*(self.x - DIRECTION[self.moveDirection][0]) + translation[0] + SQUARE_SIZE*DIRECTION[self.moveDirection][0]*self.timeMoving/self.speed, -30+SQUARE_SIZE*(self.y - DIRECTION[self.moveDirection][1]) + translation[1] + SQUARE_SIZE*DIRECTION[self.moveDirection][1]*self.timeMoving/self.speed))
            pygame.draw.line(screen, (0,0,0), ((SQUARE_SIZE*(self.x - DIRECTION[self.moveDirection][0]) + translation[0] + SQUARE_SIZE*DIRECTION[self.moveDirection][0]*self.timeMoving/self.speed, SQUARE_SIZE*(self.y - DIRECTION[self.moveDirection][1]) + translation[1] + SQUARE_SIZE*DIRECTION[self.moveDirection][1]*self.timeMoving/self.speed)), ((SQUARE_SIZE*(self.x - DIRECTION[self.moveDirection][0]) + translation[0] + SQUARE_SIZE*DIRECTION[self.moveDirection][0]*self.timeMoving/self.speed + SQUARE_SIZE, SQUARE_SIZE*(self.y - DIRECTION[self.moveDirection][1]) + translation[1] + SQUARE_SIZE*DIRECTION[self.moveDirection][1]*self.timeMoving/self.speed)) )
            pygame.draw.line(screen, (0,255,0), ((SQUARE_SIZE*(self.x - DIRECTION[self.moveDirection][0]) + translation[0] + SQUARE_SIZE*DIRECTION[self.moveDirection][0]*self.timeMoving/self.speed, SQUARE_SIZE*(self.y - DIRECTION[self.moveDirection][1]) + translation[1] + SQUARE_SIZE*DIRECTION[self.moveDirection][1]*self.timeMoving/self.speed)), ((SQUARE_SIZE*(self.x - DIRECTION[self.moveDirection][0]) + translation[0] + SQUARE_SIZE*DIRECTION[self.moveDirection][0]*self.timeMoving/self.speed + (SQUARE_SIZE*self.currentLife)/self.maxLife, SQUARE_SIZE*(self.y - DIRECTION[self.moveDirection][1]) + translation[1] + SQUARE_SIZE*DIRECTION[self.moveDirection][1]*self.timeMoving/self.speed)) )
        else:
            screen.blit(self.image, (-30+SQUARE_SIZE*self.x + translation[0], -30+SQUARE_SIZE*self.y + translation[1]))        
            pygame.draw.line(screen, (0,0,0), (SQUARE_SIZE*self.x + translation[0], SQUARE_SIZE*self.y + translation[1]), (SQUARE_SIZE*self.x + translation[0] + SQUARE_SIZE, SQUARE_SIZE*self.y + translation[1]) )
            pygame.draw.line(screen, (0,255,0), (SQUARE_SIZE*self.x + translation[0], SQUARE_SIZE*self.y + translation[1]), (SQUARE_SIZE*self.x + translation[0] + (SQUARE_SIZE*self.currentLife)/self.maxLife, SQUARE_SIZE*self.y + translation[1]) )
                  
                            