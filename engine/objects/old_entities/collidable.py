from pygame.math import Vector2
from pygame.rect import Rect

from engine.objects.old_entities.movable import Direction


class Collidable:
    def __init__(self, collider: Rect):
        self.collider = collider

    def collide(self, other: 'Collidable') -> bool:
        return self.collider.colliderect(other.collider)

    def side_from(self, other: 'Collidable'):
        if self.collider.right <= other.collider.left:
            return Direction.LEFT
        if self.collider.left >= other.collider.right:
            return Direction.RIGHT
        if self.collider.top >= other.collider.bottom:
            return Direction.DOWN
        if self.collider.bottom <= other.collider.top:
            return Direction.UP
        # TODO: fix None return bug
        raise Exception('Undefined side!')

    def __repr__(self):
        return repr(self.collider)
