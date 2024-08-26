import pygame
from game import Game
from view import View
from controller import Controller

def main():
    # Initializes pygame
    pygame.init() 
    
    # Set display's caption
    pygame.display.set_caption("Austin v.s. Felipe")
    
    # Screen dimensions
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    
    # Initializes a screen and a clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Constructs the Game, View, and Controller
    game = Game(screen)
    view = View(screen, game)
    controller = Controller(game)
    
    # Chooses a frame rate
    frame_rate = 60
    
    # Starts the game loop
    while True:
        # start the clock
        clock.tick(frame_rate)
        
        # handle and respond to events with Controller
        controller.get_and_handle_events()
        
        # run one game cycle
        game.run_one_cycle()
        
        # display the game (draw everything)
        view.draw_everything()
        

main()