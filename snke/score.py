import pygame

pygame.font.init()

font = pygame.font.SysFont('calibri', 20)

class Score():

    def __init__(self, ws) -> None:
        self.winWidth = ws[0]
        self.val = 0
        self.maxVal = 1000
        self.rect = pygame.Rect(self.winWidth - font.render(str(self.val), True, (255,255,255)).get_rect().right, 0, 0, 0)

    def show(self, win):
        self.rect = pygame.Rect(self.winWidth - font.render(str(self.val), True, (255,255,255)).get_rect().right, 0, 0, 0)
        displaying = font.render(str(self.val), True, (255,255,255))
        win.blit(displaying, self.rect)

    def add(self):
        if self.val < self.maxVal - 1:
            self.val += 1
