import pygame
from random import randint

# Setup
pygame.init()

WIDTH = 1400
HEIGHT = 800
FPS = 120
SCREEN =  pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Trouble")
LEVEL = 1
BALL_POSITIONS = []

# Colors
black = (0, 0, 0)
blue = (0, 100, 255)
gray = (255, 255, 255)


class Player:

    def __init__(self):
        self.lives = 5
        self.alive = True    
        self.position = 700



    def draw(self, position):
        pygame.draw.rect(SCREEN, blue, (self.position, 710, 40, 90))
        pygame.display.update()



    def shoot(self, position):        
        pygame.draw.line(SCREEN, gray, (position + 20, 710), (position + 20, 0))




def main():

    running = True
    clock = pygame.time.Clock()
    player = Player()


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # Input functionality
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]: 
            player.shoot(player.position)

        if keys[pygame.K_LEFT] and player.position > 5: 
            player.position -= 8  

        if keys[pygame.K_RIGHT] and player.position < 1349: 
            player.position += 8


        player.draw(player.position)

        clock.tick(FPS)
        SCREEN.fill(black)


    pygame.quit()


if __name__ == "__main__":
    main()





