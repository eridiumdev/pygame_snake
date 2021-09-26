import sys

import pygame

from . import window as _window
from . import event as _event


class Game:
    def __init__(
            self,
            window: _window.Window,
            fps: int
    ):
        pygame.init()
        # Catch KEY_PRESS events every 50 ms
        # (10ms = delay before first catch)
        # pygame.key.set_repeat(10, 50)

        self.win = window
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.display = pygame.display

        # display.set_caption should precede display.set_mode
        self.display.set_caption(window.title)

    def run(self):
        self.screen = self.display.set_mode((self.win.width, self.win.height), 0, 32)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.handle_quit_event()
                elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    self.handle_key_event(event)
                elif event.type >= pygame.USEREVENT:
                    self.handle_user_event(_event.Event(event.type, event.name, event.payload))
                else:
                    self.handle_event(event)

            self.handle_keys_pressed(pygame.key.get_pressed())

            self.render()
            self.clock.tick(self.fps)

    def handle_key_event(self, event: pygame.event.Event):
        pass

    def handle_keys_pressed(self, keys_pressed):
        pass

    def handle_user_event(self, event: pygame.event.Event):
        pass

    def handle_event(self, event: pygame.event.Event):
        pass

    def render(self):
        self.display.update()

    def post_event(self, event: _event.Event):
        pygame.event.post(pygame.event.Event(event.type, {'name': event.name, 'payload': event.payload}))

    @staticmethod
    def handle_quit_event():
        pygame.quit()
        sys.exit()
