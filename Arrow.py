'''
Created on Oct 24, 2010

@author: lucas
'''

import pygame

from Power import Power

from math import sqrt

from Constants import *

class Arrow(Power):
    
    def __init__(self, x, y, damageValue, target):
        
        self.x = x+0.5
        self.y = y+0.5
        
        self.vx = 0
        self.vy = 0
        
        self.target = target
        
        self.speed = ARROW_SPEED
        
        self.damage = damageValue
        
        self.alive = True
        
        
    def process(self,terrain, creaturePopulation, buildingPopulation):
        
        distX = self.x - self.target.getX()-0.5
        distY = self.y - self.target.getY()-0.5
        
        dist = sqrt(distX*distX + distY*distY)
        
        self.vx = -self.speed*distX/dist
        self.vy = -self.speed*distY/dist
        
        self.x += self.vx
        self.y += self.vy
        
        if(dist < 0.5):
            self.target.damage(self.damage)
            self.alive = False
            
    def paint(self, screen, translation):
        
        pygame.draw.line(screen, (0,0,0), (SQUARE_SIZE*self.x + translation[0], SQUARE_SIZE*self.y + translation[1]), (SQUARE_SIZE*self.x+100*self.vx + translation[0], SQUARE_SIZE*self.y+100*self.vy + translation[1]))
        
        