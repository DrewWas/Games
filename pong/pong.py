import pygame
from random import randint


# Constants
WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (22, 134, 255)
RED = (226, 1, 1) 
HEIGHT, WIDTH = 1500, 750
FPS = 60


class Game:

    def __init__(self):
        self.running = True
        self.player1_score = 0
        self.player2_score = 0
        #self.ball = Ball()
        pygame.init()
        pygame.font.init()
        MY_FONT = pygame.font.SysFont('Futura', 20)
        self.score = Score(MY_FONT)

    def start(self):

        # basic setup
        self.clock = pygame.time.Clock()
        self.SCREEN = pygame.display.set_mode((HEIGHT, WIDTH))
        pygame.display.set_caption("python pong")

        # main event loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False



            self.score.draw_score(self.player1_score, self.player2_score)
            self.player1_score += 1
            self.player2_score += 1

            pygame.display.update()
            self.clock.tick(FPS)
            self.SCREEN.fill(BLACK)

        pygame.quit()     




#class Ball:



#class Paddle:



class Score:
    
    def __init__(self, font):
        self.font = font
        
        
    def draw_score(self, player1_score, player2_score):
        
        player1_surface= self.font.render(str(player1_score), False, WHITE)
        player2_surface = self.font.render(str(player2_score), False, WHITE)

        game.SCREEN.blit(player1_surface, (100,100))
        game.SCREEN.blit(player2_surface, (200,200))






if __name__ == "__main__":
    game = Game()
    game.start() 




