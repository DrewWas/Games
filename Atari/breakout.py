import pygame
from time import sleep
from random import randint, choice

# Create window 
pygame.init()
pygame.display.init()
window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("breakout")

# Variables
run = True
paddle_x = randint(100,700)
ball_x, ball_y = 700,300
ball_x_velo = choice([-7,7])
ball_y_velo = choice([-7,7])
lives = 3

# Create a grid of 6 x 5 rectangles. Each row is a different color. 
block_color = 10 
blocks = []
for j in range(6):
    for i in range(5):
        blocks.append(pygame.draw.rect(window, (block_color,153,153), pygame.Rect(7 + (i * 198),60 + (j * 40),193,35)))
    block_color += 40

# Create game loop (that you can exit from) (with 60FPS refresh)
while run:
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # FIX COLOR!!!
    for block in blocks:
        pygame.draw.rect(window, (0,138,255),block) 
        print(blocks)




# Create paddle that moves back and forth
    paddle = pygame.draw.rect(window, (0,138,255), pygame.Rect(paddle_x,580,150,15))
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and paddle_x > 10:
        paddle_x -= 8 
    if keys[pygame.K_RIGHT] and paddle_x < 840:
        paddle_x += 8  
    
# Create ball 
    pygame.draw.circle(window, (255,138,0), (ball_x, ball_y), 10)
    ball = pygame.Rect(ball_x - 7, ball_y - 7,15,15)
    ball_x += ball_x_velo 
    ball_y -= ball_y_velo 

# Ball bounces off walls and paddle
    if ball_x < 15 or ball_x > 985:
        ball_x_velo *= -1
    if ball_y < 15:
        ball_y_velo *= -1
    if paddle.colliderect(ball):
        ball_y -= 15
        ball_y_velo *= -1

# If ball goes past paddle, ball resets and player loses life (3 lives)
    if ball_y > 590:
        ball_x = randint(300,700)
        ball_y = 400 
        ball_y_velo *= -1
        lives -= 1

# When ball hits rectangle, one of the RGB values drops and ball bounces off rectangle
    to_remove = [block for block in blocks if block.colliderect(ball)]
    #for block in to_remove:
        #blocks.remove(block)
    print(len(blocks))
    """
    if ball.colliderect(blocks):
        print("collision")
        ball_y_velo *= -1
        ball_y -= 30 * (ball_y_velo / 7) 
    """

# If this r/g/b value is below a certain #, rectangle deletes
    pygame.time.Clock().tick(120)
    pygame.display.update()

# Game over functionality

"""
OBSERVATIONS:

* Lots of if statements
    - It seems like a lot to be checking 120 times a second. Are there alternatives for checking ball coordinates?

* Definetly better ways to manage this code. Should definitely break it into more modular pieces in future

"""




