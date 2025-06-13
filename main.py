import pygame
from game import game

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

running = True
while running:
    delta = clock.tick(60) / 1000.0    # define delta time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
