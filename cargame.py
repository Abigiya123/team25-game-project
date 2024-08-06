from car import Car
from track import Track
from obstacle import Obstacle

# Example usage:
car = Car(speed=5, x=0, y=0, width=50, height=50, image="car_image.png")
track = Track(x=0, y=0, width=800, height=600, image="track_image.png", checkpoints=[(100, 100), (200, 200)])
obstacle = Obstacle(x=100, y=100, width=50, height=50, image="obstacle_image.png")

# Example methods usage
car.move('right')
car.display()
car.check_collision(obstacle)

track.display()
track.check_checkpoint(car)

obstacle.display()
obstacle.check_collision(car)
