import pygame

from StartMenu import MainStartMenu
from GameWindow import GameWindow


if __name__ == "__main__":

    running = True

    while running:

        # Menu
        mainMenu = MainStartMenu()
        mainMenu.run()

        # Se apertou QUIT
        if not mainMenu.IsGameStarted():
            running = False
            break

        # Jogo
        gameWindow = GameWindow()
        gameWindow.run()

        # Se o jogo terminou por colisão,
        # o loop volta para o StartMenu

    pygame.quit()