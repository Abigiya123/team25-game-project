import pygame
from track import Track
from car import Car

class Game:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        
        # Define paths to images
        self.track_image_path = "asset/track.png"
        self.car1_image_path = 'asset/car1.png'
        self.car2_image_path = 'asset/car2.png'
        
        # Create track and cars
        self.track = Track(self.screen, self.track_image_path)
        self.car1 = Car(self.screen, 5, int(screen.get_width() * 0.2), 0, 50, 80, self.car1_image_path)
        self.car2 = Car(self.screen, 3, int(screen.get_width() * 0.6), 0, 50, 80, self.car2_image_path)


    def draw_game(self) -> None:
        """Asks all the Game objects to draw themselves"""
        self.track.display()
        self.car1.display()
        self.car2.display()

    
    def run_one_cycle(self) -> None:
        """Called to do whatever action needs to happen in one game cycle, 
        (independently of events/user inputs)"""
        # self.draw_game()
        pass