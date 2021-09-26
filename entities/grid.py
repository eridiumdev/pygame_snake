import random

import config
import entities.snake
import entities.snake_chunk
import entities.food


class Grid:
    def __init__(self, width, height, cell_width, cell_height):
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.width = self._adjust_x(width)
        self.height = self._adjust_y(height)

    def generate_snake_xy(self) -> tuple[int, int]:
        # Put snake in the left center
        x = self.width // 4
        y = self.height // 2 - self.cell_width // 2
        config.DEBUG and print("Generated new snake x,y:", (x, y))
        x = self._adjust_x(x)
        y = self._adjust_y(y)
        config.DEBUG and print("Adjusted snake x,y:", (x, y))

        return x, y

    def generate_food_xy(self) -> tuple[int, int]:
        x = random.randrange(0, self.width - self.cell_width, self.cell_width)
        y = random.randrange(0, self.height - self.cell_height, self.cell_height)
        config.DEBUG and print("Generated new food x,y:", (x, y))
        x = self._adjust_x(x)
        y = self._adjust_y(y)
        config.DEBUG and print("Adjusted food x,y:", (x, y))

        return x, y

    def food_overlaps_with_snake(self, snake: entities.snake.Snake, food: entities.food.Food) -> bool:
        for chunk in snake.chunks:
            if food.rect.clip(chunk.border.rect):
                config.DEBUG and print("Food overlaps with snake ({0} clips {1})".format(
                                       (food.rect.x, food.rect.y),
                                       (chunk.border.rect.x, chunk.border.rect.y)))
                return True
        return False

    def food_overlaps_with_snakes_head(self, snake_head: entities.snake_chunk.SnakeChunk,
                                       food: entities.food.Food) -> bool:
        if food.rect.clip(snake_head.border.rect):
            config.DEBUG and print("Food overlaps with snake head ({0} clips {1})".format(
                                   (food.rect.x, food.rect.y),
                                   (snake_head.border.rect.x, snake_head.border.rect.y)))
            return True
        return False

    def snake_head_overlaps_with_chunk(self, snake_head: entities.snake_chunk.SnakeChunk,
                                       chunk: entities.snake_chunk.SnakeChunk) -> bool:
        if snake_head.border.rect.clip(chunk.border.rect):
            config.DEBUG and print("Snake head overlaps with chunk ({0} clips {1})".format(
                (snake_head.border.rect.x, snake_head.border.rect.y),
                (chunk.border.rect.x, chunk.border.rect.y)))
            return True
        return False

    def _adjust_x(self, x):
        return x - (x % self.cell_width)

    def _adjust_y(self, y):
        return y - (y % self.cell_height)
