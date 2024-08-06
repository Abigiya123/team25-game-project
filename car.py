class Car:
    def __init__(self, speed, x, y, width, height, image):
        self.speed = speed
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    def move(self, direction):
        if direction == 'left':
            self.x -= self.speed
        elif direction == 'right':
            self.x += self.speed
        elif direction == 'up':
            self.y -= self.speed
        elif direction == 'down':
            self.y += self.speed

    def display(self):
        # Code to display the car using Pygame
        pass

    def check_collision(self, other_object):
        # Code to check collision with another object
        pass