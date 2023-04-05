import pygame
import random

from . import Block
from .. import farm
from ..plants import plants_list

class Sprinkle(Block.Block):
    vitamin: bool = False
    name:str = "sprinkle"
    rangeList:list = []
    
    def init(self):
        for j in [-2,-1,0,1,2]:
            for i in [-2,-1,0,1,2]:
                self.rangeList.append(int(super().returnVar()[1].x//32 + i))
                self.rangeList.append(int(super().returnVar()[1].y//32 + j))
        self.rangeList = [self.rangeList[i:i+2] for i in range(0, len(self.rangeList), 2)]
                
    
    def water(self, screen):
        for i in self.rangeList:
            pygame.draw.rect(screen,(0,0,0),(i[0]*32,i[1]*32,10,10))
            if isinstance(farm.tileMap[i[0]][i[1]], plants_list.plants_type):
                print(farm.tileMap[i[0]][i[1]])
                farm.tileMap[i[0]][i[1]].water = True # type: ignore
            