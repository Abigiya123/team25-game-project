import pygame
from Game import Game
from View import View
from Controller import Controller

def main():
    # Initializes pygame
    pygame.init() 
    
    # Set display's caption
    pygame.display.set_caption("Austin v.s. Felipe")
    
    # Initializes a screen and a clock
    screen = pygame.display.set_mode((1500, 1000))
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