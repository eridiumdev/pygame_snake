import pygame


# Colors
COLOR_BLACK = (0, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_DARK_GREEN = (0, 45, 0)
COLOR_YELLOW = (200, 200, 30)
COLOR_BLUE = (0, 80, 200)
COLOR_ORANGE = (255, 153, 51)
COLOR_RED = (220, 0, 0)

# Direction holds x,y coordinates change
# -1 = x/y decreases
# 0 = x/y stays the same
# 1 = x/y increases
DIRECTION_UP = (0, -1)
DIRECTION_DOWN = (0, 1)
DIRECTION_LEFT = (-1, 0)
DIRECTION_RIGHT = (1, 0)

# Events
EVENT_SNAKE_HEAD_HITS_FOOD = pygame.USEREVENT + 1
