import pygame 
import time 
import random
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Snake Game")

    surface.fill((255, 153, 255))

    block = pygame.image.load("block.jpg").convert()
    block_x,block_y = 100,100

    surface.blit(block, (block_x, block_y))


    pygame.display.flip()


    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        time.sleep(0.1)


        