import pygame

class Obstacle:
    def __init__(self, x, y, width, height, image_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        try:
            self.image = pygame.image.load(image_path)
        except pygame.error as e:
            print(f"Unable to load image at {image_path}: {e}")
            self.image = None

    def display(self, screen):
        if self.image:
            screen.blit(self.image, (self.x, self.y))
    def check_collision(self, car):
        pass


