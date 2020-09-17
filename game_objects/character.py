import pygame

from game_objects.collidable_movable_objects import CollidableMovableObject
from game_objects.drawables import AnimatedImage
from game_objects.movable_object import Direction


class Character(CollidableMovableObject):
    def __init__(self, rect: pygame.rect.Rect,
                 animation_right: AnimatedImage, animation_left: AnimatedImage,
                 animation_up: AnimatedImage, animation_down: AnimatedImage,
                 layer: int,
                 velocity: int, angle: float):
        super().__init__(rect, animation_down, layer, 0, angle)
        self.max_velocity = velocity

        self.animations = {
            Direction.RIGHT: animation_right,
            Direction.LEFT: animation_left,
            Direction.DOWN: animation_down,
            Direction.UP: animation_up
        }

    def direct(self, angle):
        self.angle = angle
        self.drawable = self.animations[Direction.of(angle)]
        self.velocity = self.max_velocity
        self.move()
