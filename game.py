import pygame
from rat import Rat
from ui import UI

class Game:
    def __init__(self, screen_width=700, screen_height=400):
        pygame.init()

        pygame.display.set_caption("PIZZA RAT")
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

        # Start button rect
        self.start_button_rect = pygame.Rect(275, 220, 150, 50)   # x, y, width, height
        self.start_button_color = (100, 100, 100)
        self.start_button_hover_color = (160, 160, 160)

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
                    if self.start_button_rect.collidepoint(event.pos):     # <---- check if clicked inside button
                        self.click_sound.play()
                        self.reset_game()

                elif self.state == "PLAYING":
                    if self.rat.is_clicked(event.pos):
                        self.ui.update_score()
                        self.rat.move_randomly()
                        self.click_sound.play()

                elif self.state == "GAME OVER":
                    self.state = "TITLE"
            
            elif event.type == pygame.KEYDOWN:
                if self.state == "TITLE":
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        self.click_sound.play()
                        self.reset_game()

                elif self.state == "GAME OVER":
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        self.state = "TITLE"

    def update(self, delta):
        if self.state == "PLAYING":
            self.rat.update(delta)

    def draw_title_screen(self):
        font_big = pygame.font.Font(None, 80)
        font_small = pygame.font.Font(None, 40)

        title = font_big.render("Pizza Rat", True, (255, 255, 255))
        self.screen.blit(title, title.get_rect(center=(350, 155)))
        
        # Check hover
        mouse_pos = pygame.mouse.get_pos()
        if self.start_button_rect.collidepoint(mouse_pos):
            color = self.start_button_hover_color
        else:
            color = self.start_button_color

        # Draw the button
        pygame.draw.rect(self.screen, color, self.start_button_rect, border_radius=10)

        # Button text
        text = font_small.render("Start", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.start_button_rect.center)
        self.screen.blit(text, text_rect)

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