import pygame
from framework import renderable


class SnakeChunkSprite(renderable.Renderable):
    def __init__(self, x, y, width, height):
        surf = pygame.Surface((width, height))
        rect = surf.get_rect()
        rect.x = x
        rect.y = y
        self.surf = surf
        self.rect = rect

    def move(self, delta_x, delta_y):
        self.rect.x += delta_x
        self.rect.y += delta_y

    def paint(self, color):
        self.surf.fill(color)

    def render(self, screen: pygame.Surface):
        screen.blit(self.surf, self.rect)
