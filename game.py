import pygame

import framework.game
import framework.escapable
import framework.colors as colors

import objects.snake

SNAKE_CHUNK_SIZE = [50, 50]


class Game(framework.escapable.ExitOnEscape, framework.game.Game):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Init snake
        snake_x = self.win.width / 4
        snake_y = self.win.height / 4
        self.snake = objects.snake.Snake(snake_x, snake_y, *SNAKE_CHUNK_SIZE)

    def render(self):
        # background = pygame.Surface(self.win.get_size())
        # background.fill(colors.BLACK)
        # self.screen.blit(background, (0, 0))
        # self.display.flip()
        self.screen.fill(colors.DARK_GREEN)
        self.snake.render(self.screen)
        super().render()

    def handle_event(self, event: pygame.event.Event):
        super().handle_event(event)
