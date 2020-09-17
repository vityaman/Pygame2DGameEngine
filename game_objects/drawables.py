import pygame
from abc import ABC, abstractmethod


class IDrawable(ABC):
    @abstractmethod
    def draw(self, canvas, x: int, y: int):
        pass


class Image(IDrawable):
    def __init__(self, image, shift_x=0, shift_y=0):
        self.image = image
        self.shift_x = shift_x
        self.shift_y = shift_y

    def draw(self, canvas, x: int, y: int):
        canvas.blit(self.image, (x + self.shift_x, y + self.shift_y))


def load_image(path: str, scale: tuple, color_key: tuple = None):
    image = pygame.image.load(path).convert()
    image = pygame.transform.scale(image, scale)
    if color_key is not None:
        image.set_colorkey(color_key)
    return image


class Circle(IDrawable):
    def __init__(self, radius: int, width: int, color: tuple):
        self.radius = radius
        self.width = width
        self.color = color

    def draw(self, canvas, x: int, y: int):
        pygame.draw.circle(canvas, self.color, (x, y), self.radius, self.width)


class Rectangle(IDrawable):
    def __init__(self, rwidth: int, rheight: int, width: int, color: tuple):
        self.rwidth = rwidth
        self.rheight = rheight
        self.width = width
        self.color = color

    def draw(self, canvas, x: int, y: int):
        pygame.draw.rect(canvas, self.color,
                         (x - self.rwidth // 2, y - self.rheight // 2, self.rwidth, self.rheight),
                         self.width)


class AnimatedImage(IDrawable):
    def __init__(self, images: list, image_duration: int, shift_x=0, shift_y=0):
        self.images = images
        self.shift_x = shift_x
        self.shift_y = shift_y
        self.animation_duration = image_duration * len(images)
        self.image_duration = image_duration
        self.counter = 0

    def tick(self):
        self.counter = (self.counter + 1) % self.animation_duration

    def draw(self, canvas, x: int, y: int):
        canvas.blit(self.images[self.counter // self.image_duration], (x + self.shift_x, y + self.shift_y))
        self.tick()


