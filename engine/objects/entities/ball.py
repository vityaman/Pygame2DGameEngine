import pygame
from pygame.color import Color
from pygame.math import Vector2
from pygame.rect import Rect
from pygame.surface import Surface

from engine.objects.entities.collidable import Collidable
from engine.objects.entities.movable import Direction
from engine.objects.entities.movable_collidable import MovableCollidable
from engine.objects.primitives.drawable import CircleDrawable

from random import randint


class Ball(MovableCollidable):
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 12)

    def __init__(self, x: int, y: int, r: int, v: Vector2, a: Vector2 = None):
        super().__init__(Rect(x - r, y - r, 2 * r, 2 * r), v=v, a=a)
        self.drawable = CircleDrawable(
            radius=r,
            color=Color(randint(0, 255), randint(0, 255), randint(0, 255)))
        self.m = r

    def draw(self, screen: Surface):
        self.drawable.draw(screen, Vector2(self.collider.center))
        pygame.draw.rect(screen, (255, 0, 0), self.collider, 1)
        screen.blit(self.font.render(str(self.v), False, (255, 255, 255)), self.collider.center)

