import pygame

class Game:
    """Constructor"""
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen

    """Asks all the Game objects to draw themselves"""
    def draw_game() -> None:
        pass

    """Called to do whatever action needs to happen in one game cycle, 
    (independently of events/user inputs)"""
    def run_one_cycle() -> None:
        pass