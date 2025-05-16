from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, position, radius):
        asteroid = pygame.draw.circle(screen, position, radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
