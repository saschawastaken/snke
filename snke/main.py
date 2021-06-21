import pygame
from pygame.display import mode_ok
from pygame.locals import *
# 
import player
import coin
import score
import grid
# window
ws = [500,500]
win = pygame.display.set_mode(ws)

# objects
gridRows = 20
coin = coin.Coin((0,0,255))
score = score.Score(ws)
grid = grid.Grid(ws, gridRows, (255,255,255))
player = player.Player(ws[0] / gridRows)

player.squares.append(pygame.Rect(1, 0, 25, 25))
player.squares.append(pygame.Rect(2, 0, 25, 25))

player.movement[0] = -1
print(player.squares)
player.move()
print(player.squares)
player.move()
print(player.squares)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.movement[0] = -1
            if event.key == pygame.K_d:
                player.movement[0] = 1
            if event.key == pygame.K_w:
                player.movement[1] = -1
            if event.key == pygame.K_s:
                player.movement[1] = 1

    # interactions

    #player.move()

    # graphics
    win.fill((0,0,0))
    
    player.show(win)


    score.show(win)
    grid.show(win)
    pygame.display.update()