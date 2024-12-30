import pygame
import circleshape
import random
import constants as c


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= c.ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle = random.uniform(20, 50)
            new_radius = self.radius - c.ASTEROID_MIN_RADIUS
            split1 = Asteroid(self.position.x, self.position.y, new_radius)
            split1.velocity = self.velocity.rotate(new_angle) * 1.2
            split2 = Asteroid(self.position.x, self.position.y, new_radius)
            split2.velocity = self.velocity.rotate(-new_angle) * 1.2

            

