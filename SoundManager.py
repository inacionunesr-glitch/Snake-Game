import pygame

class SoundManager:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.eat_sound = pygame.mixer.Sound("sounds/eat.mp3")

        pygame.mixer.music.load("sounds/music2.mp3")

    def play_eat_sound(self):
        self.eat_sound.play()

    def play_music(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)

    def stop_music(self):
        pygame.mixer.music.stop()
