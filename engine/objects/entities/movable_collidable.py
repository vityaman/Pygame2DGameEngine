import math

from pygame.math import Vector2
from pygame.rect import Rect

from engine.objects.entities.collidable import Collidable
from engine.objects.entities.movable import Movable


class MovableCollidable(Collidable, Movable):
    def __init__(self, collider: Rect, v: Vector2 = None, a: Vector2 = None):
        Collidable.__init__(self, collider)
        Movable.__init__(self, v, a)

    def update(self):
        self.v += self.a

    def move_position(self, v: Vector2):
        super().move_position(v)
        self._check_velocity()
        self.collider.move_ip(v.x, v.y)

