'''
Created on Oct 23, 2010

@author: lucas
'''

import random

from Paintable import Paintable
from PeasantSpawner import PeasantSpawner
from SwordsmanSpawner import SwordsmanSpawner
from ArcherSpawner import ArcherSpawner
from WizardSpawner import WizardSpawner

from Constants import *

class BuildingPopulation(Paintable):
    
    def __init__(self, terrain):
        
        self.numBuildings = 0
        self.buildings = []
        
        #self.buildings.append(PeasantSpawner(random.randint(0,terrain.getNumColumns()-1), random.randint(0,terrain.getNumRows()-1), terrain, 0))
        #self.buildings.append(PeasantSpawner(random.randint(0,terrain.getNumColumns()-1), random.randint(0,terrain.getNumRows()-1), terrain, 1))
          
          
    def addBuilding(self, x, y, type, team, terrain):
           
        if(type == PEASANT_SPAWNER):
            self.buildings.append(PeasantSpawner(x, y, terrain, team))
            self.numBuildings += 1
        elif(type == SWORDSMAN_SPAWNER):
            self.buildings.append(SwordsmanSpawner(x, y, terrain, team))
            self.numBuildings += 1
        elif(type == ARCHER_SPAWNER):
            self.buildings.append(ArcherSpawner(x, y, terrain, team))
            self.numBuildings += 1
        elif(type == WIZARD_SPAWNER):
            self.buildings.append(WizardSpawner(x,y,terrain,team))
            self.numBuildings += 1
            
    def process(self, terrain, population):
        
        toRemove = []
        
        for i in range(self.numBuildings):
            
            if(self.buildings[i].isAlive()):
                self.buildings[i].process(terrain, population)
            else:
                toRemove.append(self.buildings[i])
                
        for i in range(len(toRemove)):
            self.buildings.remove(toRemove[i])
            toRemove[i].freeTerrain(terrain)
            self.numBuildings -= 1
        
    def paint(self, screen, translation):
        
        for i in range(self.numBuildings):
            self.buildings[i].paint(screen, translation)
            
            
            