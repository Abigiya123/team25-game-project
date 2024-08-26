import sys
import pygame
from game import Game

class Controller:
    def __init__(self, game: Game) -> None:
        self.game = game
        self.events = None
    
    
    def get_and_handle_events(self) -> None:
        """
        - Called by the game loop
        - Gets the events, then asks the appropriate Game objects to handle them
        """
        self.events = pygame.event.get()
        self.exit_if_quit()
        pressed_keys = pygame.key.get_pressed()
        
        # WASD for Car 1
        if pressed_keys[pygame.K_w]:
            self.game.car1.move_forward()
        if pressed_keys[pygame.K_s]:
            self.game.car1.move_backward()
        if pressed_keys[pygame.K_a]:
            self.game.car1.move_left()
        if pressed_keys[pygame.K_d]:
            self.game.car1.move_right()
        
        # Arrow keys for Car 2
        if pressed_keys[pygame.K_UP]:
            self.game.car2.move_forward()
        if pressed_keys[pygame.K_DOWN]:
            self.game.car2.move_backward()   
        if pressed_keys[pygame.K_LEFT]:
            self.game.car2.move_left()
        if pressed_keys[pygame.K_RIGHT]:
            self.game.car2.move_right()
    
    
    def exit_if_quit(self) -> None:
        """Exit the game if the user quits"""
        for event in self.events:
            if event.type == pygame.QUIT:
                sys.exit()
      