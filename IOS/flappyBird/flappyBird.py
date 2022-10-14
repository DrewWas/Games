import pygame

pygame.init()
pygame.display.init()
window = pygame.display.set_mode((800,890))
pygame.display.set_caption("flappy bird")
score = 0
birdY = 100
bg = pygame.image.load("background.png")
teals_list = [i * 15 for i in range(110)]

def bird(birdY):
    bird = pygame.image.load("bird.png")
    player = window.blit(bird, (100, birdY)) 
    print(bird)
    pygame.draw.rect(window, (255,138,0), pygame.Rect(400,200,100,100))

#Background fr
def background():
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
    my_font = pygame.font.SysFont('Blocky', 40)
    game_over_text =  my_font.render("Game Over", False, (255,255,255))
    score_text =  my_font.render("Score: " + str(score), False, (255,255,255))
    if birdY > 900:
        background()
        pygame.draw.rect(window, (207,185,151), pygame.Rect(300, 320, 200, 290), 0, 20) 
        pygame.draw.rect(window, (169,149,123), pygame.Rect(315, 335, 170, 255), 0, 20) 
        window.blit(game_over_text, (325,390))
        window.blit(score_text, (350,490))

    #return gameOver 




def main():
    global birdY, teals_list
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        background()
        bird(birdY)
        birdY += 3
        gameover(birdY, score)

        pygame.display.update()


main()



# Make background end to end (all in one function)
