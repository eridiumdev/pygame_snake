import pygame

from . import game


class ExitOnEscape(game.Game):
    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.handle_quit_event()
