import pygame

class Button:
    def __init__(self, text, pos, size, font, bg_color, text_color):
        self.text = text
        self.rect = pygame.Rect(pos, size)
        self.color = bg_color
        self.text_color = text_color
        self.font = font
        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=10)
        screen.blit(self.text_surface, self.text_rect)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)