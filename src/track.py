import pygame

class Track:
    def __init__(self, screen: pygame.Surface, image_path):
        self.screen = screen
        self.image = pygame.image.load(image_path)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def display(self):
        self.screen.blit(self.image, (0, 0))



