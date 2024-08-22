import pygame

class Car:
    def __init__(self, speed, x, y, width, height, image):
        self.speed = speed
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def move(self, direction):
        if direction == 'up':
            self.y -= self.speed
        elif direction == 'down':
            self.y += self.speed

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))


