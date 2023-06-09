import pygame
from CheckersHelpers.constants import WIDTH, HEIGHT, ROWS, COLS, WHITE, BLUE
from CheckersHelpers.board import Board
from CheckersHelpers.pieces import Piece

FPS = 60

# Window Setup
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")


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
                pass

        board.draw(WIN)
        pygame.display.update()

    pygame.quit()


main()
