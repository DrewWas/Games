import pygame
from CheckersHelpers.constants import WIDTH, HEIGHT

FPS = 60

# Window Setup
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


main()
