import constants
import framework.event
import entities.food as _food


class SnakeHeadHitsFood(framework.event.Event):
    def __init__(self, food: _food.Food):
        super().__init__(constants.EVENT_SNAKE_HEAD_HITS_FOOD, "snake_head_hits_food", {'food': food})
