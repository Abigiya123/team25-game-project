import pygame

class Car:
    def __init__(self, speed, x, y, image_path):
        self.speed = speed
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def move(self):
        self.y += self.speed

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))



