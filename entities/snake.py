import collections

import pygame

import config
from framework import renderable
from . import snake_chunk as _chunk
from . import clock


class Snake(renderable.Renderable):
    def __init__(self, start_x, start_y):
        self.chunks = []    # type: list[_chunk.SnakeChunk]
        self.tip = (start_x, start_y)
        self.chunk_size = config.SNAKE_CHUNK_SIZE
        self.direction = config.SNAKE_STARTING_DIRECTION
        self.next_moves = collections.deque(maxlen=4)
        self.clock = clock.Clock(config.SNAKE_MOVEMENT_CYCLES_PER_SECOND)
        self.add_head()
        for i in range(config.SNAKE_STARTING_CHUNKS - 1):
            self.add_tail()

    def add_head(self):
        new_head = _chunk.SnakeChunk(*self.tip, *self.chunk_size, self.direction)
        new_head.is_head = True

        if len(self.chunks) > 0:
            self.chunks[0] = new_head
        else:
            self.chunks.append(new_head)

    def add_tail(self):
        current_tail = self.chunks[len(self.chunks) - 1]
        current_tail.is_tail = False

        new_tail = _chunk.SnakeChunk(
            current_tail.border.rect.x,
            current_tail.border.rect.y,
            *self.chunk_size,
            current_tail.direction
        )
        new_tail.is_tail = True
        # Hide new tail for now (will appear on the screen after previous tail moves away)
        new_tail.hidden_cycles_counter = current_tail.hidden_cycles_counter + 1

        self.chunks.append(new_tail)

    def queue_move(self, direction: (int, int)):
        # Only queue move if it is not already queued
        try:
            self.next_moves.index(direction)
        except ValueError:
            # Index not found = move not yet queued
            self.next_moves.append(direction)

    def _move_is_valid(self, move):
        # Only apply up next move if moving in a valid direction
        reverse_direction = (self.direction[0] * -1, self.direction[1] * -1)
        return move != self.direction and move != reverse_direction

    def _move(self):
        # Loop through all queued moves
        config.DEBUG and print("Queued moves:", self.next_moves)
        move_taken = False
        while len(self.next_moves) > 0:
            next_move = self.next_moves.popleft()
            config.DEBUG and print("Next move is", next_move)
            if self._move_is_valid(next_move):
                config.DEBUG and print("Move is valid, applying")
                self._apply_move(next_move)
                move_taken = True
                break
            else:
                config.DEBUG and print("Move is invalid, skipping")

        # If no queued move was valid, just move forward in the current direction
        if not move_taken:
            config.DEBUG and print("No move was taken, moving forward")
            self._apply_move(self.direction)

    def _apply_move(self, direction: (int, int)):
        # Reflect next move in the snake direction
        self.direction = direction

        # Move every chunk, starting from the tail
        for i in range(len(self.chunks) - 1, -1, -1):
            config.DEBUG and print("--- CHUNK {0}".format(i))
            chunk = self.chunks[i]
            if chunk.is_hidden():
                # Update chunk cycles counter
                config.DEBUG and print("Chunk is hidden, hidden_cycles_counter: {1} -> {2}"
                                       .format(i, chunk.hidden_cycles_counter, chunk.hidden_cycles_counter - 1))
                chunk.decrease_hidden_counter()
                # Do not move hidden chunks - they stay in place
                continue
            if i == 0:
                # Update heads direction to overall snake direction
                config.DEBUG and print("Updating chunk direction from {0} to {1}".format(chunk.direction, self.direction))
                chunk.direction = self.direction
            if i < len(self.chunks) - 1:
                # Update previous chunk direction so it follows current chunk in the next cycle
                config.DEBUG and print("Updating previous chunk ({0}) direction from {1} to {2}"
                                       .format(i + 1, self.chunks[i + 1].direction, chunk.direction))
                self.chunks[i+1].direction = chunk.direction
            # Proceed with updating chunk coordinates
            chunk.move()

    def render(self, screen: pygame.Surface):
        if self.clock.has_ticked():
            config.DEBUG and print("============= STARTING NEXT MOVE =============")
            self._move()
        for chunk in self.chunks:
            chunk.render(screen)
