import pygame
from rat import Rat
from ui import UI

class Game:
    def __init__(self, screen_width=800, screen_height=600):
        pygame.init()
        pygame.display.set_caption("Pizza Rat")
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "TITLE"   # TITLE, PLAYING, GAME_OVER

        # Background
        self.bg_image = pygame.image.load("assets/subway_bg.png").convert()

        # Audio
        pygame.mixer.music.load("assets/background_music.wav")
        pygame.mixer.music.play(-1)
        self.click_sound = pygame.mixer.Sound("assets/click.wav")

        # Game Elements
        self.rat = Rat("assets/rat_idle.png", "assets/rat_move.png", screen_width, screen_height)
        self.rat_group = pygame.sprite.GroupSingle(self.rat)
        self.ui = UI()

    def reset_game(self):
        self.ui.reset()
        self.rat.move_randomly()
        self.state = "PLAYING"

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.state == "TITLE":
                    self.reset_game()
                elif self.state == "PLAYING":
                    if self.rat.is_clicked(event.pos):
                        self.ui.update_score()
                        self.rat.move_randomly()
                        self.click_sound.play()
                elif self.state == "GAME OVER":
                    self.state = "TITLE"

    def update(self, delta):
        self.rat.update(delta)

    def draw_title_screen(self):
        font_big = pygame.font.Font(None, 64)
        font_small = pygame.font.Font(None, 36)
        title = font_big.render("Pizza Rat", True, (255, 255, 255))
        start_msg = font_small.render("Click to Start", True, (200, 200, 200))

        self.screen.blit(title, title.get_rect(center=(400, 200)))
        self.screen.blit(start_msg, start_msg.get_rect(center=(400, 300)))

    def draw_game_over(self):
        font = pygame.font.Font(None, 48)
        text = font.render("Time's Up! Click to Return", True, (255, 255, 255))
        self.screen.blit(text, text.get_rect(center=(400, 300)))

    def draw(self):
        self.screen.blit(self.bg_image, (0, 0))
        if self.state == "TITLE":
            self.draw_title_screen()
        elif self.state == "PLAYING":
            self.rat_group.draw(self.screen)
            self.ui.draw(self.screen)
        elif self.state == "GAME_OVER":
            self.rat_group.draw(self.screen)
            self.ui.draw(self.screen)
            self.draw_game_over()
        pygame.display.flip()

    def run(self):
        while self.running:
            delta_time = self.clock.tick(60) / 1000.0
            self.handle_events()
            self.update(delta_time)
            self.draw()
        pygame.quit()