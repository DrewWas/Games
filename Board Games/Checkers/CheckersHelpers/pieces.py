import pygame
from .constants import BLUE, WHITE, SQUARE_SIZE, ROWS, COLS, CROWN


class Piece:
    PADDING = 15
    BORDER = 5

    def __init__(self, row, col, color, opp_color):
        self.row = row
        self.col = col
        self.color = color
        self.opp_color = opp_color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

        """
        if self.color == BLUE:
            self.direction = -1
        else:
            self.direction = 1
        """


    def calc_pos(self):
        self.x = (SQUARE_SIZE * self.col) + (SQUARE_SIZE // 2)
        self.y = (SQUARE_SIZE * self.row) + (SQUARE_SIZE // 2)

    def make_king(self):
        self.king = True
    
    def draw(self, win):
        rad = (SQUARE_SIZE // 2) - self.PADDING 
        pygame.draw.circle(win, self.opp_color, (self.x, self.y), rad + self.BORDER)
        pygame.draw.circle(win, self.color, (self.x, self.y), rad)
        if self.king:
            win.blit(CROWN, (self.x - (CROWN.get_width() // 2), self.y - (CROWN.get_height() // 2)))
 
   
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()


    def __repr__(self):
        return str(self.color)



