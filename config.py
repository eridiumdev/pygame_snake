import constants

# General
DEBUG = True    # full debug logs
ADHOC = False   # ad-hoc logs for testing

# Window
WINDOW_TITLE = 'Snek'
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Game
GAME_FPS = 60
GAME_BACKGROUND_COLOR = constants.COLOR_DARK_GREEN

# Snake
SNAKE_MOVEMENT_CYCLES_PER_SECOND = 12    # how often snake can move
SNAKE_STARTING_DIRECTION = constants.DIRECTION_RIGHT

SNAKE_STARTING_CHUNKS = 8           # including head
SNAKE_CHUNK_SIZE = [30, 30]         # width, height
SNAKE_BODY_SIZE_FACTOR = 0.8        # relative to full chunk size (body + border)

SNAKE_BORDER_COLOR = constants.COLOR_BLACK
SNAKE_BODY_COLOR = constants.COLOR_YELLOW
SNAKE_HEAD_BORDER_COLOR = constants.COLOR_BLACK
SNAKE_HEAD_BODY_COLOR = constants.COLOR_BLUE
