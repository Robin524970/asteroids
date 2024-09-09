import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    game_speed = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    center_x = SCREEN_WIDTH / 2
    center_y = SCREEN_HEIGHT / 2 
    player = Player(center_x, center_y)
    asteroid_field = AsteroidField()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))

        for group in drawable:
            group.draw(screen)
        
        for group in updatable:
            group.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_detected(player) == True:
                exit("Game over!")

        pygame.display.flip()
        delta_time = game_speed.tick(60)
        dt = delta_time / 1000

if __name__ == "__main__":
    main()