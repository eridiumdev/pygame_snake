import pygame


class Event:
    def __init__(self, type: int, name: str, payload: dict = None):
        if type <= pygame.USEREVENT:
            raise Exception("Type must be less than {0}".format(pygame.USEREVENT))

        self.type = type
        self.name = name
        self.payload = payload
