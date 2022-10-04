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
game_over = False
paddle_x = randint(100,700)
ball_x, ball_y = 700,300
# put velo back to 6
ball_x_velo = choice([-6,6])
ball_y_velo = choice([-6,6])
lives = 3

# Create a grid of 6 x 5 rectangles. Each row is a different color. 
block_color = 255 # I dont know why I need this variable here but otherwise it dont work 
blocks = []
for j in range(6):
    for i in range(5):
        blocks.append(pygame.draw.rect(window, (255,255,255), pygame.Rect(7 + (i * 198),60 + (j * 40),193,35)))



# Create game loop (that you can exit from) (with 60FPS refresh)
while run:
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    block_color = 254 
    block_color2 = 100
    for block in blocks:
        pygame.draw.rect(window, (block_color,block_color2,255), block) 
        # This still needs to be fixed bc when an index is deleted, it changes the length, then when this is called again it shifts the color values
        if (blocks.index(block) + 1) % 5  == 0:
            block_color -= 40
            block_color2 += 25 

# Create paddle that moves back and forth
    if game_over == False:
        paddle = pygame.draw.rect(window, (0,138,255), pygame.Rect(paddle_x,580,150,15))
        # Create ball
        pygame.draw.circle(window, (255,138,0), (ball_x, ball_y), 10)
        ball = pygame.Rect(ball_x - 7, ball_y - 7,15,15)
        # Scoreboard 
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 30)
        scoreboard = window.blit(font.render("Lives: " + str(lives), False, (255,138,255)), (20,15)) 

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and paddle_x > 10:
        paddle_x -= 10 
    if keys[pygame.K_RIGHT] and paddle_x < 840:
        paddle_x += 10  
    
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
    for block in to_remove:
        blocks.remove(block)
    #if ball.colliderect(block):
        ball_y_velo *= -1
        ball_y -= 30 * (ball_y_velo / 6) 


# After loss of life, game pauses and resumes on paddle movement

# When ball hits paddle AND BLOCK, angle is dependent on where it hit the paddle

# If this r/g/b value is below a certain #, rectangle deletes

# Lives scoreboard
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 30)

# Game over functionality
    if lives == 0:
        print("\n\nyou lost nerd\n\n")
        run = False


# Win functionality
    if len(blocks) == 0:
        print("\n\nyou won brudda\n\n")
        run = False 


    pygame.time.Clock().tick(120)
    pygame.display.update()

"""
OBSERVATIONS:

* Lots of if statements
    - It seems like a lot to be checking 120 times a second. Are there alternatives for checking ball coordinates?

* Definetly better ways to manage this code. Should definitely break it into more modular pieces in future (functions)

* Could definetly run alot smoother, especially given were already at 120 FPS
    - Must mean theres too many calculations/check statements going on 

"""
"""
IMPROVEMENTS:
* The game over functionality should be better
"""


