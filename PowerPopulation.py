'''
Created on Oct 24, 2010

@author: lucas
'''

class PowerPopulation():
    
    def __init__(self):
        
        self.numPowers = 0;
        self.powers = [];
        
        
    def process(self, terrain, creaturePopulation, buildingPopulation):
        
        toRemove = []
        
        for i in range(self.numPowers):       
                
            if(self.powers[i].isAlive()): 
                self.powers[i].process(terrain, creaturePopulation, buildingPopulation)
            else:
                toRemove.append(self.powers[i])
                
        for i in range(len(toRemove)):
            self.powers.remove(toRemove[i])
            self.numPowers -= 1
              
              
    def addPower(self, power):
        
        self.powers.append(power)
        self.numPowers += 1
            
            
    def paint(self, screen, translation):
        
        for i in range(self.numPowers):
            self.powers[i].paint(screen, translation)