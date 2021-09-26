import pygame

import framework.renderable as renderable


class FoodSprite(renderable.Renderable):
    def __init__(self, x, y, width, height):
        self.circle = ((x + width // 2, y + height // 2), width // 2)
        self.color = None

    def paint(self, color):
        self.color = color

    def render(self, screen: pygame.Surface):
        pygame.draw.circle(screen, self.color, *self.circle)
