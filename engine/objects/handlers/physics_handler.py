from pygame.math import Vector2

from engine.objects.entities.collidable import Collidable
from engine.objects.entities.movable import Direction
from engine.objects.entities.ball import Ball


class PhysicsHandler:
    def __init__(self):
        self.balls: list[Ball] = []
        self.collidables: list[Collidable] = []

    def add(self, entity):
        if isinstance(entity, Ball):
            self.balls.append(entity)
        elif isinstance(entity, Collidable):
            self.collidables.append(entity)

    def handle_physics(self):
        self._handle_balls()

    def _handle_balls(self):
        # consider all pairs (i, j), i < j
        # for ball-ball collisions
        for i in range(len(self.balls)):
            for j in range(i + 1, len(self.balls)):
                a = self.balls[i]
                b = self.balls[j]

                v = Vector2(a.v)
                a.move_position(v)

                if a.collide(b):
                    av, am = a.v, a.m
                    bv, bm = b.v, b.m

                    a.set_movement(v=(am - bm) / (am + bm) * av + 2 * bm / (am + bm) * bv)
                    b.set_movement(v=2 * am / (am + bm) * av + (bm - am) / (am + bm) * bv)

                a.move_position(-v)

        for ball in self.balls:
            v = Vector2(ball.v)
            ball.move_position(v)
            collided = [collidable for collidable in self.collidables
                        if ball.collide(collidable)]
            ball.move_position(-v)

            for collidable in collided:
                if ball.side_from(collidable) in (Direction.UP, Direction.DOWN):
                    ball.v.y = -ball.v.y
                else:
                    ball.v.x = -ball.v.x
