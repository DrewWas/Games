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
ball_x_velo = choice([-5,5])
ball_y_velo = choice([-5,5])
lives = 3
block_color = 255

# Create game loop (that you can exit from) (with 60FPS refresh)
while run:
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# Create a grid of 5 x 8 rectangles. Each row is a different color. 
    for i in range(8):
        for j in range(5):
            pygame.draw.rect(window, (block_color,138,0), pygame.Rect(10 + (i * 200),20 + (j * 20),190,15)) 

# Create paddle that moves back and forth
    paddle = pygame.draw.rect(window, (0,138,255), pygame.Rect(paddle_x,580,150,15))

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and paddle_x > 10:
        paddle_x -= 6 
    if keys[pygame.K_RIGHT] and paddle_x < 840:
        paddle_x += 6 
    
# Create ball 
    pygame.draw.circle(window, (255,138,0), (ball_x, ball_y), 10)
    ball = pygame.Rect(ball_x - 7, ball_y - 7,15,15)
    ball_x += ball_x_velo 
    ball_y -= ball_y_velo 

# Ball bounces off walls, paddle, and rect
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

# When ball hits rectangle, one of the RGB values drops. 
# If this r/g/b value is below a certain #, rectangle deletes
    pygame.time.Clock().tick(120)
    pygame.display.update()
# Game over functionality




"""
OBSERVATIONS:

* Lots of if statements
    - It seems like a lot to be checking 120 times a second. Are there alternatives for checking ball coordinates?

"""
