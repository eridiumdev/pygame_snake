import pygame

import framework.renderable as renderable
import framework.objects.scalable as scalable
import config
import entities.food_sprite as _sprite
import entities.grid_cell as grid_cell


class Food(grid_cell.GridCell, renderable.Renderable, scalable.Scalable):
    is_eaten = False

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.sprite = _sprite.FoodSprite(*self.get_scaled_dimensions(x, y, width, height, config.FOOD_SCALE_FACTOR))

    def render(self, screen: pygame.Surface):
        self.sprite.paint(config.FOOD_COLOR)
        self.sprite.render(screen)
