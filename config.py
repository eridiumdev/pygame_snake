import constants

# General
DEBUG = False    # full debug logs
ADHOC = True   # ad-hoc logs for testing

# Window
WINDOW_TITLE = 'Snek'
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

# Game
GAME_FPS = 144
GAME_BACKGROUND_COLOR = constants.COLOR_DARK_GREEN

# Grid
GRID_CELL_SIZE = [40, 40]

# Snake
SNAKE_MOVEMENT_CYCLES_PER_SECOND = 8    # how often snake can move
SNAKE_STARTING_DIRECTION = constants.DIRECTION_RIGHT

SNAKE_STARTING_CHUNKS = 3        # including head
SNAKE_BODY_SCALE_FACTOR = 0.8    # how much space does a snake chunk body occupy in a grid cell

SNAKE_COLOR = constants.COLOR_YELLOW
SNAKE_HEAD_COLOR = constants.COLOR_BLUE
SNAKE_DIGESTING_FOOD_COLOR = constants.COLOR_ORANGE
SNAKE_HIT_COLOR = constants.COLOR_RED

# Food
FOOD_COLOR = constants.COLOR_ORANGE
FOOD_SCALE_FACTOR = 0.5
