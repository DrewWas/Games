import pygame
from random import randint, choice
pygame.init()

# Create a window
pygame.display.init()
WIDTH, HEIGHT = 1000, 550
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
window.fill((0,0,0))

# Useful variables 
run = True
player1_y = randint(5, 425)
player2_y = randint(5, 425) 
ball_x = randint(300,700)
ball_y = randint(150, 400)
ball_x_velo = choice([-6,6])
ball_y_velo = choice([-6,6])
player1_score = 0
player2_score = 0
 
# Create a continiously updating game loop (FPS)
while run:
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            run = False
# Create 2 paddles that move up and down with input

    keys = pygame.key.get_pressed() # this variable must be in while loop (who knew??)
    if keys[pygame.K_s] and player1_y < 422: #FIX THESE DOMAINS!!
        player1_y += 6 
    if keys[pygame.K_w] and player1_y > 8:
        player1_y -= 6 
    if keys[pygame.K_DOWN] and player2_y < 422:
        player2_y += 6 
    if keys[pygame.K_UP] and player2_y > 8:
        player2_y -= 6 

    player1 = pygame.draw.rect(window, (255,138,0), pygame.Rect(15,player1_y,15,120))
    player2 = pygame.draw.rect(window, (0,138,255), pygame.Rect(970,player2_y,15,120))

# Create a ball that bounces around the screen and off paddles
    pygame.draw.circle(window, (255,255,255), (ball_x, ball_y), 9) 
    THE_BALL = pygame.draw.rect(window, (255,255,255), pygame.Rect(ball_x, ball_y, 5,5))
    ball_x += ball_x_velo
    ball_y += ball_y_velo 
    if ball_y < 10 or ball_y > 540:
        ball_y_velo *= -1 
    """
    ---This collision detection implementation seems like it should work, but for whatever reason it    only works half the time. Maybe too much to calculate/check too quickly?----
    if ball_x > 960 and ball_y in range(player1_y, player1_y + 120):
        ball_x_velo = (ball_x_velo * -1)
    if ball_x < 40 and ball_y in range(player2_y, player2_y + 120):
        ball_x_velo = (ball_x_velo * -1)
    """
    if player1.colliderect(THE_BALL): 
        ball_x += 13
        ball_x_velo *= -1
    
    if player2.colliderect(THE_BALL): 
        ball_x -= 13
        ball_x_velo *= -1

# If ball goes past paddle, other player gets a point and game resets
    if ball_x > 990:
        player1_score += 1
        ball_x = 500 
        ball_y = randint(150, 400)
        ball_x_velo *= -1 
        ball_y_velo = choice([-6,6])
    if ball_x < 10:
        player2_score += 1
        ball_x = 500
        ball_y = randint(150, 400)
        ball_x_velo *= -1 
        ball_y_velo = choice([-6,6])
    
# Create scoreboard
    pygame.font.init()
    font = pygame.font.SysFont('Arial', 40)
    scoreboard1 = font.render(str(player1_score), False, (255,138,0))
    scoreboard2 = font.render(str(player2_score), False, (0,138,255))
    window.blit(scoreboard1, (200,50))
    window.blit(scoreboard2, (750,50))

# If one player gets more than 11 points, game is over

    if player1_score > 10:
        window.fill((0,0,0))
        winner = font.render("Player 1 wins!", False, (255,138,0))
        window.blit(winner, (350, 225))
    if player2_score > 10:
        window.fill((0,0,0))
        winner = font.render("Player 2 wins!", False, (0,138,255))
        window.blit(winner, (350, 225))


    pygame.display.update()
    pygame.time.Clock().tick(60)


