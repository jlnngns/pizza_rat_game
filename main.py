import pygame
from game import Game
from button import Button

pygame.init()
screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption("Pizza Rat")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 60)
start_button = Button("Click to Start", (250, 260), (300, 80), font, (50, 150, 255), (255, 255, 255))

game = Game()
running = True
game_started = False

while running:
    delta = clock.tick(60) / 1000.0    # define delta time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if not game_started:
            if start_button.is_clicked(event):
                game_started = True
        else:
            game.handle_events(event)

    game.update(delta)
    game.draw()

    pygame.display.flip()
pygame.quit()
