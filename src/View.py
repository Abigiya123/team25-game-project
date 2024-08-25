import pygame
from game import Game

class View:
    def __init__(self, screen: pygame.Surface, game: Game) -> None:
        self.screen = screen
        self.game = game
    
    def draw_everything(self) -> None:
        """
        - Draws the background
        - Asks the Game to draw all of its objects
        """
        self.game.draw_game()
        pygame.display.update()
    