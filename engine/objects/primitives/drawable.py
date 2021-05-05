from abc import abstractmethod

import pygame
from pygame.color import Color
from pygame.math import Vector2
from pygame.rect import Rect
from pygame.surface import Surface


class Drawable:
    def __init__(self, offset_x: int = 0, offset_y: int = 0):
        self.offset_x = offset_x
        self.offset_y = offset_y

    @abstractmethod
    def draw(self, screen: Surface, pos: Vector2):
        pass


class RectangleDrawable(Drawable):
    def __init__(self, width: float, height: float, color: Color,
                 offset_x: int = 0, offset_y: int = 0):
        super().__init__(offset_x, offset_y)
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen: Surface, pos: Vector2):
        pygame.draw.rect(screen, self.color,
                         Rect(pos.x - self.offset_x,
                              pos.y - self.offset_y,
                              self.width, self.height))


class CircleDrawable(Drawable):
    def __init__(self, radius: float, color: Color,
                 offset_x: int = 0, offset_y: int = 0):
        super().__init__(offset_x, offset_y)
        self.radius = radius
        self.color = color

    def draw(self, screen: Surface, pos: Vector2):
        pygame.draw.circle(screen, self.color,
                           (pos.x - self.offset_x, pos.y - self.offset_y),
                           self.radius)


class Image(Drawable):
    def __init__(self, image: Surface,
                 offset_x: int = 0, offset_y: int = 0):
        super().__init__(offset_x, offset_y)
        self.image = image

    def draw(self, screen: Surface, pos: Vector2):
        screen.blit(self.image, (pos.x - self.offset_x, pos.y - self.offset_y))

    def scale(self, scale_x: int, scale_y: int):
        self.image = pygame.transform.scale(self.image, (scale_x, scale_y))

    @classmethod
    def load_from(cls, path: str):
        return Image(pygame.image.load(path).convert())

    @classmethod
    def make(cls, path: str, scale: tuple = None, color_key: tuple = None):
        image = Image.load_from(path)
        if scale is not None:
            image.scale(scale[0], scale[1])
        if color_key is not None:
            image.image.set_colorkey(color_key)
        return image


class Animation(Drawable):
    def __init__(self, images: list[Image], image_duration: int,
                 offset_x: int = 0, offset_y: int = 0):
        super().__init__()
        self.images = images
        for image in images:
            image.offset_x = offset_x
            image.offset_y = offset_y
        self.animation_step = 0
        self.animation_duration = image_duration * len(images)
        self.image_duration = image_duration

    def tick(self):
        self.animation_step = (self.animation_step + 1) % self.animation_duration

    def draw(self, screen: Surface, pos: Vector2):
        self.images[self.animation_step // self.image_duration].draw(screen, pos)
        self.tick()
