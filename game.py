import pygame

import constants
import framework.game
import framework.escapable
import entities.grid
import entities.snake
import entities.food
import entities.food_spawner
import events.snake_head_hits_food
import config


class Game(framework.escapable.ExitOnEscape, framework.game.Game):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid = entities.grid.Grid(self.win.width, self.win.height, *config.GRID_CELL_SIZE)
        # Re-apply window dimensions after grid adjustment
        self.win.width = self.grid.width
        self.win.height = self.grid.height

        snake_x, snake_y = self.grid.generate_snake_xy()
        self.snake = entities.snake.Snake(snake_x, snake_y, *config.GRID_CELL_SIZE)

        self.food_spawner = entities.food_spawner.FoodSpawner(self.grid, self.snake)
        food = self.food_spawner.spawn_food()

        self.foods = []    # type: list[entities.food.Food]
        self.foods.append(food)

        self.pressed_keys = []

    def render(self):
        super().render()

        # Handle game logic
        if self.snake.clock.has_ticked():
            config.DEBUG and print("============= STARTING NEXT CYCLE =============")
            self.snake.digest_food()
            self.snake.move()
            for food in self.foods:
                if self.grid.food_overlaps_with_snakes_head(self.snake.get_head(), food):
                    self.post_event(events.snake_head_hits_food.SnakeHeadHitsFood(food))

        # Handle drawing on screen
        self.screen.fill(config.GAME_BACKGROUND_COLOR)
        self.snake.render(self.screen)
        for food in self.foods:
            food.render(self.screen)

    def print_keys_pressed(self):
        s = "Keys pressed: ["
        for key in self.pressed_keys:
            desc, _ = self._get_direction_by_key(key)
            s += " " + desc
        s += " ]"
        print(s)

    def handle_key_event(self, event: pygame.event.Event):
        super().handle_key_event(event)

        if event.type == pygame.KEYDOWN:
            desc, _ = self._get_direction_by_key(event.key)
            config.DEBUG and print("<{0}> pressed".format(desc))
            if self.pressed_keys.count(event.key) == 0:
                self.pressed_keys.insert(0, event.key)
            config.DEBUG and self.print_keys_pressed()
        elif event.type == pygame.KEYUP:
            desc, _ = self._get_direction_by_key(event.key)
            config.DEBUG and print("<{0}> released".format(desc))
            while self.pressed_keys.count(event.key) > 0:
                self.pressed_keys.remove(event.key)
            config.DEBUG and self.print_keys_pressed()

    def handle_keys_pressed(self, keys_pressed):
        for key in self.pressed_keys:
            _, direction = self._get_direction_by_key(key)
            if direction is not None:
                self.snake.queue_move(direction)
                break

    def handle_user_event(self, event: pygame.event.Event):
        config.DEBUG and print("User event caught: {0}, payload: {1}".format(event.name, event.payload))
        if event.type == constants.EVENT_SNAKE_HEAD_HITS_FOOD:
            self.snake.get_head().digesting_food_counter += 1
            self.foods.remove(event.payload['food'])
            self.foods.append(self.food_spawner.spawn_food())

    def _get_direction_by_key(self, key):
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
