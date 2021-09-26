import constants
import framework.event
import entities.snake_chunk as _chunk
import entities.food as _food


class SnakeHeadHitsBody(framework.event.Event):
    def __init__(self, chunk: _chunk.SnakeChunk):
        super().__init__(constants.EVENT_SNAKE_HEAD_HITS_BODY, "snake_head_hits_body", {'chunk': chunk})


class SnakeHeadHitsFood(framework.event.Event):
    def __init__(self, food: _food.Food):
        super().__init__(constants.EVENT_SNAKE_HEAD_HITS_FOOD, "snake_head_hits_food", {'food': food})
