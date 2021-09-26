import entities.grid as _grid
import entities.snake as _snake
import entities.food as _food


class FoodSpawner:
    def __init__(self, grid: _grid.Grid, snake: _snake.Snake):
        self.grid = grid
        self.snake = snake

    def spawn_food(self) -> _food.Food:
        food = _food.Food(*self.grid.generate_food_xy(), self.grid.cell_width, self.grid.cell_height)
        while self.grid.food_overlaps_with_snake(self.snake, food):
            food = _food.Food(*self.grid.generate_food_xy(), self.grid.cell_width, self.grid.cell_height)
        return food
