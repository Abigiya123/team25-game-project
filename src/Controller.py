import sys
import pygame
from Game import Game

class Controller:
    def __init__(self, game: Game) -> None:
        self.game = game
        self.events = None
    
    """
    - Called by the game loop
    - Gets the events, then asks the appropriate Game objects to handle them
    """
    def get_and_handle_events() -> None:
        pass
    
    """Exit the game if the user quits"""
    def exit_if_quit(events) -> None:
        pass
    
    """Checks if a specific key was pressed on this cycle of the game loop"""
    def key_was_pressed_on_this_cycle(key, events) -> bool:
        pass