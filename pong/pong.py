import pygame
from random import randint, choice


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
        self.difficulty = 12 
        self.level = 1
        self.player1_score = 0
        self.player2_score = 0
        pygame.init()
        pygame.font.init()
        self.MY_FONT_LARGE = pygame.font.Font('fontpixel.ttf', 70)
        self.MY_FONT_MED = pygame.font.Font('fontpixel.ttf', 40)
        self.player1_pos = [10, randint(200, 500)] 
        self.player2_pos = [1470, randint(200, 500)] 
        self.ball_pos = [750, 375]
        self.ball = Ball(self.ball_pos)
        self.score = Score(self.MY_FONT_LARGE)

    def resetGame(self):
        self.player1_pos = [10, randint(200, 500)] 
        self.player2_pos = [1470, randint(200, 500)] 
        self.ball_pos = [750, 375]
        self.ball = Ball(self.ball_pos)
        self.score = Score(self.MY_FONT_LARGE)

    def homescreen(self):
        runHomescreen = True
        while runHomescreen:
            self.SCREEN.fill(BLACK)
            gameOverText1 = self.MY_FONT_LARGE.render("Welcome To PythonPong!", False, BLUE)
            gameOverText2 = self.MY_FONT_MED.render("Click Spacebar to play", False, WHITE)
            gameOverText3 = self.MY_FONT_MED.render("Difficulty: " + str(self.level), False, RED)

            game.SCREEN.blit(gameOverText1, (300, 250))
            game.SCREEN.blit(gameOverText2, (500, 400))
            game.SCREEN.blit(gameOverText3, (600, 475))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_SPACE]: 
                runHomescreen = False

            pygame.display.update()


    def start(self):
        # basic setup
        self.clock = pygame.time.Clock()
        self.newGame = True
        self.SCREEN = pygame.display.set_mode((HEIGHT, WIDTH))
        pygame.display.set_caption("python pong")
        
        player1 = Paddle(self.player1_pos) 
        player2 = Paddle(self.player2_pos) 

        # main event loop
        while self.running:


            if self.newGame:
                self.homescreen()
                self.newGame = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            
            keys = pygame.key.get_pressed()

            if keys[pygame.K_w] and self.player1_pos[1] > 5:
                self.player1_pos[1] -= 15 
                player1.update(BLUE, self.player1_pos)

            if keys[pygame.K_s] and self.player1_pos[1] < 620:
                self.player1_pos[1] += 15 
                player1.update(BLUE, self.player1_pos)

            if keys[pygame.K_UP] and self.player2_pos[1] > 5:
                self.player2_pos[1] -= 15 
                player2.update(RED, self.player2_pos)

            if keys[pygame.K_DOWN] and self.player2_pos[1] < 620:
                self.player2_pos[1] += 15 
                player2.update(RED, self.player2_pos)

            # Paddle deflect logic (added additional margin of error of 20 pixels) 
            if self.ball_pos[0] < 40:
                if self.player1_pos[1] - 10 < self.ball_pos[1] < self.player1_pos[1] + 120 + 10:
                    self.ball.x_velo *= -1 
                    self.ball.pos[0] += 10 

            elif self.ball_pos[0] > 1460: 
                if self.player2_pos[1] - 10 < self.ball_pos[1] < self.player2_pos[1] + 120 + 10:
                    self.ball.x_velo *= -1 
                    self.ball.pos[0] -= 10 


            # Bounce off roof/floor logic 
            if self.ball_pos[1] < 5 or self.ball_pos[1] > 745:
                self.ball.y_velo *= -1 

            # self.difficulty changes the speed of the ball (defaulted to 12)
            self.ball_pos[0] += self.difficulty * self.ball.x_velo
            self.ball_pos[1] += self.difficulty * self.ball.y_velo 


            # Check if a player scores
            if self.ball_pos[0] > 1500:
                self.player1_score += 1
                self.ball_pos[0] = 750 
                self.ball_pos[1] = 375 
                self.ball.x_velo *= -1

            #if self.ball_pos[0] < 5:
            if self.ball_pos[0] < 0:
                self.player2_score += 1 
                self.ball_pos[0] = 750 
                self.ball_pos[1] = 375 
                self.ball.x_velo *= -1



            # Game over logic
            if self.player2_score > 10 or self.player1_score > 10:  
                self.gameOver()
                self.resetGame()
                continue

            player1.update(BLUE, self.player1_pos)
            player2.update(RED, self.player2_pos)
            self.ball.update(self.ball_pos)



            self.score.draw_score(self.player1_score, self.player2_score)


            pygame.display.update()
            self.clock.tick(FPS)
            self.SCREEN.fill(BLACK)




    def gameOver(self):

        gameOverScreen = True
        keys = pygame.key.get_pressed()

        while gameOverScreen:
            self.SCREEN.fill(BLACK)
            gameOverText1 = self.MY_FONT_LARGE.render("Game Over : (", False, RED)
            gameOverText2 = self.MY_FONT_MED.render("Click Spacebar to play again or q to exit", False, BLUE)
            gameOverText3 = self.MY_FONT_MED.render("Select a number (1-3) to play again with a new difficulty", False, WHITE)

            game.SCREEN.blit(gameOverText1, (500, 250))
            game.SCREEN.blit(gameOverText2, (335, 400))
            game.SCREEN.blit(gameOverText3, (210, 500))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_q]: 
                gameOverScreen = False
                pygame.quit()

            if keys[pygame.K_SPACE]:
                self.player1_score = 0
                self.player2_score = 0
                self.newGame = True
                gameOverScreen = False

            if keys[pygame.K_1]:
                self.difficulty = 12 
                self.level = 1
                self.player1_score = 0
                self.player2_score = 0
                self.newGame = True
                gameOverScreen = False

            if keys[pygame.K_2]:
                self.difficulty = 15 
                self.level = 2 
                self.player1_score = 0
                self.player2_score = 0
                self.newGame = True
                gameOverScreen = False


            if keys[pygame.K_3]:
                self.difficulty = 18 
                self.level = 3
                self.player1_score = 0
                self.player2_score = 0
                self.newGame = True
                gameOverScreen = False

            pygame.display.update()

        pygame.display.update()



class Ball:

    def __init__(self, ball_pos):
        self.pos = ball_pos
        self.x_velo = choice([-1,1]) 
        self.y_velo = choice([-1,1]) 

    def update(self, ball_pos):
        # change movement conditions
        pygame.draw.circle(game.SCREEN, WHITE, ball_pos, 12)




class Paddle:

    def __init__(self, player_pos):
        self.player_pos = player_pos

    def update(self, color, pos):
        self.player_pos = pos
        pygame.draw.rect(game.SCREEN, color, (self.player_pos[0], self.player_pos[1], 20, 120))



class Score:
    
    def __init__(self, font):
        self.font = font
        
        
    def draw_score(self, player1_score, player2_score):
        
        player1_surface = self.font.render(str(player1_score), False, WHITE)
        player2_surface = self.font.render(str(player2_score), False, WHITE)

        game.SCREEN.blit(player1_surface, (350,50))
        game.SCREEN.blit(player2_surface, (1050,50))




if __name__ == "__main__":
    game = Game()
    game.start() 




