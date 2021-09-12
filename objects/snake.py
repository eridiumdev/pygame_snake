import pygame

import framework.colors as colors

BORDER_FACTOR = 0.8


class Snake:
    def __init__(self, start_x, start_y, width, height):
        self.chunks = []
        self.chunks.append(SnakeChunk(start_x, start_y, width, height))

    def render(self, screen: pygame.Surface):
        for chunk in self.chunks:
            screen.blit(chunk.border.surf, chunk.border.rect)
            screen.blit(chunk.body.surf, chunk.body.rect)


class SnakeChunk:
    def __init__(self, x, y, width, height):
        border = SnakeChunkSprite(x, y, width, height)
        border_rect = border.rect

        body = SnakeChunkSprite(
            border_rect.x + round(border_rect.width * (1 - BORDER_FACTOR) / 2),
            border_rect.y + round(border_rect.height * (1 - BORDER_FACTOR) / 2),
            round(border_rect.width * BORDER_FACTOR),
            round(border_rect.height * BORDER_FACTOR)
        )
        border.paint(colors.BLACK)
        body.paint(colors.YELLOW)

        self.border = border
        self.body = body


class SnakeChunkSprite:
    def __init__(self, x, y, width, height):
        surf = pygame.Surface((width, height))
        rect = surf.get_rect()
        rect.x = x
        rect.y = y
        self.surf = surf
        self.rect = rect

    def paint(self, color):
        self.surf.fill(color)
