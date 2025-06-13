import pygame
from game import Game

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pizza Rat")
clock = pygame.time.Clock()

game = Game()
running = True

while running:
    delta = clock.tick(60) / 1000.0    # define delta time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            game.handle_events(event)

    game.update(delta)
    game.draw(screen)

    pygame.display.flip()
pygame.quit()
