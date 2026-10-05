import pygame


class Fruit:

    def __init__(self, x, y, size_x, size_y, color, img):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.color = color

        self.img = pygame.image.load(img).convert_alpha()

        self.img = pygame.transform.scale(
            self.img,
            (self.size_x, self.size_y)
        )

    def draw(self, screen):
        screen.blit(
            self.img,
            (self.x, self.y)
        )

    def get_rect(self):
        return pygame.Rect(
            self.x,
            self.y,
            self.size_x,
            self.size_y
        )