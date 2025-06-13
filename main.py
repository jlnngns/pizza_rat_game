import pygame
from game import Game

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pizza Rat")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 60)
start_text = font.render("Click to Start", True, (255, 255, 255))
text_rect = start_text.get_rect(center=(400, 300))

game = Game()
running = True
game_started = False

while running:
    delta = clock.tick(60) / 1000.0    # define delta time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if not game_started:
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_started = True
        else:
            game.handle_events(event)

    game.update(delta)
    game.draw(screen)

    pygame.display.flip()
pygame.quit()
