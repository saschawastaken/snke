import pygame
from random import randint

class Coin():

    def __init__(self, color):
        self.rect = pygame.Rect(0,0,50,50)
        self.color = color

    def show(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def reset(self, rMax, rMin):
        self.rect.left = randint(rMin, rMax)
        self.rect.top = randint(rMin, rMax)