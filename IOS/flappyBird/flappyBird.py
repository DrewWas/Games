"""
Honestly, right now, I don't necesarily see the point in this project. I am not really interested in pure software or pure game developement - moreso software as a means of machine larning and simulation. Therefore, I will leave my 'gamedev' phase, one that feels a bit insincere, to persue straight up ML shit. I don't know nearly enough about ML as I would like, and therefore will be moving most of my coding projects to that domain. For the past few weeks, I've kinda been like 'im not gonna start ML right now because I'm not a good enough programmer and I'll start after I have more experience from coding games.' This is the wrong mentality. Im jumping straight into this shit. Hopefully I return to coding games/sims when I get into RL, but knowing my current understanding of ML, that may be awhile. See you in the matrix
"""


import pygame
from random import randint

pygame.init()
pygame.display.init()
window = pygame.display.set_mode((800,890))
pygame.display.set_caption("flappy bird")

score = 0
birdY = 300
birdAngle = 336
player_velo = -1.5
groundX = 0
collumnsX = 1100
collumnsY = [randint(300,640) for i in range(4)]
gameStart = False

# I AM SUCH A DEGENERATE

def bird(birdY, birdAngle):
    bird = pygame.image.load("bird.png")
    bird = pygame.transform.rotate(bird, birdAngle)
    player = window.blit(bird, (100, birdY)) 
    

def background():
    global gameStart, groundX, collumnsX, collumnsY
    bg = pygame.image.load("background.png")
    ground = pygame.image.load("ground.png")
    window.blit(bg, (0,-50))
    window.blit(bg, (550, -50))
    collumns()
    window.blit(ground, (groundX, 745)) 
    window.blit(ground, (groundX + 420, 745)) 
    window.blit(ground, (groundX + 840, 745)) 
    if groundX < -600:
        groundX = 0

    if gameStart:
        # SPEEEEEDDDDD
        groundX -= 4
        collumnsX -= 4

    if collumnsX < -300:
        collumnsX = 700
        #collumnsY = randint(300,640)



def collumns():
    global collumnsY, collumnsX, gameStart
    pipe = pygame.image.load("pipe.png")
    pipe2 = pygame.transform.rotate(pipe, 180)
    # -740 determines the space between pipes
    window.blit(pipe, (collumnsX + 400, collumnsY[0]))
    window.blit(pipe2, (collumnsX + 400, collumnsY[0] - 740))


def scoreboad(score):
    return 1

def gameover(birdY, score):
    global gameStart
    my_font = pygame.font.SysFont('Blocky', 40)
    game_over_text =  my_font.render("Game Over", False, (255,255,255))
    score_text =  my_font.render("Score: " + str(score), False, (255,255,255))
    if birdY > 690:
        gameStart = False
        background()
        bird(690, birdAngle)
        pygame.draw.rect(window, (207,185,151), pygame.Rect(300, 320, 200, 290), 0, 20) 
        pygame.draw.rect(window, (169,149,123), pygame.Rect(315, 335, 170, 255), 0, 20) 
        window.blit(game_over_text, (325,390))
        window.blit(score_text, (350,490))
    return gameStart




def main():
    global birdY, birdAngle, player_velo, gameStart, collumnsX
    run = True
    clock = pygame.time.Clock()
    #gameStart = False
    while run:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                gameStart = True

 
        birdY += player_velo

        if keys[pygame.K_SPACE]:
            birdY -= 40 
            #print("we hit da space")


        if keys[pygame.K_SPACE] and gameStart == False:
            birdY = 300
            player_velo = 1.5
            collumnsX = 1100
            gameStart == True
            

        if gameStart == False:
            if birdY > 320 or birdY < 280:
                player_velo *= -1

        if gameStart == True:
            player_velo = 5
        
        background()
        bird(birdY, birdAngle)
        gameover(birdY, score)

        clock.tick(60)
        pygame.display.update()


main()

# make space move bird up a normal amount (make this movement look normal
# same shit but with the rotation angle (looks like hes falling face first then picks back up)
# collumns
# scoreboard 




