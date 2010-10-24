
import pygame
from pygame.locals import *

    
def loadImage(name, colorkey=None):
   
    try:
        image = pygame.image.load(name)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    
    image = image.convert()
    
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
        
    #return image, image.get_rect()
    return image

class Paintable():
    
    def __init__(self):
        
        pass
    
    
    def paint(self, screen, translation):
        
        pass