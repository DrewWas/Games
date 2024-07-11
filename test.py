import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Starting point and direction of the line (e.g., shooting an arrow from center)
start_pos = (screen_width // 2, screen_height // 2)
direction = (1, 0)  # horizontal line to the right
line_length = 300  # length of the line
line_speed = 200  # pixels per second

# Calculate the end point based on the direction
end_pos = (start_pos[0] + direction[0] * line_length,
           start_pos[1] + direction[1] * line_length)

# Initialize variables
current_length = 0
line_done = False

# Clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(white)

    # Calculate the time elapsed since the last frame
    dt = clock.get_time() / 1000  # convert milliseconds to seconds

    # Update the current length of the line
    if not line_done:
        current_length += line_speed * dt
        if current_length >= line_length:
            current_length = line_length
            line_done = True

    # Calculate the current end point of the line
    current_end_pos = (start_pos[0] + direction[0] * current_length,
                       start_pos[1] + direction[1] * current_length)

    # Draw the line
    pygame.draw.line(screen, black, start_pos, current_end_pos, 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()

