import pygame
from game_objects.drawables import IDrawable


class GameObject:
    def __init__(self, rect: pygame.rect.Rect, drawable: IDrawable, layer: int):
        self.rect = rect
        self.drawable = drawable
        self.layer = layer

    def set_position(self, x: int, y: int):
        self.rect.centerx = x
        self.rect.centery = y

    def move_to(self, dx: int, dy: int):
        self.rect.x += dx
        self.rect.y += dy

    def get_x(self):
        return self.rect.centerx

    def get_y(self):
        return self.rect.centery

    def draw(self, canvas):
        self.drawable.draw(canvas, self.rect.centerx, self.rect.centery)
        # TODO: delete debug
        pygame.draw.rect(canvas, (255, 0, 0), self.rect, 1)

    def __lt__(self, other):
        return self.layer < other.layer

    def __gt__(self, other):
        return self.layer > other.layer

    def __le__(self, other):
        return self.layer <= other.layer

    def __ge__(self, other):
        return self.layer >= other.layer
