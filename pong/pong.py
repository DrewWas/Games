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
        MY_FONT = pygame.font.Font('fontpixel.ttf', 70)
        self.player1_pos = [10, randint(200, 500)] 
        self.player2_pos = [1470, randint(200, 500)] 
        self.score = Score(MY_FONT)

    def start(self):

        # basic setup
        self.clock = pygame.time.Clock()
        self.SCREEN = pygame.display.set_mode((HEIGHT, WIDTH))
        pygame.display.set_caption("python pong")
        
        player1 = Paddle(self.player1_pos) 
        player2 = Paddle(self.player2_pos) 

        # main event loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            
            keys = pygame.key.get_pressed()

            if keys[pygame.K_w] and self.player1_pos[1] > 5:
                self.player1_pos[1] -= 7 
                player1.update(BLUE, self.player1_pos)

            if keys[pygame.K_s] and self.player1_pos[1] < 620:
                self.player1_pos[1] += 7 
                player1.update(BLUE, self.player1_pos)

            if keys[pygame.K_UP] and self.player2_pos[1] > 5:
                self.player2_pos[1] -= 7 
                player2.update(RED, self.player2_pos)

            if keys[pygame.K_DOWN] and self.player2_pos[1] < 620:
                self.player2_pos[1] += 7 
                player2.update(RED, self.player2_pos)

            player1.update(BLUE, self.player1_pos)
            player2.update(RED, self.player2_pos)



            self.score.draw_score(self.player1_score, self.player2_score)


            pygame.display.update()
            self.clock.tick(FPS)
            self.SCREEN.fill(BLACK)

        pygame.quit()     




#class Ball:



class Paddle:

    def __init__(self, player_pos):
        self.player_pos = player_pos

    def update(self, color, pos):
        self.player_pos = pos
        pygame.draw.rect(game.SCREEN, color, (self.player_pos[0], self.player_pos[1], 20, 120))

        print(self.player_pos)


class Score:
    
    def __init__(self, font):
        self.font = font
        
        
    def draw_score(self, player1_score, player2_score):
        
        player1_surface= self.font.render(str(player1_score), False, WHITE)
        player2_surface = self.font.render(str(player2_score), False, WHITE)

        game.SCREEN.blit(player1_surface, (350,50))
        game.SCREEN.blit(player2_surface, (1050,50))




if __name__ == "__main__":
    game = Game()
    game.start() 




