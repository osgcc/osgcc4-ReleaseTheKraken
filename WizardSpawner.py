'''
Created on Oct 23, 2010

@author: lucas
'''

from Building import Building
from Wizard import Wizard
from Paintable import loadImage

from Constants import *

class WizardSpawner(Building):

    def __init__(self, x, y, terrain, team):
        
        Building.__init__(self, x,y,terrain, BUILDING_LIFE, BUILDING_REGENERATION, team, "art/building1.png")
        
        if team == 0:
            self.image = loadImage('art/greek_temple.png', (255,255,255))
        else:
            self.image = loadImage('art/egyptian_temple.png', (255,255,255))
        
        
        self.wizards = []
        self.numWizards = 0
        self.maxNumberWizards = MAX_NUMBER_WIZARDS
        
        self.spawTime = WIZARD_SPAWN_TIME
        
        self.timer = 0
        
        
    def process(self, terrain, population):
                        
        self.timer += TIME_QUANTUM
        
        if(self.numWizards < self.maxNumberWizards):
            
            if(self.timer > self.spawTime):                
                                                                
                wizard = Wizard(self.x - 1, self.y - 1, self.team)
                
                if(population.addCreature(self.x - 1, self.y - 1, wizard, terrain)):
                    self.timer = 0
                    self.numWizards += 1
                    self.wizards.append(wizard)
                else:
                    pass
        else:
            
            for i in range(self.numWizards):
                if(self.wizards[i].isAlive() == False):
                    self.wizards.remove(self.wizards[i])
                    self.numWizards -= 1
                    return
                    
                
               
        