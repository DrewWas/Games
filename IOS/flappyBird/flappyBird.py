import pygame

pygame.init()
pygame.display.init()
window = pygame.display.set_mode((800,890))
pygame.display.set_caption("flappy bird")
score = 0
birdY = 100
birdAngle = 370
gameOver = False
teals_list = [i * 15 for i in range(110)]

def bird(birdY, birdAngle):
    bird = pygame.image.load("bird.png")
    bird = pygame.transform.rotate(bird, birdAngle)
    player = window.blit(bird, (100, birdY)) 
    

#Background fr
def background():
    bg = pygame.image.load("background.png")
    window.blit(bg, (0,-50))
    window.blit(bg, (550, -50))
    # Bottom shit
    pygame.draw.rect(window, (205,183,149), pygame.Rect(0, 805, 800, 125))
    pygame.draw.rect(window, (184,134,11), pygame.Rect(0, 800, 800, 5))
    pygame.draw.rect(window, (32,178,170), pygame.Rect(0, 780, 800, 20))
    pygame.draw.rect(window, (101,67,33), pygame.Rect(0, 775, 800, 5))
    for i in range(110):
        # Make these fucking squares move while game is going FITFO!!!!
        pygame.draw.rect(window, (0,139,139), pygame.Rect(teals_list[i], 783, 9, 14))

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
        bird(birdY, birdAngle)
        pygame.draw.rect(window, (207,185,151), pygame.Rect(300, 320, 200, 290), 0, 20) 
        pygame.draw.rect(window, (169,149,123), pygame.Rect(315, 335, 170, 255), 0, 20) 
        window.blit(game_over_text, (325,390))
        window.blit(score_text, (350,490))

    return gameOver 




def main():
    global birdY, birdAngle
    run = True
    clock = pygame.time.Clock()
    while run:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        background()
        bird(birdY, birdAngle)


        if gameOver == False:
            birdY += 6
            if birdAngle > 270:
                birdAngle -= 2
            if keys[pygame.K_SPACE]:
                birdAngle = 380
                birdY -= 70


        gameover(birdY, score)

        clock.tick(30)
        pygame.display.update()


main()



# Make background end to end (all in one function)
