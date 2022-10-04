"""
My last version of breakout was very messy. This is an attempt to re-write in cleaner code
"""
import pygame
from random import randint, choice

# Initialize window
pygame.init()
pygame.display.init()

window = pygame.display.set_mode((1000,600))
pygame.display.set_caption("breakoutV2")
keys = pygame.key.get_pressed()
paddle_x = randint(0,850)

# Main game loop
def main():
    run = True
    while run:
        window.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        paddle()
        pygame.display.update()


# Paddle and Paddle movement
def paddle():
    global paddle_x
    keys = pygame.key.get_pressed()
    pygame.draw.rect(window, (0,138,255), pygame.Rect(paddle_x, 580, 150, 15))
    if keys[pygame.K_LEFT] and paddle_x > 10:
        paddle_x -= 5 
    if keys[pygame.K_RIGHT] and paddle_x < 840:
        paddle_x += 5

main()



