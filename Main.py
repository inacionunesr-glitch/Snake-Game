import pygame

from StartMenu import MainStartMenu
from GameWindow import GameWindow
from ConfigWindow import ConfigWindow


if __name__ == "__main__":

    running = True

    while running:

        mainMenu = MainStartMenu()
        mainMenu.run()

        # Se o usuário fechou o Pygame
        if not mainMenu.running:

            if not mainMenu.IsGameStarted() and not mainMenu.IsConfigOpened():

                running = False
                break

        # Abriu configurações
        if mainMenu.IsConfigOpened():

            configWindow = ConfigWindow()
            configWindow.run()

            # Depois de fechar a configuração,
            # o while volta para o começo e cria o menu novamente.
            continue

        # Começou o jogo
        if mainMenu.IsGameStarted():

            gameWindow = GameWindow()
            gameWindow.run()

            continue

    pygame.quit()