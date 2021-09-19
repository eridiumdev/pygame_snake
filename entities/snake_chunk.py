import pygame

from framework import renderable
from . import snake_chunk_sprite as sprite
import config


class SnakeChunk(renderable.Renderable):
    is_head = False
    is_tail = False
    hidden_cycles_counter = 0

    def __init__(self, x, y, width, height, direction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction

        border = sprite.SnakeChunkSprite(x, y, width, height)
        body = sprite.SnakeChunkSprite(
            self.get_body_x(border.rect),
            self.get_body_y(border.rect),
            self.get_body_width(border.rect),
            self.get_body_height(border.rect),
        )
        self.border = border
        self.body = body

    def get_body_x(self, border_rect: pygame.Rect):
        return border_rect.x + round(border_rect.width * (1 - config.SNAKE_BODY_SIZE_FACTOR) / 2)

    def get_body_y(self, border_rect: pygame.Rect):
        return border_rect.y + round(border_rect.height * (1 - config.SNAKE_BODY_SIZE_FACTOR) / 2)

    def get_body_width(self, border_rect: pygame.Rect):
        return round(border_rect.width * config.SNAKE_BODY_SIZE_FACTOR)

    def get_body_height(self, border_rect: pygame.Rect):
        return round(border_rect.height * config.SNAKE_BODY_SIZE_FACTOR)

    def is_hidden(self):
        return self.hidden_cycles_counter > 0

    def decrease_hidden_counter(self):
        self.hidden_cycles_counter -= 1

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
        delta_y = self.direction[1] * self.width

        self.border.move(delta_x, delta_y)

        if self.border.rect.x + self.border.rect.width > config.WINDOW_WIDTH:
            self.border.rect.x = 0
        elif self.border.rect.x < 0:
            self.border.rect.x = config.WINDOW_WIDTH - self.border.rect.width

        if self.border.rect.y + self.border.rect.height > config.WINDOW_HEIGHT:
            self.border.rect.y = 0
        elif self.border.rect.y < 0:
            self.border.rect.y = config.WINDOW_HEIGHT - self.border.rect.height

        self.body.rect.x = self.get_body_x(self.border.rect)
        self.body.rect.y = self.get_body_y(self.border.rect)

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

        if self.is_head:
            self.border.paint(config.SNAKE_HEAD_BORDER_COLOR)
            self.body.paint(config.SNAKE_HEAD_BODY_COLOR)
        else:
            self.border.paint(config.SNAKE_BORDER_COLOR)
            self.body.paint(config.SNAKE_BODY_COLOR)

        self.border.render(screen)
        self.body.render(screen)
