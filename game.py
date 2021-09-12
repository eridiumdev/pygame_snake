import pygame

import framework.game
import framework.escapable
import framework.colors as colors


class Game(framework.escapable.ExitOnEscape, framework.game.Game):
    def render(self):
        # background = pygame.Surface(self.win.get_size())
        # background.fill(colors.BLACK)
        # self.screen.blit(background, (0, 0))
        # self.display.flip()
        self.screen.fill(colors.DARK_GREEN)
        super().render()

    def handle_event(self, event: pygame.event.Event):
        super().handle_event(event)
