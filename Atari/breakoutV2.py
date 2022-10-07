"""
My last version of breakout was very messy. This is an attempt to re-write in cleaner code
"""
import pygame
from random import randint, choice
from time import sleep

# Initialize window
pygame.init()
pygame.display.init()
pygame.font.init()

window = pygame.display.set_mode((1000,600))
pygame.display.set_caption("breakoutV2")
paddle_x = randint(0,850)
ball_x = 100
ball_y = 100
ball_x_velo = choice([-5,5]) 
ball_y_velo = choice([-5,5]) 
lives = 3


# ---Main game loop---
def main():
    run = True
    gameOver = False
    keys = pygame.key.get_pressed()
    while run:
        window.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        paddle()
        ball()
        scoreboard_and_gameOver(lives)

        pygame.display.update()


# ---Paddle and Paddle movement---
def paddle():
    global paddle_x
    keys = pygame.key.get_pressed()
    the_paddle = pygame.draw.rect(window, (0,138,255), pygame.Rect(paddle_x, 580, 150, 15))
    if keys[pygame.K_LEFT] and paddle_x > 10:
        paddle_x -= 5 
    if keys[pygame.K_RIGHT] and paddle_x < 840:
        paddle_x += 5
    return the_paddle


# Ball and ball functionality ----(need to add ball interactions with blocks)-----
def ball():
    global ball_x, ball_y, ball_x_velo, ball_y_velo, lives 
    pygame.draw.circle(window, (255,138,0), (ball_x, ball_y), 10) 
    ball = pygame.Rect(ball_x - 7, ball_y - 7, 13,13)

    ball_x += ball_x_velo
    ball_y += ball_y_velo 

    if ball_y < 10:
        #ball_y -= 15 * (5/ball_y_velo) 
        ball_y_velo *= -1
    if ball.colliderect(paddle()):
        ball_y_velo *= -1
        ball_y -= 20
        print('collision')

    elif ball_y > 590:
        lives -= 1 
        ball_y = ball_y - 100
        ball_y_velo *= -1
        # Somewhere here, the ball needs to be updates so that it pauses in new position, not where it got passed paddle
        pygame.time.wait(1000)
        
    if ball_x > 990 or ball_x < 10:
        #ball_x -= 15 * (5/ball_x_velo)
        ball_x_velo *= -1


# ---Scoreboard---
def scoreboard_and_gameOver(lives):
    my_font = pygame.font.SysFont("Arial", 30)
    board = my_font.render("Lives: " + str(lives), False, (255,138,255))
    window.blit(board, (20,15)) 
    if lives <= 0:
        game_over()
    # if len(blocks) <= 0: ___ win()


# ---Game Over Functionality---
def game_over():
    window.fill((0,0,0))
    my_font1 = pygame.font.SysFont("Arial", 55)
    game_over_text = my_font1.render("You Lost :(", False, (255,38,15))
    window.blit(game_over_text, (350,260))



"""
TODO:
- Make ball bounce of paddle at incident angle
- n x m grid of blocks
- if ball hits block, it loses some strength (block functionality)
- if all blocks are gone. win SCREEN
- If ball goes below screen, game quickly pauses then ball resets up top
"""



if __name__ == "__main__":
    main()

