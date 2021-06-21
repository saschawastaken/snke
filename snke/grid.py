import pygame

class Grid():

    def __init__(self, ws, rows, color) -> None:
        self.ws = ws
        self.rows = rows
        self.color = color

    def show(self, win):
        
        for i in range(self.rows):
            pygame.draw.line(win, self.color, (0, self.ws[1] * (i + 1)/self.rows), (self.ws[0], self.ws[1] * (i + 1)/self.rows))
        
        for i in range(self.rows):
            pygame.draw.line(win, self.color, (self.ws[0] * (i + 1)/self.rows, 0), (self.ws[0] * (i + 1)/self.rows, self.ws[1]))
