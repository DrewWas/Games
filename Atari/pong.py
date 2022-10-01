import pygame
from random import randint
pygame.init()

# Create a window
pygame.display.init()
WIDTH, HEIGHT = 1000, 550
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
window.fill((0,0,0))
 
# Create a continiously updating game loop (FPS)
run = True
player1_y = randint(5, 425)
player2_y = randint(5, 425) 

while run:
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            run = False
# Create 2 paddles that move up and down with input

    keys = pygame.key.get_pressed() # this variable must be in while loop (who knew??)
    if keys[pygame.K_s] and player1_y < 425: #FIX THESE DOMAINS!!
        player1_y += 5
    if keys[pygame.K_w] and player1_y > 13:
        player1_y -= 5 
    if keys[pygame.K_DOWN]:
        player2_y += 5
    if keys[pygame.K_UP]:
        player2_y -= 5

    pygame.draw.rect(window, (255,138,0), pygame.Rect(15,player1_y,15,120))
    pygame.draw.rect(window, (0,138,255), pygame.Rect(970,player2_y,15,120))
   
 
    pygame.display.update()
    pygame.time.Clock().tick(60)

# Create a ball that bounces around the screen and off paddles

# If ball goes past paddle, other player gets a point and game resets

# If one player gets more than 11 points, game is over
