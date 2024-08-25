import pygame
import time

# Initialize pygame and the mixer module
pygame.init()
pygame.mixer.init()

# Load the sound
cool_sound = pygame.mixer.Sound("cool_sound.wav")  # Ensure this file is in the same directory as your script

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Racing Game")

# Colors
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 74)

# Track class
class Track:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, screen):
        # Draw the road
        pygame.draw.rect(screen, black, [150, 0, self.width - 300, self.height])

        # Draw the finish line
        pygame.draw.rect(screen, red, [150, 100, self.width - 300, 10])

        # Draw the middle dashed line
        for i in range(0, self.height, 40):
            pygame.draw.rect(screen, yellow, [width // 2 - 5, i, 10, 20])

# Car class
class Car:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self, speed):
        self.y -= speed

def display_message(screen, message, color, font, position):
    text = font.render(message, True, color)
    screen.blit(text, position)
    pygame.display.update()

def main():
    running = True
    clock = pygame.time.Clock()

    # Create the track
    track = Track(width, height)

    # Create the cars
    car1 = Car(200, height - 100, 50, 80, "asset/car1.jpg")
    car2 = Car(width - 250, height - 100, 50, 80, "asset/car2.jpg")


    car1_speed = 5
    car2_speed = 3

    car1_won = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move the cars
        car1.move(car1_speed)
        car2.move(car2_speed)

        # Check for the finish line crossing
        if car1.y <= 100:  # Assuming finish line is at y=100
            car1_won = True
            car1_speed = 0
            car2_speed = 0
            cool_sound.play()  # Play the sound
            display_message(screen, "cool, cool, cool", white, font, (200, 200))
            pygame.display.update()
            time.sleep(5)  # Keep the message on screen for 5 seconds
            running = False

        # Drawing everything
        screen.fill(white)
        track.draw(screen)
        car1.draw(screen)
        car2.draw(screen)
        pygame.display.update()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
