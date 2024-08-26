import pygame

class Car:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.speed = 0  # Initialize speed to 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move_up(self):
        self.y -= self.speed

<<<<<<< HEAD
    def move_down(self):
        self.y += self.speed
=======

>>>>>>> d5bcf1b34ca8f62cc5cd9d7a01f54f2edbdba27d
