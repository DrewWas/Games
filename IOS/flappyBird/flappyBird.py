import pygame

pygame.init()
pygame.display.init()
window = pygame.display.set_mode((800,890))
pygame.display.set_caption("flappy bird")
score = 0
birdY = 300
birdAngle = 336
player_velo = -1.5
tealsX = 15
gameOver = False

def bird(birdY, birdAngle):
    bird = pygame.image.load("bird.png")
    bird = pygame.transform.rotate(bird, birdAngle)
    player = window.blit(bird, (100, birdY)) 
    

def background():
    global tealsX
    bg = pygame.image.load("background.png")
    window.blit(bg, (0,-50))
    window.blit(bg, (550, -50))
    # Bottom shit
    pygame.draw.rect(window, (205,183,149), pygame.Rect(0, 805, 800, 125))
    pygame.draw.rect(window, (184,134,11), pygame.Rect(0, 800, 800, 5))
    pygame.draw.rect(window, (32,178,170), pygame.Rect(0, 780, 800, 20))
    pygame.draw.rect(window, (101,67,33), pygame.Rect(0, 775, 800, 5))
        # Make these fucking squares move while game is going FITFO!!!!
    for i in range(110):
        pygame.draw.rect(window, (0,139,139), pygame.Rect(tealsX * i, 783, 9, 14))


def collumns():
    return 1

def scoreboad(score):
    return 1

def gameover(birdY, score):
    global gameOver
    my_font = pygame.font.SysFont('Blocky', 40)
    game_over_text =  my_font.render("Game Over", False, (255,255,255))
    score_text =  my_font.render("Score: " + str(score), False, (255,255,255))
    if birdY > 725:
        gameOver = True
        background()
        bird(725, birdAngle)
        pygame.draw.rect(window, (207,185,151), pygame.Rect(300, 320, 200, 290), 0, 20) 
        pygame.draw.rect(window, (169,149,123), pygame.Rect(315, 335, 170, 255), 0, 20) 
        window.blit(game_over_text, (325,390))
        window.blit(score_text, (350,490))

    return gameOver 




def main():
    global birdY, birdAngle, player_velo, tealsX
    run = True
    clock = pygame.time.Clock()
    gameStart = False
    while run:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
 
        birdY += player_velo

        if keys[pygame.K_SPACE]:
            gameStart = True

        if gameStart == False:
            if birdY > 320 or birdY < 280:
                player_velo *= -1

        if gameStart == True:
            player_velo = 5
            """FIX THESE NOT ALL MOVING AT SAME VELO"""
            tealsX -= .025

        background()
        bird(birdY, birdAngle)
        gameover(birdY, score)

        clock.tick(60)
        pygame.display.update()


main()



