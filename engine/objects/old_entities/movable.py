import math
from abc import abstractmethod
from pygame.math import Vector2

class Direction:
    RIGHT       = 0
    LEFT        = -180
    UP          = -90
    DOWN        = 90
    UP_RIGHT    = -45
    UP_LEFT     = -135
    DOWN_RIGHT  = 45
    DOWN_LEFT   = 135

    START_VECTOR = Vector2(1, 0)
    NULL_VECTOR = Vector2(0, 0)

    @staticmethod
    def of(vector: Vector2):
        angle = vector.angle_to(Direction.START_VECTOR)
        if Direction.UP_RIGHT < angle < Direction.DOWN_RIGHT:
            return Direction.RIGHT
        if Direction.UP_LEFT <= angle <= Direction.UP_RIGHT:
            return Direction.DOWN
        if Direction.DOWN_RIGHT <= angle <= Direction.DOWN_LEFT:
            return Direction.UP
        return Direction.LEFT


def sign(n: float):
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0


class Movable:
    MAX_VELOCITY = 50

    def __init__(self, v: Vector2 = None, a: Vector2 = None):
        self.v = v if v is not None else Vector2(0, 0)
        self.a = a if a is not None else Vector2(0, 0)

    @abstractmethod
    def move_position(self, v: Vector2):
        pass

    def set_movement(self, v: Vector2, a: Vector2 = None):
        self.v = v
        if a is not None:
            self.a = a

    def update(self):
        self.v += self.a
        self.move_position(self.v)

    def _check_velocity(self):
        self.v.x = math.ceil(abs(self.v.x)) * sign(self.v.x)
        self.v.y = math.ceil(abs(self.v.y)) * sign(self.v.y)

        if self.v.x > self.MAX_VELOCITY:
            self.v.x = self.MAX_VELOCITY
        if self.v.y > self.MAX_VELOCITY:
            self.v.y = self.MAX_VELOCITY
