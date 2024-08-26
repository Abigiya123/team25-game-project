import pygame

class Track:
    def __init__(self, width, height, lane_width):
        self.width = width
        self.height = height
        self.lane_width = lane_width
        self.track_width = 2 * lane_width  # Total track width (left lane + right lane)
        self.track_start_x = (width - self.track_width) // 2  # Start of the track on the x-axis
        self.cool_sound = pygame.mixer.Sound("cool_sound.wav")  # Load the sound file

    def display(self, screen):
        # Draw the left and right lanes
        left_lane_rect = pygame.Rect(self.track_start_x, 0, self.lane_width, self.height)
        right_lane_rect = pygame.Rect(self.track_start_x + self.lane_width, 0, self.lane_width, self.height)
        
        pygame.draw.rect(screen, (50, 50, 50), left_lane_rect)  # Left lane color (gray)
        pygame.draw.rect(screen, (50, 50, 50), right_lane_rect)  # Right lane color (gray)

        # Draw the middle yellow line separating the lanes
        middle_line_x = self.track_start_x + self.lane_width
        pygame.draw.line(screen, (255, 255, 0), (middle_line_x, 0), (middle_line_x, self.height), 5)  # Yellow line

        # Draw the finish line across the track
        finish_line_y = self.height // 8  # Position of the finish line (moved toward the top)
        pygame.draw.line(screen, (255, 0, 0), (self.track_start_x, finish_line_y), (self.track_start_x + self.track_width, finish_line_y), 10)  # Red finish line

    def check_finish_line(self, car1, car2):
        # Check if car1 has crossed the finish line first
        finish_line_y = self.height // 8  # Finish line y-coordinate
        
        if car1.y < finish_line_y and car2.y >= finish_line_y:
            self.cool_sound.play()  # Play the sound if Car 1 crosses the finish line first
            return True
        return False
