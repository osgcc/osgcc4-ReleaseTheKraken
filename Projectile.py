import pygame
from Power import Power
from pygame.locals import *

class Projectile(Power):
    
    
    def __init__(self, x, y, speed, strength, life, image_name):
        self.x = x
        self.y = y
        '''Initilize a clock to degrade the arrow'''
        clock = pygame.time.Clock()
        
        self.alive = True
        self.speed = speed
        self.strength = strength
        self.life = life
         '''Load the image of the projectile'''
         self.image = loadImage(image_name, (255,255,255))
        
        '''determines damage based on degradation function'''
    def damage(self, strength):
        self.life *= self.strength
        '''function that degrades the life of the projectile'''
    def degrade(self, factor):
        self.strength = self.strength - factor
        
    def process(self, terrain, creaturePopulation, buildingPopulation):    
        '''fly across the screen'''
        
        while self.life > 0 && self.strength > 0:
            '''move arrow towards the target'''
            
            '''degrade the arrow by a factor'''
            self.degrade(self, clock)
            
        if self.life <=0 && self.strength <=0:
            self.alive = False;
            '''delete the object!'''
        