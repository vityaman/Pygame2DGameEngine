import math

from engine.objects.entities.collidable import Collidable
from engine.objects.entities.movable import Direction
from engine.objects.entities.movable_collidable import MovableCollidable


class CollisionsHandler:
    def __init__(self):
        self.collidables: list[Collidable] = []
        self.movable_collidables: list[MovableCollidable] = []

    def add(self, entity):
        if isinstance(entity, Collidable):
            self.collidables.append(entity)
        if isinstance(entity, MovableCollidable):
            self.movable_collidables.append(entity)

    def handle_movables(self):
        for entity in self.movable_collidables:
            if entity.v == Direction.NULL_VECTOR:
                continue

            entity.move_position(entity.v)
            collided_objects = [other for other in self.collidables
                                if entity.collide(other) and other is not entity]
            entity.move_position(-entity.v)

            velocity = entity.v
            _dx: int = entity.v.x
            _dy: int = entity.v.y
            for collided in collided_objects:
                if entity.side_from(collided) == Direction.RIGHT:
                    _dx = collided.collider.right - entity.collider.left
                elif entity.side_from(collided) == Direction.LEFT:
                    _dx = collided.collider.left - entity.collider.right
                if abs(_dx) < abs(velocity.x):
                    velocity.x = _dx

                if entity.side_from(collided) == Direction.UP:
                    _dy = collided.collider.top - entity.collider.bottom
                elif entity.side_from(collided) == Direction.DOWN:
                    _dy = collided.collider.bottom - entity.collider.top
                if abs(_dy) < abs(velocity.y):
                    velocity.y = _dy

            entity.move_position(velocity)

            if [other for other in self.collidables
                if entity.collide(other) and other is not entity]:
                entity.move_position(-velocity)
