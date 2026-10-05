import pygame


class Player:

    def __init__(
        self,
        x,
        y,
        size_x,
        size_y,
        color,
        speed,
        dir,
        lenght
    ):

        self.x = x
        self.y = y

        self.size_x = size_x
        self.size_y = size_y

        self.color = color

        # Tamanho de cada movimento
        self.speed = speed

        self.dir = dir
        self.lenght = lenght

        self.body = []

    def move(self):

        # Salva a posição anterior
        self.body.append((self.x, self.y))

        if self.dir == "left":
            self.x -= self.speed

        elif self.dir == "right":
            self.x += self.speed

        elif self.dir == "up":
            self.y -= self.speed

        elif self.dir == "down":
            self.y += self.speed

        # Mantém apenas o tamanho necessário da cauda
        self.body = self.body[-self.lenght:]

    def draw(self, screen):

        # Desenha a cauda
        for x, y in self.body:

            pygame.draw.rect(
                screen,
                self.color,
                (
                    x,
                    y,
                    self.size_x,
                    self.size_y
                )
            )

        # Desenha a cabeça
        pygame.draw.rect(
            screen,
            self.color,
            (
                self.x,
                self.y,
                self.size_x,
                self.size_y
            )
        )

    def get_rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            self.size_x,
            self.size_y
        )

    def collided_border(self):

        rect = self.get_rect()

        return (
            rect.left < 0 or
            rect.right > 450 or
            rect.top < 0 or
            rect.bottom > 450
        )

    def collided_body(self):

        # Não tem cauda suficiente para colidir
        if self.lenght <= 1:
            return False

        player_rect = self.get_rect()

        # Ignora a posição mais recente
        for x, y in self.body[:-1]:

            body_rect = pygame.Rect(
                x,
                y,
                self.size_x,
                self.size_y
            )

            if player_rect.colliderect(body_rect):
                return True

        return False