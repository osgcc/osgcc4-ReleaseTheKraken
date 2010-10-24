'''
Created on Oct 23, 2010

@author: lucas
'''
import pygame
from pygame.locals import *

from Terrain import Terrain
from Population import Population
from BuildingPopulation import BuildingPopulation
from PowerPopulation import PowerPopulation
from Explosion import Explosion
from Kraken import Kraken
from Peasant import Peasant
from Swordsman import Swordsman
from Wizard import Wizard
from Archer import Archer

from Constants import *

class Game():

    def __init__(self):
        
        self.running = True
        self.clock = pygame.time.Clock()
        
        self.initializeScreen()
        
        self.viewPositionX = 0
        self.viewPositionY = 0
        
        self.terrain = Terrain(40,40)
        self.population = Population(self.terrain)
        self.buildingPopulation = BuildingPopulation(self.terrain)
        self.powers = PowerPopulation()
        
        self.explosionTimer = 0;
        
        
    def initializeScreen(self):
        
        #Initialize Everything
        pygame.init()
        self.screen = pygame.display.set_mode((1024, 768))
        pygame.display.set_caption('Release the Kraken!')
        pygame.mouse.set_visible(1)
    
        #Create The Background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))
        
    def handleInput(self):
            
        kraken = 0    
            
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
                
        self.explosionTimer += TIME_QUANTUM
            
        if(pygame.mouse.get_pressed()[0] and self.explosionTimer > 500):
            self.powers.addPower(Explosion((-self.viewPositionX + pygame.mouse.get_pos()[0])/30, (-self.viewPositionY + pygame.mouse.get_pos()[1])/30))
            self.explosionTimer = 0
                
        if(pygame.key.get_pressed()[K_k]):
            self.population.addCreatureKraken((-self.viewPositionX + pygame.mouse.get_pos()[0])/30, (-self.viewPositionY + pygame.mouse.get_pos()[1])/30, Kraken((-self.viewPositionX + pygame.mouse.get_pos()[0])/30, (-self.viewPositionY + pygame.mouse.get_pos()[1])/30), self.terrain)  
            phaser_sound = pygame.mixer.Sound("art/release.ogg")
            channel = phaser_sound.play()    
           
            if kraken < 1:
                pygame.mixer.music.load("sfx/carmina.ogg")
                pygame.mixer.music.play()
                kraken += 1
                
       
        if(pygame.key.get_pressed()[K_q]):
            self.population.addCreature((-self.viewPositionX + pygame.mouse.get_pos()[0])/30, (-self.viewPositionY + pygame.mouse.get_pos()[1])/30, Peasant((-self.viewPositionX + pygame.mouse.get_pos()[0])/30, (-self.viewPositionY + pygame.mouse.get_pos()[1])/30, 0), self.terrain)
        if(pygame.key.get_pressed()[K_w]):
            self.population.addCreature((-self.viewPositionX + pygame.mouse.get_pos()[0])/30, (-self.viewPositionY + pygame.mouse.get_pos()[1])/30, Swordsman((-self.viewPositionX + pygame.mouse.get_pos()[0])/30, (-self.viewPositionY + pygame.mouse.get_pos()[1])/30, 0), self.terrain)
        if(pygame.key.get_pressed()[K_e]):
            self.population.addCreature((-self.viewPositionX + pygame.mouse.get_pos()[0])/30, (-self.viewPositionY + pygame.mouse.get_pos()[1])/30, Archer((-self.viewPositionX + pygame.mouse.get_pos()[0])/30, (-self.viewPositionY + pygame.mouse.get_pos()[1])/30, 0), self.terrain)
        if(pygame.key.get_pressed()[K_r]):
            self.population.addCreature((-self.viewPositionX + pygame.mouse.get_pos()[0])/30, (-self.viewPositionY + pygame.mouse.get_pos()[1])/30, Wizard((-self.viewPositionX + pygame.mouse.get_pos()[0])/30, (-self.viewPositionY + pygame.mouse.get_pos()[1])/30, 0), self.terrain)
       
        if(pygame.key.get_pressed()[K_a]):
            self.population.addCreature((-self.viewPositionX + pygame.mouse.get_pos()[0])/30, (-self.viewPositionY + pygame.mouse.get_pos()[1])/30, Peasant((-self.viewPositionX + pygame.mouse.get_pos()[0])/30, (-self.viewPositionY + pygame.mouse.get_pos()[1])/30, 1), self.terrain)
        if(pygame.key.get_pressed()[K_s]):
            self.population.addCreature((-self.viewPositionX + pygame.mouse.get_pos()[0])/30, (-self.viewPositionY + pygame.mouse.get_pos()[1])/30, Swordsman((-self.viewPositionX + pygame.mouse.get_pos()[0])/30, (-self.viewPositionY + pygame.mouse.get_pos()[1])/30, 1), self.terrain)
        if(pygame.key.get_pressed()[K_d]):
            self.population.addCreature((-self.viewPositionX + pygame.mouse.get_pos()[0])/30, (-self.viewPositionY + pygame.mouse.get_pos()[1])/30, Archer((-self.viewPositionX + pygame.mouse.get_pos()[0])/30, (-self.viewPositionY + pygame.mouse.get_pos()[1])/30, 1), self.terrain)
        if(pygame.key.get_pressed()[K_f]):
            self.population.addCreature((-self.viewPositionX + pygame.mouse.get_pos()[0])/30, (-self.viewPositionY + pygame.mouse.get_pos()[1])/30, Wizard((-self.viewPositionX + pygame.mouse.get_pos()[0])/30, (-self.viewPositionY + pygame.mouse.get_pos()[1])/30, 1), self.terrain)
       
       
        if(pygame.key.get_pressed()[K_UP]):
            self.viewPositionY+=8
        if(pygame.key.get_pressed()[K_DOWN]):
            self.viewPositionY-=8
        if(pygame.key.get_pressed()[K_LEFT]):
            self.viewPositionX+=8
        if(pygame.key.get_pressed()[K_RIGHT]):
            self.viewPositionX-=8

            
        
    def run(self):
            
        time = pygame.time.get_ticks()
        pygame.mixer.music.load("art/rose.ogg")
        pygame.mixer.music.play()
        
        while self.running:
                           
            while(time < pygame.time.get_ticks()):   
                            
                self.handleInput()
                
                self.population.process(self.powers, self.buildingPopulation, self.terrain)
                self.buildingPopulation.process(self.terrain, self.population)
                self.powers.process(self.terrain, self.population, self.buildingPopulation)
                
                time += TIME_QUANTUM
                        
            
            self.screen.blit(self.background, (0,0))
            
            self.terrain.paint(self.screen, (self.viewPositionX, self.viewPositionY))
            self.buildingPopulation.paint(self.screen, (self.viewPositionX, self.viewPositionY))
            self.population.paint(self.screen, (self.viewPositionX, self.viewPositionY))
            self.powers.paint(self.screen, (self.viewPositionX, self.viewPositionY))
            
            pygame.display.flip()
            
                        