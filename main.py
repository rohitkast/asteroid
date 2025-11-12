import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroidField = AsteroidField()

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')
        player.draw(screen)

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        deltaTime = clock.tick(60)
        dt = deltaTime / 1000 #seconds passed after clock ticked
        updatable.update(dt)
        
        for asteroid in asteroids:
            player_collide = asteroid.collides_with(player)

            if player_collide:
                log_event("player_hit")
                print('Game over!')
                sys.exit()
            
            for shot in shots:
                shot_collide = shot.collides_with(asteroid)
            
                if shot_collide:
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        
if __name__ == "__main__":
    main()
