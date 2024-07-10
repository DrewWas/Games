import pygame
from random import randint

# Setup
pygame.init()

WIDTH = 1400
HEIGHT = 800
FPS = 120
SCREEN =  pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Trouble")


# Colors
black = (0,0,0)


def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        SCREEN.fill(black)
        pygame.display.flip()


    pygame.quit()


if __name__ == "__main__":
    main()

