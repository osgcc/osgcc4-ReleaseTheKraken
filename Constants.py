'''
Created on Oct 23, 2010

@author: lucas
'''

TIME_QUANTUM = 15

DIRECTION = ((1,0),(-1,0),(0,1),(0,-1))

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

SQUARE_SIZE = 30

WATER = 2
ROCK = 3

PEASANT_SPAWNER = 1
SWORDSMAN_SPAWNER = 2
ARCHER_SPAWNER = 3
WIZARD_SPAWNER = 4

BUILDING_REGENERATION = 0.02
BUILDING_LIFE = 500

PEASANT_SPAW_TIME = 5000
MAX_NUMBER_PEASANTS = 2
PEASANT_REPAIR_RATE = 0.5
PEASANT_BUILD_INTERVAL = 3000
PEASANT_BUILD_CHANCE = 20
PEASANT_REGENERATION = 0.02
PEASANT_SPEED = 1000
PEASANT_LIFE = 100

KRAKEN_SPEED = 600
KRAKEN_LIFE = 5000
KRAKEN_REGENERATION = 0.05
KRAKEN_ATTACK = 500
KRAKEN_ATTACK_SPEED = 800


'''archer'''
ARCHER_LIFE = 100
ARCHER_SPEED = 800
ARCHER_REGENERATION = 0.02
ARCHER_ATTACK = 40
ARCHER_ATTACK_SPEED = 1000
ARCHER_SPAWN_TIME = 10000
MAX_NUMBER_ARCHERS = 4

ARROW_SPEED = 0.1

'''Swordsman'''
SWORDSMAN_SPEED = 1000
SWORDSMAN_LIFE = 220
SWORDSMAN_REGENERATION = 0.05
SWORDSMAN_ATTACK = 100
SWORDSMAN_ATTACK_SPEED = 1000
SWORDSMAN_SPAWN_TIME = 10000
MAX_NUMBER_SWORDSMAN = 4

'''Wizard'''
LIGHTNING_SPEED = 0.1
WIZARD_SPEED = 750
WIZARD_LIFE = 150
WIZARD_REGENERATION = 0.06
WIZARD_ATTACK = 80
WIZARD_ATTACK_SPEED = 1500
WIZARD_SPAWN_TIME = 20000
MAX_NUMBER_WIZARDS = 2