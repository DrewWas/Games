import pygame
from random import randint
from time import sleep


"""
TODO:
* Homescreen and gameover screen

* Nicer graphics and backgrounds

* Player and ball collision detection

* Ball split

* Weird skipping/lagging

* Implement levels which is basically just dying except next rendering a harder version (more balls) instead of a homescreen
"""





# Setup
pygame.init()

WIDTH = 1400
HEIGHT = 800
FPS = 120
SCREEN =  pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Trouble")
GAMEOVER = True

balls = []



# Colors
black = (0, 0, 0)
blue = (0, 100, 255)
gray = (255, 255, 255)


class Player:


    def __init__(self):
        self.lives = 5
        self.alive = True    
        self.position = 700

        self.line = None
        self.shooting = False
        self.arrow_start_time = 0
        self.arrow_current_length = 0
        self.arrow_speed = 800
        self.arrow_max_length = 800  
        self.arrow_position = self.position




    def draw(self, position):
        pygame.draw.rect(SCREEN, blue, (self.position, 710, 40, 90))



    def shoot(self):
        if not self.shooting:
            self.shooting = True
            self.arrow_start_time = pygame.time.get_ticks()  # Get the current time
            self.arrow_current_length = 0
            self.arrow_position = self.position + 20

    def draw_arrow(self):
        if self.shooting:
            current_time = pygame.time.get_ticks()
            time_elapsed = (current_time - self.arrow_start_time) / 1000  # time in seconds
            self.arrow_current_length = self.arrow_speed * time_elapsed

            if self.arrow_current_length >= self.arrow_max_length:
                self.arrow_current_length = self.arrow_max_length
                self.shooting = False

            end_y = 800 - self.arrow_current_length
            self.line = pygame.draw.line(SCREEN, gray, (self.arrow_position, 800), (self.arrow_position, end_y), 5)


class Balls:

    def __init__(self, layers, bouncy, x_vel, y_vel):
        self.layers = layers
        self.bouncy = bouncy
        self.radius = 24 
        self.x_pos = randint(100,1300) 
        self.y_pos = 100 
        self.x_vel = x_vel 
        self.y_vel = y_vel  
        self.x_acc = 0
        self.y_acc = 9.81 / 100 



    def draw(self):
        self.x_pos += self.x_vel
        self.y_vel += self.y_acc
        self.y_pos += self.y_vel

        if self.y_pos >= (HEIGHT - self.radius):
            self.y_vel *= -1

        if self.x_pos >= (WIDTH - self.radius):
            self.x_vel *= -1

        if self.x_pos <= (self.radius):
            self.x_vel *= -1


        pygame.draw.circle(SCREEN, blue, (self.x_pos, self.y_pos), self.radius)



    def split(self):
        global balls

        new1 = Balls(2,2, self.x_vel * -1, abs(self.y_vel) + 2)
        new2 = Balls(2,2, self.x_vel, abs(self.y_vel) + 2)
        balls.extend([new1, new2])
        




def main():

    running = True
    clock = pygame.time.Clock()
    player = Player()


    # MAKE BETTER
    balls.append(Balls(2, 2, 3, 2))

    while running:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # Input functionality
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]: 
            player.shoot()

        if keys[pygame.K_LEFT] and player.position > 5: 
            player.position -= 8  

        if keys[pygame.K_RIGHT] and player.position < 1349: 
            player.position += 8


        player.draw_arrow()
        player.draw(player.position)


        # TESTING
        for ball in balls:
            ball.draw()
            if player.shooting:
                if ball.x_pos - ball.radius <= player.arrow_position <= ball.x_pos + ball.radius: 
                    if ball.y_pos <= player.arrow_current_length:
                        print(ball.x_pos) 



            # NOT WORKING!!!
            #if ball.x_pos - ball.radius <= player.position + 40 <= ball.x_pos + ball.radius:
            if ball.x_pos + ball.radius <= player.position + 40 <= ball.x_pos - ball.radius:
                if ball.y_pos - ball.radius <= 90 <= ball.y_pos + ball.radius:
                    print("HIT!!! \nGAME OVER!!")



        # DONE TESTING
    
        pygame.display.update()

        clock.tick(FPS)
        SCREEN.fill(black)


    pygame.quit()



if __name__ == "__main__":
    main()





