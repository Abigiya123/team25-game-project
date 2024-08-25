import pygame

class Car:
    def __init__(self, screen: pygame.Surface, speed, x, y, width, height, image):
        self.screen = screen
        self.speed = speed
        self.x = x
        self.y = y
        self.width = width
        self.height = height        
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        
    def move_left(self):
        self.x -= self.speed
        
    def move_right(self):
        self.x += self.speed

    def move_forward(self):
        self.y -= self.speed
        
    def move_backward(self):
        self.y += self.speed

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))



