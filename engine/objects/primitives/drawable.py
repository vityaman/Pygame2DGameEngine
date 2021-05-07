from abc import ABC, abstractmethod

import pygame
from pygame.color import Color
from pygame.surface import Surface

from engine.objects.primitives.vector2d import Vector2D


class IDrawable(ABC):
    @abstractmethod
    def draw(self, surface: Surface, position: Vector2D):
        pass


class IOffset(ABC):
    def __init__(self, offset: Vector2D = None):
        self.offset: Vector2D = offset if offset is not None else Vector2D(0, 0)


class RectangleDrawable(IDrawable):
    def __init__(self, width: float, height: float, color: Color):
        self.width: float = width
        self.height: float = height
        self.color: Color = color

    def draw(self, surface: Surface, position: Vector2D):
        pygame.draw.rect(surface, self.color,
                         (position.x, position.y, self.width, self.height))


class OffsetRectangleDrawable(RectangleDrawable, IOffset):
    def __init__(self, width: float, height: float, color: Color, offset: Vector2D = None):
        RectangleDrawable.__init__(self, width, height, color)
        IOffset.__init__(self, offset)

    def draw(self, surface: Surface, position: Vector2D):
        pygame.draw.rect(surface, self.color,
                         (position.x + self.offset.x, position.y + self.offset.y, self.width, self.height))


class CircleDrawable(IDrawable):
    def __init__(self, radius: float, color: Color):
        self.radius: float = radius
        self.color: Color = color

    def draw(self, surface: Surface, position: Vector2D):
        pygame.draw.circle(surface, self.color,
                           (position.x, position.y), self.radius)


class OffsetCircleDrawable(CircleDrawable, IOffset):
    def __init__(self, radius: float, color: Color, offset: Vector2D = None):
        CircleDrawable.__init__(self, radius, color)
        IOffset.__init__(self, offset)

    def draw(self, surface: Surface, position: Vector2D):
        pygame.draw.circle(surface, self.color,
                           (position.x + self.offset.x, position.y + self.offset.y),
                           self.radius)


class Image(IDrawable):
    def __init__(self, file_path: str):
        self.image: Surface = pygame.image.load(file_path).convert()

    def scale(self, scale: Vector2D):
        self.image = pygame.transform.scale(self.image, scale.as_tuple())

    def set_transparent_color(self, color: Color):
        self.image.set_colorkey(color)

    def draw(self, surface: Surface, position: Vector2D):
        surface.blit(self.image, position.as_tuple())


class OffsetImage(Image, IOffset):
    def __init__(self, file_path: str, offset: Vector2D = None):
        Image.__init__(self, file_path)
        IOffset.__init__(self, offset)


class Animation(IDrawable):
    def __init__(self, frames: list[IDrawable], frame_duration: int):
        self.frames = frames
        self.step = 0
        self.frame_duration = frame_duration
        self.animation_duration = frame_duration * len(frames)

    def tick(self):
        self.step = (self.step + 1) % self.animation_duration

    def draw(self, surface: Surface, position: Vector2D):
        self.frames[self.step // self.frame_duration].draw(surface, position)
        self.tick()