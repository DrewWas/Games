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
keys = pygame.key.get_pressed()
paddle_x = randint(0,850)
ball_x = 100
ball_y = 100
ball_x_velo = choice([-5,5]) 
ball_y_velo = choice([-5,5]) 
lives = 3



# ---Main game loop---
def main():
    run = True
    while run:
        window.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        paddle()
        ball()
        scoreboard(lives)
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
    elif ball_y > 590:
        lives -= 1 
        ball_y_velo *= -1 # This line will be deleted
        # ---- FINISH BALL RESET FUNCTION. THIS CHECKPOINT IS JUST FOR SCOREBOARD -----
    if ball_x > 990 or ball_x < 10:
        #ball_x -= 15 * (5/ball_x_velo)
        ball_x_velo *= -1


# ---Scoreboard---
def scoreboard(lives):
    my_font = pygame.font.SysFont("Arial", 30)
    board = my_font.render("Lives: " + str(lives), False, (255,138,255))
    window.blit(board, (20,15)) 


"""
TODO:
- Make ball bounce of paddle at incident angle
- If ball goes below paddle, player loses life
- If player loses 3 lives, game over SCREEN
- n x m grid of blocks
- if ball hits block, it loses some strength (block functionality)
- if all blocks are gone. win SCREEN
"""



if __name__ == "__main__":
    main()

