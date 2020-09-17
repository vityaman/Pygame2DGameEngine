import pygame

from game_objects.collidable_movable_objects import CollidableMovableObject
from game_objects.drawables import IDrawable


class Character(CollidableMovableObject):
    def __init__(self, rect: pygame.rect.Rect, drawable: IDrawable, layer: int,
                 velocity: int, angle: float):
        super().__init__(rect, drawable, layer, 0, angle)
        self.max_velocity = velocity

    def direct(self, angle):
        self.angle = angle
        self.velocity = self.max_velocity
        self.move()
        self.velocity = 0
