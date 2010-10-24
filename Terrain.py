
import random

from TerrainCell import TerrainCell
from Paintable import Paintable

from Constants import *

class Terrain(Paintable):
    
    def __init__(self, numRows, numColumns):
        
        self.terrainCellMatrix = []
        
        self.rows = numRows
        self.columns = numColumns
        
        for i in range(numRows):
            
            tempRow = []
            
            for j in range(numColumns):                
               
                type = random.randint(0,1)
                    
                tempRow.append(TerrainCell(SQUARE_SIZE*i, SQUARE_SIZE*j, type))
                
            self.terrainCellMatrix.append(tempRow)
            
        self.generateRegions()
    
    
    def generateRegions(self):
        
        for k in range(10):
            for i in range(self.rows-2):
               
                for j in range(self.columns-2):
                   
                    x = random.randint(-1,1)
                    y = random.randint(-1,1)
                    
                    self.terrainCellMatrix[i+1][j+1] = TerrainCell(SQUARE_SIZE*(i+1), SQUARE_SIZE*(j+1), self.terrainCellMatrix[i+x+1][j+y+1].getType())
                    
        mountains = random.randint(1, 10)
        
        for i in range(mountains):
            self.makeRegion(random.randint(0, self.columns), random.randint(0, self.rows), 3, 15+random.randint(0, 60))
            
        lakes = random.randint(1, 10)
        
        for i in range(lakes):
            self.makeRegion(random.randint(0, self.columns), random.randint(0, self.rows), 2, 15+random.randint(0, 60))
                    
        self.generateBorder()
        
          
    def generateBorder(self):
        
        for i in range(self.columns):
            self.terrainCellMatrix[i][0] = TerrainCell(SQUARE_SIZE*(i), SQUARE_SIZE*(0), 3)
            
        for i in range(self.columns):
            self.terrainCellMatrix[i][self.rows-1] = TerrainCell(SQUARE_SIZE*(i), SQUARE_SIZE*(self.rows-1), 3)
            
        for i in range(self.columns):
            self.terrainCellMatrix[0][i] = TerrainCell(SQUARE_SIZE*(0), SQUARE_SIZE*(i), 3)
            
        for i in range(self.columns):
            self.terrainCellMatrix[self.columns-1][i] = TerrainCell(SQUARE_SIZE*(self.columns-1), SQUARE_SIZE*(i), 3)
                    
    def makeRegion(self, x, y, type, n): 
        
        if(n>=0 and x>=0 and y>=0 and x < self.columns and y < self.columns):
            
            self.terrainCellMatrix[x][y] = TerrainCell(SQUARE_SIZE*(x), SQUARE_SIZE*(y), type)
            
            next = random.randint(0, 2)
            remaining = n
            
            for i in range(next):                
                
                remaining -= 1
                
                if(random.randint(0,1)==0):
                    self.makeRegion(x, y + random.randint(0,1)*2-1, type, remaining)
                else:
                    self.makeRegion(x + random.randint(0,1)*2-1, y, type, remaining)
               
                
            
            
    def getNumRows(self):

        return self.rows
    
    def getNumColumns(self):
        
        return self.columns
    
    def getThingOcupying(self, x, y):
        
        if(x < 0 or x >= self.columns or y < 0 or y >= self.rows):        
            return None
        
        return self.terrainCellMatrix[x][y].getThingOcupying()
         
    def getType(self, x, y):
        return self.terrainCellMatrix[x][y].getType()
            
    def removeThingOcupying(self, x, y):
        if(x >= 0 and x < self.columns and y >= 0 and y < self.rows):          
            self.terrainCellMatrix[x][y].setThingOcupying(None)
        
    def removeThingOcupyingKraken(self, x, y):    
        if(self.terrainCellMatrix[x][y].getType() == WATER):
            self.terrainCellMatrix[x][y].setThingOcupying(WATER)
        else:
            self.terrainCellMatrix[x][y].setThingOcupying(None)
        
    def setThingOcupying(self, x, y, thing):        
        self.terrainCellMatrix[x][y].setThingOcupying(thing)
    
    def walkable(self, x, y):
             
        if(x >= 0 and x < self.columns and y >= 0 and y < self.rows):                                
                                   
            if(self.terrainCellMatrix[x][y].getThingOcupying() == None):                              
                return True
            else:
                return False            
        else:
            
            return False
        
    def krakenWalkable(self, x, y):
             
        if(x >= 0 and x < self.columns and y >= 0 and y < self.rows):                                
                                   
            if(self.terrainCellMatrix[x][y].getThingOcupying() == None or self.terrainCellMatrix[x][y].getThingOcupying() == WATER):                              
                return True
            else:
                return False            
        else:
            
            return False
    
            
    def paint(self, screen, translation):
        
        for i in range(self.rows):
            
            for j in range(self.columns):
                
                    self.terrainCellMatrix[i][j].paint(screen, translation)
                
                