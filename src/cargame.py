import pygame
from car import Car
from track import Track

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define paths to images
track_image_path = 'asset/track.png'
car1_image_path = 'asset/car1.jpg'
car2_image_path = 'asset/car2.jpg'

# Create track and cars
track = Track(track_image_path)
car1 = Car(5, int(SCREEN_WIDTH * 0.2), 0, car1_image_path)
car2 = Car(3, int(SCREEN_WIDTH * 0.6), 0, car2_image_path)

# Function to move cars until they reach the bottom
def move_cars(car1, car2, screen, track):
    while car1.y < SCREEN_HEIGHT or car2.y < SCREEN_HEIGHT:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        # if car1.y < SCREEN_HEIGHT:
        #     car1.move()
        # if car2.y < SCREEN_HEIGHT:
        #     car2.move()

        # Draw everything
        screen.fill((0, 0, 0))  # Clear the screen with black
        track.display(screen)
        car1.display(screen)
        car2.display(screen)

        pygame.display.flip()
        pygame.time.delay(50)  # Delay for smoother animation

# Start the race
move_cars(car1, car2, screen, track)

# Quit Pygame
pygame.quit()
