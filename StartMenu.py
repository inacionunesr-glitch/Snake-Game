import pygame


class MainStartMenu:

    def __init__(self):

        pygame.init()

        self.running = True
        self.GameStarted = False
        self.ConfigOpened = False

        self.screen = pygame.display.set_mode((450, 450))
        pygame.display.set_caption("Snake Game")

        self.MenuFont = "fonts/gameFont.ttf"

        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(
            self.MenuFont,
            30
        )

        self.title_font = pygame.font.Font(
            self.MenuFont,
            40
        )

        self.play_button = pygame.Rect(
            125, 160, 200, 60
        )

        self.config_button = pygame.Rect(
            125, 235, 200, 60
        )

        self.quit_button = pygame.Rect(
            125, 310, 200, 60
        )

    def run(self):

        while self.running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.play_button.collidepoint(event.pos):

                        self.GameStarted = True
                        self.running = False

                    elif self.config_button.collidepoint(event.pos):

                        self.ConfigOpened = True
                        self.running = False

                    elif self.quit_button.collidepoint(event.pos):

                        self.running = False

            self.screen.fill("black")

            title = self.title_font.render(
                "SNAKE GAME",
                True,
                "white"
            )

            title_rect = title.get_rect(
                center=(225, 100)
            )

            self.screen.blit(title, title_rect)

            pygame.draw.rect(
                self.screen,
                "green",
                self.play_button
            )

            play_text = self.font.render(
                "PLAY",
                True,
                "white"
            )

            play_rect = play_text.get_rect(
                center=self.play_button.center
            )

            self.screen.blit(play_text, play_rect)

            pygame.draw.rect(
                self.screen,
                "blue",
                self.config_button
            )

            config_text = self.font.render(
                "CONFIG",
                True,
                "white"
            )

            config_rect = config_text.get_rect(
                center=self.config_button.center
            )

            self.screen.blit(config_text, config_rect)

            pygame.draw.rect(
                self.screen,
                "red",
                self.quit_button
            )

            quit_text = self.font.render(
                "QUIT",
                True,
                "white"
            )

            quit_rect = quit_text.get_rect(
                center=self.quit_button.center
            )

            self.screen.blit(quit_text, quit_rect)

            pygame.display.flip()

            self.clock.tick(60)

    def IsGameStarted(self):
        return self.GameStarted

    def IsConfigOpened(self):
        return self.ConfigOpened