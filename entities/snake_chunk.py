import pygame

import framework.renderable as renderable
import framework.objects.scalable as bordered_rect
from . import snake_chunk_sprite as sprite
import config


class SnakeChunk(renderable.Renderable, bordered_rect.Scalable):
    is_head = False
    is_tail = False
    is_hit = False
    hidden_cycles_counter = 0
    digesting_food_counter = 0

    def __init__(self, x, y, width, height, direction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction
        self.body_size_factor = config.SNAKE_BODY_SCALE_FACTOR

        border = sprite.SnakeChunkSprite(x, y, width, height)
        body = sprite.SnakeChunkSprite(*self.get_scaled_dimensions(x, y, width, height, config.SNAKE_BODY_SCALE_FACTOR))
        self.border = border
        self.body = body

    def is_hidden(self):
        return self.hidden_cycles_counter > 0

    def is_digesting_food(self):
        return self.digesting_food_counter > 0

    def move(self):
        config.DEBUG and print("Moving chunk in direction {0}.\nBefore:"
                               "\n\t\tborder.x: {1}"
                               "\n\t\tborder.y: {2}"
                               "\n\t\tbody.x: {3}"
                               "\n\t\tbody.y: {4}".format(self.direction,
                                                          self.border.rect.x,
                                                          self.border.rect.y,
                                                          self.body.rect.x,
                                                          self.body.rect.y,
                                                          ))
        delta_x = self.direction[0] * self.width
        delta_y = self.direction[1] * self.height

        self.border.move(delta_x, delta_y)

        if self.border.rect.x + self.border.rect.width > config.WINDOW_WIDTH:
            self.border.rect.x = 0
        elif self.border.rect.x < 0:
            self.border.rect.x = config.WINDOW_WIDTH - self.border.rect.width

        if self.border.rect.y + self.border.rect.height > config.WINDOW_HEIGHT:
            self.border.rect.y = 0
        elif self.border.rect.y < 0:
            self.border.rect.y = config.WINDOW_HEIGHT - self.border.rect.height

        self.body.rect.x = self.get_scaled_x(self.border.rect.x, self.border.rect.width, self.body_size_factor)
        self.body.rect.y = self.get_scaled_y(self.border.rect.y, self.border.rect.height, self.body_size_factor)

        config.DEBUG and print("\nAfter:"
                               "\n\t\tborder.x: {1}"
                               "\n\t\tborder.y: {2}"
                               "\n\t\tbody.x: {3}"
                               "\n\t\tbody.y: {4}".format(self.direction,
                                                          self.border.rect.x,
                                                          self.border.rect.y,
                                                          self.body.rect.x,
                                                          self.body.rect.y,
                                                          ))

    def render(self, screen: pygame.Surface):
        if self.hidden_cycles_counter > 0:
            # Skip rendering in case chunk is hidden
            return

        if self.is_hit:
            self.body.paint(config.SNAKE_HIT_COLOR)
        elif self.is_digesting_food():
            self.body.paint(config.SNAKE_DIGESTING_FOOD_COLOR)
        elif self.is_head:
            self.body.paint(config.SNAKE_HEAD_COLOR)
        else:
            self.body.paint(config.SNAKE_COLOR)

        self.body.render(screen)
