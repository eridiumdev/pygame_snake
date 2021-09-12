import sys

import pygame

from . import window as _window


class Game:
    def __init__(
            self,
            window: _window.Window,
            fps: int
    ):
        pygame.init()

        self.win = window
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.display = pygame.display

        # display.set_caption should precede display.set_mode
        self.display.set_caption(window.title)
        self.screen = self.display.set_mode((window.width, window.height), 0, 32)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.handle_quit_event()
                else:
                    self.handle_event(event)

            self.render()
            self.clock.tick(self.fps)

    def render(self):
        self.display.update()

    def handle_event(self, event: pygame.event.Event):
        pass

    @staticmethod
    def handle_quit_event():
        pygame.quit()
        sys.exit()
