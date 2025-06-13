import pygame

class UI:
    def __init__(self, font_path=None, font_size=24):
        self.font = pygame.font.Font(font_path, font_size)
        self.score = 0
        self.high_score = 0
        self.time_left = 60   # seconds

    def update_score(self, amount=1):
        self.score += amount
        if self.score > self.high_score:
            self.high_score = self.score

    def reset(self):
        self.score = 0
        self.time_left = 60

    def update_timer(self, delta_time):
        self.time_left -= delta_time
        if self.time_left < 0:
            self.time_update = 0

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, (255, 215, 0))
        timer_text = self.font.render(f"Time: {int(self.time_left)}", True, (255, 100, 100))

        screen.blit(score_text, (10, 10))
        screen.blit(high_score_text, (10, 40))
        screen.blit(timer_text, (10, 70))