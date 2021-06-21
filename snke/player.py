import pygame

class Square():
    def __init__(self) -> None:
        pass

    def new(self):
        pass

class Player():

    def __init__(self, squareWidth) -> None:
        self.squareWidth = squareWidth
        self.squares = [pygame.Rect(0, 0, squareWidth, squareWidth)]
        self.color = (255,0,0)
        self.movement = [0,0]

    def show(self, win):
        for i in self.squares:
            pygame.draw.rect(win, self.color, i)

    def add_square(self):
        self.squares.append(self.squares[len(self.squares) - 1])

    def move(self):

        temporaryList = self.squares

        for i in self.squares:
            index = temporaryList.index(i)

            try:
                self.squares[index + 1] = temporaryList[index]
            except IndexError:
                self.squares.pop(index)

        rect = self.squares[0]

        if self.movement[0] == -1:
            rect.left -= self.squareWidth
        if self.movement[0] == 1:
            rect.left += self.squareWidth
        if self.movement[1] == -1:
            rect.top -= self.squareWidth
        if self.movement[1] == 1:
            rect.top += self.squareWidth

        self.squares.pop(0)
        self.squares.insert(0, rect)
