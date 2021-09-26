import pygame


class Scalable:
    def get_scaled_dimensions(self, x, y, width, height, scale_factor):
        return pygame.Rect(self.get_scaled_x(x, width, scale_factor),
                           self.get_scaled_y(y, height, scale_factor),
                           self.get_scaled_width(width, scale_factor),
                           self.get_scaled_height(height, scale_factor))

    @staticmethod
    def get_scaled_x(x, width, scale_factor):
        return x + round(width * (1 - scale_factor) / 2)

    @staticmethod
    def get_scaled_y(y, height, scale_factor):
        return y + round(height * (1 - scale_factor) / 2)

    @staticmethod
    def get_scaled_width(width, scale_factor):
        return round(width * scale_factor)

    @staticmethod
    def get_scaled_height(height, scale_factor):
        return round(height * scale_factor)
