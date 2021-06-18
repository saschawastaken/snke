import pygame

pygame.font.init()

font = pygame.font.SysFont('calibri', 20)

class Score():

    def __init__(self, ws) -> None:
        self.val = 999
        self.maxVal = 1000
        self.rect = pygame.Rect(ws[0] - font.render(str(self.maxVal), True, (255,255,255)).get_rect(), 0, 50, 50)
        

    def show(self, win):
        displaying = font.render(str(self.val), True, (255,255,255))
        win.blit(displaying, self.rect)


    def add(self):
        if self.val < self.maxVal:
            self.val += 1