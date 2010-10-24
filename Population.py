'''
Created on Oct 23, 2010

@author: lucas
'''
import pygame
import random

from Paintable import Paintable
from Peasant import Peasant
from Kraken import Kraken
from Paintable import loadImage

from Constants import *

class Population(Paintable):
    
    def __init__(self, terrain):
        
        self.numCreatures = 2
        self.creatures = []
        
        x = random.randint(0,terrain.getNumColumns()-1)
        y = random.randint(0,terrain.getNumRows()-1)
        
        while(terrain.walkable(x, y) == False):
            x = random.randint(0,terrain.getNumColumns()-1)
            y = random.randint(0,terrain.getNumRows()-1)
            
        self.creatures.append(Peasant(x, y, 0))
        
        x = random.randint(0,terrain.getNumColumns()-1)
        y = random.randint(0,terrain.getNumRows()-1)
        
        while(terrain.walkable(x, y) == False):
            x = random.randint(0,terrain.getNumColumns()-1)
            y = random.randint(0,terrain.getNumRows()-1)
            
        self.creatures.append(Peasant(x, y, 1))
        
        self.populationCount = 0
        
          
    def addCreature(self, x, y, creature ,terrain):
        
        if(terrain.walkable(x,y)):
            self.creatures.append(creature)
            self.numCreatures += 1
            terrain.setThingOcupying(x,y,creature)
            self.populationCount += 1
            if(self.populationCount >= 75):
                self.addKraken(terrain)
                self.populationCount = 0
            return True
        else:
            return False
    
    def addKraken(self, terrain):
        
        kraken = 0
        
        x = random.randint(0, terrain.getNumColumns()-1)
        y = random.randint(0, terrain.getNumRows()-1)
        
        while(terrain.getType(x, y) != WATER):
            x = random.randint(0, terrain.getNumColumns()-1)
            y = random.randint(0, terrain.getNumRows()-1)
             
        self.addCreatureKraken(x, y, Kraken(x,y), terrain)
        phaser_sound = pygame.mixer.Sound("art/release.ogg")
        channel = phaser_sound.play()
        if kraken < 1:
            pygame.mixer.music.load("sfx/carmina.ogg")
            pygame.mixer.music.play()
            kraken += 1
            
    def addCreatureKraken(self, x, y, creature ,terrain):
        
        if(terrain.krakenWalkable(x,y)):
            self.creatures.append(creature)
            self.numCreatures += 1
            terrain.setThingOcupying(x,y,creature)
            return True
        else:
            return False
          
    def process(self, powerPopulation, buildingPopulation, terrain):
        
        toRemove = []
        
        for i in range(self.numCreatures):
            if(self.creatures[i].isAlive()):
                self.creatures[i].process(powerPopulation, buildingPopulation, terrain)
            else:
                toRemove.append(self.creatures[i])
                
           
        for i in range(len(toRemove)):
            self.creatures.remove(toRemove[i])
            toRemove[i].freeTerrain(terrain)
            self.numCreatures -= 1
        
    def paint(self, screen, translation):
        
        for i in range(self.numCreatures):
            self.creatures[i].paint(screen, translation)