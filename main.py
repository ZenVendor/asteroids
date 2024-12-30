import pygame
import constants as c
import player
import asteroid
import asteroidfield
import shot
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

    # Set up clock
    clock = pygame.time.Clock()
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (updatable, drawable, shots)

    # Create objects
    ship = player.Player(c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2)
    field = asteroidfield.AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        for item in updatable:
            item.update(dt)

        for item in asteroids:
            if ship.collide(item):
                print("Game over!")
                sys.exit(0)

        for item in drawable:
            item.draw(screen)

        clock.tick(60)
        dt = clock.get_time() / 1000
        pygame.display.flip()


if __name__ == "__main__":
    main()
