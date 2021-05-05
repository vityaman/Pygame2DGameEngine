import pygame
from pygame.math import Vector2
from pygame.rect import Rect
from pygame.surface import Surface
from engine.objects.entities.collidable import Collidable
from engine.objects.primitives.drawable import Drawable


class Wall(Collidable):
    def __init__(self, collider: Rect, drawable: Drawable):
        super().__init__(collider)
        self.drawable = drawable

    def draw(self, screen: Surface):
        self.drawable.draw(screen, Vector2(self.collider.topleft))
        pygame.draw.rect(screen, (255, 0, 0), self.collider, 1)

    def on_collide(self, other: Collidable):
        pass
