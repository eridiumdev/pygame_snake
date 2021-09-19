import collections

import pygame

import constants
import framework.game
import framework.escapable

import entities.snake
import config


class Game(framework.escapable.ExitOnEscape, framework.game.Game):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Init snake
        snake_width, snake_height = config.SNAKE_CHUNK_SIZE
        snake_x = self.win.width // 4
        snake_y = self.win.height // 2 - snake_height // 2
        # adjust x/y to conform to rectangular grid
        snake_x -= snake_x % snake_width
        snake_y -= snake_y % snake_height

        self.snake = entities.snake.Snake(snake_x, snake_y)
        self.pressed_keys = []

    def render(self):
        super().render()
        self.screen.fill(config.GAME_BACKGROUND_COLOR)
        self.snake.render(self.screen)

    def print_keys_pressed(self):
        s = "Keys pressed: ["
        for key in self.pressed_keys:
            desc, _ = self.get_direction_by_key(key)
            s += " " + desc
        s += " ]"
        print(s)

    def handle_event(self, event: pygame.event.Event):
        super().handle_event(event)

        if event.type == pygame.KEYDOWN:
            desc, _ = self.get_direction_by_key(event.key)
            config.DEBUG and print("<{0}> pressed".format(desc))
            if self.pressed_keys.count(event.key) == 0:
                self.pressed_keys.insert(0, event.key)
            config.DEBUG and self.print_keys_pressed()
        elif event.type == pygame.KEYUP:
            desc, _ = self.get_direction_by_key(event.key)
            config.DEBUG and print("<{0}> released".format(desc))
            while self.pressed_keys.count(event.key) > 0:
                self.pressed_keys.remove(event.key)
            config.DEBUG and self.print_keys_pressed()

    def handle_keys_pressed(self, keys_pressed):
        for key in self.pressed_keys:
            _, direction = self.get_direction_by_key(key)
            if direction is not None:
                self.snake.queue_move(direction)
                break

    def get_direction_by_key(self, key):
        if key == pygame.K_UP:
            return "UP", constants.DIRECTION_UP
        elif key == pygame.K_DOWN:
            return "DOWN", constants.DIRECTION_DOWN
        elif key == pygame.K_LEFT:
            return "LEFT", constants.DIRECTION_LEFT
        elif key == pygame.K_RIGHT:
            return "RIGHT", constants.DIRECTION_RIGHT
        else:
            return "NONE", None
