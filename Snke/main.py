import pygame
from pygame.locals import *
# 
import coin
import score

# window
ws = [500,500]
win = pygame.display.set_mode(ws)

# objects
coin = coin.Coin((0,0,255))
score = score.Score(ws)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
    
    win.fill((0,0,0))

    coin.show(win)
    score.show(win)
    pygame.display.update()