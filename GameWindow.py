import pygame
import random

from Player import Player
from Fruit import Fruit

from SoundManager import SoundManager

class GameWindow:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((450, 450))
        pygame.display.set_caption("Snake Game")

        self.clock = pygame.time.Clock()

        self.running = True
        self.GameOver = False

        icon = pygame.image.load("imgs/icon.png")
        pygame.display.set_icon(icon)

        self.font = pygame.font.Font(
            "fonts/gameFont.ttf",
            20
        )

        self.player = Player(
            224,
            224,
            16,
            16,
            (0, 255, 0),
            16,
            "right",
            1
        )

        self.fruit = None
        self.points = 0

        # Controle da velocidade
        self.move_timer = 0
        self.move_delay = 120

        self.sound_manager = SoundManager()

    def run(self):

        while self.running:

            # Delta time em milissegundos
            dt = self.clock.tick(60)

            # Eventos
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("black")

            self.sound_manager.play_music()

            # Input
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and self.player.dir != "right":
                self.player.dir = "left"

            if keys[pygame.K_d] and self.player.dir != "left":
                self.player.dir = "right"

            if keys[pygame.K_w] and self.player.dir != "down":
                self.player.dir = "up"

            if keys[pygame.K_s] and self.player.dir != "up":
                self.player.dir = "down"

            # Criar fruta
            if self.fruit is None:

                self.fruit = Fruit(
                    random.randint(0, 418),
                    random.randint(0, 418),
                    32,
                    32,
                    (255, 0, 0),
                    "imgs/mushroom.png"
                )

            # Timer do movimento
            self.move_timer += dt

            if self.move_timer >= self.move_delay:

                self.player.move()

                self.move_timer = 0

                # Colisão com borda
                if self.player.collided_border():

                    self.sound_manager.stop_music()
                    self.GameOver = True
                    self.running = False

                # Colisão com cauda
                elif self.player.collided_body():

                    self.sound_manager.stop_music()
                    self.GameOver = True
                    self.running = False

                # Colisão com fruta
                elif self.player.get_rect().colliderect(

                    self.fruit.get_rect()
                ):

                    self.sound_manager.play_eat_sound()
                    self.points += 1
                    self.player.lenght += 1
                    self.fruit = None
                    

            # Desenhar fruta
            if self.fruit is not None:

                self.fruit.draw(self.screen)

            # Score
            score_text = self.font.render(
                f"Score: {self.points}",
                True,
                (255, 255, 255)
            )

            self.screen.blit(
                score_text,
                (10, 10)
            )

            # Player
            self.player.draw(self.screen)

            pygame.display.flip()