import pygame
import random

class Rat(pygame.sprite.Sprite):
    def __init__(self, idle_image_path, move_image_path, screen_width, screen_height):
        super().__init__()
        self.idle_image = pygame.image.load(idle_image_path).convert_alpha()
        self.move_image = pygame.image.load(move_image_path).convert_alpha()
        self.image = self.idle_image
        self.rect = self.image.get_rect()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.move_randomly()
        self.last_switch = 0

    def move_randomly(self):
        self.rect.x = random.randint(0, self.screen_width - 0)
        self.rect.y = random.randint(0, self.screen_height - 0)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
    def update_idle(self):
        # Flip between idle and move image every half second
        current_time = pygame.time.get_ticks()
        if current_time - self.last_switch > 500:
            self.image = self.move_image if self.image == self.idle_image else self.idle_image
            self.last_switch = current_time