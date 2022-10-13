import pygame

pygame.init()
pygame.display.init()
window = pygame.display.set_mode((800,1000))
pygame.display.set_caption("flappy bird")
score = 0
birdY = 100
bg = pygame.image.load("background.png")


def bird(birdY):
    player = pygame.draw.rect(window, (0,138,255), pygame.Rect(100,birdY,100,100))
    pygame.draw.rect(window, (255,138,0), pygame.Rect(400,200,100,100))


def collumns():
    return 1

def scoreboad(score):
    return 1

def gameover(birdY, score):
    # FINISH AFTER BACKGROUND
    my_font = pygame.font.SysFont('Moderna', 50)
    game_over_text =  my_font.render("Game Over", False, (240,10,10))
    score_text =  my_font.render("Score: " + str(score), False, (240,10,10))
    if birdY > 900:
        window.fill((0,0,0))
        window.blit(game_over_text, (300,450))
        window.blit(score_text, (300,650))


def main():
    global birdY
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #background 
        window.blit(bg, (0,0))
        window.blit(bg, (550, 0))
        bird(birdY)
        birdY += 3
        gameover(birdY, score)
        pygame.display.update()

main()
