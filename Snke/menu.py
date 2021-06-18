import pygame
from pygame.locals import *

ws = [500,500]
win = pygame.display.set_mode(ws)

clock = pygame.time.Clock()
fps = 60

while True:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
    
    win.fill((0,0,0))



    pygame.display.update()