import pygame
from CheckersHelpers.constants import WIDTH, HEIGHT, ROWS, COLS, WHITE, BLUE, SQUARE_SIZE
from CheckersHelpers.board import Board
from CheckersHelpers.pieces import Piece

FPS = 60

# Window Setup
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

def get_row_col_from_mouse(pos):
    x,y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col



def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()


    while run:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                piece = board.get_piece(row, col)


        board.draw(WIN)
        pygame.display.update()

    pygame.quit()


main()
