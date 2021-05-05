import pygame

from pygame.math import Vector2
from pygame.rect import Rect
from pygame.surface import Surface

from engine.objects.entities.movable import Direction
from engine.objects.entities.movable_collidable import MovableCollidable
from engine.objects.primitives.drawable import Animation


class AnimatedCharacter(MovableCollidable):
    def __init__(self, collider: Rect,
                 animation_right: Animation, animation_left: Animation,
                 animation_up: Animation, animation_down: Animation):
        super().__init__(collider)

        self.direction = Direction.DOWN

        self.animations = {
            Direction.RIGHT: animation_right,
            Direction.LEFT: animation_left,
            Direction.DOWN: animation_down,
            Direction.UP: animation_up
        }

    def set_movement(self, v: Vector2, a: Vector2 = None):
        if v != Direction.NULL_VECTOR:
            new_direction = Direction.of(v)
            if new_direction != self.direction:
                self.animations[self.direction].animation_step = 0
                self.animations[new_direction].animation_step = 0
            self.direction = new_direction
        else:
            self.animations[self.direction].animation_step -= 1
        super().set_movement(v, a)

    def draw(self, screen: Surface):
        self.animations[self.direction].draw(screen, Vector2(self.collider.topleft))
        pygame.draw.rect(screen, (255, 0, 0), self.collider, 1)
