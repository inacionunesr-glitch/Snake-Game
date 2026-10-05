import pygame

from DataManager import DataManager


class SoundManager:

    def __init__(self):

        pygame.init()
        pygame.mixer.init()

        self.data_manager = DataManager()

        self.eat_sound = pygame.mixer.Sound(
            "sounds/eat.mp3"
        )

        pygame.mixer.music.load(
            "sounds/music2.mp3"
        )

        self.set_volume(
            self.data_manager.get_data("volume")
        )

        self.update_sound()
        self.update_music()

    def set_volume(self, volume):

        volume = volume / 100

        self.eat_sound.set_volume(volume)
        pygame.mixer.music.set_volume(volume)

    def update_sound(self):

        sound = self.data_manager.get_data("sound")

        if sound == 0:
            self.eat_sound.set_volume(0)
        else:
            self.set_volume(
                self.data_manager.get_data("volume")
            )

    def update_music(self):

        music = self.data_manager.get_data("music")

        if music == 0:
            pygame.mixer.music.stop()

        else:
            self.play_music()

    def play_eat_sound(self):

        if self.data_manager.get_data("sound") == 1:
            self.eat_sound.play()

    def play_music(self):

        if self.data_manager.get_data("music") == 1:

            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play(-1)

    def stop_music(self):

        pygame.mixer.music.stop()