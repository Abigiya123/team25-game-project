import pygame
import time
from track import Track
from car import Car

# Initialize pygame and the mixer module
pygame.init()
pygame.mixer.init()

# Load the sound
try:
    cool_sound = pygame.mixer.Sound("cool_sound.wav")
except pygame.error as e:
    print(f"Unable to load sound file: {e}")

# Screen dimensions (Increase height to extend track length)
width, height = 800, 900  # Increased height from 600 to 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Racing Game")

# Colors
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 74)
score_font = pygame.font.SysFont(None, 48)

# Create the track
track = Track(width, height, lane_width=100)

# Create the cars (adjusted positions to start from the lower end of the new, longer track)
car1 = Car(track.track_start_x + 10, height - 100, 50, 80, "asset/car1.jpg")
car2 = Car(track.track_start_x + track.lane_width + 10, height - 100, 50, 80, "asset/car2.jpg")

def display_message(screen, message, color, font, position):
    text = font.render(message, True, color)
    screen.blit(text, position)
    pygame.display.update()

def display_score(screen, score, color, position):
    pygame.draw.rect(screen, black, (position[0] - 10, position[1] - 10, 60, 60))
    score_text = score_font.render(str(score), True, color)
    screen.blit(score_text, position)

def main():
    running = True
    clock = pygame.time.Clock()

    car1_speed = 0
    car2_speed = 0

    car1_score = 0
    car2_score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    car1_speed = -5
                elif event.key == pygame.K_DOWN:
                    car1_speed = 5
                elif event.key == pygame.K_w:
                    car2_speed = -5
                elif event.key == pygame.K_s:
                    car2_speed = 5
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_UP, pygame.K_DOWN]:
                    car1_speed = 0
                elif event.key in [pygame.K_w, pygame.K_s]:
                    car2_speed = 0

        # Move the cars
        car1.y += car1_speed
        car2.y += car2_speed

        # Check if car1 crossed the finish line
        if track.check_finish_line(car1):
            car1_score += 1
            car1.y = height - 100  # Reset car1's position
            try:
                cool_sound.play()  # Play the sound when car1 crosses the finish line
            except pygame.error as e:
                print(f"Unable to play sound: {e}")
            display_message(screen, "Cool!", yellow, font, (width // 2 - 100, height // 2))  # Display message

        # Check if car2 crossed the finish line
        if track.check_finish_line(car2):
            car2_score += 1
            car2.y = height - 100  # Reset car2's position

        # Restrict car1 to the track
        if car1.y < 0:
            car1.y = 0
        elif car1.y > height - car1.height:
            car1.y = height - car1.height

        # Restrict car2 to the track
        if car2.y < 0:
            car2.y = 0
        elif car2.y > height - car2.height:
            car2.y = height - car2.height

        # Drawing everything
        screen.fill(white)
        track.display(screen)
        car1.draw(screen)
        car2.draw(screen)

        # Display the scores
        display_score(screen, car1_score, white, (50, 50))  # Top-left corner for car 1
        display_score(screen, car2_score, white, (width - 100, 50))  # Top-right corner for car 2

        pygame.display.update()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
