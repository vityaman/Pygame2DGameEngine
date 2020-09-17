from math import sin, cos, pi
import pygame
from game_objects.drawables import IDrawable
from game_objects.game_object import GameObject


class Direction:
    RIGHT       = 0
    LEFT        = pi
    UP          = - pi / 2
    DOWN        = pi / 2
    UP_RIGHT    = - pi / 4
    UP_LEFT     = - 3 * pi / 4
    DOWN_RIGHT  = pi / 4
    DOWN_LEFT   = 3 * pi / 4


def side_from(other, obj):
    if other.rect.right <= obj.rect.left:
        return Direction.RIGHT
    if other.rect.left >= obj.rect.right:
        return Direction.LEFT
    if other.rect.top >= obj.rect.bottom:
        return Direction.UP
    if other.rect.bottom <= obj.rect.top:
        return Direction.DOWN
    # TODO: fix None return bug
    return None


class MovableObject(GameObject):
    def __init__(self, rect: pygame.rect.Rect, drawable: IDrawable, layer: int,
                 velocity: int, angle: float):
        super().__init__(rect, drawable, layer)
        self.angle = angle
        self.velocity = velocity

    def transfer(self, dx: int, dy: int):
        self.move_to(dx, dy)

    def get_velocity(self):
        return self.velocity

    def get_angle(self):
        return self.angle

    def move(self):
        self.transfer(cos(self.get_angle()) * self.get_velocity(), sin(self.get_angle()) * self.get_velocity())
