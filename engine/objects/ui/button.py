from abc import abstractmethod, ABC
from pygame.surface import Surface
from pygame.rect import Rect
from pygame.math import Vector2
from engine.objects.primitives.circle import Circle
from engine.objects.primitives.drawable import Drawable


class Button:
    def __init__(self, text: str, callback_function):
        self.text = text
        self.callback_function = callback_function

    def click(self):
        self.callback_function()

    @abstractmethod
    def contains(self, point: Vector2) -> bool:
        pass

    @abstractmethod
    def draw(self, screen: Surface, pos: Vector2):
        pass


class RectButton(Button, ABC):
    def __init__(self, callback_function, rect: Rect):
        super().__init__(callback_function)
        self.rect = rect

    def contains(self, point: Vector2) -> bool:
        return self.rect.collidepoint(point.x, point.y)


class CircleButton(Button, ABC):
    def __init__(self, callback_function, circle: Circle):
        super().__init__(callback_function)
        self.circle = circle

    def contains(self, point: Vector2) -> bool:
        return self.circle.collide_point(point)


class ImageButton(RectButton):
    def __init__(self, callback_function, rect: Rect, drawable: Drawable):
        super().__init__(callback_function, rect)
        self.drawable = drawable

    def draw(self, screen: Surface, pos: Vector2):
        self.drawable.draw(screen, pos)
