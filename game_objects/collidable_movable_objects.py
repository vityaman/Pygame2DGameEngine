import pygame

from game_objects.drawables import IDrawable
from game_objects.collidable import Collidable
from game_objects.movable_object import MovableObject


class CollidableMovableObject(MovableObject, Collidable):
    def __init__(self, rect: pygame.rect.Rect, drawable: IDrawable, layer: int,
                 velocity: int, angle: float):
        super().__init__(rect, drawable, layer, velocity, angle)
        self.intent_dx = 0
        self.intent_dy = 0

    def transfer(self, dx: int, dy: int):
        self.intent_dx += dx
        self.intent_dy += dy

    def round_intent(self):
        self.intent_dx = round(self.intent_dx)
        self.intent_dy = round(self.intent_dy)

    def restore_intent(self):
        self.intent_dx = 0
        self.intent_dy = 0

    def on_collide(self, other):
        pass

    def get_rect(self):
        return self.rect
