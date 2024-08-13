import pygame

class Track:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def display(self, screen):
        screen.blit(self.image, (0, 0))



