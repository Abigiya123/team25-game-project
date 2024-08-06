import pygame
from Game import Game

class View:
    """Constructor"""
    def __init__(self, screen: pygame.Surface, game: Game) -> None:
        self.screen = screen
        self.game = game
    
    """
    - Draws the background
    - Asks the Game to draw all of its objects
    """
    def draw_everything() -> None:
        pass
    