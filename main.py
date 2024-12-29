import pygame
import constants as c


def main():
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
